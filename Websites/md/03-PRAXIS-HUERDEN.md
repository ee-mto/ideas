# Die praxis-spezifischen Hürden (und deren Lösung)

Arztpraxen haben spezifische Anforderungen, die reines Static Hosting erweitern muss.

## Inhaltspflege ohne Git-Kenntnisse

Ärzte oder MFA (Medizinische Fachangestellte) können kein Git bedienen.

**Lösung: kein Redaktionssystem.** Die Pflege läuft zentral über engel&engel: Die Praxis meldet Änderungen formlos (Telefon oder E-Mail), wir setzen sie im Praxis-Repository um, prüfen sie und deployen. Die Praxis braucht keinen Zugang zu Git, Pipeline oder Server und muss nichts lernen.

Das ist eine bewusste Entscheidung. Eine Redaktionsoberfläche wäre ein zusätzliches System, das gepflegt, abgesichert und geschult werden müsste – und sie würde die inhaltliche Kontrolle (HWG, Sprechzeiten, Rechtstexte) aus der Hand geben.

### Änderungsprozess

| Schritt | Wer | Ergebnis |
| --- | --- | --- |
| Änderung melden (Telefon, E-Mail) | Praxis | Anforderung liegt vor |
| Eingangsbestätigung mit Termin | engel&engel | Praxis weiß, wann es live ist |
| Umsetzung im Praxis-Repository | engel&engel | Commit, Build, Deploy |
| Kontrolle (HWG, Sprechzeiten, Tonalität) | engel&engel | geprüfter Stand |
| Rückmeldung an die Praxis | engel&engel | Änderung bestätigt |
| Rollback bei Fehlern | engel&engel | vorheriger Stand live |

### Regeln für den Änderungsprozess

- **Feste Reaktionszeiten** je Paket zusagen (z. B. Standard zwei Werktage; Urlaubsvertretung und dringende Fälle am selben Tag).
- **Änderungskontingent** je Monat definieren, Mehrbedarf bepreisen (Kapitel 16).
- **Urlaub und Schließtage haben Vorrang** – sie sind der häufigste Anlass und verhindern Fehlanrufe bei der Praxis.
- **Kein Zugang der Praxis** zu Repository, Pipeline oder Hosting; Zugangsdaten liegen ausschließlich bei engel&engel im Passwort-Manager.
- **Nachvollziehbarkeit:** jede Änderung ist ein Commit mit Datum und Grund – bei Rückfragen belegbar.

## Online-Terminvergabe

Praxen nutzen Systeme wie Doctolib, jameda, samedi oder CGM.

**Lösung:** DSGVO-konforme Einbindung per Consent-Management (z. B. Two-Click-Lösung / lokaler Banner) oder direkter Deep-Link zum jeweiligen Buchungsportal. Details in Kapitel 07.

## Rechtssicherheit & Notdienst-Hinweise

- Lokale Auslieferung von Schriftarten (kein ungeschütztes Google-Fonts-CDN).
- Dynamische Notdienst-Boxen über kleine clientseitige Vanilla-JS-Snippets gegen die Schnittstellen der Kassenärztlichen Vereinigung (KV).

> Hinweis: Notdienst- und Bereitschaftsdaten niemals aus fremden Quellen übernehmen. Sie werden von der Praxis bestätigt oder aus einer offiziellen KV-Quelle bezogen und mit Stand-Datum geführt.

## Weitere Hürden im Betrieb

| Hürde | Lösung |
| --- | --- |
| Bestehende WordPress-Seite mit Rankings | Redirect-Konzept (301) vor dem Domainumzug, alte URLs auf neue Inhalte abbilden |
| Praxis-Mailadresse liegt beim alten Hoster | Mail-Handling beim Umzug getrennt planen (MX-Einträge), Website-Umzug nie mit Mail-Umzug vermischen |
| Bilder in Druckqualität | Build-Schritt zur Bildoptimierung (Kapitel 09), Einwilligungen vorher einholen |
| Änderungswünsche per Telefon | fester Änderungsprozess mit Eingangsbestätigung (Kapitel 12) |
| Praxis wechselt den Buchungsanbieter | Buchungslink ist ein Datenfeld, kein Template-Eingriff (Kapitel 07) |
