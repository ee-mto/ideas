# Betrieb & Wartung

## 1. Hosting: zwei Wege

| Kriterium | STRATO-Webhosting (Modell A) | Terra Cloud + Coolify (Modell B) |
| --- | --- | --- |
| Betriebsaufwand | keiner – Webhosting-Tarif, Panel | eigener Server: Updates, Monitoring, Backups |
| Auslieferung | Apache, `.htaccess`, PHP 8.4 | Nginx/Caddy-Container hinter Coolify-Proxy |
| SSL | automatisch über STRATO | Let's Encrypt über Coolify |
| Deployment | SFTP/rsync je Praxis | Git-Push, Webhook, Pipeline |
| Skalierung | ein Tarif je Praxis | eine Infrastruktur für viele Praxen |
| Ausfallrisiko | verteilt (je Praxis) | konzentriert (alle Praxen) |
| DSGVO | deutsches Rechenzentrum, AV-Vertrag | deutsches Rechenzentrum (Wortmann AG), AV-Vertrag |
| Kosten | ab ca. 10 €/Monat je Praxis | ein VPS + Runner für alle Praxen |
| Passend für | Einzelpraxen, Managed Service | viele Praxen, zentrale Pflege |

## 2. Deployment-Workflow (Modell A)

| Änderung | Vorgehen |
| --- | --- |
| Sprechzeiten, Aktuelles | Datenquelle anpassen (in `config.js`/Content) → nur geänderte Dateien hochladen |
| Design | `styles.css` anpassen → Upload, Cache-Busting (`?v=`) erhöhen |
| Interaktion/JS | Quelle editieren → Build (`npm run build`) → kompiliertes Bundle hochladen |
| Geplant | GitLab CI/CD: Push auf `main` → rsync/lftp auf das Hosting (Zugangsdaten in CI-Variablen) |

Wichtig beim Upload: `.htaccess`, Formular-Handler, `assets/`, `robots.txt` und `sitemap.xml` mitnehmen – auch versteckte Dateien.

## 3. Monitoring

- **Verfügbarkeit:** externer Monitor auf die Startseite jeder Praxis, Alarm bei Ausfall (Uptime-Monitor oder Zabbix)
- **SSL-Ablauf:** Warnung einrichten, auch wenn die Verlängerung automatisch läuft
- **Formular:** monatlicher Testversand (das Formular ist der einzige dynamische Teil)
- **Core Web Vitals:** Search-Console-Bericht nach dem Go-Live beobachten
- **Im Factory-Modell zusätzlich:** Pipeline-Status, Runner-Auslastung, Speicherplatz der Praxis-Repositories

## 4. Backup und Wiederherstellung

| Was | Wie |
| --- | --- |
| Website-Dateien | Hosting-Backup (Tarif-Funktion) + Kopie im Repository |
| Praxis-Daten und Inhalte | Git-Historie je Praxis – vollständig versioniert |
| Theme und Konfiguration | zentrales Repository |
| Zugangsdaten | Passwort-Manager (nie im Repo) |
| Datenbanken | nur relevant, wenn eine Praxis echte Anwendungsdaten hat – Standard ist: keine |

**Wiederherstellung üben:** Ein Restore aus dem Repository plus Deployment muss dokumentiert und mindestens einmal durchgespielt sein.

## 5. Wartungsroutine (monatlich)

- [ ] Formularversand je Praxis testen
- [ ] Sprechzeiten, Urlaub, Aktuelles aktuell?
- [ ] SSL gültig, Security-Header unverändert
- [ ] Verfügbarkeitsmonitor ohne Alarme
- [ ] Abhängigkeiten, Build-Tools und (im Factory-Modell) Container-Images aktualisiert
- [ ] Backups vorhanden und lesbar

## 6. Störungen und Notfälle

| Störung | Sofortmaßnahme |
| --- | --- |
| Seite nicht erreichbar | Hosting-Status prüfen, DNS prüfen, letzte Änderung zurückrollen |
| Formular sendet nicht | Ersatzweg kommunizieren (Telefon/E-Mail prominent), Handler prüfen |
| Falsche Inhalte live | Rollback auf den letzten Commit, Korrektur, erneut deployen |
| Kompromittierung vermutet | Seite offline nehmen, Zugänge rotieren, Ursache klären, dann wieder online |

Grundsatz: **Rollback vor Ursachenforschung.** Die Seite muss zuerst wieder korrekt stehen.

## 7. Checkliste

- [ ] Domain und SSL live, HTTP→HTTPS 301 geprüft
- [ ] Alle Dateien inklusive versteckter Dateien deployed
- [ ] Formular sendet an das Praxis-Postfach
- [ ] Search Console, Bing und Google Business Profile verknüpft
- [ ] Backup aktiv, Monitoring und SSL-Warnung eingerichtet
