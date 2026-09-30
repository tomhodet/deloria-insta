"""Contrôle géométrique des visuels, à lancer après chaque modification du contenu.

Signale les textes qui sortent du cadre, qui touchent le pied de page (logotype, pictos),
les blocs qui débordent et les mots seuls en fin de ligne.

Usage : python3 templates/verifier.py calendrier/20*/*.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import render as R  # noqa: E402
from playwright.sync_api import sync_playwright  # noqa: E402

TMP = Path(__file__).resolve().parent / "_verif.html"

JS_LIGNES = r"""
(sel) => {
  const out = [];
  for (const el of document.querySelectorAll(sel)) {
    const walker = document.createTreeWalker(el, NodeFilter.SHOW_TEXT | NodeFilter.SHOW_ELEMENT);
    const toks = [];
    let prevSpace = true, br = false, n;
    while ((n = walker.nextNode())) {
      if (n.nodeType === 1) { if (n.tagName === 'BR' || n.classList.contains('ln')) { br = true; prevSpace = true; } continue; }
      const t = n.textContent;
      const re = /[^ \n\t\r]+/g; let m;
      while ((m = re.exec(t))) {
        const rg = document.createRange();
        rg.setStart(n, m.index); rg.setEnd(n, m.index + m[0].length);
        const rects = rg.getClientRects();
        const top = rects.length ? rects[0].top : -1;
        if (m.index === 0 && !prevSpace && toks.length && !br) toks[toks.length - 1].text += m[0];
        else toks.push({text: m[0], top, br});
        br = false;
      }
      if (t.length) prevSpace = /[ \n\t\r]$/.test(t);
    }
    const lines = [];
    for (const k of toks) {
      const last = lines[lines.length - 1];
      if (last && !k.br && Math.abs(last.top - k.top) < 10) last.toks.push(k.text);
      else lines.push({top: k.top, toks: [k.text], dure: k.br || !last});
    }
    out.push({cls: el.className, lignes: lines.map(l => ({mots: l.toks, dure: l.dure}))});
  }
  return out;
}
"""

JS_GEOM = r"""
() => {
  const W = 1080, H = 1350, res = [];
  const q = s => Array.from(document.querySelectorAll(s));
  const r = e => e.getBoundingClientRect();
  const txt = '.texte, .chute, .titre, .txt, .phrase, .item, .pl, .cta, .label, .lab, .l1, .l2, .num, .lieu, .compteur, .wm, .handle, .v, .k';
  for (const e of q(txt)) {
    const rg = document.createRange(); rg.selectNodeContents(e);
    const b = rg.getBoundingClientRect();
    if (!b.width) continue;
    if (b.left < 44 || b.right > W - 44 || b.top < 44 || b.bottom > H - 44)
      res.push(`hors cadre ${e.className} [${Math.round(b.left)},${Math.round(b.top)},${Math.round(b.right)},${Math.round(b.bottom)}]`);
  }
  const contenu = q('.texte, .chute, .titre, .txt, .phrase, .items, .pictos, .contact, .num, .cta, .aa');
  const pieds = q('.foot, .bas');
  let ecart = 1e9;
  for (const c of contenu) for (const f of pieds) {
    if (f.contains(c) || c.contains(f)) continue;
    const a = r(c), b = r(f);
    const inter = !(a.right <= b.left || b.right <= a.left || a.bottom <= b.top || b.bottom <= a.top);
    if (inter) res.push(`chevauche le pied : ${c.className}`);
    if (a.bottom <= b.top) ecart = Math.min(ecart, b.top - a.bottom);
  }
  for (const g of q('.gauche')) { if (r(g).height > r(g.parentElement).height + 1) res.push('liste trop haute'); }
  for (const e of q('.frame, .bloc, .g')) if ((e.className !== 'bloc' || getComputedStyle(e).position === 'absolute') && e.scrollHeight > e.clientHeight + 6) res.push(`déborde ${e.className} ${e.scrollHeight}>${e.clientHeight}`);
  return {res, ecart: ecart === 1e9 ? null : Math.round(ecart)};
}
"""

SEL = ".texte, .chute, .titre, .phrase, .txt, .item, .l1, .v"


def main(paths):
    rapport = []
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport={"width": R.W, "height": R.H}, device_scale_factor=1)
        for path in paths:
            spec = json.loads(path.read_text(encoding="utf-8"))
            TMP.write_text(R.build_html(spec), encoding="utf-8")
            page.goto(TMP.as_uri())
            page.evaluate("document.fonts.ready")
            geo = page.evaluate(JS_GEOM)
            problemes = list(geo["res"])
            if geo["ecart"] is not None and geo["ecart"] < 36:
                problemes.append(f"écart texte / pied serré : {geo['ecart']} px")
            for bloc in page.evaluate(JS_LIGNES, SEL):
                for i, l in enumerate(bloc["lignes"]):
                    if not l["dure"] and len(l["mots"]) == 1:
                        problemes.append(f"orphelin dans {bloc['cls']} : « {l['mots'][0]} »")
            nom = f"{path.parent.name}/{path.stem}"
            gab = spec["template"]
            if gab in ("plein", "constat", "service") and spec.get("ton") == "clair":
                gab = "arche"
            if problemes:
                rapport.append((nom, gab, spec.get("ton"), problemes))
        browser.close()
    TMP.unlink(missing_ok=True)
    for nom, gab, t, pbs in rapport:
        print(f"{nom}  [{gab} / {t}]")
        for p in pbs:
            print("    ", p)
    print(f"\n{len(rapport)} visuels à revoir sur {len(paths)}")


if __name__ == "__main__":
    main([Path(a).resolve() for a in sys.argv[1:] if not a.endswith("calendrier.json")])
