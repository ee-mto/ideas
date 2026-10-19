# Betrieb & Wartung

Betrieben wird **ein System**: der VPS mit Coolify, GitLab Runner und den Auslieferungs-Containern. Alle Praxen laufen darüber — es gibt keine Einzelinstallationen mehr.

## 1. Was betrieben wird

| Baustein | Betriebsaufgabe |
| --- | --- |
| **VPS** (Terra Cloud) | Systemupdates, Ressourcen, Monitoring, Backup, Zugänge |
| **Coolify** | Version, Container, Domains, TLS-Zertifikate, Deployments |
| **GitLab + Runner** | Runner-Image, Secrets, Pipeline-Status, Repository-Backups |
| **Auslieferung** (Caddy/Traefik) | Cache, Security-Header, Ausfallsicherheit |
| **Domains und DNS** (Hetzner) | Zonen und Einträge je Praxis, API-Token, Ablaufüberwachung |

## 2. Deployment-Workflow

| Änderung | Vorgehen |
| --- | --- |
| Sprechzeiten, Aktuelles | Praxis meldet → Praxis-Repository anpassen → Commit → Pipeline baut → Coolify deployt |
| Design/Theme | Theme-Repository anpassen → Staging-Build über alle Praxen → Freigabe → Ausrollen |
| Neue Praxis | Domain registrieren, DNS-Zone per API anlegen, Einträge aus dem Deployment setzen, Domain in Coolify hinterlegen, Pipeline |
| Notfall | Coolify auf das vorherige Deployment zurückstellen oder Commit reverten |

## 3. Monitoring

- **Verfügbarkeit je Praxis:** externer Monitor auf die Startseite jeder Praxis, Alarm bei Ausfall
- **Infrastruktur:** Pipeline-Status, Runner-Auslastung, Speicherplatz, Container-Zustand, Coolify-Version
- **TLS:** Ablaufüberwachung für alle Domains, auch bei automatischer Erneuerung
- **Formular:** monatlicher Testversand je Praxis (der einzige dynamische Teil)
- **Core Web Vitals:** Search-Console-Bericht nach dem Go-Live beobachten

## 4. Backup und Wiederherstellung

| Was | Wie |
| --- | --- |
| Theme und Praxis-Repositories | GitLab-Backup plus Spiegel-Repository |
| Coolify-Konfiguration | Coolify-Backup (Konfiguration und Datenbank) |
| Secrets | Passwort-Manager, zusätzlich verschlüsseltes Backup |
| Build-Artefakte | jederzeit reproduzierbar aus Commit plus Theme-Version |
| VPS | Snapshot/Backup des Anbieters |

**Wiederherstellung üben:** Ein Restore aus Repository plus Coolify-Deployment wird dokumentiert und mindestens einmal durchgespielt.

## 5. Wartungsroutine (monatlich)

- [ ] Formularversand je Praxis testen
- [ ] Sprechzeiten, Urlaub, Aktuelles aktuell?
- [ ] SSL gültig, Security-Header unverändert
- [ ] Verfügbarkeitsmonitor ohne Alarme
- [ ] VPS-Updates, Coolify- und Container-Images aktualisiert
- [ ] Pipeline-Status und Runner aktuell, keine fehlgeschlagenen Deployments
- [ ] Backups vorhanden und lesbar

## 6. Störungen und Notfälle

| Störung | Sofortmaßnahme |
| --- | --- |
| VPS oder Coolify nicht erreichbar | Notfall-Auslieferung aus statischem Archiv, Anbieterstatus prüfen, Kunden informieren |
| Pipeline bricht ab | letzte gute Version bleibt live, Fehler beheben, erneut deployen |
| Fehlerhafte Inhalte live | Rollback auf den letzten Commit |
| Domain oder Zertifikat | DNS- und Coolify-Konfiguration prüfen |
| Kompromittierung vermutet | Container stoppen, Zugänge rotieren, Ursache klären, dann wieder online |

Grundsatz: **Rollback vor Ursachenforschung.** Die Seite muss zuerst wieder korrekt stehen.

## 7. Checkliste

- [ ] Domains und TLS live, HTTP→HTTPS 301 geprüft
- [ ] Alle Praxen über die Pipeline deploybar
- [ ] Formular sendet je Praxis an das richtige Postfach
- [ ] Search Console, Bing und Google Business Profile verknüpft
- [ ] Backup aktiv, Monitoring und SSL-Warnung eingerichtet
- [ ] Notfallplan (Auslieferung ohne VPS) dokumentiert und einmal getestet
