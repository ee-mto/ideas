# SEO – lokale Suche & strukturierte Daten

Praxis-Websites werden fast ausschließlich **lokal** gesucht („Hausarzt [Ort]", „[Leistung] [Ort]"). Der Fokus liegt daher auf lokaler Sichtbarkeit und strukturierten Daten – nicht auf Masse an Keywords.

## 1. On-Page-Grundlagen (je Seite)

- **Eindeutiger `title`** (≤ ~60 Zeichen): „Hausarzt in Musterstadt | Hausarztpraxis Muster"
- **`meta description`** (≤ ~155 Zeichen) mit Leistung + Ort
- **Eine H1 je Seite**, fachlich und regional („Vorsorge & Check-up in Musterstadt")
- **`canonical`** auf jeder Seite
- Verständliche URLs (`/leistungen`, `/sprechzeiten`), keine Parameter, keine Umlaute

## 2. Strukturierte Daten (JSON-LD)

| Seite | Schema | Inhalt |
| --- | --- | --- |
| Startseite | `Physician` | `medicalSpecialty` (z. B. GeneralPractice), `openingHoursSpecification`, `address`, `geo`, `telephone`, `url` |
| FAQ | `FAQPage` | Question/Answer je Frage |
| Aktuelles | `Article`/`NewsArticle` | mit `datePublished` |

Validierung über den **Rich Results Test** von Google.

## 3. Lokale SEO

- **Google Business Profile (GBP):** Kategorien (z. B. „Hausarzt"), Sprechzeiten, Fotos, Website-URL verknüpfen; Beiträge für Neuigkeiten (Urlaubsvertretung!)
- **NAP-Konsistenz:** Name, Adresse und Telefon identisch auf Website, GBP, Jameda, Doctolib und in der KV-Suche
- **Portale verlinken:** Jameda/Doctolib sachlich verlinken (HWG-konform, Kapitel 06)
- **Standortbezug** in H1 und Titeln, „in [Ort]" natürlich einbauen – keine Keyword-Stuffing-Seiten

## 4. Technisches SEO

- **`sitemap.xml`** mit allen Seiten, `priority`/`lastmod`; bei Google Search Console und Bing Webmaster einreichen
- **`robots.txt`** – KI-Crawler ausdrücklich erlauben (GPTBot, ClaudeBot, PerplexityBot, Google-Extended, Applebot-Extended); erhöht die Chance, in KI-Antworten zitiert zu werden
- **Search Console** einrichten: Indexierung, Sitemap, Core-Web-Vitals-Bericht
- **404-Seite** vorhanden, keine verwaisten Links

## 5. Content-SEO (HWG-konform)

- **Schwerpunktseiten** je Leistung mit Anlässen, Ablauf und FAQ – informierend, nicht anpreisend
- **FAQ** mit echten Patientenfragen (Long-Tail: „Was ist ein Gesundheits-Check-up?")
- **Aktuelles** regelmäßig pflegen – Aktualität ist ein Ranking-Signal und vermeidet Anrufe
- **Keine Doorway-Pages** – jede Seite muss echten Wert haben

## 6. Checkliste

- [ ] JSON-LD `Physician` validiert (Rich Results Test)
- [ ] `sitemap.xml` und `robots.txt` live, in der Search Console eingereicht
- [ ] GBP verknüpft, NAP auf Website = GBP = Jameda
- [ ] Jede Seite mit unique title/description/H1 und canonical
- [ ] KI-Crawler in `robots.txt` erlaubt

## 7. Im Factory-Modell

- Title, Description, H1 und JSON-LD werden **aus den Praxis-Daten generiert** (Generator in der Pipeline) – keine handgepflegten Meta-Tags je Seite.
- Der Generator zieht Ort, Fachbereich, Koordinaten und Sprechzeiten aus `config`/Content und erzeugt `sitemap.xml` und `robots.txt` mit der echten Domain.
- Nach dem Go-Live: Search Console je Praxis anlegen (Domain-Verifizierung) und GBP verknüpfen – Teil des Onboardings.
