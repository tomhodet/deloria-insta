"""Rendu des posts Instagram DelorIA : spec JSON -> HTML -> JPEG 1080x1350 (4:5).

Usage :
    python3 templates/render.py calendrier/2026-10/07.json      # un post
    python3 templates/render.py calendrier/20*/*.json           # tout le calendrier

Chaque spec JSON contient "template", "ton" (sombre | marron | clair) et les champs
du gabarit. Le JPEG est écrit à côté du JSON, même nom, extension .jpg.
Le ton est fixé par construire.py selon la position du post dans le fil, pour
que la grille du profil forme un damier clair / foncé traversé de diagonales marron.
Règles de charte appliquées ici, pas dans les specs : palette officielle,
Cormorant Garamond + Montserrat, "IA" toujours en italique, aucun tiret long,
aucun dégradé : les fonds photo reçoivent un voile uni.
"""

import html
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
FONTS = ROOT / "fonts"
REPO = ROOT.parent

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
.grade {{ filter: saturate(.86) sepia(.08) contrast(1.02); }}
"""

# Trois tons, un par famille de la grille. bg : fond ; txt : texte ; acc : italique d'accent ;
# lab : label ; doux : texte courant ; wm : couleurs du logotype ; num : numéros de série.
PAL = {
    "sombre": {"bg": "var(--noir)", "txt": "var(--blanc)", "acc": "var(--or)", "lab": "var(--or)",
               "doux": "var(--beige)", "wm": ("--blanc", "--or"), "num": "var(--or)", "ico": "#C9A96E",
               "trait": "rgba(232,221,208,.28)"},
    "marron": {"bg": "var(--marron)", "txt": "var(--blanc)", "acc": "var(--or)", "lab": "var(--beige)",
               "doux": "var(--beige)", "wm": ("--blanc", "--or"), "num": "var(--or)", "ico": "#C9A96E",
               "trait": "rgba(232,221,208,.28)"},
    "clair": {"bg": "var(--beige-clair)", "txt": "var(--noir)", "acc": "var(--marron)", "lab": "var(--marron)",
              "doux": "var(--noir)", "wm": ("--noir", "--marron"), "num": "var(--or)", "ico": "#3B2314",
              "trait": "rgba(59,35,20,.25)"},
}


def ton(p: dict, defaut: str = "sombre") -> str:
    t = p.get("ton", defaut)
    if t not in PAL:
        raise ValueError(f"Ton inconnu : {t!r}")
    return t


def esc(s: str) -> str:
    """Échappe le HTML, convertit *texte* en italique d'accent, insère les espaces insécables."""
    s = html.escape(s, quote=False).replace("'", "’")
    for signe in ("?", "!", ":", ";", "»"):
        s = s.replace(" " + signe, " " + signe)
    s = s.replace("« ", "« ")
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
    "grille": '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M9.33 4v16M14.67 4v16M4 9.33h16M4 14.67h16"/>',
    "ecran": '<rect x="3" y="5" width="18" height="12" rx="1"/><path d="M9 20h6M12 17v3"/>',
    "palette": '<circle cx="12" cy="12" r="9"/><circle cx="8.5" cy="10" r="1"/><circle cx="12" cy="7.5" r="1"/><circle cx="15.5" cy="10" r="1"/><path d="M12 21a3 3 0 0 1 0-6h2"/>',
    "courbe": '<path d="M4 19h16"/><path d="M5 16l4-5 3 3 6-7"/>',
    "fleche": '<path d="M5 12h14M13 6l6 6-6 6"/>',
}


def icone(nom: str, couleur: str, taille: int = 46) -> str:
    return (f'<svg width="{taille}" height="{taille}" viewBox="0 0 24 24" fill="none" stroke="{couleur}" '
            f'stroke-width="1.1" stroke-linecap="round" stroke-linejoin="round">{ICONES[nom]}</svg>')


def photo_uri(p: dict) -> str:
    chemin = (REPO / p["photo"]).resolve()
    if not chemin.is_file():
        raise FileNotFoundError(f"Photo introuvable : {chemin}")
    return chemin.as_uri()


def fond_photo(p: dict, t: str, voile: float) -> str:
    """Photo pleine page derrière le texte, voile uni, jamais de dégradé.
    sombre : noir et blanc assombri. marron : noir et blanc teinté marron de la charte."""
    if not p.get("photo"):
        return ""
    cadrage = p.get("cadrage", "center")
    v = p.get("voile", voile)
    img = (f'<img src="{photo_uri(p)}" style="position:absolute; inset:0; width:100%; height:100%; z-index:-1; '
           f'object-fit:cover; object-position:{cadrage}; filter:grayscale(1) contrast(1.06)">')
    if t == "marron":
        return (img + '<div style="position:absolute; inset:0; z-index:-1; background:#8A5A3C; mix-blend-mode:color"></div>'
                f'<div style="position:absolute; inset:0; z-index:-1; background:rgba(59,35,20,{v})"></div>')
    return img + f'<div style="position:absolute; inset:0; z-index:-1; background:rgba(13,13,13,{v})"></div>'


def taille_phrase(phrase: str) -> int:
    """Réduit la taille quand une ligne est longue, pour éviter les mots orphelins."""
    plus_longue = max(len(l.replace("*", "")) for l in phrase.split("\n"))
    return 88 if plus_longue <= 22 else 76 if plus_longue <= 26 else 66


def pied(pal: dict, position: str = "relative") -> str:
    return f"""<div class="foot" style="position:{position}">
    {wordmark(*pal['wm'])}
    <div class="handle" style="color:{pal['lab']}; opacity:.6">@DELORIA.IA</div>
  </div>"""


# ─────────────────────────────── Gabarits ───────────────────────────────

def tpl_constat(p: dict) -> str:
    """Un constat du quotidien, une chute en italique or. Fond photo noir et blanc (sombre) ou teinté (marron)."""
    t = ton(p)
    pal = PAL[t]
    fond = fond_photo(p, t, 0.6 if t == "sombre" else 0.72)
    anneaux = "" if fond else ('<div class="ring r1"></div><div class="ring r2"></div>')
    return f"""
<style>
body {{ background: {pal['bg']}; color: var(--blanc); }}
.ring {{ position: absolute; border: 1px solid var(--or); border-radius: 50%; left: 50%; top: 46%; transform: translate(-50%, -50%); }}
.r1 {{ width: 980px; height: 980px; opacity: 0.07; }}
.r2 {{ width: 700px; height: 700px; opacity: 0.11; }}
.body {{ margin-top: auto; margin-bottom: auto; position: relative; }}
.texte {{ font-family: 'Cormorant'; font-weight: 300; font-size: {92 if len(p['texte']) <= 40 else 76}px; line-height: 1.1; letter-spacing: 0.01em; }}
.chute {{ font-family: 'Cormorant'; font-style: italic; font-weight: 400; font-size: {96 if len(p['chute']) <= 24 else 84}px; line-height: 1.08; color: var(--or); margin-top: 44px; }}
</style>
<div class="frame">
  {fond or anneaux}
  <div class="label" style="color:{pal['lab']}; position:relative">{esc(p['label'])}</div>
  <div class="body">
    <div class="texte">{esc(p['texte'])}</div>
    <div class="chute">{esc(p['chute'])}</div>
  </div>
  {pied(pal)}
</div>"""


def tpl_service(p: dict) -> str:
    """Titre et trois points maximum sur fond photo teinté marron (ou noir et blanc en ton sombre)."""
    t = ton(p, "marron")
    pal = PAL[t]
    items = "".join(
        f'<div class="item"><div class="d"></div><div>{esc(i)}</div></div>'
        for i in p["points"][:3]
    )
    return f"""
<style>
body {{ background: {pal['bg']}; color: var(--blanc); }}
.titre {{ font-family: 'Cormorant'; font-weight: 300; font-size: 82px; line-height: 1.1; margin-top: 90px; }}
.titre em {{ color: var(--or); font-weight: 400; }}
.items {{ margin-top: 80px; display: flex; flex-direction: column; gap: 38px; }}
.item {{ display: flex; align-items: baseline; gap: 30px; font-family: 'Montserrat'; font-weight: 300; font-size: 33px; line-height: 1.45; color: var(--beige); }}
.item .d {{ flex: none; width: 10px; height: 10px; background: var(--or); transform: rotate(45deg) translateY(-6px); }}
</style>
<div class="frame">
  {fond_photo(p, t, 0.84 if t == "marron" else 0.66)}
  <div class="label" style="color:var(--beige); opacity:.75">{esc(p['label'])}</div>
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


def tpl_plein(p: dict) -> str:
    """Photo pleine page, filet intérieur, une phrase centrée. Couleur retouchée (sombre) ou teintée (marron)."""
    t = ton(p)
    cadrage = p.get("cadrage", "center")
    if t == "marron":
        fond = fond_photo(p, "marron", 0.64)
        em = "var(--or)"
    else:
        fond = (f'<img class="bg grade" src="{photo_uri(p)}">'
                f'<div class="voile" style="background: rgba(13,13,13,{p.get("voile", 0.42)})"></div>')
        em = "var(--beige)"
    return f"""
<style>
body {{ background: var(--noir); }}
.bg {{ position: absolute; inset: 0; width: 100%; height: 100%; object-fit: cover; object-position: {cadrage}; }}
.voile {{ position: absolute; inset: 0; }}
.filet {{ position: absolute; inset: 44px; border: 1px solid rgba(250,250,248,.55); }}
.centre {{ position: absolute; inset: 0; transform: translateY({p.get('decalage', 0)}px); display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; padding: 0 130px; color: var(--blanc); }}
.lieu {{ font-family: 'Montserrat'; font-weight: 400; font-size: 22px; letter-spacing: .38em; text-transform: uppercase; opacity: .9; margin-bottom: 34px; }}
.phrase {{ font-family: 'Cormorant'; font-weight: 300; font-size: {taille_phrase(p['phrase'])}px; line-height: 1.08; text-shadow: 0 2px 24px rgba(0,0,0,.45), 0 0 2px rgba(0,0,0,.3); }}
.phrase em {{ font-weight: 400; color: {em}; }}
.bas {{ position: absolute; left: 0; right: 0; bottom: 96px; display: flex; flex-direction: column; align-items: center; gap: 20px; }}
</style>
{fond}
<div class="filet"></div>
<div class="centre">
  {f'<div class="lieu">{esc(p["lieu"])}</div>' if p.get('lieu') else ''}
  <div class="phrase">{esc(p['phrase'])}</div>
</div>
<div class="bas">
  {ornament('--beige')}
  {wordmark('--blanc', '--or')}
</div>"""


def tpl_arche(p: dict) -> str:
    """Ton clair : fond beige clair, photo dans une arche, texte noir et italique marron.
    Accepte une phrase, un constat (texte + chute) ou une liste (titre + points)."""
    pal = PAL["clair"]
    label = p.get("label") or p.get("lieu") or ""
    photo = f'<img class="arche grade" src="{photo_uri(p)}" style="object-position:{p.get("cadrage", "center")}">'
    if p.get("points"):
        items = "".join(f'<div class="item"><div class="d"></div><div>{esc(i)}</div></div>' for i in p["points"][:3])
        corps = f"""
<div class="liste">
  <div class="gauche">
    <div class="label" style="color:{pal['lab']}; opacity:.8">{esc(label)}</div>
    <div class="titre">{esc(p['titre'])}</div>
    <div class="items">{items}</div>
  </div>
  {photo}
</div>"""
        css = """
.liste { position: absolute; left: 110px; right: 96px; top: 150px; bottom: 250px; display: flex; gap: 56px; align-items: center; }
.gauche { flex: 1; display: flex; flex-direction: column; }
.titre { font-family: 'Cormorant'; font-weight: 400; font-size: 62px; line-height: 1.08; margin-top: 34px; }
.titre em { color: var(--marron); }
.items { margin-top: 52px; display: flex; flex-direction: column; gap: 30px; }
.item { display: flex; align-items: baseline; gap: 22px; font-family: 'Montserrat'; font-weight: 300; font-size: 27px; line-height: 1.45; }
.item .d { flex: none; width: 9px; height: 9px; background: var(--or); transform: rotate(45deg) translateY(-5px); }
.arche { flex: none; width: 360px; height: 620px; object-fit: cover; border-radius: 180px 180px 0 0; }
"""
    else:
        if p.get("phrase"):
            lignes = p["phrase"]
            texte = f'<div class="texte">{esc(lignes)}</div>'
            n = len(lignes.replace("*", ""))
        else:
            texte = f'<div class="texte">{esc(p["texte"])}</div><div class="chute">{esc(p["chute"])}</div>'
            n = len(p["texte"]) + len(p["chute"])
        taille = 66 if n <= 48 else 58 if n <= 78 else 50
        corps = f"""
<div class="haut"><div class="label" style="color:{pal['lab']}; opacity:.8">{esc(label)}</div></div>
<div class="centre">{photo}<div class="bloc">{texte}</div></div>"""
        css = f"""
.haut {{ position: absolute; left: 0; right: 0; top: 104px; text-align: center; }}
.centre {{ position: absolute; left: 0; right: 0; top: 168px; display: flex; flex-direction: column; align-items: center; }}
.arche {{ width: 520px; height: 600px; object-fit: cover; border-radius: 260px 260px 0 0; }}
.bloc {{ margin-top: 46px; padding: 0 120px; text-align: center; }}
.texte {{ font-family: 'Cormorant'; font-weight: 300; font-size: {taille}px; line-height: 1.1; }}
.texte em, .chute {{ font-style: italic; font-weight: 400; color: var(--marron); }}
.chute {{ font-family: 'Cormorant'; font-size: {taille}px; line-height: 1.1; margin-top: 10px; }}
"""
    return f"""
<style>
body {{ background: {pal['bg']}; color: {pal['txt']}; }}
.filet {{ position: absolute; inset: 44px; border: 1px solid {pal['trait']}; }}
.bas {{ position: absolute; left: 0; right: 0; bottom: 92px; display: flex; flex-direction: column; align-items: center; gap: 20px; }}
{css}
</style>
<div class="filet"></div>
{corps}
<div class="bas">
  {ornament('--or')}
  {wordmark(*pal['wm'])}
</div>"""


def tpl_edito(p: dict) -> str:
    """Texte à gauche, photo à droite, rangée de 3 pictos. Esprit magazine. Fond selon le ton."""
    t = ton(p, "clair")
    pal = PAL[t]
    cadrage = p.get("cadrage", "center")
    pictos = "".join(
        f'<div class="picto">{icone(i["icone"], pal["ico"])}<div class="pl">{esc(i["texte"])}</div></div>'
        for i in p["pictos"][:3]
    )
    cta = f'<div class="cta">{esc(p["cta"])}</div>' if p.get("cta") else ""
    return f"""
<style>
body {{ background: {pal['bg']}; color: {pal['txt']}; }}
.g {{ position: absolute; left: 0; top: 0; bottom: 0; width: 540px; padding: 100px 56px 90px 76px; display: flex; flex-direction: column; }}
.ph {{ position: absolute; right: 0; top: 0; width: 540px; height: {H}px; object-fit: cover; object-position: {cadrage}; }}
.wm {{ font-size: 32px; }}
.lab {{ margin-top: 74px; font-family: 'Montserrat'; font-weight: 500; font-size: 16px; letter-spacing: .4em; text-transform: uppercase; color: var(--or); }}
.titre {{ font-family: 'Cormorant'; font-weight: 400; font-size: 64px; line-height: 1.04; margin-top: 26px; }}
.titre em {{ color: {'var(--or)' if t != 'clair' else 'var(--marron)'}; }}
.sep {{ width: 60px; height: 1px; background: {pal['txt']}; opacity: .35; margin: 36px 0 30px; }}
.txt {{ font-family: 'Montserrat'; font-weight: 300; font-size: 22px; line-height: 1.6; opacity: .85; color: {pal['doux']}; }}
.pictos {{ margin-top: auto; display: grid; grid-template-columns: repeat(3, 1fr); }}
.picto {{ display: flex; flex-direction: column; align-items: center; gap: 16px; text-align: center; padding: 0 8px; }}
.picto + .picto {{ border-left: 1px solid {pal['trait']}; }}
.pl {{ font-family: 'Montserrat'; font-weight: 500; font-size: 13px; letter-spacing: .14em; line-height: 1.5; text-transform: uppercase; color: {pal['lab'] if t == 'clair' else 'var(--beige)'}; }}
.cta {{ margin-top: 48px; align-self: flex-start; border: 1px solid {pal['txt']}; border-radius: 40px; padding: 18px 34px; font-family: 'Montserrat'; font-weight: 500; font-size: 15px; letter-spacing: .32em; text-transform: uppercase; }}
</style>
<div class="g">
  {wordmark(*pal['wm'])}
  <div class="lab">{esc(p['label'])}</div>
  <div class="titre">{esc(p['titre'])}</div>
  <div class="sep"></div>
  <div class="txt">{esc(p['texte'])}</div>
  <div class="pictos">{pictos}</div>
  {cta}
</div>
<img class="ph grade" src="{photo_uri(p)}">"""


def bandeau(p: dict, hauteur: int, t: str, titre_px: int, txt_px: int, num_px: int, chute: bool) -> str:
    """Photo en haut, bandeau de texte en bas, couleur du bandeau selon le ton."""
    pal = PAL[t]
    cadrage = p.get("cadrage", "center")
    em = "var(--marron)" if t == "clair" else "var(--or)"
    ch = (f'<div class="chute">{esc(p["chute"])}</div>' if chute and p.get("chute") else "")
    return f"""
<style>
body {{ background: {pal['bg']}; color: {pal['txt']}; }}
.ph {{ position: absolute; left: 0; right: 0; top: 0; height: {hauteur}px; width: 100%; object-fit: cover; object-position: {cadrage}; }}
.bloc {{ position: absolute; left: 0; right: 0; top: {hauteur}px; bottom: 0; padding: 62px 110px 92px; display: flex; flex-direction: column; }}
.haut {{ display: flex; align-items: baseline; gap: 30px; }}
.num {{ font-family: 'Cormorant'; font-variant-numeric: lining-nums; font-weight: 300; font-size: {num_px}px; line-height: .8; color: {pal['num']}; }}
.titre {{ font-family: 'Cormorant'; font-weight: {400 if t == 'clair' else 300}; font-size: {titre_px}px; line-height: 1.08; margin-top: 28px; }}
.titre em {{ color: {em}; font-weight: 400; }}
.txt {{ font-family: 'Montserrat'; font-weight: 300; font-size: {txt_px}px; line-height: 1.6; color: {pal['doux']}; opacity: .85; margin-top: 26px; }}
.chute {{ font-family: 'Cormorant'; font-style: italic; font-weight: 500; font-size: 38px; line-height: 1.25; color: {em}; margin-top: 26px; }}
</style>
<img class="ph grade" src="{photo_uri(p)}">
<div class="bloc">
  <div class="haut"><div class="num">{esc(p['numero'])}</div><div class="label" style="color:{pal['lab'] if t != 'sombre' else 'var(--or)'}; opacity:.85">{esc(p['label'])}</div></div>
  <div class="titre">{esc(p['titre'])}</div>
  <div class="txt">{esc(p['texte'])}</div>
  {ch}
  {pied(pal, 'static')}
</div>"""


def tpl_terrain_photo(p: dict) -> str:
    """Note de série (terrain, ingénieur, design) : bandeau photo en haut, texte en bas."""
    return bandeau(p, 520, ton(p, "clair"), 60, 26, 96, True)


def tpl_carte(p: dict) -> str:
    """Astuce du samedi : grande photo en haut, bandeau en bas."""
    return bandeau(p, 700, ton(p, "sombre"), 58, 25, 64, False)


def tpl_slide(p: dict) -> str:
    """Page intérieure de carrousel : numéro, titre, texte, sur fond texture teinté selon le ton."""
    t = ton(p, "clair")
    pal = PAL[t]
    if p.get("photo") and t != "clair":
        fond = fond_photo(p, t, 0.82 if t == "marron" else 0.8)
    elif p.get("photo"):
        fond = (f'<img class="grade" src="{photo_uri(p)}" style="position:absolute; inset:0; width:100%; height:100%; '
                f'z-index:-1; object-fit:cover"><div style="position:absolute; inset:0; z-index:-1; background:rgba(244,238,230,.84)"></div>')
    else:
        fond = ""
    em = "var(--marron)" if t == "clair" else "var(--or)"
    return f"""
<style>
body {{ background: {pal['bg']}; color: {pal['txt']}; }}
.tete {{ display: flex; justify-content: space-between; align-items: baseline; }}
.compteur {{ font-family: 'Montserrat'; font-weight: 400; font-size: 19px; letter-spacing: .3em; font-variant-numeric: lining-nums; color: {pal['lab']}; opacity: .6; }}
.milieu {{ margin: auto 0; }}
.num {{ font-family: 'Cormorant'; font-variant-numeric: lining-nums; font-weight: 300; font-size: 150px; line-height: .9; color: var(--or); }}
.titre {{ font-family: 'Cormorant'; font-weight: {400 if t == 'clair' else 300}; font-size: 76px; line-height: 1.08; margin-top: 34px; }}
.titre em {{ color: {em}; font-weight: 400; }}
.sep {{ width: 90px; height: 1px; background: var(--or); margin: 46px 0 40px; }}
.txt {{ font-family: 'Montserrat'; font-weight: 300; font-size: 34px; line-height: 1.55; color: {pal['doux']}; opacity: .9; }}
</style>
<div class="frame">
  {fond}
  <div class="tete"><div class="label" style="color:{pal['lab']}; opacity:.8">{esc(p['label'])}</div><div class="compteur">{esc(p['compteur'])}</div></div>
  <div class="milieu">
    <div class="num">{esc(p['numero'])}</div>
    <div class="titre">{esc(p['titre'])}</div>
    <div class="sep"></div>
    <div class="txt">{esc(p['texte'])}</div>
  </div>
  {pied(pal)}
</div>"""


def tpl_slide_fin(p: dict) -> str:
    """Dernière page de carrousel : la phrase qui reste, et comment me joindre."""
    t = ton(p, "marron")
    pal = PAL[t]
    fond = fond_photo(p, t if t != "clair" else "marron", 0.84) if p.get("photo") else ""
    if t == "clair":
        pal = PAL["marron"]
    return f"""
<style>
body {{ background: {pal['bg']}; color: var(--blanc); }}
.tete {{ display: flex; justify-content: space-between; align-items: baseline; }}
.compteur {{ font-family: 'Montserrat'; font-weight: 400; font-size: 19px; letter-spacing: .3em; color: var(--beige); opacity: .6; }}
.milieu {{ margin: auto 0; }}
.titre {{ font-family: 'Cormorant'; font-weight: 300; font-size: 80px; line-height: 1.1; }}
.titre em {{ color: var(--or); font-weight: 400; }}
.contact {{ margin-top: 64px; display: flex; flex-direction: column; gap: 18px; }}
.l1 {{ font-family: 'Montserrat'; font-weight: 300; font-size: 31px; color: var(--beige); margin-top: 22px; }}
.l2 {{ font-family: 'Cormorant'; font-variant-numeric: lining-nums; font-weight: 400; font-size: 62px; letter-spacing: .04em; }}
</style>
<div class="frame">
  {fond}
  <div class="tete"><div class="label" style="color:var(--beige); opacity:.75">{esc(p['label'])}</div><div class="compteur">{esc(p['compteur'])}</div></div>
  <div class="milieu">
    <div class="titre">{esc(p['titre'])}</div>
    <div class="contact">
      {ornament('--or')}
      <div class="l1">Écrivez-moi en message privé, ou appelez-moi.</div>
      <div class="l2">06 14 99 76 59</div>
    </div>
  </div>
  {pied(PAL['marron'])}
</div>"""


def tpl_terrain(p: dict) -> str:
    """Ancien gabarit sur fond uni, conservé pour compatibilité : rendu en note à bandeau photo si photo."""
    if p.get("photo"):
        return tpl_terrain_photo(p)
    raise ValueError("Le gabarit 'terrain' sans photo n'est plus utilisé")


TEMPLATES = {
    "constat": tpl_constat, "service": tpl_service, "plein": tpl_plein, "arche": tpl_arche,
    "edito": tpl_edito, "terrain_photo": tpl_terrain_photo, "carte": tpl_carte, "terrain": tpl_terrain,
    "slide": tpl_slide, "slide_fin": tpl_slide_fin,
}


def build_html(spec: dict) -> str:
    check_text(spec)
    gabarit = spec["template"]
    if gabarit in ("plein", "constat", "service") and spec.get("ton") == "clair":
        gabarit = "arche"
    body = TEMPLATES[gabarit](spec)
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
    render([Path(a).resolve() for a in sys.argv[1:] if not a.endswith("calendrier.json")])
