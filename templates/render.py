"""Rendu des posts Instagram DelorIA : spec JSON -> HTML -> JPEG 1080x1350 (4:5).

Usage :
    python3 templates/render.py posts/2026-10/01.json        # un post
    python3 templates/render.py posts/2026-10/*.json         # un lot

Chaque spec JSON contient "template" (constat | terrain | service) et les champs
du gabarit. Le JPEG est écrit à côté du JSON, même nom, extension .jpg.
Règles de charte appliquées ici, pas dans les specs : palette officielle,
Cormorant Garamond + Montserrat, "IA" toujours en italique, aucun tiret long.
"""

import html
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"

W, H = 1080, 1350

BASE_CSS = f"""
@font-face {{ font-family: 'Cormorant'; src: url('{(FONTS / 'CormorantGaramond.ttf').as_uri()}'); font-weight: 300 700; font-style: normal; }}
@font-face {{ font-family: 'Cormorant'; src: url('{(FONTS / 'CormorantGaramond-Italic.ttf').as_uri()}'); font-weight: 300 700; font-style: italic; }}
@font-face {{ font-family: 'Montserrat'; src: url('{(FONTS / 'Montserrat.ttf').as_uri()}'); font-weight: 100 900; }}
:root {{
  --noir: #0D0D0D; --blanc: #FAFAF8; --marron: #3B2314;
  --beige: #E8DDD0; --beige-clair: #F4EEE6; --or: #C9A96E;
}}
* {{ margin: 0; padding: 0; box-sizing: border-box; }}
html, body {{ width: {W}px; height: {H}px; overflow: hidden; }}
body {{ font-family: 'Montserrat', sans-serif; font-weight: 300; -webkit-font-smoothing: antialiased; }}
.frame {{ position: relative; width: {W}px; height: {H}px; padding: 120px 110px; display: flex; flex-direction: column; }}
.label {{ font-family: 'Montserrat'; font-weight: 500; font-size: 20px; letter-spacing: 0.42em; text-transform: uppercase; }}
.orn {{ display: flex; align-items: center; gap: 18px; }}
.orn .l {{ height: 1px; width: 70px; }}
.orn .d {{ width: 9px; height: 9px; transform: rotate(45deg); }}
.wm {{ font-family: 'Cormorant'; font-weight: 300; font-size: 40px; letter-spacing: 0.2em; text-transform: uppercase; }}
.wm em {{ font-style: italic; font-weight: 400; }}
.foot {{ margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end; }}
.handle {{ font-family: 'Montserrat'; font-weight: 400; font-size: 19px; letter-spacing: 0.3em; }}
"""


def esc(s: str) -> str:
    """Échappe le HTML puis convertit *texte* en italique d'accent."""
    s = html.escape(s, quote=False).replace("'", "\u2019")
    out, italic = [], False
    for part in s.split("*"):
        out.append(("<em>" if italic else "") + part + ("</em>" if italic else ""))
        italic = not italic
    return "".join(out).replace("\n", "<br>")


def check_text(spec: dict) -> None:
    """Refuse les tirets longs et moyens : règle de charte non négociable."""
    blob = json.dumps(spec, ensure_ascii=False)
    for bad in ("—", "–"):
        if bad in blob:
            raise ValueError(f"Tiret interdit trouvé dans la spec : {bad!r}")


def wordmark(color_name: str, color_ia: str) -> str:
    return f'<div class="wm" style="color:var({color_name})">Delor<em style="color:var({color_ia})">IA</em></div>'


def ornament(color: str) -> str:
    return (f'<div class="orn"><div class="l" style="background:var({color})"></div>'
            f'<div class="d" style="background:var({color})"></div>'
            f'<div class="l" style="background:var({color})"></div></div>')


def tpl_constat(p: dict) -> str:
    """Noir + crème + or. Un constat du quotidien, une chute en italique or."""
    return f"""
<style>
body {{ background: var(--noir); color: var(--blanc); }}
.ring {{ position: absolute; border: 1px solid var(--or); border-radius: 50%; left: 50%; top: 46%; transform: translate(-50%, -50%); }}
.r1 {{ width: 980px; height: 980px; opacity: 0.07; }}
.r2 {{ width: 700px; height: 700px; opacity: 0.11; }}
.body {{ margin-top: auto; margin-bottom: auto; position: relative; }}
.texte {{ font-family: 'Cormorant'; font-weight: 300; font-size: 76px; line-height: 1.12; letter-spacing: 0.01em; }}
.chute {{ font-family: 'Cormorant'; font-style: italic; font-weight: 400; font-size: 84px; line-height: 1.1; color: var(--or); margin-top: 44px; }}
</style>
<div class="frame">
  <div class="ring r1"></div><div class="ring r2"></div>
  <div class="label" style="color:var(--or); position:relative">{esc(p['label'])}</div>
  <div class="body">
    <div class="texte">{esc(p['texte'])}</div>
    <div class="chute">{esc(p['chute'])}</div>
  </div>
  <div class="foot" style="position:relative">
    {wordmark('--blanc', '--or')}
    <div class="handle" style="color:var(--beige); opacity:.55">@DELORIA.IA</div>
  </div>
</div>"""


def tpl_terrain(p: dict) -> str:
    """Crème + noir + marron. Une leçon vécue en production, ton éditorial."""
    return f"""
<style>
body {{ background: var(--beige-clair); color: var(--noir); }}
.num {{ font-family: 'Cormorant'; font-variant-numeric: lining-nums; font-weight: 300; font-size: 150px; line-height: 1; color: var(--or); margin-top: 70px; }}
.titre {{ font-family: 'Cormorant'; font-weight: 400; font-size: 74px; line-height: 1.1; margin-top: 30px; }}
.titre em {{ color: var(--marron); }}
.sep {{ width: 90px; height: 1px; background: var(--marron); opacity: .45; margin: 56px 0 48px; }}
.texte {{ font-family: 'Montserrat'; font-weight: 300; font-size: 31px; line-height: 1.65; opacity: .82; }}
.chute {{ font-family: 'Cormorant'; font-style: italic; font-weight: 500; font-size: 46px; line-height: 1.25; color: var(--marron); margin-top: 44px; }}
</style>
<div class="frame">
  <div class="label" style="color:var(--marron); opacity:.75">{esc(p['label'])}</div>
  <div class="num">{esc(p['numero'])}</div>
  <div class="titre">{esc(p['titre'])}</div>
  <div class="sep"></div>
  <div class="texte">{esc(p['texte'])}</div>
  <div class="chute">{esc(p['chute'])}</div>
  <div class="foot">
    {wordmark('--noir', '--marron')}
    <div class="handle" style="color:var(--marron); opacity:.6">@DELORIA.IA</div>
  </div>
</div>"""


def tpl_service(p: dict) -> str:
    """Marron + crème + beige. Ce que DelorIA fait, trois points maximum."""
    items = "".join(
        f'<div class="item"><div class="d"></div><div>{esc(i)}</div></div>'
        for i in p["points"][:3]
    )
    return f"""
<style>
body {{ background: var(--marron); color: var(--blanc); }}
.titre {{ font-family: 'Cormorant'; font-weight: 300; font-size: 82px; line-height: 1.1; margin-top: 90px; }}
.titre em {{ color: var(--or); font-weight: 400; }}
.items {{ margin-top: 80px; display: flex; flex-direction: column; gap: 38px; }}
.item {{ display: flex; align-items: baseline; gap: 30px; font-family: 'Montserrat'; font-weight: 300; font-size: 33px; line-height: 1.45; color: var(--beige); }}
.item .d {{ flex: none; width: 10px; height: 10px; background: var(--or); transform: rotate(45deg) translateY(-6px); }}
</style>
<div class="frame">
  <div class="label" style="color:var(--beige); opacity:.7">{esc(p['label'])}</div>
  <div class="titre">{esc(p['titre'])}</div>
  <div class="items">{items}</div>
  <div class="foot">
    <div style="display:flex; flex-direction:column; gap:22px">
      {ornament('--or')}
      {wordmark('--blanc', '--or')}
    </div>
    <div class="handle" style="color:var(--beige); opacity:.6">{esc(p.get('signature', '@DELORIA.IA'))}</div>
  </div>
</div>"""


TEMPLATES = {"constat": tpl_constat, "terrain": tpl_terrain, "service": tpl_service}


def build_html(spec: dict) -> str:
    check_text(spec)
    body = TEMPLATES[spec["template"]](spec)
    return f'<!doctype html><html lang="fr"><head><meta charset="utf-8"><style>{BASE_CSS}</style></head><body>{body}</body></html>'


def render(paths: list[Path]) -> list[Path]:
    outputs = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": W, "height": H}, device_scale_factor=1)
        for path in paths:
            spec = json.loads(path.read_text(encoding="utf-8"))
            html_path = path.with_suffix(".html")
            html_path.write_text(build_html(spec), encoding="utf-8")
            page.goto(html_path.as_uri())
            page.evaluate("document.fonts.ready")
            out = path.with_suffix(".jpg")
            page.screenshot(path=str(out), type="jpeg", quality=92, full_page=False)
            html_path.unlink()
            outputs.append(out)
            print(f"ok  {out}")
        browser.close()
    return outputs


if __name__ == "__main__":
    render([Path(a).resolve() for a in sys.argv[1:]])
