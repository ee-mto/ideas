# Automatisierte Factory-Pipeline

Um hunderte Praxen ohne manuellen Aufwand zu provisionieren, empfiehlt sich eine Template- & Daten-Entkopplung:

```text
[Arztdaten / CMS]
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

1. **Theme als Git-Submodule / Hugo Module:** Ein zentrales, hochgradig barrierefreies Praxistemplate (inkl. Fachrichtungen wie Allgemeinmedizin, Zahnarzt, Orthopädie). Änderungen am Theme fließen per Runner-Update automatisch in alle Praxen ein.
2. **Praxis-spezifisches Repository:** Enthält ausschließlich Textdaten, Bilder, Öffnungszeiten, Impressum und Kontaktdaten (`/content` und `config.yaml` / JSON).
3. **Automatischer Build:** Ändert die Praxis ihre Sprechzeiten, stößt ein Commit die CI-Pipeline an. Der Runner rendert das HTML und übergibt die fertigen Artefakte via Coolify-Webhook an den ausliefernden Webserver.
