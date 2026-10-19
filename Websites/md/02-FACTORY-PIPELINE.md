# Automatisierte Factory-Pipeline

Um hunderte Praxen ohne manuellen Aufwand zu provisionieren, empfiehlt sich eine Template- & Daten-Entkopplung:

```text
[Arztdaten / Onboarding]
       |
       v
[GitLab Repo: praxis-mueller] --(Webhook)--> [GitLab Runner]
                                                    | (Hugo Build + Theme Submodule)
                                                    v
                                            [Docker Artifact / HTML]
                                                    |
                                                    v
                                            [Coolify API / Webhook] --> [Caddy/Traefik Proxy] --> [Live Website]
```

## Bausteine

1. **Theme als Git-Submodule / Hugo Module:** Ein zentrales, hochgradig barrierefreies Praxistemplate (inkl. Fachrichtungen wie Allgemeinmedizin, Zahnarzt, Orthopädie). Änderungen am Theme fließen per Runner-Update automatisch in alle Praxen ein.
2. **Praxis-spezifisches Repository:** Enthält ausschließlich Textdaten, Bilder, Öffnungszeiten, Impressum und Kontaktdaten (`/content` und `config.yaml` / JSON).
3. **Automatischer Build:** Ändert die Praxis ihre Sprechzeiten, stößt ein Commit die CI-Pipeline an. Der Runner rendert das HTML und übergibt die fertigen Artefakte via Coolify-Webhook an den ausliefernden Webserver.

## Provisionierung einer neuen Praxis

| Schritt | Aktion | Ergebnis |
| --- | --- | --- |
| 1 | Repository aus dem Praxis-Template erzeugen | leeres Daten-Repo mit Ordnerstruktur |
| 2 | Theme als Submodule/Modul in fester Version binden | reproduzierbarer Build-Stand |
| 3 | Praxis-Daten und Inhalte einpflegen (Onboarding-Formular) | Content vollständig |
| 4 | Domain im Proxy hinterlegen, DNS umstellen | Routing und TLS |
| 5 | Pipeline laufen lassen, Vorschau prüfen | Test-Website |
| 6 | Freigabe der Praxis einholen | dokumentiertes OK |
| 7 | Produktiv-Domain scharf schalten | live |

Der Aufwand liegt damit bei **Daten und Freigabe**, nicht bei Technik – das ist der eigentliche Skalierungsgewinn.

## Versionierung und Rollback

- Das Theme wird in **fester Version** je Praxis gebunden. Ein Update ist eine bewusste Änderung (Versionsnummer anheben), kein automatisches Mitziehen.
- Jede Änderung an Inhalten ist ein Commit und damit rückholbar; ein Rollback ist ein Revert plus erneuter Build.
- Builds sind reproduzierbar: derselbe Commit plus dieselbe Theme-Version ergibt dasselbe Ergebnis.
- Vor dem Ausrollen eines Theme-Updates läuft ein Staging-Build über alle Praxen; erst danach wird produktiv deployt.

## Fehlerfälle

| Fall | Ursache | Gegenmaßnahme |
| --- | --- | --- |
| Build bricht ab | fehlerhafte Inhalte, ungültige Konfiguration | letzte gute Version bleibt live, Fehlermeldung an den Verantwortlichen |
| Webhook erreicht den Proxy nicht | Netzwerk, abgelaufenes Token | erneuter Trigger, Alarm bei fehlgeschlagenem Deploy |
| Theme-Update bricht einzelne Praxen | Sonderfall in den Praxis-Daten | Staging-Durchlauf, Rollback auf vorherige Theme-Version |
| Vorschau öffentlich erreichbar | vergessener Zugriffsschutz | Vorschau immer mit Zugriffsschutz und `noindex` |
| Bilder fehlen oder sind zu groß | fehlender Build-Schritt | Bildoptimierung als Pflichtschritt im Build (Kapitel 09) |

## Rollen

| Rolle | Verantwortung |
| --- | --- |
| Theme-Verantwortlicher | Design-System, Komponenten, Freigabe von Theme-Releases |
| Pipeline-Verantwortlicher | Runner, Secrets, Proxy, Monitoring |
| Redakteur | engel&engel – die Praxis meldet Änderungen (Kapitel 03) |
| Freigeber | dokumentierte Freigabe vor dem Go-Live und vor Theme-Releases |
