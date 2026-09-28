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
    for signe in ("?", "!", ":", ";"):
        s = s.replace(" " + signe, "\u00a0" + signe)
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


REPO = ROOT.parent

# Icônes au trait, dessinées à la main (viewBox 24), pour la rangée de 3 pictos.
ICONES = {
    "globe": '<circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3a14 14 0 0 1 0 18a14 14 0 0 1 0-18"/>',
    "lune": '<path d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
    "cloche": '<path d="M6 16v-5a6 6 0 0 1 12 0v5l1.5 2h-15z"/><path d="M10 20a2 2 0 0 0 4 0"/>',
    "maison": '<path d="M4 11l8-7 8 7v9H4z"/><path d="M10 20v-5h4v5"/>',
    "cle": '<circle cx="8" cy="15" r="4"/><path d="M11 12l8-8"/><path d="M16 7l3 3"/>',
    "calendrier": '<rect x="4" y="5" width="16" height="15" rx="1"/><path d="M4 10h16M9 3v4M15 3v4"/>',
    "message": '<path d="M4 5h16v11H9l-5 4z"/>',
    "etoile": '<path d="M12 3l2.6 5.8 6.4.6-4.8 4.3 1.4 6.3L12 16.8 6.4 20l1.4-6.3L3 9.4l6.4-.6z"/>',
    "mobile": '<rect x="7" y="3" width="10" height="18" rx="2"/><path d="M11 18h2"/>',
    "loupe": '<circle cx="11" cy="11" r="6"/><path d="M15.5 15.5L20 20"/>',
    "pinceau": '<path d="M14 4l6 6-8 8H6v-6z"/><path d="M11 7l6 6"/>',
    "video": '<rect x="3" y="6" width="13" height="12" rx="1"/><path d="M16 10l5-3v10l-5-3z"/>',
    "document": '<path d="M6 3h8l4 4v14H6z"/><path d="M14 3v4h4M9 12h6M9 16h6"/>',
    "engrenage": '<circle cx="12" cy="12" r="3"/><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2.1 2.1M16.3 16.3l2.1 2.1M5.6 18.4l2.1-2.1M16.3 7.7l2.1-2.1"/>',
    "check": '<circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.7 2.7L16 9.8"/>',
    "horloge": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
    "photo": '<rect x="3" y="6" width="18" height="14" rx="1"/><circle cx="12" cy="13" r="3.5"/><path d="M8 6l1.5-2h5L16 6"/>',
}


def icone(nom: str, couleur: str, taille: int = 46) -> str:
    return (f'<svg width="{taille}" height="{taille}" viewBox="0 0 24 24" fill="none" stroke="{couleur}" '
            f'stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round">{ICONES[nom]}</svg>')


def photo_uri(p: dict) -> str:
    chemin = (REPO / p["photo"]).resolve()
    if not chemin.is_file():
        raise FileNotFoundError(f"Photo introuvable : {chemin}")
    return chemin.as_uri()


def taille_phrase(phrase: str) -> int:
    """Réduit la taille quand une ligne est longue, pour éviter les mots orphelins."""
    plus_longue = max(len(l.replace("*", "")) for l in phrase.split("\n"))
    return 88 if plus_longue <= 22 else 76 if plus_longue <= 26 else 66


def tpl_plein(p: dict) -> str:
    """Photo pleine page, filet intérieur, une phrase centrée. Esprit hôtellerie de luxe."""
    cadrage = p.get("cadrage", "center")
    return f"""
<style>
body {{ background: var(--noir); }}
.bg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: {cadrage}; }}
.voile {{ position: absolute; inset: 0; background: rgba(13,13,13,{p.get('voile', 0.42)}); }}
.filet {{ position: absolute; inset: 44px; border: 1px solid rgba(250,250,248,.55); }}
.centre {{ position: absolute; inset: 0; transform: translateY({p.get('decalage', 0)}px); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0 130px; color: var(--blanc); }}
.lieu {{ font-family: 'Montserrat'; font-weight: 400; font-size: 22px; letter-spacing: .38em; text-transform: uppercase; opacity: .9; margin-bottom: 34px; }}
.phrase {{ font-family: 'Cormorant'; font-weight: 300; font-size: {taille_phrase(p['phrase'])}px; line-height: 1.08; text-shadow: 0 2px 24px rgba(0,0,0,.45), 0 0 2px rgba(0,0,0,.3); }}
.phrase em {{ font-weight: 400; color: var(--beige); }}
.bas {{ position: absolute; left: 0; right: 0; bottom: 96px; display: flex; flex-direction: column; align-items: center; gap: 20px; }}
</style>
<img class="bg" src="{photo_uri(p)}">
<div class="voile"></div>
<div class="filet"></div>
<div class="centre">
  {f'<div class="lieu">{esc(p["lieu"])}</div>' if p.get('lieu') else ''}
  <div class="phrase">{esc(p['phrase'])}</div>
</div>
<div class="bas">
  {ornament('--beige')}
  {wordmark('--blanc', '--or')}
</div>"""


def tpl_edito(p: dict) -> str:
    """Texte à gauche sur crème, photo à droite, rangée de 3 pictos. Esprit magazine."""
    cadrage = p.get("cadrage", "center")
    pictos = "".join(
        f'<div class="picto">{icone(i["icone"], "#3B2314")}<div class="pl">{esc(i["texte"])}</div></div>'
        for i in p["pictos"][:3]
    )
    cta = f'<div class="cta">{esc(p["cta"])}</div>' if p.get("cta") else ""
    return f"""
<style>
body {{ background: var(--beige-clair); color: var(--noir); }}
.g {{ position: absolute; left: 0; top: 0; bottom: 0; width: 540px; padding: 100px 56px 90px 76px; display: flex; flex-direction: column; }}
.ph {{ position: absolute; right: 0; top: 0; width: 540px; height: {H}px; object-fit: cover; object-position: {cadrage}; }}
.wm {{ font-size: 32px; }}
.lab {{ margin-top: 74px; font-family: 'Montserrat'; font-weight: 500; font-size: 16px; letter-spacing: .4em; text-transform: uppercase; color: var(--or); }}
.titre {{ font-family: 'Cormorant'; font-weight: 400; font-size: 64px; line-height: 1.04; margin-top: 26px; }}
.titre em {{ color: var(--or); }}
.sep {{ width: 60px; height: 1px; background: var(--noir); opacity: .35; margin: 36px 0 30px; }}
.txt {{ font-family: 'Montserrat'; font-weight: 300; font-size: 22px; line-height: 1.6; opacity: .8; }}
.pictos {{ margin-top: auto; display: grid; grid-template-columns: repeat(3, 1fr); }}
.picto {{ display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center; padding: 0 8px; }}
.picto + .picto {{ border-left: 1px solid rgba(59,35,20,.25); }}
.pl {{ font-family: 'Montserrat'; font-weight: 500; font-size: 13px; letter-spacing: .14em; line-height: 1.5; text-transform: uppercase; color: var(--marron); }}
.cta {{ margin-top: 48px; align-self: flex-start; border: 1px solid var(--noir); border-radius: 40px; padding: 18px 34px; font-family: 'Montserrat'; font-weight: 500; font-size: 15px; letter-spacing: .32em; text-transform: uppercase; }}
</style>
<div class="g">
  {wordmark('--noir', '--or')}
  <div class="lab">{esc(p['label'])}</div>
  <div class="titre">{esc(p['titre'])}</div>
  <div class="sep"></div>
  <div class="txt">{esc(p['texte'])}</div>
  <div class="pictos">{pictos}</div>
  {cta}
</div>
<img class="ph" src="{photo_uri(p)}">"""


def tpl_terrain_photo(p: dict) -> str:
    """Note de terrain avec bandeau photo en haut. Même voix que 'terrain'."""
    cadrage = p.get("cadrage", "center")
    return f"""
<style>
body {{ background: var(--beige-clair); color: var(--noir); }}
.ph {{ position: absolute; left: 0; right: 0; top: 0; height: 520px; width: 100%; object-fit: cover; object-position: {cadrage}; }}
.bloc {{ position: absolute; left: 0; right: 0; top: 520px; bottom: 0; padding: 64px 110px 96px; display: flex; flex-direction: column; }}
.haut {{ display: flex; align-items: baseline; gap: 34px; }}
.num {{ font-family: 'Cormorant'; font-variant-numeric: lining-nums; font-weight: 300; font-size: 96px; line-height: .8; color: var(--or); }}
.titre {{ font-family: 'Cormorant'; font-weight: 400; font-size: 60px; line-height: 1.08; margin-top: 30px; }}
.titre em {{ color: var(--marron); }}
.txt {{ font-family: 'Montserrat'; font-weight: 300; font-size: 26px; line-height: 1.6; opacity: .82; margin-top: 30px; }}
.chute {{ font-family: 'Cormorant'; font-style: italic; font-weight: 500; font-size: 38px; line-height: 1.25; color: var(--marron); margin-top: 28px; }}
</style>
<img class="ph" src="{photo_uri(p)}">
<div class="bloc">
  <div class="haut"><div class="num">{esc(p['numero'])}</div><div class="label" style="color:var(--marron); opacity:.75">{esc(p['label'])}</div></div>
  <div class="titre">{esc(p['titre'])}</div>
  <div class="txt">{esc(p['texte'])}</div>
  <div class="chute">{esc(p['chute'])}</div>
  <div class="foot">
    {wordmark('--noir', '--marron')}
    <div class="handle" style="color:var(--marron); opacity:.6">@DELORIA.IA</div>
  </div>
</div>"""


def tpl_carte(p: dict) -> str:
    """Astuce d'accueil : grande photo en haut, bandeau noir en bas. Série du samedi."""
    cadrage = p.get("cadrage", "center")
    return f"""
<style>
body {{ background: var(--noir); color: var(--blanc); }}
.ph {{ position: absolute; left: 0; right: 0; top: 0; height: 700px; width: 100%; object-fit: cover; object-position: {cadrage}; }}
.bloc {{ position: absolute; left: 0; right: 0; top: 700px; bottom: 0; padding: 62px 110px 90px; display: flex; flex-direction: column; }}
.haut {{ display: flex; align-items: baseline; gap: 26px; }}
.num {{ font-family: 'Cormorant'; font-variant-numeric: lining-nums; font-weight: 300; font-size: 64px; line-height: .8; color: var(--or); }}
.titre {{ font-family: 'Cormorant'; font-weight: 300; font-size: 58px; line-height: 1.08; margin-top: 28px; }}
.titre em {{ color: var(--or); font-weight: 400; }}
.txt {{ font-family: 'Montserrat'; font-weight: 300; font-size: 25px; line-height: 1.6; color: var(--beige); opacity: .85; margin-top: 24px; }}
</style>
<img class="ph" src="{photo_uri(p)}">
<div class="bloc">
  <div class="haut"><div class="num">{esc(p['numero'])}</div><div class="label" style="color:var(--or)">{esc(p['label'])}</div></div>
  <div class="titre">{esc(p['titre'])}</div>
  <div class="txt">{esc(p['texte'])}</div>
  <div class="foot">
    {wordmark('--blanc', '--or')}
    <div class="handle" style="color:var(--beige); opacity:.55">@DELORIA.IA</div>
  </div>
</div>"""


TEMPLATES = {
    "constat": tpl_constat, "terrain": tpl_terrain, "service": tpl_service,
    "plein": tpl_plein, "edito": tpl_edito, "terrain_photo": tpl_terrain_photo,
    "carte": tpl_carte,
}


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
