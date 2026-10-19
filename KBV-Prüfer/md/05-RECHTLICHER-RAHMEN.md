# Rechtlicher Rahmen

Dieses Kapitel fasst zusammen, worauf das Angebot aufsetzt: die **Richtlinie nach § 390 SGB V** und ihre Anlagen. Alle Angaben sind gegen die Originalquellen geprüft (Stand der Recherche: Oktober 2026); die Quellen stehen am Ende.

## 1. Die Richtlinie

| Punkt | Inhalt |
| --- | --- |
| **Bezeichnung** | „Richtlinie nach § 390 SGB V über die Anforderungen zur Gewährleistung der IT-Sicherheit" (IT-Sicherheitsrichtlinie der KBV) |
| **Fassung** | veröffentlicht 31.03.2025, in Kraft seit 01.04.2025; ersetzt die Richtlinie nach § 75b SGB V vom 16.12.2020 |
| **Übergangsfrist** | neu hinzugekommene Anforderungen gelten seit **01.10.2025** |
| **Umfang** | 19 Seiten; Teil A (Geltungsbereich, Praxisgrößen, Anforderungen), Teil B (Inkrafttreten), **fünf Anlagen** |
| **Charakter** | beschreibt den Stand der technischen und organisatorischen Maßnahmen nach Art. 32 DSGVO — Vertraulichkeit, Integrität, Verfügbarkeit |

## 2. Rechtsgrundlage

- **§ 390 SGB V** (vormals § 75b SGB V) verpflichtet die Kassenärztlichen Bundesvereinigungen, die Anforderungen festzulegen — im Einvernehmen mit dem BSI.
- **§ 390 Abs. 6 SGB V:** Die Richtlinie ist für die an der vertragsärztlichen Versorgung teilnehmenden Leistungserbringer **verbindlich**. Sie gilt unabhängig davon, ob die Praxis an die Telematikinfrastruktur angebunden ist.
- **§ 390 Abs. 4 SGB V:** Die Anforderungen müssen dem Stand der Technik entsprechen und spätestens alle zwei Jahre angepasst werden — die Richtlinie wird also weiterentwickelt (nächster Turnaround wäre bis April 2027).
- **§ 390 Abs. 7 SGB V:** Die KBV **zertifiziert auf Antrag Mitarbeitende von IT-Anbietern** (Personenzertifizierung, siehe Kapitel 11).

## 3. Verantwortung liegt bei der Praxis

- Verantwortlich ist der **Praxisinhaber**. Er kann die Umsetzung einzelner Anforderungen **delegieren** — die Verantwortung bleibt aber bei ihm.
- Risiken können laut Präambel der Richtlinie ausdrücklich **an Dritte wie IT-Dienstleister übertragen** oder bewusst akzeptiert werden. Genau hier setzt das Risiko-Formular an (Kapitel 04).
- Gegenüber der KV besteht **keine Nachweispflicht**; die KBV empfiehlt lediglich eine interne Dokumentation von Umsetzung und Kontrolle.
- **Keine Praxis-Audits:** Die KBV sieht derzeit keine Kontrollen in Form von Audits oder Praxisbegehungen vor. § 390 SGB V enthält keine eigenen Sanktionen — Sanktionen drohen über DSGVO, Straf- und Berufsrecht.

## 4. Praxisgrößen und Anlagen

| Praxisgröße | Kriterium | Geltende Anlagen |
| --- | --- | --- |
| **Praxis** | bis 5 ständig mit Datenverarbeitung betraute Personen | **Anlage 1** (50 Anforderungen) + **Anlage 5** (9) |
| **Mittlere Praxis** | 6 bis 20 Personen | Anlage 1 + **Anlage 2** (10) + Anlage 5 |
| **Großpraxis** | über 20 Personen oder Datenverarbeitung im erheblichen Umfang (z. B. Groß-MVZ, Großlabore) | Anlage 1 + Anlage 2 + **Anlage 3** (17) + Anlage 5 |
| **Medizinische Großgeräte** | z. B. CT, MRT, PET, Linearbeschleuniger, IVD-Geräte | zusätzlich **Anlage 4** (6) |

Die Anlagen bauen aufeinander auf und sind **kumulativ** zu erfüllen. Anlage 5 (dezentrale TI-Komponenten) gilt für **alle** Praxen. Kleinere Praxen dürfen Anforderungen größerer Praxisgrößen freiwillig umsetzen — ein Ansatzpunkt für Zusatzleistungen.

## 5. Muss und Soll — der Unterschied, der im Verkauf zählt

Die Richtlinie kennzeichnet Anforderungen nicht mit Kategorien, sondern über die Formulierung („müssen" vs. „sollten"). Für die Beratung ist die Unterscheidung zentral, weil sie bestimmt, was im Audit rot und was gelb wird.

| Beispiel | Anlage/Nr. | Verbindlichkeit |
| --- | --- | --- |
| Firewall am Netzübergang ins Internet | A1 Nr. 11 | **Muss** |
| Dokumentation des internen Netzes inkl. Netzplan | A1 Nr. 12 | **Muss** |
| Regelmäßige Datensicherung, Intervalle festlegen | A1 Nr. 21 | **Muss** |
| Schutz der Datensicherung (weggeschlossen oder verschlüsselt) | A1 Nr. 22 | **Muss** |
| **Test der Wiederherstellbarkeit** | A1 Nr. 25 | **Soll** (BSI empfiehlt quartalsweise, KVWL konkretisiert) |
| Systeme ohne Sicherheitsupdates identifizieren | A1 Nr. 16 | **Muss** |
| Systeme ohne Sicherheitsupdates ausmustern oder separieren | A1 Nr. 17 | **Muss** |
| Netzwerksegmentierung mit Trennung von Gesundheitsdaten | A3 Nr. 2 | **Soll**, nur Großpraxen |
| Trennung medizinischer Großgeräte vom übrigen Netz | A4 Nr. 6 | **Soll** |

> **Wichtig für die Außendarstellung:** Ein „Bestandsverzeichnis aller IT-Systeme" und ein „Notfallplan mit Meldepflichten" stehen **nicht** als Anforderung in der Richtlinie. Verbindlich sind die Identifikation von End-of-Life-Systemen (Nr. 16/17) und die Netzplan-Dokumentation (Nr. 12); die Bestandsliste ist eine KBV-Empfehlung, der Notfallplan eine dringende Empfehlung aus KBV-/KV-/BSI-Material.

## 6. Angrenzende Regelwerke

| Regelwerk | Wen es trifft | Kern |
| --- | --- | --- |
| **NIS-2 / novelliertes BSI-Gesetz** (in Kraft seit 06.12.2025) | Praxen und MVZ ab 50 Beschäftigten oder mindestens 10 Mio. € Jahresumsatz und Bilanz (geschätzt rund 1.000 Einrichtungen) | BSI-Registrierung, Risikomanagement, Meldung erheblicher Vorfälle 24 h / 72 h / 1 Monat, Schulungen, MFA |
| **DSGVO** | jede Praxis | Meldung von Datenschutzverstößen binnen **72 Stunden** an die Aufsichtsbehörde, Benachrichtigung Betroffener bei hohem Risiko |
| **Cloud mit Sozial-/Gesundheitsdaten** | bei entsprechenden Diensten | Anlage 1 Nr. 50 verlangt ein aktuelles **C5-Testat** des Anbieters |
| **TI / gematik** | Praxen mit TI-Anbindung | Anlage 5: Installation und Betrieb nach gematik- und Herstellerdokumentation, VPN bei gehostetem Konnektor, zeitnahe Updates |

Eine Meldepflicht an die KV ist **nicht** Teil der Richtlinie; einzelne KVen empfehlen sie (z. B. Brandenburg), andere nennen sie „ggf." (z. B. Baden-Württemberg).

## 7. Was die KBV den Praxen selbst anbietet

Für die Positionierung wichtig, weil es den kostenpflichtigen Teil scharf abgrenzt:

- **Online-Plattform (Hub)** mit Umsetzungshinweisen und FAQ
- **Musterdokumente** (z. B. Eintritts-/Austrittsformulare, Verschwiegenheitserklärungen, Netzplan, IT-Notfallkarte des BSI)
- **Kostenlose Schulungsmaterialien** (Basis-Schulung, separate Phishing-Schulung) — Schulungen selbst sind also kein exklusives Produkt
- **PraxisWissen „IT-Sicherheit"** und Fortbildungen
- KVen ergänzen regionale Umsetzungshilfen und Beratung (z. B. KVWL, KV Nordrhein, KVB)

**Unsere Rolle:** Material gibt es, aber weder die strukturierte Prüfung vor Ort noch die Nachverfolgung, Dokumentation und Nachweise. Genau das verkaufen wir (Kapitel 02, 06).

## 8. Quellen

- KBV-IT-Sicherheitsrichtlinie (PDF): https://www.kbv.de/documents/infothek/rechtsquellen/bekanntmachungen/richtlinien/IT-Sicherheitsrichtlinie_390_KBV.pdf
- § 390 SGB V: https://www.gesetze-im-internet.de/sgb_5/__390.html
- KBV-Hub mit Anlagen und FAQ: https://hub.kbv.de/spaces/itsrl/pages/67765477/FAQ
- KBV-Seite IT-Sicherheit in der Praxis: https://www.kbv.de/praxis/digitalisierung/it-sicherheit
- BSI-Pressemitteilung 14.07.2026 zu Cyberangriffen auf Praxen: https://www.bsi.bund.de/DE/Service-Navi/Presse/Pressemitteilungen/Presse2026/260714_Cyberangriffe_auf_Praxen.html
- KBV PraxisInfo NIS-2: https://www.kbv.de/documents/infothek/publikationen/praxisinfo/praxisinfo-it-sicherheit-nis-2.pdf
- KVWL-Umsetzungshilfe: https://www.kvwl.de/it-sicherheit
- BSI-Kurzbroschüre IT-Sicherheit in Praxen: https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/Broschueren/Kurzbroschuere_IT-Sicherheit_Praxen.pdf
