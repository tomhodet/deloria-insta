"""Série « Vos questions » : carrousels de 5 slides au format 4:5 (1080x1350).

Structure de chaque carrousel :
  1. couverture : la question entre guillemets, étiquette « Vos questions », « Faites défiler »
  2 à 4. trois questions/réponses numérotées 01/03 à 03/03, sur la même photo
     panoramique qui défile d'une slide à l'autre
  5. conclusion : une phrase, le site, l'invitation à écrire en message privé

Usage : python3 questions/generer.py            # rend les 5 carrousels dans questions/<id>/
        python3 questions/generer.py q3         # un seul
Les photos (Pexels) sont dans questions/photos/, le logo dans questions/logo-deloria.png.
"""

import html
import re
import json
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright
from PIL import Image

ICI = Path(__file__).resolve().parent
REPO = ICI.parent
FONTS = REPO / "templates" / "fonts"
PHOTOS = ICI / "photos"
LOGO = (ICI / "logo-deloria.png").as_uri()
W, H = 1080, 1350

CARROUSELS = [
    {
        "id": "q1",
        "pano": {"photo": "15070806", "y": 0.55},
        "fin_photo": {"photo": "36411723", "x": 0.5, "y": 0.5},
        "question": "« Et si l’assistant\n*se trompe* ? »",
        "qr": [
            ("« Il invente une réponse ? »",
             "Jamais. Quand une information n’est pas dans ses données, il ne devine pas. "
             "Il fait patienter le voyageur et vous prévient aussitôt.", "haut"),
            ("« Il annonce un prix ? »",
             "Non plus. Le montant exact s’affiche sur l’annonce, frais compris. "
             "Il y renvoie le voyageur, pour qu’aucun total ne soit jamais faux.", "bas"),
            ("« Et s’il y a un vrai problème ? »",
             "Une panne, une clé introuvable : vous êtes alerté tout de suite, avec le motif. "
             "Le voyageur, lui, sait que c’est pris en main.", "haut"),
        ],
        "fin": "Il répond.\n*Vous décidez.*",
        "mot": "DÉMO",
    },
    {
        "id": "q2",
        "pano": {"photo": "18295808", "y": 0.5},
        "fin_photo": {"photo": "9220877", "x": 0.5, "y": 0.5},
        "question": "« Ça se verra\nque *ce n’est pas moi* ? »",
        "qr": [
            ("« Il écrit comme moi ? »",
             "Il est réglé sur votre ton : vouvoiement, longueur des réponses, chaleur. "
             "Pas de formules toutes faites, jamais deux messages identiques.", "haut"),
            ("« Et un voyageur allemand ? »",
             "Il répond dans la langue du message reçu. Allemand, anglais, italien, "
             "sans que vous ayez à traduire quoi que ce soit.", "bas"),
            ("« Il connaît le logement ? »",
             "Le wifi, l’arrivée, le règlement, les disponibilités. Il s’appuie sur la fiche "
             "du logement, mise à jour là où vous la tenez déjà.", "haut"),
        ],
        "fin": "Votre voix,\n*même la nuit.*",
        "mot": "DÉMO",
    },
    {
        "id": "q3",
        "pano": {"photo": "18297089", "y": 0.5},
        "fin_photo": {"photo": "4626268", "x": 0.5, "y": 0.5},
        "question": "« Un message\nà *23h*, en août ? »",
        "qr": [
            ("« Qui répond, à cette heure-là ? »",
             "Aujourd’hui, c’est vous. Pendant le dîner, entre deux arrivées, "
             "parfois déjà couché.", "haut"),
            ("« Et demain ? »",
             "L’assistant répond à 23h comme à 9h. Le voyageur a sa réponse en quelques minutes, "
             "vous gardez votre soirée.", "bas"),
            ("« Il répond même pour rien ? »",
             "Non. Un simple merci n’appelle pas trois lignes. Quand aucune réponse n’est utile, "
             "il n’écrit rien.", "haut"),
        ],
        "fin": "Vos soirées\n*vous reviennent.*",
        "mot": "DÉMO",
    },
    {
        "id": "q4",
        "pano": {"photo": "13625709", "y": 0.5},
        "fin_photo": {"photo": "7174386", "x": 0.5, "y": 0.5},
        "question": "« Il peut *vendre*\nmes services ? »",
        "qr": [
            ("« Il les connaît ? »",
             "Petit-déjeuner, vélos, ménage, sorties : vous lui listez vos services. "
             "Il les évoque quand la conversation s’y prête.", "haut"),
            ("« Sans forcer ? »",
             "Une seule proposition à la fois, jamais d’insistance. "
             "Le voyageur ne se sent pas démarché.", "bas"),
            ("« Et quand le voyageur dit oui ? »",
             "Vous êtes prévenu aussitôt, avec le service, la date, l’heure et le nombre "
             "de personnes. Il ne reste qu’à confirmer.", "haut"),
        ],
        "fin": "Chaque message\npeut *rapporter.*",
        "mot": "DÉMO",
    },
    {
        "id": "q5",
        "pano": {"photo": "567186", "y": 0.6},
        "fin_photo": {"photo": "276508", "x": 0.5, "y": 0.5},
        "question": "« Je dois *changer*\nmes outils ? »",
        "qr": [
            ("« Mes comptes, mes accès ? »",
             "Tout reste à votre nom. Votre outil de réservation et vos annonces "
             "ne changent pas de propriétaire.", "haut"),
            ("« Et les codes d’accès ? »",
             "L’assistant ne les connaît pas. Ils partent comme aujourd’hui, la veille "
             "de l’arrivée, par vos messages programmés.", "bas"),
            ("« Et Airbnb, dans tout ça ? »",
             "Il n’écrit jamais de lien ni de numéro, que la plateforme bloquerait. "
             "Chaque message arrive bien au voyageur.", "haut"),
        ],
        "fin": "Vous gardez tout.\n*Sauf la charge.*",
        "mot": "DÉMO",
    },
    {
        "id": "q6",
        "pano": {"photo": "27536617", "y": 0.55},
        "fin_photo": {"photo": "7546599", "x": 0.5, "y": 0.5},
        "question": "« Votre location,\nsur quel *outil* ? »",
        "qr": [
            ("« Un channel manager, c’est quoi ? »",
             "Un seul calendrier pour toutes les plateformes. Node, par exemple, relie Airbnb, "
             "Booking, Vrbo et Expedia au même endroit.", "haut"),
            ("« Et les doubles réservations ? »",
             "Une réservation tombe sur Airbnb : selon Node, les autres calendriers se mettent à jour "
             "en moins de 30 secondes. C’est ce délai qui les évite.", "bas"),
            ("« Et moi, propriétaire ? »",
             "Un portail propriétaire vous laisse suivre vos réservations vous-même, "
             "sans attendre qu’on vous envoie les chiffres.", "haut"),
        ],
        "fin": "L’outil synchronise.\n*Vous, vous accueillez.*",
        "mot": "DÉMO",
    },
    {
        "id": "q7",
        "pano": {"photo": "7174113", "y": 0.5},
        "fin_photo": {"photo": "8135118", "x": 0.5, "y": 0.5},
        "question": "« Un voyageur *casse*\nquelque chose ? »",
        "qr": [
            ("« Que faire en premier ? »",
             "Photographier tout de suite, avant le ménage suivant. Photos, vidéos, devis, factures : "
             "ce sont les preuves qui comptent.", "haut"),
            ("« Il y a un délai ? »",
             "Oui. Sur Airbnb, la demande se fait dans les 14 jours qui suivent le départ du voyageur, "
             "par le Centre de résolution.", "bas"),
            ("« Et si le voyageur refuse ? »",
             "Il a 24 heures pour répondre. S’il refuse, paie en partie ou se tait, "
             "Airbnb peut intervenir.", "haut"),
        ],
        "fin": "Un dossier prêt,\n*avant d’en avoir besoin.*",
        "mot": "DÉMO",
    },
]

CSS = f"""
@font-face {{ font-family: 'Cormorant'; src: url('{(FONTS / 'CormorantGaramond.ttf').as_uri()}'); font-weight: 300 700; font-style: normal; }}
@font-face {{ font-family: 'Cormorant'; src: url('{(FONTS / 'CormorantGaramond-Italic.ttf').as_uri()}'); font-weight: 300 700; font-style: italic; }}
@font-face {{ font-family: 'Montserrat'; src: url('{(FONTS / 'Montserrat.ttf').as_uri()}'); font-weight: 100 900; }}
:root {{ --noir:#0D0D0D; --blanc:#FAFAF8; --beige:#E8DDD0; --or:#C9A96E; }}
* {{ margin:0; padding:0; box-sizing:border-box; }}
html, body {{ width:{W}px; height:{H}px; overflow:hidden; background:var(--noir); }}
body {{ font-family:'Montserrat',sans-serif; -webkit-font-smoothing:antialiased; color:var(--blanc); }}
.s {{ position:relative; width:{W}px; height:{H}px; overflow:hidden; }}
.bg {{ position:absolute; inset:0; background-repeat:no-repeat; filter:saturate(.9) contrast(1.03); }}
.ov {{ position:absolute; inset:0; }}
.halo {{ position:absolute; left:50%; transform:translateX(-50%); width:520px; height:360px;
  background:radial-gradient(closest-side,rgba(13,13,13,.62),rgba(13,13,13,0)); }}
.logo {{ position:absolute; left:50%; transform:translateX(-50%); filter:drop-shadow(0 4px 18px rgba(0,0,0,.75)) drop-shadow(0 0 2px rgba(0,0,0,.6)); }}
.tag {{ position:absolute; left:50%; transform:translateX(-50%); display:flex; align-items:center; gap:14px;
  padding:14px 30px; border:1.5px solid rgba(250,250,248,.55); border-radius:999px; background:rgba(13,13,13,.38);
  backdrop-filter:blur(6px); font-weight:600; font-size:23px; letter-spacing:.14em; text-transform:uppercase; white-space:nowrap; }}
.tag i {{ width:11px; height:11px; border-radius:50%; background:var(--or); display:block; }}
.rule {{ width:96px; height:4px; background:var(--or); border-radius:2px; }}
.big {{ font-family:'Cormorant'; font-weight:700; color:var(--blanc); text-wrap:balance;
  text-shadow:0 4px 34px rgba(0,0,0,.7), 0 2px 6px rgba(0,0,0,.5); }}
.big em, .t em {{ font-style:italic; color:var(--or); }}
.ln {{ display:block; }}
.defile {{ position:absolute; left:84px; bottom:86px; font-weight:600; font-size:22px; letter-spacing:.24em; color:var(--or);
  text-transform:uppercase; text-shadow:0 2px 12px rgba(0,0,0,.8); display:flex; align-items:center; gap:16px; }}
.defile b {{ display:block; width:60px; height:2px; background:var(--or); }}
.cpt {{ position:absolute; top:62px; right:70px; padding:10px 20px; border-radius:999px; background:rgba(13,13,13,.5); font-weight:500; font-size:24px; letter-spacing:.18em; color:var(--beige);
  text-shadow:0 2px 10px rgba(0,0,0,.8); }}
.cpt span {{ color:var(--or); }}
.bloc {{ position:absolute; left:84px; right:84px; }}
.bloc.panneau {{ background:rgba(13,13,13,.58); backdrop-filter:blur(8px); padding:56px 56px 60px; border-radius:6px;
  border:1px solid rgba(201,169,110,.25); left:64px; right:64px; }}
.t {{ font-family:'Cormorant'; font-weight:700; font-size:78px; line-height:1.02; text-wrap:balance;
  text-shadow:0 4px 30px rgba(0,0,0,.65); }}
.p {{ font-weight:400; font-size:35px; line-height:1.5; color:var(--blanc); text-wrap:pretty;
  text-shadow:0 2px 16px rgba(0,0,0,.75); }}
.site {{ font-family:'Cormorant'; font-weight:700; font-size:92px; letter-spacing:.01em; color:var(--or);
  text-shadow:0 4px 28px rgba(0,0,0,.7); text-align:center; }}
.pill {{ display:inline-block; padding:20px 40px; border-radius:999px; background:rgba(13,13,13,.62); border:1.5px solid rgba(250,250,248,.6);
  font-weight:600; font-size:28px; letter-spacing:.03em; white-space:nowrap; }}
.petit {{ font-weight:400; font-size:24px; letter-spacing:.06em; color:var(--beige); text-shadow:0 2px 10px rgba(0,0,0,.8); }}
.handle {{ font-weight:500; font-size:21px; letter-spacing:.34em; color:var(--beige); }}
.c {{ position:absolute; left:0; right:0; display:flex; flex-direction:column; align-items:center; text-align:center; }}
"""


def esc(s: str) -> str:
    s = html.escape(s, quote=False)
    for signe in ("?", "!", ":", ";", "»"):
        s = s.replace(" " + signe, " " + signe)
    s = s.replace("« ", "« ")
    s = re.sub(r"(\d) (?=\w)", "\\1\u00a0", s)   # « 14 jours » ne se coupe jamais
    out, it = [], False
    for part in s.split("*"):
        out.append(("<em>" if it else "") + part + ("</em>" if it else ""))
        it = not it
    return "".join(out)


def lignes(s: str) -> str:
    out, ouvert = [], False
    for l in esc(s).split("\n"):
        if ouvert:
            l = "<em>" + l
        ouvert = l.count("<em>") > l.count("</em>")
        if ouvert:
            l += "</em>"
        out.append(f'<span class="ln">{l}</span>')
    return "".join(out)


def fond(photo: str, i: int | None = None, n: int = 4, x: float = 0.5, y: float = 0.5, zoom: float = 1.0) -> str:
    """Style de fond. Avec i, la photo est mise à la hauteur de la slide et une fenêtre de
    1080 px glisse de gauche à droite sur les n slides : la photo continue d'une slide à l'autre."""
    f = PHOTOS / f"{photo}.jpg"
    pw, ph = Image.open(f).size
    if i is None:
        s = max(W / pw, H / ph) * zoom
        sw, sh = pw * s, ph * s
        ox, oy = (sw - W) * x, (sh - H) * y
    else:
        s = H / ph * zoom
        sw, sh = pw * s, ph * s
        if sw < W * 1.6:   # photo trop étroite pour défiler : on agrandit un peu
            s *= W * 1.6 / sw
            sw, sh = pw * s, ph * s
        ox = (sw - W) * i / (n - 1)
        oy = (sh - H) * y
    return (f"background-image:url('{f.as_uri()}');background-size:{sw:.1f}px {sh:.1f}px;"
            f"background-position:{-ox:.1f}px {-oy:.1f}px;")


def couverture(c: dict) -> str:
    p = c["pano"]
    return f"""<div class="s"><div class="bg" style="{fond(p['photo'], 0, y=p['y'])}"></div>
<div class="ov" style="background:linear-gradient(180deg,rgba(13,13,13,.55) 0%,rgba(13,13,13,.15) 24%,rgba(13,13,13,.55) 40%,rgba(13,13,13,.72) 62%,rgba(13,13,13,.88) 100%)"></div>
<div class="halo" style="top:-10px"></div><img class="logo" src="{LOGO}" style="top:48px;width:250px">
<div class="tag" style="top:318px"><i></i>Vos questions</div>
<div class="bloc" style="top:560px"><div class="rule" style="margin-bottom:38px"></div>
<div class="big" style="font-size:102px;line-height:1.0">{lignes(c['question'])}</div></div>
<div class="defile">Faites défiler <b></b></div></div>"""


def question(c: dict, k: int) -> str:
    p = c["pano"]
    titre, texte, pos = c["qr"][k]
    if pos == "haut":
        ov = "linear-gradient(180deg,rgba(13,13,13,.86) 0%,rgba(13,13,13,.62) 38%,rgba(13,13,13,.12) 66%,rgba(13,13,13,.25) 100%)"
        bloc = f'<div class="bloc" style="top:200px">'
        cls = ""
    else:
        ov = "linear-gradient(180deg,rgba(13,13,13,.25) 0%,rgba(13,13,13,0) 30%,rgba(13,13,13,.2) 100%)"
        bloc = f'<div class="bloc panneau" style="bottom:110px">'
        cls = "panneau"
    return f"""<div class="s"><div class="bg" style="{fond(p['photo'], k + 1, y=p['y'])}"></div>
<div class="ov" style="background:{ov}"></div>
<div class="cpt"><span>0{k + 1}</span> / 03</div>
{bloc}<div class="t">{esc(titre)}</div>
<div class="rule" style="margin:34px 0 34px;width:80px;height:3px"></div>
<div class="p">{esc(texte)}</div></div></div>"""


def conclusion(c: dict) -> str:
    f = c["fin_photo"]
    return f"""<div class="s"><div class="bg" style="{fond(f['photo'], x=f['x'], y=f['y'])}"></div>
<div class="ov" style="background:linear-gradient(180deg,rgba(13,13,13,.7) 0%,rgba(13,13,13,.62) 40%,rgba(13,13,13,.8) 100%)"></div>
<div class="halo" style="top:0"></div><img class="logo" src="{LOGO}" style="top:58px;width:270px">
<div class="c" style="top:400px"><div class="big" style="font-size:104px;line-height:1.0">{lignes(c['fin'])}</div>
<div class="rule" style="margin:54px 0 46px"></div>
<div class="site">deloria-ia.fr</div>
<div style="margin-top:46px" class="pill">Écrivez « {c['mot']} » en message privé</div>
<div class="petit" style="margin-top:30px">Réponse sous 24 h</div></div>
<div class="c" style="bottom:70px"><div class="handle">@DELORIA.IA</div></div></div>"""


def pages(c: dict) -> list[str]:
    return [couverture(c)] + [question(c, k) for k in range(3)] + [conclusion(c)]


def main() -> None:
    choix = set(sys.argv[1:])
    blob = json.dumps(CARROUSELS, ensure_ascii=False)
    for bad in ("—", "–"):
        if bad in blob:
            raise ValueError(f"Tiret interdit : {bad!r}")
    with sync_playwright() as pw:
        nav = pw.chromium.launch()
        page = nav.new_page(viewport={"width": W, "height": H})
        for c in CARROUSELS:
            if choix and c["id"] not in choix:
                continue
            dossier = ICI / c["id"]
            dossier.mkdir(exist_ok=True)
            for n, corps in enumerate(pages(c), 1):
                tmp = dossier / "_page.html"
                tmp.write_text(f"<!doctype html><html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{corps}</body></html>", encoding="utf-8")
                page.goto(tmp.as_uri(), wait_until="load")
                page.evaluate("document.fonts.ready")
                page.wait_for_timeout(200)
                tmp.unlink()
                png = dossier / f"{n:02d}.png"
                page.screenshot(path=str(png))
                Image.open(png).convert("RGB").save(dossier / f"{n:02d}.jpg", quality=92, optimize=True, progressive=True)
                png.unlink()
            print(c["id"], "ok")
        nav.close()


if __name__ == "__main__":
    main()
