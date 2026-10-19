#!/usr/bin/env python3
"""Erzeugt Websites/html/index.html aus den Markdown-Kapiteln in Websites/md/."""

import os
import re
import markdown

CHAPTERS = [
    ("I. Grundlagen", [
        ("k01", "01-ARCHITEKTUR.md"),
        ("k02", "02-FACTORY-PIPELINE.md"),
        ("k03", "03-PRAXIS-HUERDEN.md"),
        ("k04", "04-GO-TO-MARKET.md"),
    ]),
    ("II. Fachkonzept", [
        ("k05", "05-RECHT-UND-COMPLIANCE.md"),
        ("k06", "06-INHALTE-UND-MEDIEN.md"),
        ("k07", "07-TERMINBUCHUNG.md"),
        ("k08", "08-SEO-LOKAL.md"),
        ("k09", "09-PERFORMANCE.md"),
        ("k10", "10-SICHERHEIT.md"),
    ]),
    ("III. Umsetzung & Betrieb", [
        ("k11", "11-TECH-STACK-ENTSCHEIDUNG.md"),
        ("k12", "12-UMSETZUNGSPROZESS.md"),
        ("k13", "13-QA-UND-GO-LIVE.md"),
        ("k14", "14-BETRIEB-UND-WARTUNG.md"),
    ]),
    ("IV. Strategie", [
        ("k15", "15-ROADMAP.md"),
        ("k16", "16-KOSTEN-UND-KALKULATION.md"),
        ("k17", "17-VERTRIEB-UND-EINWAENDE.md"),
    ]),
]

CSS = """
:root{
  --gold:#c9a227; --gold-dark:#a8861d; --gold-soft:#faf6ea;
  --ink:#16181d; --body:#3a3f47; --muted:#6b7280;
  --line:#e6e3da; --card:#ffffff; --bg:#fbfaf7;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--body);
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  font-size:16px;line-height:1.65}
.page{max-width:940px;margin:0 auto;background:var(--card);padding:52px 60px 44px;
  box-shadow:0 1px 3px rgba(0,0,0,.06),0 14px 36px rgba(0,0,0,.05)}
.print-btn{position:fixed;top:22px;right:22px;z-index:50;background:var(--gold);color:#fff;
  border:none;border-radius:8px;padding:12px 22px;font-size:15px;font-weight:600;cursor:pointer;
  box-shadow:0 4px 14px rgba(201,162,39,.35)}
.print-btn:hover{background:var(--gold-dark)}
header.doc-head{border-bottom:3px solid var(--gold);padding-bottom:26px;margin-bottom:34px}
header.doc-head .kicker{display:inline-block;font-size:12px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--gold-dark);font-weight:700;margin-bottom:10px}
h1{color:var(--ink);font-size:34px;line-height:1.25;margin:0 0 14px;font-weight:700}
.doc-meta{display:flex;flex-wrap:wrap;gap:8px 18px;font-size:14px;color:var(--muted)}
.doc-meta b{color:var(--ink);font-weight:600}
h2.chapter{color:var(--ink);font-size:27px;margin:0 0 20px;font-weight:700;padding-left:16px;border-left:6px solid var(--gold);line-height:1.3}
section h2{color:var(--gold-dark);font-size:19px;margin:32px 0 10px;font-weight:650;padding:0 0 6px 0;border-left:none;border-bottom:1px solid var(--line)}
section h3{color:var(--ink);font-size:16px}
h3{color:var(--ink);font-size:18px;margin:30px 0 10px;font-weight:650}
h4{color:var(--gold-dark);font-size:15px;margin:22px 0 8px;font-weight:650}
p{margin:0 0 14px}
strong{color:var(--ink);font-weight:650}
a{color:var(--gold-dark);text-decoration:none;border-bottom:1px dotted var(--gold)}
a:hover{border-bottom-style:solid}
.toc{background:var(--gold-soft);border:1px solid var(--line);border-radius:12px;padding:22px 26px;margin:0 0 40px}
.toc h2{border:none;padding:0;font-size:15px;letter-spacing:.1em;text-transform:uppercase;
  color:var(--gold-dark);margin:0 0 12px}
.toc .group{margin:14px 0 4px;font-weight:650;color:var(--ink);font-size:14px}
.toc ol{margin:0;padding-left:22px}
.toc li{margin:6px 0}
.lead-in{font-size:17px}
section{margin:0 0 46px;scroll-margin-top:20px}
.table-wrap{overflow-x:auto;margin:18px 0 22px}
table{width:100%;border-collapse:collapse;font-size:14.5px;min-width:520px}
th,td{border:1px solid var(--line);padding:10px 13px;text-align:left;vertical-align:top}
th{background:var(--gold);color:#fff;font-weight:600}
tbody tr:nth-child(even){background:#fcfbf8}
tbody tr:hover{background:var(--gold-soft)}
pre{background:#1d2026;color:#f2f0e9;padding:18px 20px;border-radius:10px;overflow-x:auto;
  font-size:13px;line-height:1.55;margin:18px 0 22px;
  font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace}
code{background:#f4f1e8;color:#8a6d12;padding:2px 6px;border-radius:5px;
  font-family:'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace;font-size:13.5px}
pre code{background:transparent;color:inherit;padding:0;font-size:13px}
blockquote{margin:20px 0;padding:16px 22px;background:var(--gold-soft);border-left:5px solid var(--gold);
  border-radius:0 10px 10px 0;font-size:16px;color:var(--ink)}
blockquote p:last-child{margin-bottom:0}
ol,ul{margin:14px 0 18px;padding-left:26px}
li{margin:8px 0}
li.check{list-style:none;margin-left:-1.1em}
hr{border:none;border-top:2px solid var(--line);margin:30px 0}
footer.doc-foot{margin-top:52px;padding-top:20px;border-top:1px solid var(--line);font-size:13px;
  color:var(--muted);display:flex;flex-wrap:wrap;gap:6px 20px;justify-content:space-between}
@media (max-width:720px){
  body{font-size:15px}
  .page{padding:30px 20px 32px;box-shadow:none}
  h1{font-size:26px}
  h2{font-size:20px}
  .print-btn{position:static;display:block;width:100%;margin:0 0 22px}
  table{font-size:13px}
}
@page{size:A4;margin:18mm 15mm}
@media print{
  body{background:#fff;font-size:10.5pt;line-height:1.5}
  .page{max-width:none;margin:0;padding:0;box-shadow:none}
  .print-btn{display:none!important}
  a{color:inherit;border:none}
  .toc{page-break-after:always}
  section{page-break-before:always}
  section:first-of-type{page-break-before:avoid}
  .table-wrap,pre,blockquote{page-break-inside:avoid}
  h2,h3,h4{page-break-after:avoid}
}
"""

HTML_HEAD = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Praxis-Websites auf Jamstack-Basis — engel&amp;engel gmbh</title>
<style>{css}</style>
</head>
<body>
<button class="print-btn" onclick="window.print()">Als PDF speichern</button>
<div class="page">

<header class="doc-head">
  <span class="kicker">Konzept</span>
  <h1>Praxis-Websites auf Jamstack-Basis</h1>
  <div class="doc-meta">
    <span><b>Stack:</b> Terra Cloud + Coolify + GitLab + Hugo</span>
    <span><b>Kunde:</b> engel&amp;engel gmbh</span>
    <span><b>Stand:</b> Oktober 2026</span>
  </div>
</header>

<p class="lead-in">Der gewählte Ansatz trifft den Nerv des Marktes: Arztpraxen leiden unter schwerfälligen, wartungsintensiven WordPress-Systemen, Plugin-Schwachstellen, DSGVO-Abmahnfallen und langsamen Ladezeiten. Ein Jamstack-Setup auf Basis von <strong>Terra Cloud + Coolify + GitLab + Hugo</strong> löst diese Probleme architektonisch an der Wurzel.</p>

<nav class="toc">
  <h2>Inhalt</h2>
"""

SUMMARY_TEMPLATE = """<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} — engel&amp;engel gmbh</title>
<style>{css}</style>
</head>
<body>
<button class="print-btn" onclick="window.print()">Als PDF speichern</button>
<div class="page">

<header class="doc-head">
  <span class="kicker">Vorlage Geschäftsführung</span>
  <h1>{title}</h1>
  <div class="doc-meta">
    <span><b>Kunde:</b> engel&amp;engel gmbh</span>
    <span><b>Stand:</b> Oktober 2026</span>
    <span><b>Grundlage:</b> 17 Kapitel Konzept (Websites/md/)</span>
  </div>
</header>

{content}

<footer class="doc-foot">
  <span><strong>engel&amp;engel gmbh</strong> — Praxis-Websites auf Jamstack-Basis</span>
  <span>Als PDF: Button oben rechts bzw. Strg+P → „Als PDF speichern“</span>
</footer>

</div>
</body>
</html>
"""

HTML_FOOT = """
<footer class="doc-foot">
  <span><strong>engel&amp;engel gmbh</strong> — Praxis-Websites auf Jamstack-Basis</span>
  <span>Als PDF: Button oben rechts bzw. Strg+P → „Als PDF speichern“</span>
</footer>

</div>
</body>
</html>
"""


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    md_dir = os.path.join(base, "md")
    out_dir = os.path.join(base, "html")
    os.makedirs(out_dir, exist_ok=True)

    parts = [HTML_HEAD.format(css=CSS)]
    toc = []
    bodies = []

    for group, files in CHAPTERS:
        toc.append('  <div class="group">%s</div>' % group)
        toc.append("  <ol>")
        for anchor, fname in files:
            path = os.path.join(md_dir, fname)
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
            lines = text.split("\n")
            title = ""
            if lines and lines[0].startswith("# "):
                title = lines[0][2:].strip()
                text = "\n".join(lines[1:])
            html = markdown.markdown(text, extensions=["tables", "fenced_code", "attr_list", "sane_lists"])
            html = html.replace("<li>[ ] ", '<li class="check">☐ ')
            html = html.replace("<li>[x] ", '<li class="check">☑ ')
            bodies.append('<section id="%s">\n<h2 class="chapter">%s</h2>\n%s\n</section>' % (anchor, title, html))
            toc.append('    <li><a href="#%s">%s</a></li>' % (anchor, title))
        toc.append("  </ol>")

    parts.append("\n".join(toc))
    parts.append('  <p style="font-size:14px;color:#6b7280">Markdown-Quellen: <code>../md/01-ARCHITEKTUR.md</code> bis <code>../md/17-VERTRIEB-UND-EINWAENDE.md</code></p>')
    parts.append("</nav>")
    parts.extend(bodies)
    parts.append(HTML_FOOT)

    out = os.path.join(out_dir, "index.html")
    with open(out, "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts))
    print("geschrieben:", out, os.path.getsize(out), "Bytes")

    # Kurzfassung als eigenständiges Dokument
    src = os.path.join(md_dir, "00-MANAGEMENT-SUMMARY.md")
    if os.path.exists(src):
        with open(src, encoding="utf-8") as fh:
            text = fh.read()
        lines = text.split("\n")
        title = lines[0][2:].strip() if lines and lines[0].startswith("# ") else "Management Summary"
        text = "\n".join(lines[1:])
        html = markdown.markdown(text, extensions=["tables", "fenced_code", "attr_list", "sane_lists"])
        html = html.replace("<li>[ ] ", '<li class="check">☐ ')
        html = html.replace("<li>[x] ", '<li class="check">☑ ')
        out2 = os.path.join(out_dir, "summary.html")
        with open(out2, "w", encoding="utf-8") as fh:
            fh.write(SUMMARY_TEMPLATE.format(css=CSS, title=title, content=html))
        print("geschrieben:", out2, os.path.getsize(out2), "Bytes")


if __name__ == "__main__":
    main()
