# MCP-Wissensdatenbank – Plan und Architektur

> **Projekt:** Wissensdatenbank-Anbindung per MCP-Server
> **Kunde:** engel&engel gmbh
> **Stand:** Juli 2026

## Übersicht

Dieses Projekt beschreibt die Architektur und Umsetzung eines **MCP-Servers (Model Context Protocol)**, der Support-Mitarbeitern den Zugriff auf verschiedene Wissensquellen ermöglicht – direkt aus dem Ticketsystem heraus.

### Kernziele

- Support-Mitarbeiter greifen während der Ticketbearbeitung auf Wissensdatenbanken zu
- Altes Ticketsystem wird als historische Datenquelle eingebunden
- Neues Ticketsystem erhält MCP-Anbindung für Kontextabfragen
- Mehrere Wissenspools (Wiki, Runbooks, Dokumentation) werden zentral durchsuchbar
- Externes FAQ-Portal (hinter Login) wird für Supporter erschlossen

### Inhalte

| Datei | Beschreibung |
|-------|-------------|
| [01-ARCHITEKTUR.md](01-ARCHITEKTUR.md) | Gesamtarchitektur und Systemübersicht |
| [02-KOMPONENTEN.md](02-KOMPONENTEN.md) | Detailbeschreibung aller Komponenten |
| [03-INTEGRATION.md](03-INTEGRATION.md) | Integration der Ticketsysteme und Wissenspools |
| [04-FAQ-EXTERN.md](04-FAQ-EXTERN.md) | Konzept für externes FAQ-Portal |
| [05-STRASSENKARTE.md](05-STRASSENKARTE.md) | Umsetzungsfahrplan |
| [index.html](index.html) | Gesamtdokument als HTML (PDF-exportierbar) |

### Verwandte Projekte im eenet-Kontext

- `azure-hybrid-join/` – Technische Dokumentation Azure/Entra ID
- `social-media-plan/` – Social-Media-Strategie
- `SECURITY_AUDIT_2_engel-engel.de.md` – Sicherheitsaudit (Score 72/100)
