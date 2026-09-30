"""Carrousels de présentation DelorIA + versions story + couvertures « à la une ».

Usage : python3 a-la-une/generer.py
Sortie : a-la-une/sortie/<serie>/post-01.jpg ... (1080x1440, 3:4)
         a-la-une/sortie/<serie>/story-01.jpg ... (1080x1920, 9:16)
         a-la-une/sortie/couvertures/<serie>.jpg (1080x1920)
         a-la-une/sortie/<serie>/legende.txt
"""
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ICI = Path(__file__).resolve().parent
REPO = ICI.parent
sys.path.insert(0, str(REPO / "templates"))
import render as R  # noqa: E402

SORTIE = ICI / "sortie"
TEL = "06 14 99 76 59"

SERIES = {
    "messagerie": {
        "photo": "photos/pexels/interieur-fenetre/12481521_el-jusuf.jpg",
        "credit": "El Jusuf",
        "label": "Messagerie voyageur",
        "slides": [
            {"type": "couverture", "titre": "Un voyageur écrit à 23h.", "chute": "Il a sa réponse à 23h."},
            {"type": "texte", "label": "Le constat",
             "texte": "Le code du portail.\nLa place de parking.\nL'heure d'arrivée.",
             "chute": "Chaque question est simple.\nEnsemble, elles prennent\nvos soirées."},
            {"type": "liste", "label": "Ce que je mets en place",
             "titre": "Un assistant qui répond\n*comme vous le feriez.*",
             "points": ["Dans la langue du voyageur, jour et nuit",
                        "Avec les informations de votre logement et son calendrier",
                        "Avec votre ton, jamais celui d'un robot",
                        "Un vrai problème ? Vous êtes prévenu aussitôt"]},
            {"type": "texte", "label": "Ce qu'il ne fait jamais",
             "texte": "Annoncer un prix.\nDonner un code d'accès.\nInventer une réponse.",
             "chute": "Quand il ne sait pas,\nil vous passe la main."},
            {"type": "cta", "titre": "Vous gardez la relation\navec vos voyageurs.\n*Vous retrouvez vos soirées.*"},
        ],
        "legende": (
            "Les questions des voyageurs arrivent à toute heure. Le parking, le wifi, l'heure d'arrivée.\n\n"
            "Je mets en place un assistant qui leur répond comme vous le feriez, dans leur langue, "
            "avec les informations de votre logement. Quand il ne sait pas, il vous prévient. Il n'invente rien.\n\n"
            "Vous gardez la relation. Vous retrouvez vos soirées.\n\n"
            "Une question ? Écrivez-moi en message privé.\n\n"
            "Photo : El Jusuf / Pexels\n\n"
            "#conciergerie #conciergerieairbnb #locationcourteduree #airbnb #hotes"
        ),
    },
    "reseaux": {
        "photo": "photos/pexels/details-carnet/7657385_cup-of-couple.jpg",
        "credit": "Cup of Couple",
        "voile": .6,
        "label": "Réseaux sociaux",
        "slides": [
            {"type": "couverture", "titre": "Publier chaque semaine.", "chute": "Sans y penser."},
            {"type": "texte", "label": "Le constat",
             "texte": "Il faudrait publier.\nLe soir, il y a plus urgent.",
             "chute": "Le compte reste vide\ndes semaines."},
            {"type": "liste", "label": "Ce que je mets en place",
             "titre": "Vos publications,\n*prêtes des mois à l'avance.*",
             "points": ["Un calendrier de posts, validé avec vous",
                        "Des visuels à vos couleurs, avec vos photos ou des photos libres de droits",
                        "Des textes écrits dans votre ton",
                        "Une publication automatique, à heure fixe"]},
            {"type": "texte", "label": "La preuve",
             "texte": "Ce compte fonctionne\nexactement comme ça.",
             "chute": "Un post chaque jour,\nsix mois préparés d'avance."},
            {"type": "cta", "titre": "Vous validez une fois.\n*Votre compte vit toute l'année.*"},
        ],
        "legende": (
            "Publier régulièrement demande un temps que personne n'a.\n\n"
            "Je prépare vos publications des mois à l'avance : le calendrier, les visuels à vos couleurs, "
            "les textes dans votre ton. Ensuite, elles partent seules, au jour et à l'heure prévus.\n\n"
            "Le fil de ce compte fonctionne ainsi.\n\n"
            "Une question ? Écrivez-moi en message privé.\n\n"
            "Photo : Cup of Couple / Pexels\n\n"
            "#reseauxsociaux #instagram #automatisation #communication #pme #entrepreneur"
        ),
    },
    "site": {
        "photo": "photos/pexels/secteur-bureau/8092459_https-kaboompics-com.jpg",
        "credit": "Kaboompics.com",
        "voile": .66,
        "label": "Site internet",
        "slides": [
            {"type": "couverture", "titre": "Un client vous cherche.", "chute": "Il tombe sur votre site."},
            {"type": "texte", "label": "Ce qui se joue",
             "texte": "En quelques secondes,\nil se fait une idée.\nSérieux ou daté.\nClair ou confus.",
             "chute": "Il décide avant même\nde vous appeler."},
            {"type": "liste", "label": "Ce que je construis",
             "titre": "Un site sur mesure,\n*à votre image.*",
             "points": ["Un design unique, fidèle à votre identité",
                        "Rapide et lisible sur téléphone",
                        "Des pages que vous modifiez seul, sans toucher au code",
                        "Les pages légales prévues dès le départ"]},
            {"type": "texte", "label": "Si vous partez de zéro",
             "texte": "Logo.\nCouleurs.\nTypographies.",
             "chute": "Je construis aussi\nvotre identité visuelle."},
            {"type": "cta", "titre": "Un projet de site\nou de logo ?\n*Parlons-en.*"},
        ],
        "legende": (
            "Avant de vous appeler, un client regarde votre site. En quelques secondes, il se fait une idée.\n\n"
            "Je construis des sites sur mesure, fidèles à votre identité, rapides sur téléphone, "
            "et que vous pouvez modifier seul. Si vous partez de zéro, je crée aussi le logo et la charte.\n\n"
            "Une question ? Écrivez-moi en message privé.\n\n"
            "Photo : Kaboompics.com / Pexels\n\n"
            "#siteinternet #identitevisuelle #chartegraphique #design #pme #entrepreneur"
        ),
    },
}

FORMATS = {
    # marges : haut, côtés, bas (story : zones sûres sous la barre et au-dessus du champ réponse)
    "post": {"w": 1080, "h": 1440, "haut": 110, "cote": 110, "bas": 110},
    "story": {"w": 1080, "h": 1920, "haut": 250, "cote": 110, "bas": 330},
}

ICONES_COUV = {
    "messagerie": '<path d="M3.5 5.5h17v11h-11l-4.5 3.5v-3.5h-1.5z"/><path d="M8 10.5h8M8 13.5h5"/>',
    "reseaux": '<rect x="4" y="4" width="16" height="16" rx="1"/><path d="M9.33 4v16M14.67 4v16M4 9.33h16M4 14.67h16"/>',
    "site": '<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 9h18"/><circle cx="5.6" cy="7" r=".4"/><circle cx="7.3" cy="7" r=".4"/><path d="M7 13h6M7 15.5h9"/>',
}


def css(f: dict) -> str:
    return R.BASE_CSS + f"""
html, body {{ width:{f['w']}px; height:{f['h']}px; }}
.frame {{ width:{f['w']}px; height:{f['h']}px; padding:{f['haut']}px {f['cote']}px {f['bas']}px; }}
.tete {{ display:flex; justify-content:space-between; align-items:baseline; position:relative; }}
.compteur {{ font-family:'Montserrat'; font-weight:400; font-size:19px; letter-spacing:.3em; font-variant-numeric:lining-nums; }}
.milieu {{ margin:auto 0; position:relative; }}
"""


def compteur(i: int, n: int, couleur: str, opacite: float = .6) -> str:
    return f'<div class="compteur" style="color:var({couleur});opacity:{opacite}">{i:02d} / {n:02d}</div>'


def couverture(s, sl, i, n, fmt, f):
    glisser = ""
    if fmt == "post":
        glisser = ('<div class="compteur" style="color:var(--beige);opacity:.85;display:flex;align-items:center;gap:14px">'
                   'FAITES GLISSER<svg width="34" height="14" viewBox="0 0 34 14" fill="none" stroke="#E8DDD0" stroke-width="1.4">'
                   '<path d="M0 7h32M26 1l6 6-6 6"/></svg></div>')
    return f"""
<style>
body {{ background:var(--noir); }}
.fond {{ position:absolute; inset:0; background:url('{(REPO / s['photo']).resolve().as_uri()}') center/cover; }}
.voile {{ position:absolute; inset:0; background:rgba(13,13,13,{s.get('voile', .5)}); }}
.cadre {{ position:absolute; inset:44px; border:1px solid rgba(250,250,248,.45); }}
.titre {{ font-family:'Cormorant'; font-weight:300; font-size:92px; line-height:1.08; color:var(--blanc); text-shadow:0 2px 24px rgba(0,0,0,.35); }}
.chute {{ font-family:'Cormorant'; font-style:italic; font-weight:400; font-size:92px; line-height:1.08; color:var(--or); margin-top:18px; text-shadow:0 2px 24px rgba(0,0,0,.35); }}
</style>
<div class="fond"></div><div class="voile"></div><div class="cadre"></div>
<div class="frame" style="align-items:center; text-align:center">
  <div class="label" style="color:var(--beige); position:relative">{R.esc(s['label'])}</div>
  <div class="milieu">
    <div class="titre">{R.esc(sl['titre'])}</div>
    <div class="chute">{R.esc(sl['chute'])}</div>
  </div>
  <div style="position:relative; display:flex; flex-direction:column; align-items:center; gap:22px">
    {R.ornament('--beige')}
    {R.wordmark('--blanc', '--or')}
    {glisser}
  </div>
</div>"""


def texte(s, sl, i, n, fmt, f):
    return f"""
<style>
body {{ background:var(--noir); color:var(--blanc); }}
.ring {{ position:absolute; border:1px solid var(--or); border-radius:50%; left:50%; top:50%; transform:translate(-50%,-50%); }}
.texte {{ font-family:'Cormorant'; font-weight:300; font-size:74px; line-height:1.14; }}
.chute {{ font-family:'Cormorant'; font-style:italic; font-weight:400; font-size:74px; line-height:1.12; color:var(--or); margin-top:56px; }}
</style>
<div class="ring" style="width:980px;height:980px;opacity:.07"></div>
<div class="ring" style="width:700px;height:700px;opacity:.11"></div>
<div class="frame">
  <div class="tete"><div class="label" style="color:var(--or)">{R.esc(sl['label'])}</div>{compteur(i, n, '--beige', .5)}</div>
  <div class="milieu">
    <div class="texte">{R.esc(sl['texte'])}</div>
    <div class="chute">{R.esc(sl['chute'])}</div>
  </div>
  <div class="foot" style="position:relative">
    {R.wordmark('--blanc', '--or')}
    <div class="handle" style="color:var(--beige); opacity:.55">@DELORIA.IA</div>
  </div>
</div>"""


def liste(s, sl, i, n, fmt, f):
    items = "".join(
        f'<div class="item"><div class="num">{k + 1:02d}</div><div>{R.esc(p)}</div></div>'
        for k, p in enumerate(sl["points"])
    )
    return f"""
<style>
body {{ background:var(--beige-clair); color:var(--noir); }}
.titre {{ font-family:'Cormorant'; font-weight:400; font-size:72px; line-height:1.1; }}
.titre em {{ color:var(--marron); }}
.sep {{ width:90px; height:1px; background:var(--marron); opacity:.45; margin:52px 0 46px; }}
.items {{ display:flex; flex-direction:column; gap:34px; }}
.item {{ display:flex; gap:30px; align-items:baseline; font-family:'Montserrat'; font-weight:300; font-size:34px; line-height:1.42; }}
.item .num {{ flex:none; width:58px; font-family:'Cormorant'; font-variant-numeric:lining-nums; font-weight:500; font-size:44px; color:var(--or); }}
</style>
<div class="frame">
  <div class="tete"><div class="label" style="color:var(--marron);opacity:.75">{R.esc(sl['label'])}</div>{compteur(i, n, '--marron', .55)}</div>
  <div class="milieu">
    <div class="titre">{R.esc(sl['titre'])}</div>
    <div class="sep"></div>
    <div class="items">{items}</div>
  </div>
  <div class="foot">
    {R.wordmark('--noir', '--marron')}
    <div class="handle" style="color:var(--marron); opacity:.6">@DELORIA.IA</div>
  </div>
</div>"""


def cta(s, sl, i, n, fmt, f):
    return f"""
<style>
body {{ background:var(--marron); color:var(--blanc); }}
.titre {{ font-family:'Cormorant'; font-weight:300; font-size:78px; line-height:1.12; }}
.titre em {{ color:var(--or); font-weight:400; }}
.contact {{ margin-top:70px; display:flex; flex-direction:column; gap:18px; }}
.contact .l1 {{ font-family:'Montserrat'; font-weight:300; font-size:31px; color:var(--beige); }}
.contact .l2 {{ font-family:'Cormorant'; font-variant-numeric:lining-nums; font-weight:400; font-size:62px; letter-spacing:.04em; color:var(--blanc); }}
</style>
<div class="frame">
  <div class="tete"><div class="label" style="color:var(--beige);opacity:.7">{R.esc(s['label'])}</div>{compteur(i, n, '--beige', .5)}</div>
  <div class="milieu">
    <div class="titre">{R.esc(sl['titre'])}</div>
    <div class="contact">
      {R.ornament('--or')}
      <div class="l1" style="margin-top:22px">Écrivez-moi en message privé, ou appelez-moi.</div>
      <div class="l2">{TEL}</div>
    </div>
  </div>
  <div class="foot">
    {R.wordmark('--blanc', '--or')}
    <div class="handle" style="color:var(--beige); opacity:.6">@DELORIA.IA</div>
  </div>
</div>"""


def couverture_une(nom: str) -> str:
    return f"""
<style>
html, body {{ width:1080px; height:1920px; background:var(--beige-clair); }}
.c {{ position:absolute; inset:0; display:flex; align-items:center; justify-content:center; }}
</style>
<div class="c"><svg width="360" height="360" viewBox="0 0 24 24" fill="none" stroke="#3B2314"
  stroke-width=".75" stroke-linecap="round" stroke-linejoin="round">{ICONES_COUV[nom]}</svg></div>"""


GABARITS = {"couverture": couverture, "texte": texte, "liste": liste, "cta": cta}


def main() -> None:
    blob = str(SERIES)
    for bad in ("—", "–"):
        assert bad not in blob, f"Tiret interdit : {bad!r}"
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        for fmt, f in FORMATS.items():
            page = nav.new_page(viewport={"width": f["w"], "height": f["h"]})
            for nom, s in SERIES.items():
                dossier = SORTIE / nom
                dossier.mkdir(parents=True, exist_ok=True)
                n = len(s["slides"])
                for i, sl in enumerate(s["slides"], 1):
                    corps = GABARITS[sl["type"]](s, sl, i, n, fmt, f)
                    h = dossier / "_t.html"
                    h.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{css(f)}</style></head>'
                                 f'<body>{corps}</body></html>', encoding="utf-8")
                    page.goto(h.as_uri())
                    page.evaluate("document.fonts.ready")
                    page.screenshot(path=str(dossier / f"{fmt}-{i:02d}.jpg"), type="jpeg", quality=92)
                    h.unlink()
                (dossier / "legende.txt").write_text(s["legende"] + "\n", encoding="utf-8")
            page.close()
        page = nav.new_page(viewport={"width": 1080, "height": 1920})
        (SORTIE / "couvertures").mkdir(parents=True, exist_ok=True)
        for nom in SERIES:
            h = SORTIE / "couvertures" / "_t.html"
            h.write_text(f'<!doctype html><html><head><meta charset="utf-8"><style>{R.BASE_CSS}</style></head>'
                         f'<body>{couverture_une(nom)}</body></html>', encoding="utf-8")
            page.goto(h.as_uri())
            page.screenshot(path=str(SORTIE / "couvertures" / f"{nom}.jpg"), type="jpeg", quality=92)
            h.unlink()
        nav.close()
    print("ok")


if __name__ == "__main__":
    main()
