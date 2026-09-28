"""Construit le calendrier : dates, choix des photos, numérotation, légendes, JSON par post.

Usage :
    python3 calendrier/construire.py              # écrit les specs JSON et calendrier.json
    python3 templates/render.py calendrier/20*/*.json   # génère les visuels

Chaque post devient calendrier/AAAA-MM/JJ.json (spec de rendu + légende).
calendrier/calendrier.json est l'index lu par n8n : date, URL de l'image, légende.
"""

import datetime as dt
import json
import sys
from collections import Counter
from pathlib import Path

ICI = Path(__file__).resolve().parent
REPO = ICI.parent
sys.path.insert(0, str(ICI))
from contenu import POSTS, WEEKEND, REMPLACEMENTS  # noqa: E402

DEBUT = dt.date(2026, 10, 5)          # lundi
JOURS_SEMAINE = {0, 2, 4}             # lundi, mercredi, vendredi
JOURS_WEEKEND = {5, 6}                # samedi, dimanche
RAW = "https://raw.githubusercontent.com/tomhodet/deloria-insta/main/"

# Photos écartées après revue visuelle : visages reconnaissables, logos de marques,
# lieux mal étiquetés, sujets hors ton. Index 1 = premier fichier par ordre alphabétique.
EXCLUES = {
    "interieur-lit": [3], "accueil-panier": [2, 4, 5], "accueil-sonnette": [2, 3],
    "details-telephone": [2, 4, 5], "details-carnet": [4], "saison-noel": [5, 6],
    "saison-hiver-mer": [1, 6], "normandie-lehavre": [1, 2, 3, 4, 5],
    "secteur-chef": [4, 5, 6], "secteur-atelier": [3, 5], "secteur-boulangerie": [5, 6],
    "details-cles": [3], "secteur-bureau": [1, 3, 6], "details-cafe": [6],
    "interieur-fenetre": [1, 3], "normandie-cote": [3, 6], "interieur-cheminee": [5],
    "interieur-chambre": [1], "interieur-salon": [5], "secteur-restaurant": [5],
    "normandie-mont": [2, 3], "astuce-plaid": [1, 2, 3, 4, 5, 6], "astuce-chargeur": [1, 6],
    "astuce-chien": [], "astuce-enfants": [2, 3], "astuce-machine-cafe": [6], "astuce-menage": [2, 5],
    "astuce-mot": [6], "astuce-parapluie": [1, 5, 6], "astuce-livret": [2, 4], "astuce-deux-verres": [1, 5, 6],
}


def dates(n: int, jours: set) -> list[dt.date]:
    out, d = [], DEBUT
    while len(out) < n:
        if d.weekday() in jours:
            out.append(d)
        d += dt.timedelta(days=1)
    return out


def fichiers(dossier: str) -> list[str]:
    tous = sorted((REPO / "photos/pexels" / dossier).glob("*.jpg"))
    exclus = set(EXCLUES.get(dossier, []))
    return [str(f.relative_to(REPO)) for i, f in enumerate(tous, 1) if i not in exclus]


def resoudre_fichier(ref: str) -> str:
    """'dossier#3' -> 3e fichier du dossier (ordre alphabétique), sinon chemin tel quel."""
    if "#" in ref:
        dossier, idx = ref.split("#")
        tous = sorted((REPO / "photos/pexels" / dossier).glob("*.jpg"))
        return str(tous[int(idx) - 1].relative_to(REPO))
    return ref


def credit(chemin: str) -> str:
    slug = Path(chemin).stem.split("_", 1)[1]
    return " ".join(m.capitalize() for m in slug.split("-"))


def inserer_credit(legende: str, nom: str) -> str:
    """Place 'Photo : X / Pexels' juste avant le bloc de hashtags final."""
    blocs = legende.strip().split("\n\n")
    ligne = f"Photo : {nom} / Pexels"
    if blocs[-1].lstrip().startswith("#"):
        blocs.insert(len(blocs) - 1, ligne)
    else:
        blocs.append(ligne)
    return "\n\n".join(blocs)


def main() -> None:
    planning = list(zip(dates(len(POSTS), JOURS_SEMAINE), POSTS))
    planning += list(zip(dates(len(WEEKEND), JOURS_WEEKEND), WEEKEND))
    planning.sort(key=lambda x: x[0])
    inconnues = set(REMPLACEMENTS) - {j.isoformat() for j, _ in planning}
    assert not inconnues, f"Dates de remplacement hors calendrier : {inconnues}"
    planning = [(j, REMPLACEMENTS.get(j.isoformat(), p)) for j, p in planning]
    tous = [p for _, p in planning]
    utilisees: Counter = Counter()
    imposees = {resoudre_fichier(p["photo_fichier"]) for p in tous if p.get("photo_fichier")}
    utilisees.update(imposees)
    index, numeros = [], Counter()

    for jour, post in planning:
        spec = {k: v for k, v in post.items() if k not in ("legende", "photo", "photo_fichier", "serie")}
        legende = post["legende"]

        if post.get("photo_fichier"):
            spec["photo"] = resoudre_fichier(post["photo_fichier"])
        elif post.get("photo"):
            candidats = fichiers(post["photo"])
            libres = [f for f in candidats if utilisees[f] == 0]
            choix = (libres or sorted(candidats, key=lambda f: utilisees[f]))[0]
            utilisees[choix] += 1
            spec["photo"] = choix
        if spec.get("photo"):
            legende = inserer_credit(legende, credit(spec["photo"]))

        serie = post.get("serie") or {"terrain": "terrain", "terrain_photo": "terrain", "carte": "astuce"}.get(post["template"])
        if serie:
            numeros[serie] += 1
            spec["numero"] = f"{numeros[serie]:02d}"

        dossier = ICI / jour.strftime("%Y-%m")
        dossier.mkdir(exist_ok=True)
        chemin = dossier / f"{jour:%d}.json"
        chemin.write_text(json.dumps({**spec, "legende": legende}, ensure_ascii=False, indent=2), encoding="utf-8")

        index.append({
            "date": jour.isoformat(),
            "image_url": RAW + str(chemin.with_suffix(".jpg").relative_to(REPO)),
            "legende": legende,
            "template": post["template"],
        })

    (ICI / "calendrier.json").write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")
    doublons = [f for f, n in utilisees.items() if n > 1]
    print(f"{len(index)} posts, du {index[0]['date']} au {index[-1]['date']}")
    print(f"photos utilisées : {len(utilisees)}, réutilisées : {len(doublons)} {doublons}")


if __name__ == "__main__":
    main()
