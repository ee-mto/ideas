# Integration der Systeme

## 1. Ticketsysteme

### Altes Ticketsystem → MCP-Server

```
┌────────────────────┐     ┌──────────────────┐     ┌──────────────────┐
│  Altes Ticketsystem│────▶│  Datenexport      │────▶│  Suchindex       │
│  (wird abgeschafft)│     │  (CSV, SQL, JSON) │     │  (PostgreSQL/ES) │
└────────────────────┘     └──────────────────┘     └────────┬─────────┘
                                                             │
                                                             ▼
                                                    ┌──────────────────┐
                                                    │  MCP-Server      │
                                                    │  ticket_search_  │
                                                    │  history()       │
                                                    └──────────────────┘
```

**Schritte:**
1. Datenexport aus dem alten System anstoßen
2. Export bereinigen, normalisieren, Felder mappen
3. In Suchdatenbank importieren (einmalig, keine Synchronisation nötig)
4. MCP-Adapter greift read-only auf den Suchindex zu

**Wichtiger Hinweis:** Das alte System wird nach erfolgreicher Migration und Datenübernahme abgeschaltet. Es gibt keine Live-Synchronisation – der Export ist ein Snapshot.

### Neues Ticketsystem → MCP-Client

```
┌──────────────────────┐     ┌──────────────────┐
│  Neues Ticketsystem  │────▶│  MCP-Client      │
│                      │     │  (Plugin/Widget) │
│  - Ticket-Oberfläche │     │                  │
│  - Suche-Button      │     │  Sendet Kontext  │
│  - Ergebnis-Panel    │     │  Erhält Lösungen │
└──────────────────────┘     └────────┬─────────┘
                                      │
                                      ▼
                             ┌──────────────────┐
                             │  MCP-Server      │
                             │  (Knowledge Base)│
                             └──────────────────┘
```

**Integration im neuen Ticketsystem:**

| Methode | Beschreibung | Aufwand |
|---------|-------------|---------|
| **Native MCP-Unterstützung** | Ticketsystem hat natives MCP-Client-Interface | Gering (falls vorhanden) |
| **Browser-Plugin** | MCP-Client als Browser-Erweiterung | Mittel |
| **Custom Widget** | Eigenes UI-Element in der Ticket-Oberfläche | Hoch |
| **Slash-Command** | `/kb <suche>` im Ticket-Editor | Gering |

**Empfehlung:** Zunächst mit Browser-Plugin oder Slash-Command starten, später natives MCP-Interface nutzen.

---

## 2. Wissenspools

### Übersicht der Wissensquellen

| Quelle | Typ | Inhalt | Priorität |
|--------|-----|--------|-----------|
| Interne Wissensdatenbank | Strukturiert | Technische Artikel, Anleitungen | ⭐⭐⭐ |
| Historische Tickets | Archiv | Gelöste Probleme, Lösungen | ⭐⭐⭐ |
| FAQ (intern) | Strukturiert | Häufige Fragen | ⭐⭐ |
| Externes FAQ-Portal | Web (hinter Login) | Kunden-FAQ | ⭐⭐ |
| Runbooks/SOPs | Markdown/Git | Standardvorgehen | ⭐⭐ |
| Hersteller-Dokumentation | Web/PDF | Vendor-Docs | ⭐ |

### Integration der Wissenspools

```
                       ┌─────────────────────────┐
                       │   MCP-Wissensdatenbank   │
                       │         Server           │
                       └──────────┬──────────────┘
                                  │
        ┌─────────────────────────┼──────────────────────────┐
        ▼                         ▼                          ▼
┌──────────────┐         ┌──────────────┐          ┌──────────────┐
│  ADAPTER:    │         │  ADAPTER:    │          │  ADAPTER:    │
│  Knowledge   │         │  Ticket-     │          │  FAQ extern  │
│  Base        │         │  History     │          │              │
│              │         │              │          │              │
│  REST-API    │         │  SQL/ES      │          │  API / Crawl │
│  (Confluence │         │  (Read-only) │          │  (Auth)      │
│   o.ä.)      │         │              │          │              │
└──────┬───────┘         └──────────────┘          └──────────────┘
       │
       ├── Confluence REST API
       ├── BookStack REST API
       ├── Markdown-Git-Repository
       └── SQL-Direktzugriff (eigenes Wiki)
```

---

## 3. Authentifizierung und Berechtigungen

### MCP-Server Auth

```
Client (Ticketsystem)          MCP-Server
        │                          │
        │ POST /mcp                │
        │ Authorization: Bearer <token>
        │─────────────────────────▶│
        │                          │──▶ Token validieren
        │                          │──▶ Scope prüfen
        │                          │──▶ Anfrage ausführen
        │◀─────────────────────────│
        │ {content: [...],         │
        │  isError: false}         │
```

### Token-Management

- Jeder Client (Ticketsystem, Webbrowser, CLI) erhält einen eigenen API-Token
- Tokens werden in der MCP-Server-Konfiguration hinterlegt
- Tokens können scoped sein (z.B. nur `kb_search`, kein `ticket_search_history`)
- Rotation: Jährlicher Wechsel der Tokens

### Externes FAQ: Authentifizierung

Der MCP-Server muss sich gegenüber dem externen FAQ-Portal authentisieren:

```
MCP-Server ───▶ FAQ-Portal (extern)
                      │
               ┌──────┴──────┐
               │  Auth-Typen: │
               │  • API-Key   │
               │  • JWT       │
               │  • Basic Auth│
               │  • Session   │
               └──────────────┘
```

---

## 4. Sicherheitsaspekte

| Bereich | Maßnahme |
|---------|----------|
| **Transport** | HTTPS-only (TLS 1.3) |
| **Auth** | Bearer-Token, kein Session-Cookie |
| **Rate-Limiting** | Pro IP und Token (100 req/min) |
| **Audit-Log** | Jede Suche wird geloggt (wer, wann, was) |
| **Daten-Minimierung** | Nur lesender Zugriff, keine Schreiboperationen |
| **Externes FAQ** | Keine Weitergabe der FAQ-Zugangsdaten an Clients |
