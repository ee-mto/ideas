# Umsetzungsprozess

Der Fahrplan von der Anfrage bis zur betreuten Praxis-Website.

## 1. Projektphasen

| Phase | Inhalt | Beteiligte Skills |
| --- | --- | --- |
| **0. Kickoff** | Angebot und Leistungsumfang, Praxis-Daten sammeln, Ansprechpartner, Zugänge (Domain, GBP, Portale) | – |
| **1. Konzeption** | Seitenstruktur, Fachbereichs-Schwerpunkte, Farben/Logo, Terminbuchungs-Anbieter klären | Inhalte & Medien, Terminbuchung |
| **2. Umsetzung** | Template konfigurieren, Inhalte einpflegen, Rechtstexte, Bilder | Recht & Compliance, Inhalte & Medien |
| **3. Qualität** | Technische Tests, HWG-/Rechts-Review, Freigaberunde mit der Praxis | QA & Go-Live, Recht & Compliance |
| **4. Go-Live** | Hosting-Setup, Upload, SSL, Search Console, Google Business Profile | Deployment & Betrieb, SEO |
| **5. Betrieb** | monatliche Wartungsroutine, Änderungsprozess, Monitoring | QA & Go-Live, Deployment & Betrieb |

## 2. Grundsätze

1. **Daten von der Praxis verifizieren** – Sprechzeiten, Kammer/KV, Notfallnummern niemals raten oder aus Altbeständen übernehmen.
2. **Freigaben dokumentieren** – Inhalte, Rechtstexte und das finale Go-Live-OK schriftlich (E-Mail genügt).
3. **Rechtssicher ab Phase 1** – HWG, BFSG und DSGVO von Anfang an mitdenken, nicht nachrüsten.
4. **Eine Basis, viele Praxen** – je Praxis nur Daten, Farben und Inhalte ändern; die Template-Quellen bleiben unangetastet, sonst entsteht Fork-Aufwand.
5. **Verantwortlichkeit trennen** – engel&engel betreut Technik und Deployment, Inhalte und Rechtstexte verantwortet die Praxis.

## 3. Meilensteine

1. Daten und Freigaben für die Inhalte vollständig
2. Test-Website steht (Vorschau für die Praxis)
3. Praxis-Freigabe erteilt (schriftlich)
4. Live, Search Console und Google Business Profile verknüpft
5. Erste Wartungsrunde abgeschlossen (30 Tage nach Go-Live)

## 4. Schritt 1 – Daten erfassen

- Praxisname, Fachbereich, Claim/Untertitel
- Adresse, Telefon, E-Mail, ggf. Fax
- **Sprechzeiten** je Tag, Akutsprechstunde, Urlaub und Schließtage
- Ärzt:innen: Name, Titel, Schwerpunkte, Kurzbiografie, **Foto-Einwilligung**
- Leistungen: Kassen- und IGeL-Leistungen getrennt
- Notfall-Infos: 116117, 112, nächste Notaufnahme
- bestehende Profile: Doctolib, Jameda, Google Business Profile
- Rechtliches: Kammer, KV, Approbationsland, Berufsordnung

## 5. Schritt 2 – Konfiguration

1. Praxis-Daten zentral im Praxis-Repository eintragen (`/content` + `config`)
2. Farben setzen und **Kontraste prüfen** (Markenfarbe, dunkle Variante für Text)
3. Seiten-Generator konfigurieren: Name, Domain, Adresse, Telefon, Titles/Descriptions
4. Formular-Empfänger und Domain setzen
5. `robots.txt` und `sitemap.xml` mit der echten Domain
6. JSON-LD `Physician` mit echten Koordinaten und Sprechzeiten
7. Logo ersetzen (SVG), Farben anpassen
8. Rechtstexte mit den Praxisangaben füllen
9. Bilder aufbereiten und einbinden

## 6. Schritt 3 – Freigaberunde

- Vorschau bereitstellen (lokaler Server oder geschützte Test-Subdomain)
- Die Praxis prüft: Sprechzeiten, Leistungen, Teamtexte, Telefonnummern, Anfahrt
- Schriftliches OK einholen und dokumentieren

## 7. Schritt 4 – Go-Live

- Deployment und SSL nach Kapitel 14
- QA-Checkliste nach Kapitel 13 abarbeiten
- Search Console, Google Business Profile und Portale verknüpfen
- Übergabe und Wartungsprozess starten

## 8. Rollen

| Aufgabe | Verantwortlich |
| --- | --- |
| Inhalte liefern und verifizieren | Praxis |
| Umsetzung und Deployment | engel&engel |
| Rechtstexte final | Praxis, bei Bedarf mit rechtlicher Prüfung |
| Freigabe | Praxis (schriftlich) |
| Technischer Betrieb, Monitoring, Wartung | engel&engel |

## 9. Projektdatei je Praxis

```
projekte/<praxis>/
├── daten.md        erfasste Praxis-Daten (Stand + Verantwortlicher)
├── freigaben.md    Freigaben mit Datum (Inhalte, Rechtstexte, Go-Live)
├── zugriffe.md     Zugangsliste (Domain, Hosting, GBP) – niemals ins öffentliche Repo
└── website/        konfigurierte Kopie des Templates
```

> Zugangsdaten gehören ausschließlich in einen Passwort-Manager, nie in ein Repository.

## 10. Checkliste

- [ ] Alle Daten bei der Praxis verifiziert
- [ ] Farbschema und Logo angepasst, Kontraste geprüft
- [ ] Domain, `robots.txt`, `sitemap.xml`, JSON-LD und Formular konfiguriert
- [ ] Freigabe der Praxis dokumentiert
- [ ] Go-Live- und Wartungs-Checklisten abgearbeitet

## 11. Im neuen Stack

- Aus „Template kopieren und konfigurieren" wird „Repository anlegen und Theme binden"; die Datenerfassung (Schritt 1) bleibt unverändert und wird als strukturiertes Onboarding-Formular geführt.
- Die Freigaberunde bleibt ein **menschlicher** Schritt. Ohne dokumentierte Freigabe kein Go-Live.
- Jede Praxis erhält ein eigenes Repository (Daten) plus das gemeinsame Theme; Änderungen am Theme laufen über eine Freigabe und werden versioniert ausgerollt (Kapitel 02).
