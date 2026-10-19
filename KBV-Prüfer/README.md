# KBV-Prüfer — Ideen & Konzepte

> **Projekt:** IT-Sicherheits-Audits für Arztpraxen nach § 390 SGB V
> **Kunde:** engel&engel gmbh
> **Stand:** Oktober 2026
> **Grundlage:** Richtlinie nach § 390 SGB V (Fassung 01.04.2025) — gegen die Originalquellen geprüft, Quellen je Kapitel

## Worum es geht

Der Ansatz mit dem im Service-Level-Vertrag (SLV) rabattierten Pauschalpreis der Prüfung und dem gestaffelten Festpreis für Nicht-Vertragskunden ist ein starkes Fundament: Er belohnt Bestandskunden, schafft einen konkreten Anreiz für den Abschluss eines SLV und senkt die Einstiegshürde für Neukunden. Um daraus ein vollständiges Portfolio nach § 390 SGB V zu bauen, wird das Modell auf vier Ebenen erweitert. Ein KBV-Zertifikat nach § 390 SGB V bildet den Nachweis (Kapitel 11).

## Inhaltsverzeichnis

### I. Modell & Markt

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 01 | Das Audit-Modell schärfen (Psychologie & Upselling) | [01-AUDIT-MODELL.md](md/01-AUDIT-MODELL.md) | [ansehen](html/index.html#k01) |
| 09 | Zielkunden & Markt | [09-ZIELKUNDEN-MARKT.md](md/09-ZIELKUNDEN-MARKT.md) | [ansehen](html/index.html#k09) |
| 12 | Roadmap | [12-ROADMAP.md](md/12-ROADMAP.md) | [ansehen](html/index.html#k12) |

### II. Recht & Prozess

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 05 | Rechtlicher Rahmen | [05-RECHTLICHER-RAHMEN.md](md/05-RECHTLICHER-RAHMEN.md) | [ansehen](html/index.html#k05) |
| 06 | Der Audit-Prozess | [06-AUDIT-PROZESS.md](md/06-AUDIT-PROZESS.md) | [ansehen](html/index.html#k06) |
| 11 | Rollen & Zertifizierung | [11-ROLLEN-UND-ZERTIFIZIERUNG.md](md/11-ROLLEN-UND-ZERTIFIZIERUNG.md) | [ansehen](html/index.html#k11) |

### III. Leistungen & Vertrag

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 02 | Neue Managed Services aus der Richtlinie | [02-MANAGED-SERVICES.md](md/02-MANAGED-SERVICES.md) | [ansehen](html/index.html#k02) |
| 03 | Das „Audit-Ready“-Sorglos-Paket | [03-AUDIT-READY-PAKET.md](md/03-AUDIT-READY-PAKET.md) | [ansehen](html/index.html#k03) |
| 07 | Das SLV-Konstrukt | [07-SLV-KONSTRUKT.md](md/07-SLV-KONSTRUKT.md) | [ansehen](html/index.html#k07) |
| 10 | Die vier Add-ons im Detail | [10-ADD-ONS-IM-DETAIL.md](md/10-ADD-ONS-IM-DETAIL.md) | [ansehen](html/index.html#k10) |

### IV. Wirtschaft & Vertrieb

| # | Kapitel | Markdown | HTML |
| --- | --- | --- | --- |
| 04 | Vertriebs- und Marketing-Hebel | [04-VERTRIEB-MARKETING.md](md/04-VERTRIEB-MARKETING.md) | [ansehen](html/index.html#k04) |
| 08 | Preise & Kalkulation | [08-PREISE-KALKULATION.md](md/08-PREISE-KALKULATION.md) | [ansehen](html/index.html#k08) |
| 13 | Vertriebsmaterial | [13-VERTRIEB-MATERIAL.md](md/13-VERTRIEB-MATERIAL.md) | [ansehen](html/index.html#k13) |

**Gesamtdokument:** [html/index.html](html/index.html) — alle Kapitel in einem druckbaren Dokument (Button „Als PDF speichern“).

## Wichtige Korrekturen an der Vorlage

Die Recherche gegen die Originalrichtlinie hat drei Punkte der ursprünglichen Notiz präzisiert — sie stehen so in den Kapiteln:

| Vorlage | Belegt ist |
| --- | --- |
| „Die Richtlinie verlangt die regelmäßige Prüfung der Wiederherstellbarkeit“ | Datensicherung ist **Muss** (A1 Nr. 21–24); der Wiederherstellbarkeitstest ist **Soll** (Nr. 25), BSI empfiehlt quartalsweise |
| „Die Richtlinie fordert eine Übersicht aller IT-Systeme“ | **Muss** sind Identifikation (Nr. 16) und Ausmusterung/Separierung (Nr. 17) von End-of-Life-Systemen; die Bestandsliste ist KBV-Empfehlung |
| „Notfallplan und Meldepflichten“ | stehen **nicht** in der Richtlinie; gesetzliche Meldepflichten kommen aus DSGVO (72 h) und NIS-2 (große Praxen) |

Die offene Frage aus der Vorlage — was per Fernwartung geprüft wird und was vor Ort — ist in [Kapitel 06](md/06-AUDIT-PROZESS.md) beantwortet.

## Struktur

| Ordner | Inhalt |
| --- | --- |
| [`md/`](md/) | Quelltexte — ein Dokument je Kapitel |
| [`html/`](html/index.html) | `index.html` — Gesamtdokument für Browser und PDF-Export |
| [`tools/`](tools/) | `convert_to_html.py` — erzeugt das HTML aus den Markdown-Quellen |
