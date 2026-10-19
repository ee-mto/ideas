# Tech-Stack-Entscheidung

Dieses Kapitel führt die beiden Modelle zusammen, die im Projekt bisher nebeneinander stehen – und macht die Entscheidung explizit statt implizit.

## 1. Ausgangslage: zwei Modelle

**Modell A – Etablierter Betrieb (heute im Einsatz)**
Statische Website je Praxis: HTML/CSS mit Designsystem-Variablen, React 18 (lokal, SRI) für Routing und Interaktion, esbuild als Build, PHP 8.4 ausschließlich für den Formularversand, gehostet auf STRATO (deutsches Rechenzentrum, SSH/SFTP, `.htaccess`, SSL inklusive). Inhalte werden im Managed Service gepflegt, die Praxis liefert Änderungen per Mail.

**Modell B – Factory (Idee aus dem Konzept)**
Zentrale Build- und Delivery-Ebene auf Terra Cloud + Coolify + GitLab, Hugo als Static Site Generator, ein Theme als Submodule, ein Repository je Praxis, Auslieferung über Nginx/Caddy-Container. Die redaktionelle Pflege liegt in beiden Modellen zentral bei engel&engel.

## 2. Direktvergleich

| Dimension | Modell A (STRATO, statisch, React) | Modell B (Terra Cloud, Hugo-Factory) |
| --- | --- | --- |
| Hosting | Webhosting-Tarif je Praxis, deutsches RZ | eigener VPS + Container, deutsches RZ (Wortmann AG) |
| Auslieferung | Apache, statische Dateien, `.htaccess` | Nginx/Caddy hinter Coolify-Proxy, Traefik-Routing |
| Build | esbuild lokal, Seiten-Generator in Node | Hugo im GitLab Runner, Theme als Submodule |
| Inhaltsmodell | Daten in `config.js`, Pflege zentral | Content je Praxis-Repo, Pflege zentral |
| Redaktion | engel&engel – die Praxis meldet Änderungen | engel&engel – die Praxis meldet Änderungen |
| Neue Praxis anlegen | Template kopieren, konfigurieren, hochladen | Repo anlegen, Theme binden, Pipeline läuft |
| Skalierung auf 50+ Praxen | linearer Aufwand je Praxis (Upload, Pflege) | Aufwand wächst unterproportional, zentrales Theme |
| Betriebsrisiko | verteilt: ein Ausfall trifft eine Praxis | konzentriert: ein Ausfall trifft alle Praxen |
| Know-how | HTML/CSS/JS/Node, STRATO-Panel | zusätzlich Hugo, GitLab CI, Docker, Coolify |
| Kostenstruktur | je Praxis ein Hosting-Tarif | ein VPS + Runner, Kosten skalieren langsamer als die Kundenzahl |
| Updates am Design | je Praxis einzeln ausrollen | zentral im Theme, wirkt in alle Praxen |

## 3. Entscheidungsregeln

1. **Einzelpraxis, seltene Änderungen, Managed Service** → Modell A. Weniger bewegliche Teile, kein Server zu betreiben, sofort lieferbar.
2. **Praxis mit häufig wechselnden Inhalten** (Urlaub, News, Team) → das Modell ändert sich dadurch nicht, es braucht nur einen belastbaren Änderungsprozess mit kurzer Reaktionszeit (Kapitel 03).
3. **Ab etwa 10–15 betreuten Praxen** kippt der Aufwand: Der manuelle Rollout von Änderungen wird zum Engpass, die Factory zahlt sich aus.
4. **Kunden mit eigener IT-Erwartung** (MVZ, größere Gemeinschaftspraxen) erwarten klare Ansprechpartner, Berichte und Reaktionszeiten – keine Selbstbedienung im Redaktionssystem.
5. **Kein Mischbetrieb ohne Grund:** Wer beides parallel betreibt, pflegt zwei Toolchains. Die Entscheidung sollte pro Kunde fallen und dokumentiert werden – nicht pro Laune.

## 4. Warum kein Redaktionssystem

Die Pflege läuft **zentral über engel&engel**. Die Praxis meldet Änderungen, wir setzen sie um. Damit entfällt die Redaktionsoberfläche vollständig.

| Aspekt | Ohne Redaktionssystem (gewählt) | Mit CMS |
| --- | --- | --- |
| Angriffsfläche | keine Login-Oberfläche, kein zusätzliches System | Login, Rollen, CMS-Versionen zu pflegen |
| Inhaltliche Kontrolle | jede Änderung läuft über geprüfte Hände (HWG, Sprechzeiten) | Praxis kann ungeprüft veröffentlichen |
| Aufwand beim Aufsetzen | keiner | Einrichtung, Rollen, Freigabeworkflow, Schulung |
| Laufender Aufwand | Umsetzung je Änderung | Systemupdates, Support, Schulungsnachfragen |
| Reaktionszeit | vertraglich zugesagt (Kapitel 03) | sofort, aber ungeprüft |
| Kosten für die Praxis | Änderungskontingent in der Pauschale | Systembetreuung plus Schulung |

**Der Nachteil wird bewusst getragen:** Änderungen kosten die Praxis eine Meldung und uns Arbeitszeit – deshalb braucht das Modell ein definiertes Kontingent und klare Reaktionszeiten. Im Gegenzug bleibt die Verantwortung für Rechtssicherheit und Qualität an einer Stelle.

**Was die Praxis trotzdem kann:** jederzeit Änderungen melden – per Telefon oder formloser E-Mail, ohne Formulare, ohne Login, mit Eingangsbestätigung.

## 5. Konsequenzen und offene Entscheidungen

- **Theme-Wechsel ist die eigentliche Investition.** Modell B bedeutet, das bestehende Template als Hugo-Theme neu aufzubauen (oder Hugo nur als Build-Werkzeug für die vorhandenen HTML-Templates zu nutzen). Das ist ein eigenes Arbeitspaket.
- **Ausfallkonzentration** muss beantwortet werden: Was passiert, wenn der VPS oder die Pipeline steht? Antwort: statische Artefakte werden zusätzlich bei einem zweiten Ziel (oder als Archiv) vorgehalten und im Notfall manuell ausgeliefert.
- **Backup und Wiederherstellung** brauchen ein Konzept (Praxis-Repos, Theme, Secrets, Build-Artefakte).
- **Der Vorteil von Modell A bleibt:** Für eine einzelne Praxis ist es das robusteste und günstigste Modell – die Factory ist eine Skalierungsentscheidung, keine Qualitätsentscheidung.

**Offene Punkte für eine Entscheidung:**

1. Ab welcher Kundenzahl wird die Factory verbindlich?
2. Wird das bestehende Template nach Hugo portiert oder als Build-Input beibehalten?
3. Wer betreibt die Pipeline (engel&engel selbst, mit welcher Ausfallsicherheit)?
4. Welche Reaktionszeiten und Änderungskontingente werden je Paket zugesagt?
