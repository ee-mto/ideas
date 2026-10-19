# Performance

Ziel sind **grüne Core Web Vitals**: LCP ≤ 2,5 s, INP ≤ 200 ms, CLS ≤ 0,1. Für statisch ausgelieferte Seiten ist das ohne Kunstgriffe erreichbar – die Ladezeit ist gleichzeitig das stärkste Verkaufsargument gegenüber WordPress-Praxen.

## 1. Ziele

| Metrik | Zielwert | Was sie misst |
| --- | --- | --- |
| **LCP** (Largest Contentful Paint) | ≤ 2,5 s | wann das größte sichtbare Element geladen ist |
| **INP** (Interaction to Next Paint) | ≤ 200 ms | Reaktionszeit auf Nutzerinteraktionen |
| **CLS** (Cumulative Layout Shift) | ≤ 0,1 | visuelle Stabilität während des Ladens |

## 2. Kernmaßnahmen (in dieser Reihenfolge)

1. **Statisch ausliefern** – keine Server-Roundtrips, kein Datenbankzugriff, HTTP/2 und `cache-control` gesetzt
2. **Ein einziges Stylesheet** – Designsystem statt Framework-CSS, kritische Assets per `preload`
3. **JavaScript klein halten** – React lokal (ca. 140 KB Vendor + 28 KB App-Bundle), kein Hydration-Overhead, Skripte am Body-Ende
4. **Bilder optimieren** – WebP/AVIF, `loading="lazy"` (außer Hero), `width`/`height` gesetzt, responsive `srcset`
5. **Fonts lokal** – woff2 selbst gehostet, `font-display: swap`, nur benötigte Schnitte, System-Stack als Default
6. **Caching** – CSS/JS 7 Tage, Bilder/Fonts 30 Tage, Versionierung über `?v=…` bei Änderungen

## 3. Messung

- **Lighthouse** (Chrome DevTools) – Ziel: Performance ≥ 90, alle CWV grün
- **PageSpeed Insights** – Labor- und Felddaten
- Nach Go-Live: Core-Web-Vitals-Bericht in der Search Console beobachten

## 4. Typische Fehler in Praxis-Projekten

- Stockfotos in Originalgröße (2 MB+) → vorher komprimieren
- Google Fonts oder CDN-Requests → kosten LCP und verletzen die Datenschutz-Grundregel
- Layout-Shifts durch fehlende Bilddimensionen oder nachladende Banner
- Dutzende CSS/JS-Dateien statt einem Bundle
- Consent-Banner oder Popups, die Inhalte nachladen – ein Consent-Layer ist nur bei aktivem Tracking nötig

## 5. Checkliste

- [ ] Lighthouse ≥ 90, LCP < 2,5 s (Test mit 4G-Drosselung)
- [ ] CLS < 0,1 (Bilddimensionen gesetzt, keine nachladenden Elemente)
- [ ] INP < 200 ms (kein blockierendes JS, leichtgewichtiges FAQ-Akkordeon)
- [ ] Bilder WebP/AVIF + lazy, Hero eager mit `fetchpriority="high"`
- [ ] Cache-Header gesetzt, Assets versioniert
- [ ] Fonts lokal mit `swap`, kein externes CSS/JS

## 6. Im neuen Stack

- Die Performance-Budgets sind **Teil der Pipeline**: Ein Build, der die Grenzen reißt (z. B. unkomprimierte Bilder im Praxis-Repo), wird nicht ausgeliefert – Bildoptimierung läuft als Build-Schritt.
- Das zentrale Theme wird einmal optimiert; alle Praxen profitieren, ohne dass jemand einzelne Seiten nachbessern muss.
- Messwerte je Praxis werden nach dem Go-Live in der Search Console und über einen Uptime-/Performance-Check beobachtet (Kapitel 14).
