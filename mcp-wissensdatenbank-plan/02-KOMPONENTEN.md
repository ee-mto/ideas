# Komponenten im Detail

## 1. MCP-Wissensdatenbank-Server

Der zentrale MCP-Server ist das Herzstück. Er nimmt Anfragen von MCP-Clients (z.B. aus dem Ticketsystem) entgegen und liefert strukturierte Antworten.

### Aufbau

```
mcp-wissensdatenbank/
├── src/
│   ├── index.ts                    # Einstiegspunkt (Express-Server)
│   ├── server.ts                   # MCP-Transport (StreamableHTTP)
│   ├── tools.ts                    # Tool-Definitionen + Dispatch
│   ├── auth.ts                     # Token-Validierung
│   ├── cache.ts                    # TTL-Cache (Speicher/Redis)
│   ├── adapters/
│   │   ├── knowledge-base.ts       # Anbindung interne Wissensdatenbank
│   │   ├── ticket-history.ts       # Anbindung altes Ticketsystem
│   │   └── faq-external.ts         # Anbindung externes FAQ-Portal
│   ├── pipelines/
│   │   └── solution-suggest.ts     # Lösungsvorschläge aggregieren
│   └── utils/
│       ├── text-search.ts          # Volltextsuche-Helfer
│       └── formatter.ts            # Antwort-Formatierung
├── config/
│   └── sources.json                # Datenquellen-Konfiguration
├── Dockerfile
├── .gitlab-ci.yml
└── package.json
```

### Technischer Stack

| Komponente | Technologie |
|-----------|-------------|
| **Sprache** | TypeScript (ESM, ES2022) |
| **Webframework** | Express.js |
| **MCP-SDK** | @modelcontextprotocol/sdk (StreamableHTTP) |
| **Datenbank-Client** | pg (PostgreSQL) / prisma |
| **HTTP-Client** | undici / axios |
| **Volltextsuche** | PostgreSQL tsvector / Elasticsearch |
| **Caching** | node-cache (In-Memory) / Redis |
| **Auth** | crypto (Token-Hash-Vergleich) |
| **Test** | Vitest |
| **Build** | tsc |
| **Container** | Docker (Multi-Stage, Alpine) |

---

## 2. Wissensdatenbank-Adapter

### Interne Wissensdatenbank

Die primäre Wissensquelle. Enthält:
- Technische Artikel und Anleitungen
- Bekannte Probleme und Lösungen
- Konfigurationshandbücher
- Kunden-spezifische Dokumentation

**Anbindungsmöglichkeiten:**

| System | Adapter-Typ | Aufwand |
|--------|------------|---------|
| Confluence | REST-API | Mittel |
| BookStack | REST-API | Gering |
| MediaWiki | REST-API | Gering |
| Markdown-Dateien (Git) | File-Reader mit Index | Gering |
| Eigenes Wiki | SQL-Direktzugriff | Mittel |

### Datenmodell (Vorschlag)

```sql
CREATE TABLE knowledge_articles (
    id          UUID PRIMARY KEY,
    title       TEXT NOT NULL,
    content     TEXT NOT NULL,
    category_id UUID REFERENCES categories(id),
    tags        TEXT[],
    source      TEXT,         -- z.B. 'confluence', 'internal', 'migration'
    source_url  TEXT,         -- Original-URL im Quellsystem
    created_at  TIMESTAMPTZ,
    updated_at  TIMESTAMPTZ
);

CREATE TABLE categories (
    id          UUID PRIMARY KEY,
    name        TEXT NOT NULL,
    parent_id   UUID REFERENCES categories(id),
    sort_order  INTEGER
);
```

---

## 3. Ticket-Historien-Adapter

### Altes Ticketsystem (Read-only)

Das alte Ticketsystem wird abgeschaltet. Die historischen Daten müssen exportiert und für die Suche erschlossen werden.

**Vorgehen:**

1. **Vollexport** des alten Ticketsystems (CSV, SQL-Dump, JSON)
2. **Datenbereinigung** und Normalisierung
3. **Import** in eine Suchdatenbank (PostgreSQL / Elasticsearch)
4. **Read-only-Zugriff** über den MCP-Server

**Suchbare Felder:**

- Ticket-ID
- Betreff
- Beschreibung
- Lösungsbeschreibung
- Kategorie
- Status
- Datum
- Kundenname

**Wichtiger Hinweis:** Der Export dient ausschließlich der Referenz. Neue Tickets werden nur im neuen System erstellt.

---

## 4. FAQ-Adapter

### Internes FAQ

Bereits vorhandene FAQ-Artikel (z.B. in der Wissensdatenbank oder als Markdown-Dateien) werden durchsuchbar gemacht.

### Externes FAQ-Portal

Das externe FAQ-Portal (hinter Login) wird über einen speziellen Adapter angebunden:

- **Variante A: API** – Das Portal bietet eine API mit Authentifizierung
- **Variante B: Crawler** – Der Adapter authentifiziert sich per Headless-Browser und crawlt die FAQ-Seiten
- **Variante C: Export** – Das Portal bietet einen FAQ-Export (PDF/XML), der importiert wird

**Siehe:** [04-FAQ-EXTERN.md](04-FAQ-EXTERN.md) für das detaillierte Konzept.

---

## 5. Solutions-Pipeline

Die `solution_suggest`-Pipeline aggregiert Ergebnisse aus **allen** Quellen und gewichtet sie:

```
Problem-Beschreibung
        │
        ▼
┌───────────────────┐
│  Parallele Suche   │
│  in allen Quellen  │
│                    │
│  ├─ KB-Artikel     │
│  ├─ Historische    │
│  │  Tickets        │
│  ├─ FAQ            │
│  └─ Externes FAQ   │
└─────────┬──────────┘
          │
          ▼
┌───────────────────┐
│  Ranking & Merge   │
│                    │
│  Nach Relevanz:    │
│  1. KB-Artikel     │
│  2. FAQ-Treffer    │
│  3. Historische    │
│     Tickets        │
└─────────┬──────────┘
          │
          ▼
┌───────────────────┐
│  Antwort an Client │
│                    │
│  Top-5 Ergebnisse  │
│  mit Titel,        │
│  Quelle, Link      │
└───────────────────┘
```

### Ranking-Faktoren

| Faktor | Gewicht | Beschreibung |
|--------|---------|-------------|
| Keyword-Übereinstimmung | 40 % | Wie viele Suchbegriffe werden gefunden |
| Aktualität | 20 % | Neuere Artikel/Aktualisierungen |
| Kategorie-Übereinstimmung | 20 % | Gleiche Kategorie wie Ticket |
| Nutzer-Bewertung | 10 % | Wie hilfreich wurde der Artikel bewertet |
| Quelle | 10 % | Vertrauenswürdigkeit der Quelle |
