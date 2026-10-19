# Technische Architektur & Rollenverteilung

Damit das System horizontal skaliert, ohne dass der Wartungsaufwand linear mit der Kundenanzahl wächst, sollten Build-Infrastruktur und Web-Auslieferung strikt getrennt werden.

| Komponente | Rolle & Aufgabe | Warum dieser Stack? |
| --- | --- | --- |
| **VPS** (Hetzner Cloud oder Terra Cloud) | Deutsches Rechenzentrum, Hosting der Management- und Delivery-Ebene | Erfüllt strikte DSGVO-/BDSG-Auflagen für Mediziner; Serverstandort Deutschland ist ein wichtiges Verkaufsargument. Bei Hetzner kommen Domains und DNS über dieselbe API dazu (Kapitel 11). |
| **Coolify (v4)** | Zentrale Deployment- & Reverse-Proxy-Plattform (Traefik/Caddy) | Verwaltet automatisch Wildcard- und Custom-Domains, stellt Let's-Encrypt-SSL-Zertifikate aus und orchestriert Docker-Container per Webhook. |
| **GitLab (Self-Hosted / CI/CD)** | Zentrales Repository- & Pipeline-Management | Trennt Template-Code von Praxis-Daten; baut Seiten in Sekunden per GitLab Runner via Hugo CLI. |
| **Hugo Engine** | Static Site Generator (SSG) | Kompiliert eine Praxis-Website in unter 100 ms; kein PHP, keine SQL-Datenbank zur Laufzeit, praktisch immun gegen Angriffe. |
| **Web-Auslieferung** | Nginx-/Caddy-Container (oder GitLab Pages) | Liefert reine statische Assets (HTML/CSS/JS) extrem performant mit Core-Web-Vitals-Scores nahe 100 aus. |

## Ebenen-Trennung

Die Architektur besteht aus drei klar getrennten Ebenen. Diese Trennung ist der Kern der Skalierbarkeit: Änderungen in einer Ebene wirken nicht unkontrolliert in die anderen.

| Ebene | Aufgabe | Lebensdauer | Änderungsfrequenz |
| --- | --- | --- | --- |
| **1. Template-/Theme-Ebene** | Layout, Komponenten, Barrierefreiheit, SEO-Grundgerüst | Jahre | selten, zentral für alle Praxen |
| **2. Praxis-Ebene** | Inhalte, Bilder, Öffnungszeiten, Impressum, Kontaktdaten | dauerhaft je Praxis | regelmäßig (Praxis oder Dienstleister) |
| **3. Delivery-Ebene** | gebautes HTML/CSS/JS, Proxy, TLS, Caching | flüchtig, reproduzierbar | bei jedem Commit |

Daraus folgt: Ein Theme-Update wird **einmal** gebaut und an alle Praxen ausgerollt; eine Inhaltsänderung berührt nur die Praxis-Ebene; die Delivery-Ebene ist jederzeit aus dem Repository reproduzierbar – sie enthält keinen Zustand, den man verlieren könnte.

## Rollen und Verantwortlichkeiten

| Aufgabe | Verantwortlich |
| --- | --- |
| Theme/Design-System pflegen | engel&engel (zentral) |
| Pipeline, Runner, Proxy, TLS betreiben | engel&engel |
| Inhalte liefern und verifizieren | Praxis |
| Inhalte einpflegen | engel&engel (Managed Service) – die Praxis meldet Änderungen |
| Rechtstexte verantworten | Praxis (technische Umsetzung: engel&engel) |
| Monitoring und Störungsbehebung | engel&engel |

## Fehlerfälle und Verhalten

| Fall | Auswirkung | Verhalten |
| --- | --- | --- |
| Build schlägt fehl | Praxis-Repo bleibt unverändert | letzter erfolgreicher Build bleibt live, Pipeline meldet den Fehler |
| Theme-Update fehlerhaft | potenziell alle Praxen betroffen | Ausrollen nur mit Staging-Durchlauf, Rollback auf die vorherige Theme-Version |
| Proxy/Container-Ausfall | alle Praxen offline | zweites Auslieferungsziel oder statisches Archiv, dokumentierter Notfallplan |
| Praxis-Repo beschädigt | eine Praxis betroffen | Wiederherstellung aus der Git-Historie |
| Zertifikat abgelaufen | Warnungen im Browser | automatische Erneuerung plus Ablauf-Überwachung |

## Einordnung

Die Architektur ist bewusst schlank: ein Theme, ein Repository je Praxis, eine Pipeline, eine Auslieferungsebene. Der Aufwand liegt bei Daten und Freigabe — nicht bei Technik. Die Bausteine beschreibt Kapitel 11, den Betrieb Kapitel 14.
