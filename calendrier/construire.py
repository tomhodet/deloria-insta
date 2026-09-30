"""Construit le calendrier : dates, tons, photos, numérotation, légendes, JSON par post.

Usage :
    python3 calendrier/construire.py                      # écrit les specs JSON et calendrier.json
    python3 templates/render.py calendrier/20*/*.json     # génère les visuels
    python3 templates/verifier.py calendrier/20*/*.json   # contrôle cadrage, débordements, mots seuls

Chaque post devient calendrier/AAAA-MM/JJ.json (spec de rendu + légende).
Un carrousel ajoute JJ-02.json, JJ-03.json... pour ses pages intérieures.
calendrier/calendrier.json est l'index lu par n8n : date, URL de l'image (couverture),
liste des images pour un carrousel, légende.

La grille du profil : le ton de chaque post dépend de sa position dans le fil.
Position impaire : clair. Position multiple de 4 : sombre. Autre position paire : marron.
Le post de bienvenue du 28/09, déjà publié et sombre, occupe la position 0.
Résultat : un damier clair / foncé, traversé de diagonales marron, qui reste un damier
quel que soit le décalage apporté par chaque nouvelle publication.
"""

import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path

ICI = Path(__file__).resolve().parent
REPO = ICI.parent
sys.path.insert(0, str(ICI))
from contenu import CALENDRIER, MARDIS, JEUDIS  # noqa: E402

DEBUT = dt.date(2026, 9, 30)          # mercredi, position 1 dans le fil
JOURS = {0, 2, 4, 5, 6}               # CALENDRIER : lundi, mercredi, vendredi, samedi, dimanche
# MARDIS et JEUDIS complètent la semaine : un post chaque jour.
RAW = "https://raw.githubusercontent.com/tomhodet/deloria-insta/main/"

# Photos écartées après revue visuelle : visages reconnaissables, logos de marques,
# lieux mal étiquetés, textes étrangers ou datés, sujets hors ton.
# Index 1 = premier fichier par ordre alphabétique.
EXCLUES = {
    "interieur-lit": [3], "accueil-panier": [2, 4, 5, 6], "accueil-sonnette": [2, 3],
    "details-telephone": [2, 4, 5, 6], "details-carnet": [4, 5], "saison-noel": [5, 6],
    "saison-hiver-mer": [1, 6], "normandie-lehavre": [1, 2, 3, 4, 5],
    "secteur-chef": [4, 5, 6], "secteur-atelier": [3, 5], "secteur-boulangerie": [5, 6],
    "details-cles": [3], "secteur-bureau": [1, 3, 6], "details-cafe": [6],
    "interieur-fenetre": [1, 3], "normandie-cote": [3, 6], "interieur-cheminee": [5],
    "interieur-chambre": [1], "interieur-salon": [5], "secteur-restaurant": [5],
    "normandie-mont": [2, 3], "astuce-plaid": [1, 2, 3, 4, 5, 6], "astuce-chargeur": [1, 6],
    "astuce-enfants": [2, 3], "astuce-machine-cafe": [6], "astuce-menage": [2, 5],
    "astuce-mot": [6], "astuce-parapluie": [1, 5, 6], "astuce-livret": [2, 4], "astuce-deux-verres": [1, 5, 6],
    "normandie-falaises": [6],
    "site-bureau-sombre": [1], "site-bureau-clair": [3, 4, 5], "reseaux-telephone": [4, 5],
    "reseaux-appareil": [3, 5, 6], "reseaux-planning": [2, 3, 4, 5, 6], "design-nuancier": [2],
    "design-papeterie": [5], "design-sceau": [3], "temps-sablier": [6], "temps-horlogerie": [1, 2, 4, 5],
    "pme-dossiers": [6], "commerce-vitrine": [4], "porte-lumiere": [5, 6],
    "dev-poignee": [1], "dev-boussole": [6], "dev-croissance": [4, 5], "dev-telephone": [1, 5, 6],
    "dev-calcul": [4], "auto-colis": [4, 6], "auto-robot": [4, 5, 6], "auto-clavier": [4, 6],
    "auto-dominos": [3, 5, 6], "temps-horloge": [2],
}

# Photos déjà visibles ailleurs sur le compte : post de bienvenue publié, carrousels à la une.
DEJA_PUBLIEES = {"6395435", "12481521", "7657385", "8092459"}


def ton(position: int) -> str:
    if position % 2 == 1:
        return "clair"
    return "sombre" if position % 4 == 0 else "marron"


def dates(n: int, jours: set = JOURS) -> list[dt.date]:
    out, d = [], DEBUT
    while len(out) < n:
        if d.weekday() in jours:
            out.append(d)
        d += dt.timedelta(days=1)
    return out


def planning() -> list[tuple[dt.date, dict]]:
    """Fusionne les trois listes et vérifie qu'il y a exactement un post par jour."""
    plan = (list(zip(dates(len(CALENDRIER)), CALENDRIER))
            + list(zip(dates(len(MARDIS), {1}), MARDIS))
            + list(zip(dates(len(JEUDIS), {3}), JEUDIS)))
    plan.sort(key=lambda x: x[0])
    jours = [j for j, _ in plan]
    attendu = [DEBUT + dt.timedelta(days=i) for i in range((jours[-1] - DEBUT).days + 1)]
    assert jours == attendu, "Le calendrier doit compter exactement un post par jour, sans trou ni doublon"
    return plan


def resoudre(ref: str, controle: bool = True) -> str:
    """'dossier#3' -> 3e fichier du dossier (ordre alphabétique). Refuse les photos écartées."""
    dossier, idx = ref.split("#")
    tous = sorted((REPO / "photos/pexels" / dossier).glob("*.jpg"))
    i = int(idx)
    if not 1 <= i <= len(tous):
        raise ValueError(f"Photo inexistante : {ref}")
    if controle and i in EXCLUES.get(dossier, []):
        raise ValueError(f"Photo écartée utilisée : {ref}")
    return str(tous[i - 1].relative_to(REPO))


def pexels_id(chemin: str) -> str:
    return Path(chemin).stem.split("_", 1)[0]


def credit(chemin: str) -> str:
    slug = Path(chemin).stem.split("_", 1)[1]
    return " ".join(m.capitalize() for m in slug.split("-"))


def inserer_credit(legende: str, noms: list[str]) -> str:
    """Place la ligne de crédit juste avant le bloc de hashtags final."""
    uniques = list(dict.fromkeys(noms))
    ligne = (f"Photo : {uniques[0]} / Pexels" if len(uniques) == 1
             else f"Photos : {', '.join(uniques)} / Pexels")
    blocs = legende.strip().split("\n\n")
    if blocs[-1].lstrip().startswith("#"):
        blocs.insert(len(blocs) - 1, ligne)
    else:
        blocs.append(ligne)
    return "\n\n".join(blocs)


def controles_texte(date: dt.date, spec: dict, avertissements: list) -> None:
    """Garde-fous de lisibilité : un visuel se comprend en deux secondes."""
    blob = json.dumps(spec, ensure_ascii=False)
    for bad in ("—", "–"):
        if bad in blob:
            raise ValueError(f"{date} : tiret interdit")
    lim = {"texte": 62, "chute": 48, "phrase": 70, "titre": 72, "avant": 80, "apres": 90}
    for champ, maxi in lim.items():
        v = spec.get(champ)
        if spec["template"] in ("terrain_photo", "carte", "slide") and champ == "texte":
            maxi = 135
        if v and len(v.replace("*", "")) > maxi:
            avertissements.append(f"{date} {spec['template']} {champ} long ({len(v)} car.)")


def main() -> None:
    plan = planning()
    index, numeros, vus = [], Counter(), {}
    avertissements = []

    # On repart de zéro : les anciens fichiers de rendu sont supprimés.
    for f in list(ICI.glob("20*/*.json")) + list(ICI.glob("20*/*.jpg")):
        f.unlink()

    for position, (jour, post) in enumerate(plan, start=1):
        t = ton(position)
        dossier = ICI / jour.strftime("%Y-%m")
        dossier.mkdir(exist_ok=True)
        credits, images = [], []

        def photo_unique(ref: str) -> str:
            chemin = resoudre(ref)
            pid = pexels_id(chemin)
            if pid in DEJA_PUBLIEES:
                raise ValueError(f"{jour} : photo déjà visible sur le compte ({ref})")
            if pid in vus:
                raise ValueError(f"{jour} : photo {ref} déjà utilisée le {vus[pid]}")
            vus[pid] = jour.isoformat()
            return chemin

        def ecrire(nom: str, spec: dict) -> None:
            controles_texte(jour, spec, avertissements)
            chemin = dossier / nom
            chemin.write_text(json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
            images.append(RAW + str(chemin.with_suffix(".jpg").relative_to(REPO)))

        if post["template"] == "carrousel":
            couv = {k: v for k, v in post["couverture"].items() if k != "photo_fichier"}
            couv["photo"] = photo_unique(post["couverture"]["photo_fichier"])
            couv["ton"] = t
            credits.append(credit(couv["photo"]))
            total = len(post["pages"]) + 2
            specs = [(f"{jour:%d}.json", couv)]
            for i, page in enumerate(post["pages"], start=1):
                fond = resoudre(page["fond"])
                credits.append(credit(fond))
                specs.append((f"{jour:%d}-{i + 1:02d}.json", dict(
                    template="slide", ton="clair", label=post["label"], compteur=f"{i + 1:02d} / {total:02d}",
                    numero=f"{i:02d}", titre=page["titre"], texte=page["texte"], photo=fond)))
            fond_fin = resoudre(post["fin"]["fond"])
            credits.append(credit(fond_fin))
            specs.append((f"{jour:%d}-{total:02d}.json", dict(
                template="slide_fin", ton="marron", label=post["label"], compteur=f"{total:02d} / {total:02d}",
                titre=post["fin"]["titre"], photo=fond_fin)))
            legende = inserer_credit(post["legende"], credits)
            for nom, spec in specs:
                ecrire(nom, {**spec, "legende": legende} if nom == f"{jour:%d}.json" else spec)
            entree = {"date": jour.isoformat(), "image_url": images[0], "images": images,
                      "type": "carrousel", "legende": legende, "template": couv["template"], "ton": t}
        else:
            spec = {k: v for k, v in post.items() if k not in ("legende", "photo_fichier", "serie")}
            spec["photo"] = photo_unique(post["photo_fichier"])
            spec["ton"] = t
            credits.append(credit(spec["photo"]))
            if post.get("serie"):
                numeros[post["serie"]] += 1
                spec["numero"] = f"{numeros[post['serie']]:02d}"
            legende = inserer_credit(post["legende"], credits)
            ecrire(f"{jour:%d}.json", {**spec, "legende": legende})
            entree = {"date": jour.isoformat(), "image_url": images[0], "legende": legende,
                      "template": spec["template"], "ton": t}

        if len(legende) > 2200 or legende.count("#") > 10:
            raise ValueError(f"{jour} : légende trop longue ou trop de hashtags")
        index.append(entree)

    (ICI / "calendrier.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    carrousels = sum(1 for e in index if e.get("type") == "carrousel")
    print(f"{len(index)} posts, du {index[0]['date']} au {index[-1]['date']}, dont {carrousels} carrousels")
    print(f"photos distinctes : {len(vus)}, séries : {dict(numeros)}")
    print("tons :", dict(Counter(e['ton'] for e in index)))
    for a in avertissements:
        print("  à vérifier :", a)


if __name__ == "__main__":
    main()
