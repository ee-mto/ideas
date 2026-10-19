# Kosten & Kalkulation

> **Grobe Schätzung, keine Angebote.** Alle Werte sind Größenordnungen und werden durch echte Zahlen ersetzt, sobald der VPS läuft.

## 1. Was kostet — und was nicht

| Posten | Kosten | Anmerkung |
| --- | --- | --- |
| **VPS** (Terra Cloud) | ja | die einzige nennenswerte Infrastruktur |
| Backup/Snapshots, Domains | ja | kleine Posten |
| **Coolify** | **0 €** | Open Source, selbst betrieben |
| **GitLab** (Community Edition, selbst betrieben) | **0 €** | Open Source |
| **Hugo** | **0 €** | Open Source |
| Caddy/Traefik, Docker | **0 €** | Open Source |
| **Arbeitszeit** | ja | der größte Posten |
| **KI-Nutzung** (Claude) | ja | Unterstützung bei Texten, Code und Pflege |

Es gibt also **keine Lizenzkosten**: die Kosten sind ein Server, ein paar Domains, Arbeitszeit und KI-Nutzung.

## 2. Schätzung je 10 Praxen

| Posten | Größenordnung | Art |
| --- | --- | --- |
| VPS inkl. Backup (ein Server für alle Praxen) | ca. 30–80 €/Monat | laufend |
| Domains (10 × ca. 12 €/Jahr) | ca. 10 €/Monat | laufend |
| Lizenzen (Coolify, GitLab, Hugo) | 0 € | – |
| KI-Nutzung (Claude) | ca. 20–120 €/Monat | laufend |
| **Sachkosten gesamt** | **ca. 60–210 €/Monat** | laufend |
| Arbeitszeit laufend (10 × 45–90 Minuten) | 8–15 Stunden/Monat | laufend |
| Arbeitszeit einmalig (Aufbau plus 10 × Einrichtung) | ca. 25–45 Personentage | einmalig |

**Sachkosten je Praxis: ca. 6–21 €/Monat.** Der eigentliche Kostentreiber ist die Arbeitszeit, nicht die Technik.

## 3. KI-Nutzung (Claude)

| Variante | Größenordnung | Wofür |
| --- | --- | --- |
| Claude Pro | ca. 20 €/Monat | Texte, Code-Unterstützung, Änderungen |
| Claude Max | ca. 100–200 €/Monat | intensive Nutzung, mehrere Praxen parallel |
| API (nach Verbrauch) | nutzungsabhängig | Automatisierung im Build, z. B. Textvorschläge |

Preise Stand 2026 (Anthropic, in US-Dollar) — für die Kalkulation genügt die Größenordnung. Die KI-Kosten hängen an der Nutzung, nicht an der Zahl der Praxen.

## 4. Was das für die Kalkulation heißt

- Bei 10 Praxen stehen auf der Erlösseite 490–990 €/Monat (Monatspauschale 49–99 € je Praxis) plus die einmalige Setup-Gebühr.
- Die Sachkosten von 60–210 € sind davon ein kleiner Teil — entscheidend ist, wie viele Stunden Betreuung die Pauschale deckt.
- **Jede Minute, die die Routine je Praxis kürzer wird, wirkt direkt auf das Ergebnis:** Vorlagen, Standardisierung, KI-Unterstützung bei Texten und Änderungen.
- Der einmalige Aufwand (Aufbau der Infrastruktur plus Einrichtung je Praxis) muss über die Setup-Gebühr hereinkommen.

## 5. Skaleneffekte

- **Der VPS kostet bei 10 wie bei 30 Praxen ungefähr dasselbe** (bis die Dimensionierung wächst).
- **Lizenzen bleiben bei 0 €**, egal wie viele Praxen dazukommen.
- **KI-Kosten steigen mit der Nutzung, nicht mit der Zahl der Domains.**
- Wachstum ist damit fast ausschließlich Arbeitszeit — die Frage ist nicht, ob die Infrastruktur trägt, sondern ob die Routine je Praxis sinkt.

## 6. Risiken

| Risiko | Wirkung | Gegenmaßnahme |
| --- | --- | --- |
| Aufwand je Praxis steigt (viele Änderungswünsche) | Marge kippt | Änderungskontingent definieren, Mehrbedarf bepreisen |
| KI-Kosten laufen unkontrolliert | kleiner, aber unkalkulierter Posten | Nutzung beobachten, Abo statt API wo möglich |
| VPS wird zu klein | langsame Builds, Ausfälle | rechtzeitig skalieren, Monitoring (Kapitel 14) |
| Ausfall des VPS | alle Praxen offline | Redundanz und Notfallplan (Kapitel 14) |
