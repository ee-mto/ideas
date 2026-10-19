# Der Audit-Prozess

Dieses Kapitel beantwortet die offene Frage aus der Vorlage: **was per Fernwartung und Skripten geprüft wird und was vor Ort passieren muss.** Ziel ist ein Standardprozess, der für jede Praxis gleich abläuft — nur der Umfang wächst mit der Praxisgröße.

## 1. Ziel und Ergebnis

Ein Audit beantwortet für die Praxis zwei Fragen: *Erfüllen wir die Anforderungen der Richtlinie?* und *was müssen wir zuerst anpacken?* Ergebnis ist immer ein **Maßnahmenplan mit Ampelsystem**:

- **Rot** = Verstoß gegen eine Muss-Anforderung („müssen" in der Richtlinie)
- **Gelb** = Soll-Anforderung oder Empfehlung („sollten", BSI/KV-Empfehlung)
- **Grün** = erfüllt und dokumentiert

## 2. Ablauf in sechs Phasen

| Phase | Inhalt | Wer | Dauer |
| --- | --- | --- | --- |
| **1. Vorbereitung** | Praxistyp festlegen (bis 5 / 6–20 / über 20 Personen), Anlagen bestimmen, IT-Liste und Zugänge anfordern, Fernprüfung vorbereiten | Dienstleister | 1–2 Wochen vorab |
| **2. Fernprüfung** | technische Bestandsaufnahme per Monitoring und Skripten (Tabelle unten) | Dienstleister | ca. 0,5–1 Tag |
| **3. Vor-Ort-Termin** | Sichtprüfung, Gespräche mit Team und Leitung, Prüfung der Unterlagen | Dienstleister + Praxis | 0,5–2 Tage je Größe |
| **4. Auswertung** | Abgleich gegen die Anlagen, Ampelbewertung, Maßnahmen priorisieren, Aufwände schätzen | Dienstleister | 0,5–1 Tag |
| **5. Abschlussgespräch** | Ergebnis vorstellen, Maßnahmen erklären, Entscheidungen einholen (Behebung, Risiko-Formular) | beide | 1–2 Stunden |
| **6. Dokumentation** | Auditbericht, aktualisierter IT-Sicherheitsordner, Prüf-Siegel/Zertifikat | Dienstleister | 0,5–1 Tag |

## 3. Fernprüfung oder vor Ort?

**Fernprüfung (Monitoring, Skripte, Fragebogen):**

| Prüfpunkt | Anlage/Nr. | Wie |
| --- | --- | --- |
| Patch- und Versionsstand von Betriebssystemen und Anwendungen | A1 Nr. 14 | Inventarisierungs-/Monitoring-Skript |
| Systeme ohne Sicherheitsupdates (End-of-Life) | A1 Nr. 16 | Abgleich Versionsstände gegen Hersteller-Supportlisten |
| Virenschutz vorhanden und aktuell | A1 Nr. 20 | Statusabfrage |
| Backup-Jobs: laufen sie, welche Intervalle, welche Ziele | A1 Nr. 21, 23, 24 | Backup-Protokolle und Konfiguration |
| Schutz der Datensicherung (verschlüsselt/weggeschlossen) | A1 Nr. 22 | Konfigurationsprüfung, Nachfrage |
| Benutzerkonten und Berechtigungen | A1 Nr. 28 | Auswertung der Benutzerverwaltung (Gruppen, Rechte, inaktive Konten) |
| Netzstruktur und Dokumentationsstand | A1 Nr. 12 | Abgleich Monitoring-Daten mit vorhandenem Netzplan |
| Firewall-Regelwerk (wenn verwaltet) | A1 Nr. 11 | Regelwerk-Export, Sichtung |
| E-Mail-Konfiguration (Transportverschlüsselung, aktive Inhalte, Anhänge) | A1 Nr. 40 | Konfigurationsprüfung |
| Protokollierung/Alarmierung (mittlere und große Praxen) | A2 Nr. 1, A3 | Log-Konfiguration |
| TI-Komponenten: Update-Stand, VPN bei gehostetem Konnektor | A5 Nr. 5, 8 | Abfrage Konnektor/Konnektor-Management |

**Vor Ort (Sichtprüfung und Gespräch):**

| Prüfpunkt | Anlage/Nr. | Wie |
| --- | --- | --- |
| Arbeitsplätze: Bildschirmsperre, Passwortzettel, unbewachte Bildschirme | A1 Nr. 26, 28 | Sichtprüfung |
| Serverraum/Schrank: Zutritt, Aufstellung, USV | A1 | Sichtprüfung |
| Netzwerkkomponenten: Firewall, Switches, WLAN-Konfiguration, Verkabelung | A1 Nr. 11–13 | Sichtprüfung, Admin-Zugang |
| Medizingeräte: Zugriff auf Wartungsschnittstellen, Standardpasswörter, nicht genutzte Dienste | A4 Nr. 1, 4 | Sichtprüfung gemeinsam mit Anwender |
| TI-Konnektor: Aufstellung, physischer Schutz, Anbindung | A5 | Sichtprüfung |
| Wechseldatenträger und Speichermedien: Handhabung, Prüfung | A1 Nr. 36, 39 | Sichtprüfung, Nachfrage |
| Personal: Einarbeitung, Offboarding, Vertraulichkeitsvereinbarungen, Nachweise | A1 Nr. 1–5, 9 | Akteneinsicht und Gespräch |
| Schulungsstand und Sensibilisierung des Teams | A1 Nr. 6, 8, 9 | Gespräch, Nachweise |
| Abläufe im Notfall (Meldekette, wer informiert wen) | – (Empfehlung) | Gespräch, Notfallkarte |
| Dokumente: Netzplan, Regelungen, Verfahrensanweisungen | A1 Nr. 12 | Akteneinsicht |

**Faustregel:** Alles, was ein System über sich selbst auskunft, wird fern geprüft. Alles, was Menschen, Räume, Verkabelung oder Zugriffsrechte in der Hand betrifft, muss vor Ort gesehen werden. Das senkt den Aufwand erheblich — und ist der Grund, warum ein Audit zum Festpreis kalkulierbar ist.

## 4. Werkzeuge

- **Inventarisierung und Monitoring:** liefert Patch-Stand, EoL-Listen, Virenschutz-Status (Grundlage für A1 Nr. 14, 16, 20)
- **Backup-Reporting:** Job-Protokolle und Restore-Tests (A1 Nr. 21–25)
- **Benutzer- und Rechteauswertung:** Skript gegen die Benutzerverwaltung (A1 Nr. 28)
- **Netzplan-Generator:** aus Monitoring- und Switch-Daten vorbelegt, vor Ort verifiziert (A1 Nr. 12)
- **Fragebogen und Interviewleitfaden:** Personal, Schulung, Abläufe (A1 Nr. 1–10)
- **Sichtprüfungs-Checkliste:** je Raum und Gerät abhakbar
- **Berichtsvorlage mit Ampelsystem:** einheitlicher Auditbericht je Praxisgröße

## 5. Ergebnisdokumente

1. **Auditbericht** mit Bewertung je Anlage und Nummer (Ampel, Feststellung, Empfehlung)
2. **Maßnahmenplan** mit Priorisierung und geschätztem Aufwand — Grundlage für Angebote (Folgeprojekte!)
3. **Aktualisierter Netzplan** (A1 Nr. 12)
4. **Aktualisierter IT-Sicherheitsordner** (Kapitel 03)
5. **Prüf-Siegel/Zertifikat** des Dienstleisters mit Gültigkeit von einem Jahr
6. **Bei Nicht-SLV-Kunden:** Angebot zur Anrechnung der Auditkosten bei SLV-Abschluss (Kapitel 01)

## 6. Checkliste für den Auditstandard

- [ ] Praxistyp und geltende Anlagen bestimmt (A1 + A5, ggf. A2/A3/A4)
- [ ] IT-Liste und Zugänge vorab angefordert
- [ ] Fernprüfung durchgeführt und dokumentiert
- [ ] Vor-Ort-Termin mit Sichtprüfung und Gesprächen absolviert
- [ ] Bewertung je Anforderung mit Ampel, Muss und Soll getrennt
- [ ] Maßnahmen priorisiert, Aufwand geschätzt, Entscheidungen eingeholt
- [ ] Bericht, Netzplan und Ordner aktualisiert, Zertifikat ausgestellt
- [ ] Bei abgelehnten Maßnahmen: Risiko-Formular unterzeichnet (Kapitel 04)

## 7. Quellen

- KBV-IT-Sicherheitsrichtlinie mit Anlagen 1–5: https://www.kbv.de/documents/infothek/rechtsquellen/bekanntmachungen/richtlinien/IT-Sicherheitsrichtlinie_390_KBV.pdf
- KBV-Hub, Anlagen im Volltext: https://hub.kbv.de/spaces/itsrl/pages/63537333/Anlage+1+Anforderungen+f%C3%BCr+Praxen
- KBV PraxisWissen IT-Sicherheit (Checkliste): https://www.kbv.de/documents/infothek/publikationen/praxiswissen/praxiswissen-it-sicherheit.pdf
- BSI-Kurzbroschüre IT-Sicherheit in Praxen (Selbst-Check): https://www.bsi.bund.de/SharedDocs/Downloads/DE/BSI/Publikationen/Broschueren/Kurzbroschuere_IT-Sicherheit_Praxen.pdf
- KVWL-Umsetzungshilfe: https://www.kvwl.de/it-sicherheit
