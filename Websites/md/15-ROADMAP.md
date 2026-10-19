# Roadmap

Vom Aufbau der Infrastruktur zur betreuten Website-Flotte.

## 1. Phasen

| Phase | Ziel | Voraussetzungen | Erfolgskriterien |
| --- | --- | --- | --- |
| **0. Aufbau** | VPS aufsetzen, Coolify und GitLab Runner einrichten, Theme als Hugo-Theme umsetzen, Angebot und Preisstruktur, Onboarding-Unterlagen | Kalkulation (Kapitel 16), Mustertexte, Checklisten | Infrastruktur steht, eine Test-Praxis ist deploybar |
| **1. Pilot (1 Praxis)** | eine reale Praxis vollständig über den neuen Stack umsetzen | Pilotkunde mit Freigabebereitschaft | live, Freigaben dokumentiert, Wartungsroutine läuft 30 Tage |
| **2. Ausbau (3–10 Praxen)** | Wiederholbarkeit beweisen: Onboarding, Freigabe, Go-Live ohne Sonderfälle | standardisierte Unterlagen aus Phase 1 | Zeitaufwand je Praxis sinkt messbar |
| **3. Automatisierung (10–25 Praxen)** | Prüfungen, Rollout und Monitoring automatisieren | stabile Pipeline, Theme-Versionierung | Designänderungen in Stunden statt Tagen ausgerollt |
| **4. Skalierung (25–50+ Praxen)** | Betrieb industrialisieren: Monitoring, Reporting, klare Reaktionszeiten, Ausfallsicherheit | Betriebskonzept, Redundanz, Personal | Betreuungsaufwand je Praxis sinkt weiter |

## 2. Meilensteine und Entscheidungspunkte

| Meilenstein | Entscheidung, die dort fällt |
| --- | --- |
| Infrastruktur steht | Reicht die VPS-Größe für die ersten Praxen? |
| Pilot live | Passt der Änderungsprozess im Alltag (Reaktionszeit, Kontingent)? |
| 10 Praxen betreut | Wird ein zweiter VPS oder eine zweite Auslieferungsebene für Redundanz gebraucht? |
| 25 Praxen | Einstieg in automatisierte Reports und Self-Service-Statusseiten? |
| 50 Praxen | Eigenes Team, Partner oder Plattformbetrieb? |

## 3. Offene Fragen

1. Welche Reaktionszeiten und Änderungskontingente gelten je Paket?
2. Wie wird die Ausfallsicherheit der zentralen Ebene sichergestellt (Redundanz, zweite Auslieferung)?
3. Wie werden Praxen übernommen, die bereits eine Website haben (Migration, Redirects, Domain- und Mail-Umzug)?
4. Wie wird das Theme versioniert und wie werden Theme-Releases freigegeben?

## 4. Abhängigkeiten

- **Rechtstexte und HWG-Prüfung** sind der häufigste Zeitfresser — die Unterlagen dafür müssen in Phase 0 fertig sein.
- **Foto-Termine** bei der Praxis takten den Zeitplan; ohne Bilder kein Go-Live.
- **Der Domainumzug** einer bestehenden Website braucht ein Redirect-Konzept, sonst gehen Rankings verloren.
- **Die Theme-Portierung** ist Voraussetzung für jede weitere Praxis — sie ist das erste Arbeitspaket.

## 5. Nächste Schritte

1. VPS bei Terra Cloud bestellen und aufsetzen, Coolify installieren, GitLab Runner registrieren
2. Theme als Hugo-Theme umsetzen und eine Test-Praxis deployen
3. Pilotpraxis auswählen und Daten aufnehmen (Kapitel 12, Schritt 1)
4. Angebot mit Preisstufen aus Kapitel 16 finalisieren
5. Wartungs- und Störungsprozess (Kapitel 14) schriftlich fixieren
