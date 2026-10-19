# Online-Terminbuchung

## 1. Anbieter im Praxiskontext

| Anbieter | Typ | Hinweise |
| --- | --- | --- |
| **Doctolib** | Marktplatz + Praxis-Kalender | große Reichweite; die Praxis braucht einen Vertrag; DSGVO-Einwilligung und Hosting-Standort prüfen lassen |
| **medatixx Terminplan** (Terminplan/agenda) | Praxissoftware-Addon | naheliegend für Bestandskunden mit medatixx-Software; Integration meist als Portal-Link oder iframe |
| **Jameda-Terminbuchung** | Portal | Reichweite über das Jameda-Profil |
| **Terminland / andere** | Einzelanbieter | übernehmen, wenn die Praxis den Dienst bereits nutzt |

## 2. Umsetzung auf der Website

1. **Termin-Seite** (`/termin`) als zentrale Anlaufstelle:
   - Telefonnummer groß, mit Hinweis auf die besten Zeiten (viele Patienten rufen lieber an)
   - Online-Buchung-Button prominent („Jetzt online Termin buchen") → externer Link/Portal
   - Hinweis auf die Akutsprechstunde ohne Termin
2. **Startseite:** Termin-CTA im Hero, verlinkt auf `/termin`
3. **Konfiguration:** Buchungslink zentral in `config.js` (`bookingUrl`) pflegen und an beiden Stellen einbinden
4. **Konsistenz:** Website, Google-Business-Profil und Portale zeigen denselben Buchungsweg

## 3. Entscheidung je Praxis

- **Nur Telefon + Akutsprechstunde** – reicht vielen Hausarztpraxen, kein externer Dienst nötig
- **Portal-Anbieter vorhanden** (Doctolib/Jameda) – sachlich verlinken, nicht anpreisen (HWG, Kapitel 05)
- **medatixx-Terminplan** – bei Bestandskunden bevorzugt: ein System, keine zusätzliche DSGVO-Partei
- **Eigene Buchung** (z. B. Terminland) – nur auf Wunsch, AV-Vertrag prüfen

## 4. Datenschutz

- Externe Buchung ist Drittverarbeitung → **AV-Vertrag** mit dem Anbieter verlangen und in der Datenschutzerklärung einen Abschnitt „Online-Terminbuchung" führen (Anbieter, Zweck, Rechtsgrundlage, Empfänger)
- Liegt der Anbieter außerhalb der EU, Angemessenheitsbeschluss oder Standardvertragsklauseln dokumentieren (Standort jeweils aktuell prüfen)
- **Keine Patientendaten über eigene Server** – die Buchung läuft ausschließlich beim Anbieter

## 5. Checkliste

- [ ] Buchungslink auf `/termin` und im Hero, konsistent mit dem Google-Business-Profil
- [ ] Datenschutzerklärung um Online-Terminbuchung ergänzt (Anbieter + AV-Vertrag)
- [ ] Testbuchung end-to-end durchgeführt und wieder storniert
- [ ] Telefonnummer weiterhin prominent (Fallback ohne Internet)

## 6. Im Factory-Modell

- Der Buchungslink ist ein **Feld in den Praxis-Daten** (`bookingUrl`) – eine Änderung des Anbieters ist damit ein Datenupdate, kein Template-Eingriff.
- Die Entscheidung für einen Anbieter fällt im Onboarding (Kapitel 12) und wird in der Praxisdatei dokumentiert.
