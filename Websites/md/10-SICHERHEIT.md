# Sicherheit

Sicherheit für statisch ausgelieferte Praxis-Websites. Grundprinzip: **minimale Angriffsfläche** – was nicht existiert, kann nicht ausgenutzt werden.

## 1. Kernprinzipien

1. **Statische Auslieferung** – kein Redaktionssystem auf dem Server, kein Server-Side-Code außer dem Formular-Handler
2. **TLS überall** – HTTPS erzwingen, HTTP→HTTPS 301, Zertifikat automatisch erneuern lassen
3. **Sicherheits-Header** – zentral gesetzt, versioniert und regelmäßig geprüft
4. **Vendor-Dateien mit SRI** – `integrity="sha384-…"` auf allen lokal gehosteten JS-Dateien, Downloads verifiziert
5. **Keine Secrets in der Website** – keine API-Keys oder Zugangsdaten in HTML/JS/CSS; Formular-Empfänger nur serverseitig

## 2. Sicherheits-Header

| Header | Sollwert |
| --- | --- |
| `Strict-Transport-Security` | `max-age=31536000; includeSubDomains; preload` |
| `X-Frame-Options` | `SAMEORIGIN` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=(), usb=(), …` |
| `Cross-Origin-Opener-Policy` | `same-origin` |
| `Cross-Origin-Resource-Policy` | `same-origin` |

Prüfbefehl: `curl -sI https://www.domain.de | grep -iE "strict-transport|x-frame|x-content|referrer|permissions"`

## 3. Formular-Härtung

- **Nur POST** akzeptieren (sonst 405)
- **Honeypot-Feld** – Bots füllen versteckte Felder aus und werden still abgewiesen
- **Referer-/Host-Prüfung** – Requests fremder Domains ablehnen
- **Input-Sanitierung** – `strip_tags`/`trim` auf allen Feldern, keine CRLF-Injection in Mail-Header (`From:`/`Reply-To:` nur aus einer festen Feldliste)
- **Keine Datenbank** – Mailversand ohne Speicherung von Patientendaten
- Optional: Rate-Limit über Session oder Zeitfenster, wenn Spam zunimmt

## 4. OWASP-Bezug (Relevanz für statische Seiten)

| Risiko | Umsetzung hier |
| --- | --- |
| A01 Zugriffskontrolle | Dateirechte, `Options -Indexes`, Regeln für sensible Dateien |
| A02 Kryptografie | TLS 1.2+, HSTS, keine Eigenbau-Krypto |
| A03 Injection | nur der Formular-Handler, Parameter strikt bereinigt, keine Shell-/DB-Aufrufe |
| A04 Designfehler | Formular läuft mit minimalen Rechten (nur Mailversand) |
| A05 Fehlkonfiguration | Konfiguration versioniert, Verzeichnislisting aus, keine Debug-Ausgaben |
| A06 Verwundbare Komponenten | Vendor-JS gepinnt + SRI, Build-Tools aktuell halten |
| A07 Authentifizierung | öffentliche Seite ohne Login; Admin-Zugänge mit 2FA |
| A08 Datenintegrität | SRI verhindert manipuliertes JS |
| A09 Monitoring | Verfügbarkeits- und SSL-Ablauf-Überwachung (Kapitel 14) |
| A10 SSRF | kein Server-Side-Fetch im Formular-Handler |

## 5. Checkliste

- [ ] HTTPS aktiv, 301-Umleitung, HSTS gesetzt
- [ ] Alle Header per `curl -sI` verifiziert
- [ ] Vendor-JS mit SRI, Downloads verifiziert
- [ ] Formular: Honeypot, Referer-Check und Sanitierung aktiv
- [ ] Repo-Scan auf Secrets (`grep -rEi "api[_-]?key|token|password" .`) ohne Treffer
- [ ] Verzeichnislisting aus, Formular-Handler nicht öffentlich debugbar

## 6. Im neuen Stack

Bei einer zentralen Build- und Deployment-Pipeline verschiebt sich die Angriffsfläche von der Website zur **Pipeline**:

- **CI/CD-Secrets** (Deploy-Zugänge, Webhook-Tokens) liegen ausschließlich in den CI-Variablen, nie im Repository oder im Theme
- **Runner härten:** keine privilegierten Container, eigene Runner-Isolation je Praxis-Gruppe, Images regelmäßig aktualisieren
- **Zugänge:** 2FA für GitLab und Coolify erzwingen, Rechte nach dem Prinzip der minimalen Berechtigung vergeben
- **Staging schützen:** Vorschau-Umgebungen nicht öffentlich indexierbar und mit Zugriffsschutz versehen
- **Updates:** Container- und Toolchain-Updates sind Teil der Wartungsroutine (Kapitel 14) – ein veralteter Runner ist das größte Risiko im gesamten Aufbau
