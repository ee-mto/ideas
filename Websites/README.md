# Websites — Ideen & Konzepte

> **Projekt:** Praxis-Websites auf Jamstack-Basis (Terra Cloud + Coolify + GitLab + Hugo)
> **Kunde:** engel&engel gmbh
> **Stand:** Oktober 2026

## Worum es geht

Der gewählte Ansatz trifft den Nerv des Marktes: Arztpraxen leiden unter schwerfälligen, wartungsintensiven WordPress-Systemen, Plugin-Schwachstellen, DSGVO-Abmahnfallen und langsamen Ladezeiten. Ein Jamstack-Setup auf Basis von **Terra Cloud + Coolify + GitLab + Hugo** löst diese Probleme architektonisch an der Wurzel.

**Die Umsetzung:** GitLab (Repositories und Pipeline), ein neuer VPS im deutschen Rechenzentrum und Coolify (Deployment, Proxy, TLS). Ein Weg für alle Praxen — Kapitel 11 beschreibt den Stack.

## Für die Vorlage beim Kunden

| Dokument | Markdown | HTML |
| --- | --- | --- |
| **Management Summary** (Kurzfassung für die Geschäftsführung) | [00-MANAGEMENT-SUMMARY.md](md/00-MANAGEMENT-SUMMARY.md) | [ansehen](html/summary.html) |
| **Präsentationsdeck** (12 Folien zum Durchklicken) | – | [öffnen](html/deck.html) |

## Inhaltsverzeichnis

### I. Grundlagen

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 1 | Technische Architektur & Rollenverteilung | [01-ARCHITEKTUR.md](md/01-ARCHITEKTUR.md) | [ansehen](html/index.html#k01) |
| 2 | Automatisierte Factory-Pipeline | [02-FACTORY-PIPELINE.md](md/02-FACTORY-PIPELINE.md) | [ansehen](html/index.html#k02) |
| 3 | Die praxis-spezifischen Hürden (und deren Lösung) | [03-PRAXIS-HUERDEN.md](md/03-PRAXIS-HUERDEN.md) | [ansehen](html/index.html#k03) |
| 4 | Go-to-Market & Strategie für „Engel & Engel“ | [04-GO-TO-MARKET.md](md/04-GO-TO-MARKET.md) | [ansehen](html/index.html#k04) |

### II. Fachkonzept

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 5 | Recht & Compliance | [05-RECHT-UND-COMPLIANCE.md](md/05-RECHT-UND-COMPLIANCE.md) | [ansehen](html/index.html#k05) |
| 6 | Inhalte & Medien | [06-INHALTE-UND-MEDIEN.md](md/06-INHALTE-UND-MEDIEN.md) | [ansehen](html/index.html#k06) |
| 7 | Online-Terminbuchung | [07-TERMINBUCHUNG.md](md/07-TERMINBUCHUNG.md) | [ansehen](html/index.html#k07) |
| 8 | SEO – lokale Suche & strukturierte Daten | [08-SEO-LOKAL.md](md/08-SEO-LOKAL.md) | [ansehen](html/index.html#k08) |
| 9 | Performance | [09-PERFORMANCE.md](md/09-PERFORMANCE.md) | [ansehen](html/index.html#k09) |
| 10 | Sicherheit | [10-SICHERHEIT.md](md/10-SICHERHEIT.md) | [ansehen](html/index.html#k10) |

### III. Umsetzung & Betrieb

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 11 | Tech-Stack | [11-TECH-STACK.md](md/11-TECH-STACK.md) | [ansehen](html/index.html#k11) |
| 12 | Umsetzungsprozess | [12-UMSETZUNGSPROZESS.md](md/12-UMSETZUNGSPROZESS.md) | [ansehen](html/index.html#k12) |
| 13 | QA & Go-Live | [13-QA-UND-GO-LIVE.md](md/13-QA-UND-GO-LIVE.md) | [ansehen](html/index.html#k13) |
| 14 | Betrieb & Wartung | [14-BETRIEB-UND-WARTUNG.md](md/14-BETRIEB-UND-WARTUNG.md) | [ansehen](html/index.html#k14) |

### IV. Strategie

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 15 | Roadmap | [15-ROADMAP.md](md/15-ROADMAP.md) | [ansehen](html/index.html#k15) |
| 16 | Kosten & Kalkulation | [16-KOSTEN-UND-KALKULATION.md](md/16-KOSTEN-UND-KALKULATION.md) | [ansehen](html/index.html#k16) |
| 17 | Vertrieb & Einwände | [17-VERTRIEB-UND-EINWAENDE.md](md/17-VERTRIEB-UND-EINWAENDE.md) | [ansehen](html/index.html#k17) |

**Gesamtdokument:** [html/index.html](html/index.html) — alle Kapitel in einem druckbaren Dokument (Button „Als PDF speichern“).

## Struktur

| Ordner | Inhalt |
| --- | --- |
| [`md/`](md/) | Quelltexte — ein Dokument je Kapitel |
| [`html/`](html/index.html) | `index.html` — Gesamtdokument für Browser und PDF-Export |
| [`tools/`](tools/) | `convert_to_html.py` — erzeugt `html/index.html` und `html/summary.html` aus den Markdown-Quellen |
