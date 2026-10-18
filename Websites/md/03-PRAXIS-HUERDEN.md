# Die praxis-spezifischen Hürden (und deren Lösung)

Arztpraxen haben spezifische Anforderungen, die reines Static Hosting erweitern muss.

## Inhaltspflege ohne Git-Kenntnisse

Ärzte oder MFA (Medizinische Fachangestellte) können kein Git bedienen.

**Lösung:** Ein Git-basiertes Headless-CMS wie **Decap CMS** (ehemals Netlify CMS) oder **Keystatic** einbinden. Die Praxis editiert Öffnungszeiten in einer einfachen Web-Maske; das CMS committet automatisch in das GitLab-Repo und triggert den Hugo-Build.

## Online-Terminvergabe

Praxen nutzen Systeme wie Doctolib, jameda, samedi oder CGM.

**Lösung:** DSGVO-konforme Einbindung per Consent-Management (z. B. Two-Click-Lösung / lokaler Banner) oder direkter Deep-Link zum jeweiligen Buchungsportal.

## Rechtssicherheit & Notdienst-Hinweise

- Lokale Auslieferung von Schriftarten (kein ungeschütztes Google-Fonts-CDN).
- Dynamische Notdienst-Boxen über kleine clientseitige Vanilla-JS-Snippets gegen die Schnittstellen der Kassenärztlichen Vereinigung (KV).
