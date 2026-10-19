# Tech-Stack

Die Umsetzung besteht aus drei Bausteinen: **GitLab**, **einem neuen VPS** und **Coolify**. Es gibt keinen zweiten Weg und keine Modellvariante — jede Praxis läuft auf dieser Basis.

## 1. Die drei Bausteine

| Baustein | Rolle | Warum |
| --- | --- | --- |
| **GitLab** | Repositories und CI/CD-Pipeline | Theme und Praxis-Daten sind versioniert, Builds reproduzierbar, Änderungen nachvollziehbar und rückholbar |
| **Neuer VPS** (Hetzner Cloud oder Terra Cloud, deutsches Rechenzentrum) | Rechenleistung für Build und Auslieferung | DSGVO-/BDSG-konform; Serverstandort Deutschland ist ein Verkaufsargument, Hetzner bringt zusätzlich eine durchgängige API mit |
| **Coolify** | Deployment, Reverse-Proxy, TLS | orchestriert die Container, verwaltet Wildcard- und Custom-Domains, stellt Let's-Encrypt-Zertifikate aus, deployt per Webhook |

## 2. Was wo läuft

| Ort | Inhalt |
| --- | --- |
| GitLab | Theme-Repository, ein Repository je Praxis, CI-Pipeline |
| VPS | GitLab Runner (Build), Coolify, Container für die Auslieferung (Caddy/Traefik) |
| Auslieferung | statisches HTML/CSS/JS — kein PHP, keine Datenbank, kein Redaktionssystem |

## 3. Domains und DNS

Die Domains werden bei **Hetzner** registriert und verwaltet. Der entscheidende Vorteil: Hetzner stellt für **DNS-Zonen und DNS-Einträge eine vollständige REST-API** bereit — kostenlos und ohne Zusatzvertrag.

| Aufgabe | Weg |
| --- | --- |
| Domain registrieren und verlängern | Hetzner Console bzw. Domain Registration Robot (E-Mail-Schnittstelle, keine REST-API) |
| DNS-Zone anlegen | REST-API, Console oder CLI |
| DNS-Einträge pflegen (A, AAAA, MX, TXT, CAA …) | REST-API je Praxis — im Deployment automatisierbar |
| TLS-Zertifikate | Coolify (Let's Encrypt) übernimmt Validierung und Erneuerung |

**Praktischer Nutzen:** Beim Onboarding einer Praxis entstehen die DNS-Einträge (Website, `www`, Mail, Verifizierungen) automatisch aus dem Deployment — kein Klicken in einem fremden Panel, keine Übertragungsfehler.

**Grenzen, die man kennen sollte:**

- Standardmäßig **25 Zonen** (über ein Support-Ticket erhöhbar), **500 Records je Zone**.
- **DNSSEC wird derzeit nicht unterstützt.**
- Die Registrierung selbst läuft nicht über die REST-API — sie ist ein einmaliger Schritt im Onboarding.

**Wichtig bei Praxen mit bestehender Website:** MX-Einträge (Mail) dürfen beim Umzug nicht überschrieben werden; der Mail-Umzug wird getrennt geplant (Kapitel 03).

## 4. Ablauf einer Änderung

```text
Commit (Theme oder Praxis-Daten)
        |
        v
Pipeline: Hugo-Build + Prüfungen (Links, HTML, Barrierefreiheit, Budgets)
        |
        v
Artefakt (fertige statische Seiten)
        |
        v
Coolify-Webhook -> Container aktualisieren -> live
```

## 5. Hugo als Generator

Hugo erzeugt aus Theme und Praxis-Daten die fertigen Seiten — in Millisekunden und ohne Laufzeitumgebung auf dem Webserver. Das Theme wird als Git-Submodule oder Hugo-Modul in fester Version je Praxis gebunden, damit ein Update eine bewusste Entscheidung bleibt (Kapitel 02).

## 6. Warum kein Redaktionssystem

Die Pflege läuft **zentral über engel&engel**. Die Praxis meldet Änderungen, wir setzen sie um — damit entfällt eine Redaktionsoberfläche vollständig.

| Aspekt | Ohne Redaktionssystem (gewählt) | Mit CMS |
| --- | --- | --- |
| Angriffsfläche | keine Login-Oberfläche, kein zusätzliches System | Login, Rollen, CMS-Versionen zu pflegen |
| Inhaltliche Kontrolle | jede Änderung läuft über geprüfte Hände (HWG, Sprechzeiten) | Praxis kann ungeprüft veröffentlichen |
| Aufwand beim Aufsetzen | keiner | Einrichtung, Rollen, Freigabeworkflow, Schulung |
| Laufender Aufwand | Umsetzung je Änderung | Systemupdates, Support, Schulungsnachfragen |
| Reaktionszeit | vertraglich zugesagt (Kapitel 03) | sofort, aber ungeprüft |
| Kosten für die Praxis | Änderungskontingent in der Pauschale | Systembetreuung plus Schulung |

**Der Nachteil wird bewusst getragen:** Änderungen kosten die Praxis eine Meldung und uns Arbeitszeit — deshalb braucht das Modell ein definiertes Kontingent und klare Reaktionszeiten. Im Gegenzug bleibt die Verantwortung für Rechtssicherheit und Qualität an einer Stelle.

**Was die Praxis trotzdem kann:** jederzeit Änderungen melden — per Telefon oder formloser E-Mail, ohne Formulare, ohne Login, mit Eingangsbestätigung.

## 7. Anforderungen an den VPS

- **Build ist CPU-lastig, Auslieferung ist leicht:** die Dimensionierung richtet sich nach der Zahl der Praxen und der Häufigkeit von Theme-Builds, nicht nach dem Traffic.
- **Speicher:** Praxis-Repositories und Build-Artefakte sind klein; Backups brauchen mehr Platz als die Daten selbst.
- **Getrennte Umgebungen:** Vorschau/Staging und Produktion getrennt halten, Vorschauen zugriffsgeschützt und nicht indexierbar.
- **Reserve einplanen:** Wachstum entsteht durch Praxen, nicht durch Lastspitzen.

## 8. Konsequenzen

- **Ein System zu betreiben:** VPS, Coolify, Runner und Container brauchen Updates, Monitoring und Backups (Kapitel 14).
- **Ausfallkonzentration:** fällt der VPS aus, sind alle Praxen offline — dafür braucht es einen dokumentierten Notfallplan (Kapitel 14).
- **Know-how:** Hugo, GitLab CI, Docker, Coolify und die DNS-API müssen im Haus beherrscht werden.
- **Trennung bleibt:** Theme, Praxis-Daten und Auslieferung sind getrennte Ebenen (Kapitel 01) — eine Theme-Änderung wirkt zentral, ohne die Praxis-Daten zu berühren.

## 9. Ausblick: weitere Hetzner-Dienste

Fällt die Entscheidung auf Hetzner, liegen weitere Bausteine in derselben Umgebung — im deutschen Rechenzentrum und über dieselben Werkzeuge erreichbar. Für heute reicht der VPS; das hier ist nur ein Ausblick:

| Dienst | Möglicher Nutzen später |
| --- | --- |
| **Load Balancer** | Auslieferung auf zwei Instanzen verteilen (Redundanz statt Klumpenrisiko) |
| **Object Storage** (S3-kompatibel) | Backups und Build-Artefakte auslagern |
| **Storage Box** | Backups per Borg/Restic/rsync, 1–20 TB |
| **Firewalls, private Netzwerke** | Staging und Produktion sauber trennen |
| **Snapshots/Backups** | schnelle Wiederherstellung des VPS |
| **Cloud-API, hcloud-CLI, Terraform** | Infrastruktur als Code statt Klickarbeit |

## 10. Offene Punkte

1. **VPS-Anbieter final entscheiden:** Hetzner Cloud (durchgängige API, großes Portfolio) oder Terra Cloud — mit echten Preisen kalkulieren.
2. **Domains bei Hetzner registrieren** und die DNS-Zonen per API an die Pipeline anbinden (Onboarding-Schritt).
3. Das bestehende Praxistemplate als Hugo-Theme umsetzen (eigenes Arbeitspaket).
4. Redundanz und Notfallkonzept festlegen: Wie werden die statischen Seiten ausgeliefert, wenn VPS oder Coolify ausfallen?
5. Backup- und Wiederherstellungskonzept für Repositories, Theme und Secrets dokumentieren.
