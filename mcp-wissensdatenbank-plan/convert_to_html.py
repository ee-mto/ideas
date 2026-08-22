#!/usr/bin/env python3
"""Konvertiert MCP-Wissensdatenbank-Plan Markdown-Dokumente zu HTML."""

import os
import markdown

CSS_STYLE = """
@page {
    size: A4;
    margin: 2cm;
}

body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 12pt;
    line-height: 1.6;
    color: #333;
    max-width: 800px;
    margin: 0 auto;
    padding: 20px;
}

h1 {
    color: #003366;
    font-size: 28pt;
    border-bottom: 3px solid #003366;
    padding-bottom: 15px;
    margin-top: 40px;
}

h2 {
    color: #00A3E0;
    font-size: 20pt;
    margin-top: 35px;
    border-bottom: 1px solid #00A3E0;
    padding-bottom: 8px;
}

h3 {
    color: #003366;
    font-size: 16pt;
    margin-top: 25px;
}

h4 {
    color: #00A3E0;
    font-size: 13pt;
    margin-top: 20px;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 20px 0;
    box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

th, td {
    border: 1px solid #ddd;
    padding: 12px 15px;
    text-align: left;
}

th {
    background-color: #003366;
    color: white;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f9f9f9;
}

tr:hover {
    background-color: #f0f0f0;
}

code {
    background-color: #f4f4f4;
    padding: 3px 8px;
    border-radius: 4px;
    font-family: 'Consolas', 'Monaco', monospace;
    font-size: 10pt;
    color: #c7254e;
}

pre {
    background-color: #2d2d2d;
    color: #f8f8f2;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
    font-size: 10pt;
    line-height: 1.5;
    margin: 20px 0;
}

pre code {
    background-color: transparent;
    padding: 0;
    color: inherit;
}

blockquote {
    border-left: 5px solid #00A3E0;
    margin: 25px 0;
    padding: 15px 25px;
    background-color: #f0f8ff;
    border-radius: 0 8px 8px 0;
}

ul, ol {
    margin: 15px 0;
    padding-left: 35px;
}

li {
    margin: 8px 0;
}

strong {
    color: #003366;
    font-weight: 600;
}

a {
    color: #00A3E0;
    text-decoration: none;
    border-bottom: 1px dotted #00A3E0;
}

a:hover {
    border-bottom-style: solid;
}

hr {
    border: none;
    border-top: 2px solid #eee;
    margin: 30px 0;
}

.print-button {
    position: fixed;
    top: 20px;
    right: 20px;
    background-color: #003366;
    color: white;
    padding: 15px 30px;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    font-size: 14pt;
    font-weight: bold;
    box-shadow: 0 4px 6px rgba(0,0,0,0.2);
    z-index: 1000;
}

.print-button:hover {
    background-color: #00A3E0;
}

@media print {
    .print-button {
        display: none;
    }

    body {
        font-size: 11pt;
    }

    pre {
        white-space: pre-wrap;
        word-wrap: break-word;
    }
}

.footer {
    margin-top: 60px;
    text-align: center;
    font-size: 10pt;
    color: #666;
    border-top: 1px solid #ddd;
    padding-top: 20px;
}
"""

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>{css}</style>
</head>
<body>
    <button class="print-button" onclick="window.print()">📄 Als PDF drucken</button>
    {content}
    <div class="footer">
        <p><strong>engel&engel gmbh</strong> | MCP-Wissensdatenbank-Plan | Stand: Juli 2026</p>
        <p>Zum Speichern als PDF: Drucken → Als PDF speichern</p>
    </div>
</body>
</html>
"""


def convert_md_to_html(md_file, html_file, title):
    """Konvertiert eine Markdown-Datei zu HTML."""
    with open(md_file, 'r', encoding='utf-8') as f:
        md_content = f.read()

    html_content = markdown.markdown(
        md_content,
        extensions=['tables', 'fenced_code', 'toc', 'attr_list']
    )

    full_html = HTML_TEMPLATE.format(
        title=title,
        css=CSS_STYLE,
        content=html_content
    )

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"✓ Erstellt: {html_file}")


def main():
    base_dir = "/workspace/eenet/mcp-wissensdatenbank-plan"
    output_dir = os.path.join(base_dir, "HTML")

    os.makedirs(output_dir, exist_ok=True)

    md_files = [
        ("README.md", "00-README.html", "MCP-Wissensdatenbank – Übersicht"),
        ("01-ARCHITEKTUR.md", "01-Architektur.html", "Gesamtarchitektur"),
        ("02-KOMPONENTEN.md", "02-Komponenten.html", "Komponenten im Detail"),
        ("03-INTEGRATION.md", "03-Integration.html", "Integration der Systeme"),
        ("04-FAQ-EXTERN.md", "04-FAQ-Extern.html", "Externes FAQ-Portal"),
        ("05-STRASSENKARTE.md", "05-Strassenkarte.html", "Umsetzungsfahrplan"),
    ]

    print("=" * 60)
    print("   MCP-Wissensdatenbank-Plan")
    print("   HTML-Dokumente werden erstellt...")
    print("=" * 60)
    print()

    for md_file, html_file, title in md_files:
        md_path = os.path.join(base_dir, md_file)
        html_path = os.path.join(output_dir, html_file)

        if os.path.exists(md_path):
            try:
                convert_md_to_html(md_path, html_path, title)
            except Exception as e:
                print(f"✗ Fehler bei {md_file}: {e}")
        else:
            print(f"✗ Datei nicht gefunden: {md_file}")

    print()
    print("=" * 60)
    print("   Fertig!")
    print("=" * 60)
    print()
    print("   Die HTML-Dateien liegen in:")
    print(f"   {output_dir}")
    print()
    print("   So erstellen Sie PDFs:")
    print("   1. Öffnen Sie die HTML-Datei im Browser")
    print("   2. Klicken Sie auf '📄 Als PDF drucken'")
    print("   3. Oder verwenden Sie Strg+P / Cmd+P")
    print("   4. Wählen Sie 'Als PDF speichern'")
    print()

if __name__ == "__main__":
    main()
