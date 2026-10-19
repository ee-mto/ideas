# KBV-Prüfer — Ideen & Konzepte

> **Projekt:** IT-Sicherheits-Audits für Arztpraxen nach § 390 SGB V
> **Kunde:** engel&engel gmbh
> **Stand:** Oktober 2026

## Worum es geht

Der Ansatz mit dem kostenlosen Jahres-Audit im Service-Level-Vertrag (SLV) und dem gestaffelten Festpreis für Nicht-Vertragskunden ist ein starkes Fundament: Er belohnt Bestandskunden, schafft einen konkreten Anreiz für den Abschluss eines SLV und senkt die Einstiegshürde für Neukunden.

Um aus der Zertifizierung nach § 390 SGB V ein vollständiges, hochprofitables Portfolio zu bauen, wird das Modell auf vier Ebenen erweitert.

## Inhaltsverzeichnis

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 1 | Das Audit-Modell schärfen (Psychologie & Upselling) | [01-AUDIT-MODELL.md](md/01-AUDIT-MODELL.md) | [ansehen](html/index.html#k01) |
| 2 | Neue Managed Services aus der Richtlinie | [02-MANAGED-SERVICES.md](md/02-MANAGED-SERVICES.md) | [ansehen](html/index.html#k02) |
| 3 | Das „Audit-Ready"-Sorglos-Paket | [03-AUDIT-READY-PAKET.md](md/03-AUDIT-READY-PAKET.md) | [ansehen](html/index.html#k03) |
| 4 | Vertriebs- und Marketing-Hebel | [04-VERTRIEB-MARKETING.md](md/04-VERTRIEB-MARKETING.md) | [ansehen](html/index.html#k04) |

**Gesamtdokument:** [html/index.html](html/index.html) — alle Kapitel in einem druckbaren Dokument (Button „Als PDF speichern").

## Offene Frage aus der Vorlage

Habt ihr intern schon eine **Checkliste für den Ablauf des Audits** (was per Fernwartung über Monitoring/Skripte abgefragt wird vs. was vor Ort geprüft wird), oder soll dieser Standardprozess neu aufgesetzt werden?

## Struktur

| Ordner | Inhalt |
| --- | --- |
| [`md/`](md/) | Quelltexte — ein Dokument je Kapitel |
| [`html/`](html/index.html) | `index.html` — Gesamtdokument für Browser und PDF-Export |
| [`tools/`](tools/) | `convert_to_html.py` — erzeugt das HTML aus den Markdown-Quellen |
