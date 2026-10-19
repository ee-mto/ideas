# Tech-Stack

Die Umsetzung besteht aus drei Bausteinen: **GitLab**, **einem neuen VPS** und **Coolify**. Es gibt keinen zweiten Weg und keine Modellvariante — jede Praxis läuft auf dieser Basis.

## 1. Die drei Bausteine

| Baustein | Rolle | Warum |
| --- | --- | --- |
| **GitLab** | Repositories und CI/CD-Pipeline | Theme und Praxis-Daten sind versioniert, Builds reproduzierbar, Änderungen nachvollziehbar und rückholbar |
| **Neuer VPS** (Terra Cloud, deutsches Rechenzentrum) | Rechenleistung für Build und Auslieferung | DSGVO-/BDSG-konform; der Serverstandort Deutschland ist ein Verkaufsargument |
| **Coolify** | Deployment, Reverse-Proxy, TLS | orchestriert die Container, verwaltet Wildcard- und Custom-Domains, stellt Let's-Encrypt-Zertifikate aus, deployt per Webhook |

## 2. Was wo läuft

| Ort | Inhalt |
| --- | --- |
| GitLab | Theme-Repository, ein Repository je Praxis, CI-Pipeline |
| VPS | GitLab Runner (Build), Coolify, Container für die Auslieferung (Caddy/Traefik) |
| Auslieferung | statisches HTML/CSS/JS — kein PHP, keine Datenbank, kein Redaktionssystem |

## 3. Ablauf einer Änderung

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

## 4. Hugo als Generator

Hugo erzeugt aus Theme und Praxis-Daten die fertigen Seiten — in Millisekunden und ohne Laufzeitumgebung auf dem Webserver. Das Theme wird als Git-Submodule oder Hugo-Modul in fester Version je Praxis gebunden, damit ein Update eine bewusste Entscheidung bleibt (Kapitel 02).

## 5. Warum kein Redaktionssystem

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

## 6. Anforderungen an den VPS

- **Build ist CPU-lastig, Auslieferung ist leicht:** die Dimensionierung richtet sich nach der Zahl der Praxen und der Häufigkeit von Theme-Builds, nicht nach dem Traffic.
- **Speicher:** Praxis-Repositories und Build-Artefakte sind klein; Backups brauchen mehr Platz als die Daten selbst.
- **Getrennte Umgebungen:** Vorschau/Staging und Produktion getrennt halten, Vorschauen zugriffsgeschützt und nicht indexierbar.
- **Reserve einplanen:** Wachstum entsteht durch Praxen, nicht durch Lastspitzen.

## 7. Konsequenzen

- **Ein System zu betreiben:** VPS, Coolify, Runner und Container brauchen Updates, Monitoring und Backups (Kapitel 14).
- **Ausfallkonzentration:** fällt der VPS aus, sind alle Praxen offline — dafür braucht es einen dokumentierten Notfallplan (Kapitel 14).
- **Know-how:** Hugo, GitLab CI, Docker und Coolify müssen im Haus beherrscht werden.
- **Trennung bleibt:** Theme, Praxis-Daten und Auslieferung sind getrennte Ebenen (Kapitel 01) — eine Theme-Änderung wirkt zentral, ohne die Praxis-Daten zu berühren.

## 8. Offene Punkte

1. VPS-Größe und Anbieter final festlegen (Terra Cloud) und mit echten Preisen kalkulieren.
2. Das bestehende Praxistemplate als Hugo-Theme umsetzen (eigenes Arbeitspaket).
3. Redundanz und Notfallkonzept festlegen: Wie werden die statischen Seiten ausgeliefert, wenn VPS oder Coolify ausfallen?
4. Backup- und Wiederherstellungskonzept für Repositories, Theme und Secrets dokumentieren.
