# Technische Architektur & Rollenverteilung

Damit das System horizontal skaliert, ohne dass der Wartungsaufwand linear mit der Kundenanzahl wächst, sollten Build-Infrastruktur und Web-Auslieferung strikt getrennt werden.

| Komponente | Rolle & Aufgabe | Warum dieser Stack? |
| --- | --- | --- |
| **Terra Cloud (VPS)** | Deutsches Rechenzentrum (Wortmann AG), Hosting der Management- und Delivery-Ebene | Erfüllt strikte DSGVO-/BDSG-Auflagen für Mediziner; Serverstandort Deutschland ist ein wichtiges Verkaufsargument. |
| **Coolify (v4)** | Zentrale Deployment- & Reverse-Proxy-Plattform (Traefik/Caddy) | Verwaltet automatisch Wildcard- und Custom-Domains, stellt Let's-Encrypt-SSL-Zertifikate aus und orchestriert Docker-Container per Webhook. |
| **GitLab (Self-Hosted / CI/CD)** | Zentrales Repository- & Pipeline-Management | Trennt Template-Code von Praxis-Daten; baut Seiten in Sekunden per GitLab Runner via Hugo CLI. |
| **Hugo Engine** | Static Site Generator (SSG) | Kompiliert eine Praxis-Website in unter 100 ms; kein PHP, keine SQL-Datenbank zur Laufzeit, praktisch immun gegen Angriffe. |
| **Web-Auslieferung** | Nginx-/Caddy-Container (oder GitLab Pages) | Liefert reine statische Assets (HTML/CSS/JS) extrem performant mit Core-Web-Vitals-Scores nahe 100 aus. |
