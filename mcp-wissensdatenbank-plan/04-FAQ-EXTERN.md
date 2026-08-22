# Externes FAQ-Portal – Konzept

## Idee

Ein externes FAQ-Portal bietet Kunden selbstständige Hilfe zu häufigen Problemen. Dieses Portal liegt **hinter einer Authentifizierung** (Login-Bereich) und ist daher nicht öffentlich zugänglich.

Für Support-Mitarbeiter soll dieses FAQ ebenfalls durchsuchbar sein – ohne dass sie sich separat einloggen müssen. Der MCP-Server übernimmt die Authentifizierung transparent.

## Architektur

```
┌──────────────────────────────────────────────────────────────┐
│                    Kunde (extern)                             │
│                                                              │
│  Browser ───▶ FAQ-Portal ───▶ Login ───▶ FAQ-Artikel lesen  │
└──────────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────────┐
│                Support-Mitarbeiter (intern)                   │
│                                                              │
│  Ticketsystem ───▶ MCP-Server ───▶ FAQ-Adapter ───▶ Portal  │
│                      │                  │                    │
│                  faq_search_          Auth-Token             │
│                  external()           (hinterlegt)           │
└──────────────────────────────────────────────────────────────┘
```

## Anbindungsvarianten

### Variante A: REST-API (⭐ Empfohlen)

Das FAQ-Portal bietet eine API für die Suche.

```
GET /api/faq/search?q={query}
Authorization: Bearer {api-token}

Response:
{
  "results": [
    {
      "id": 123,
      "title": "Drucker einrichten",
      "excerpt": "So richten Sie Ihren Drucker ein...",
      "url": "https://faq.example.de/artikel/123",
      "category": "Drucker",
      "updated_at": "2026-06-15"
    }
  ]
}
```

**Vorteile:** Sauber, schnell, wenig Ressourcen
**Nachteile:** API muss vom Portal bereitgestellt werden

### Variante B: Headless-Browser (Crawler)

Der MCP-Server verwendet einen Headless-Browser (Playwright/Puppeteer), um sich einzuloggen und die FAQ-Seiten zu crawlen.

```
MCP-Server ───▶ Login (Credentials hinterlegt)
     │              │
     │              ▼
     │         ───▶ FAQ-Startseite
     │              │
     │              ▼
     ├──▶ Seite 1 crawlen ───▶ Index
     ├──▶ Seite 2 crawlen ───▶ Index
     └──▶ Seite n crawlen ───▶ Index
```

**Vorteile:** Keine API nötig, funktioniert mit jedem Portal
**Nachteile:** Langsam, wartungsintensiv (bei UI-Änderungen), Ressourcen-lastig

### Variante C: Regelmäßiger Export

Das FAQ-Portal bietet einen Export (XML, JSON, PDF), der regelmäßig in den MCP-Server importiert wird.

```
FAQ-Portal ───▶ Export (täglich) ───▶ MCP-Server-Index
                                        │
                                        ▼
                                   Suche über
                                   importierte Daten
```

**Vorteile:** Einfach, performant, keine Live-Abhängigkeit
**Nachteile:** Daten sind nicht tagesaktuell (max. 24h alt)

---

## Empfohlenes Vorgehen

| Phase | Variante | Begründung |
|-------|----------|-----------|
| **1. Sofort (MVP)** | Variante C (Export) | Schnell umsetzbar, keine API nötig |
| **2. Kurzfristig** | Variante A (API) | Wenn FAQ-Portal API bereitstellt |
| **3. Mittelfristig** | Hybrid: API + Export | Fallback wenn API nicht erreichbar |

---

## FAQ-Portal: Feature-Ideen

Das FAQ-Portal selbst könnte um folgende Funktionen erweitert werden:

| Feature | Nutzen |
|---------|--------|
| **Volltextsuche** | Kunden finden Antworten schnell |
| **Kategorien** | Strukturierte Navigation |
| **Bewertung** | "War dieser Artikel hilfreich?" |
| **Feedback** | "Antwort nicht gefunden" → Ticket-Erstellung |
| **Artikel-Versionen** | Änderungen nachvollziehbar |
| **PDF-Export** | Artikel als PDF speicherbar |
| **MCP-API** | Direkte Anbindung an das Ticketsystem |

---

## Technische Umsetzung (Skizze)

### Crawler-Variante (Playwright)

```typescript
import { chromium } from 'playwright';

async function crawlFAQ(): Promise<FAQArticle[]> {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Login
  await page.goto('https://faq.example.de/login');
  await page.fill('#username', process.env.FAQ_USER);
  await page.fill('#password', process.env.FAQ_PASS);
  await page.click('#login-button');
  await page.waitForNavigation();

  // FAQ-Seiten crawlen
  const articles: FAQArticle[] = [];
  const urls = await page.locator('.faq-article a').allHrefs();

  for (const url of urls) {
    await page.goto(url);
    articles.push({
      title: await page.locator('h1').textContent(),
      content: await page.locator('.article-content').textContent(),
      url: page.url(),
    });
  }

  await browser.close();
  return articles;
}
```

### API-Variante (TypeScript)

```typescript
async function searchExternalFAQ(query: string): Promise<SearchResult[]> {
  const response = await fetch('https://faq.example.de/api/search', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${process.env.FAQ_API_TOKEN}`,
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ q: query, limit: 10 }),
  });

  if (!response.ok) {
    throw new Error(`FAQ API error: ${response.status}`);
  }

  const data = await response.json();
  return data.results.map(r => ({
    title: r.title,
    excerpt: r.excerpt,
    url: r.url,
    source: 'faq-extern',
    score: r.score,
  }));
}
```
