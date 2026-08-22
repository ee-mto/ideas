# Umsetzungsfahrplan

## Phasenübersicht

```
Phase 1: Basis           ───▶ 2 Wochen
Phase 2: Wissensdatenbank ───▶ 4 Wochen
Phase 3: FAQ-Integration  ───▶ 3 Wochen
Phase 4: Optimierung      ───▶ 2 Wochen
                               ────────
                               11 Wochen gesamt
```

---

## Phase 1: Basis (Woche 1–2)

### Ziel: MCP-Server-Grundgerüst bereitstellen

| Aufgabe | Beschreibung | Dauer |
|---------|-------------|-------|
| 1.1 | Git-Projekt anlegen (`mcp-wissensdatenbank`) | 1 Tag |
| 1.2 | MCP-Server-Skeleton (Express + MCP-SDK + Auth) | 3 Tage |
| 1.3 | Health-/Metrics-Endpunkt | 1 Tag |
| 1.4 | CI/CD-Pipeline (.gitlab-ci.yml + Docker) | 2 Tage |
| 1.5 | Deployment auf Coolify | 1 Tag |
| 1.6 | Basis-Test (Tool-Count, Smoke-Test) | 1 Tag |
| 1.7 | Dokumentation (README, AGENTS.md) | 1 Tag |

**Ergebnis:** Lauffähiger MCP-Server mit Auth, aber ohne Datenquellen.

---

## Phase 2: Wissensdatenbank (Woche 3–6)

### Ziel: Interne Wissensdatenbank anbinden + historische Tickets

| Aufgabe | Beschreibung | Dauer |
|---------|-------------|-------|
| 2.1 | Datenmodell für Wissensartikel definieren | 2 Tage |
| 2.2 | PostgreSQL-Tabellen erstellen + Indexe | 1 Tag |
| 2.3 | `kb_search`-Tool implementieren | 2 Tage |
| 2.4 | `kb_get_article`-Tool implementieren | 1 Tag |
| 2.5 | `kb_list_categories`-Tool implementieren | 1 Tag |
| 2.6 | Wissensdatenbank-Befüllung (Migration/Import) | 3 Tage |
| 2.7 | Altes Ticketsystem exportieren | 2 Tage |
| 2.8 | Export bereinigen + normalisieren | 3 Tage |
| 2.9 | Historische Tickets in Suchindex importieren | 2 Tage |
| 2.10 | `ticket_search_history`-Tool implementieren | 2 Tage |
| 2.11 | `ticket_get_history`-Tool implementieren | 1 Tag |
| 2.12 | Integrationstests | 2 Tage |

**Ergebnis:** Supporter können in der Wissensdatenbank und in historischen Tickets suchen.

---

## Phase 3: FAQ-Integration (Woche 7–9)

### Ziel: FAQ-Portale (intern + extern) anbinden

| Aufgabe | Beschreibung | Dauer |
|---------|-------------|-------|
| 3.1 | Internes FAQ identifizieren + exportieren | 2 Tage |
| 3.2 | `faq_search`-Tool implementieren | 2 Tage |
| 3.3 | Externes FAQ-Portal analysieren (API vorhanden?) | 2 Tage |
| 3.4 | **Variante C (Export):** FAQ exportieren + importieren | 2 Tage |
| 3.5 | **Variante A (API):** FAQ-API-Adapter bauen | 3 Tage |
| 3.6 | **Variante B (Crawler):** Playwright-Crawler bauen | 4 Tage |
| 3.7 | `faq_search_external`-Tool implementieren | 2 Tage |
| 3.8 | `solution_suggest`-Pipeline (Aggregation) | 3 Tage |

**Ergebnis:** Supporter erhalten Lösungsvorschläge aus allen Quellen.

---

## Phase 4: Optimierung (Woche 10–11)

### Ziel: Performance, UX, Betrieb

| Aufgabe | Beschreibung | Dauer |
|---------|-------------|-------|
| 4.1 | Caching-Strategie implementieren (TTL) | 2 Tage |
| 4.2 | Ranking verbessern (Feedback-Loop) | 2 Tage |
| 4.3 | Audit-Log (wer sucht wann wonach?) | 1 Tag |
| 4.4 | Rate-Limiting konfigurieren | 1 Tag |
| 4.5 | Monitoring (Prometheus-Metriken) | 1 Tag |
| 4.6 | Lasttest (k6 / autocannon) | 2 Tage |
| 4.7 | Rollout und Supporter-Schulung | 2 Tage |

**Ergebnis:** Produktionsreifer MCP-Server mit Monitoring.

---

## Ressourcenabschätzung

### Entwicklungsaufwand

| Rolle | Tage | Verteilung |
|-------|------|-----------|
| Backend-Entwickler (TypeScript) | 25 | Phasen 1–4 |
| Datenbank/DevOps | 10 | Phasen 2 + 4 |
| FAQ-Portal-Integration | 8 | Phase 3 |
| Projektleitung/Koordination | 5 | Begleitend |

**Gesamt:** ca. 48 Personentage (11 Wochen)

### Infrastruktur

| Ressource | Kosten (mtl.) |
|-----------|--------------|
| Server (Docker-Host) | Bereits vorhanden (Coolify) |
| PostgreSQL-Datenbank | Bereits vorhanden oder ~5 €/mtl. |
| Redis (optional) | ~3 €/mtl. |
| **Gesamt** | **~8 €/mtl.**
