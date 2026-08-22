# Gesamtarchitektur

## Architekturdiagramm

```
┌─────────────────────────────────────────────────────────────────────┐
│                        Support-Mitarbeiter                          │
│                    (im neuen Ticketsystem)                          │
└──────────────────────────┬──────────────────────────────────────────┘
                           │
                           ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      Neues Ticketsystem                              │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │  MCP-Client (im Ticketsystem integriert)                     │   │
│  │  - Sendet Kontext (Ticket-ID, Problembeschreibung)           │   │
│  │  - Empfängt Lösungsvorschläge und Wissensartikel             │   │
│  │  - Zeigt Ergebnisse direkt in der Ticket-Oberfläche an       │   │
│  └──────────────────────────┬───────────────────────────────────┘   │
└─────────────────────────────┼───────────────────────────────────────┘
                              │
                              │ MCP-Protokoll (HTTP/JSON-RPC)
                              ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     MCP-Wissensdatenbank-Server                       │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐   │
│  │                   Orchestrierungsschicht                      │   │
│  │  - Nimmt MCP-Tools-Anfragen entgegen                         │   │
│  │  - Routet an zuständige Datenquelle                          │   │
│  │  - Vereinheitlicht Antwortformat                             │   │
│  │  - Caching (TTL-basiert)                                     │   │
│  │  - Authentifizierung (API-Token)                             │   │
│  └──────────────────────────────────────────────────────────────┘   │
│                              │                                       │
│     ┌────────────────────────┼────────────────────────────┐         │
│     ▼                        ▼                            ▼         │
│  ┌──────────────┐    ┌──────────────┐          ┌──────────────┐    │
│  │ Wissensdaten- │    │  Ticket-     │          │  Externe     │    │
│  │ bank-Adapter  │    │  Historien-  │          │  FAQ-Adapter │    │
│  │               │    │  Adapter     │          │              │    │
│  │ - KB-Suche    │    │ - Alte       │          │ - FAQ-Suche  │    │
│  │ - Artikel     │    │   Tickets    │          │ - Auth       │    │
│  │ - Kategorien  │    │   durchsuchen│          │ - Crawling   │    │
│  └───────┬───────┘    └───────┬──────┘          └───────┬──────┘    │
└──────────┼────────────────────┼──────────────────────────┼──────────┘
           │                    │                          │
           ▼                    ▼                          ▼
    ┌──────────────┐   ┌──────────────┐          ┌──────────────┐
    │  Interne     │   │  Exportierte  │          │  FAQ-Portal  │
    │  Wissensdaten│   │  Ticket-DB   │          │  (extern,    │
    │  bank (z.B.  │   │  (Read-only) │          │  hinter      │
    │  Confluence/ │   │              │          │  Login)      │
    │  Wiki)       │   │  SQL/ES/Dump │          │              │
    └──────────────┘   └──────────────┘          └──────────────┘
```

## MCP-Tools (Übersicht)

Der Server stellt folgende MCP-Tools bereit:

| Tool | Beschreibung | Datenquelle |
|------|-------------|-------------|
| `kb_search` | Volltextsuche in der Wissensdatenbank | Interne KB |
| `kb_get_article` | Einzelnen Artikel abrufen | Interne KB |
| `kb_list_categories` | Kategorien/Ordnerstruktur auflisten | Interne KB |
| `ticket_search_history` | Historische Tickets durchsuchen | Altes Ticketsystem (Export) |
| `ticket_get_history` | Einzelnes historisches Ticket abrufen | Altes Ticketsystem (Export) |
| `faq_search` | FAQ durchsuchen | Internes FAQ |
| `faq_search_external` | Externes FAQ-Portal durchsuchen | Externes Portal (via API/Scrape) |
| `solution_suggest` | Lösungsvorschläge zu Problembeschreibung | Alle Quellen aggregiert |

## Technologie-Entscheidungen

| Aspekt | Entscheidung | Begründung |
|--------|-------------|-----------|
| **Protokoll** | MCP over HTTP (JSON-RPC 2.0) | Standard für MCP, einfaches Routing |
| **Sprache** | TypeScript (ESM) | Bewährt in bestehenden MCP-Projekten |
| **Framework** | Express.js + MCP SDK | StreamableHTTP-Transport, erprobt |
| **Datenbank** | PostgreSQL (für KB-Struktur) | Relational, Volltextsuche, JSON-Support |
| **Cache** | Redis (optional) | Für häufige Suchanfragen |
| **Auth** | Bearer-Token (pro Client) | Einfach, sicher, auditierbar |
| **Deployment** | Docker + Coolify | Bestehende Infrastruktur |
