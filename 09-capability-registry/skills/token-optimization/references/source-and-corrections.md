# Source and Corrections

## Herkunft

- Upstream: `valorisa/Claude-Skills`, Skill `token-optimization`
- Gepinnter Upstream-Commit: `5ac62e2273f2fa9b2c7db3082dfc688509e4f4bb` vom 18.08.2026
- Lizenz: MIT, Copyright 2026 valorisa
- Geprüfte Avenward-Fassung: `1.0.0-avenward.1`
- Portable Konsolidierung: 23.08.2026

## Übernommene Grundideen

- Cache-/Wiederholungsaufwand reduzieren
- Kontextaufblähung vermeiden
- Modell-/Effort-Wahl proportional zur Aufgabe treffen
- verbose Eingabe- und Toolformate begrenzen

## Nicht übernommene oder korrigierte Aussagen

- kein erfundener `contextWindow`-Schlüssel in Claude-Einstellungen;
- kein nicht vorhandener Agentenparameter `context: fork`;
- RTK nicht Simon Willison und nicht als npm-Paket darstellen;
- Stagehand nicht als Claude-Code-Plugin darstellen;
- keine unbelegten Prozent-, Kosten- oder Sternzahlen als Erwartung verwenden;
- keine unrealistischen absoluten Token-Zielwerte verwenden;
- Cache-TTL nicht pauschal an einen Sitzungsneustart koppeln;
- keine pauschale Delegation, wenn kumulatives Präzedenzwissen die Qualität trägt.

Die Avenward-Fassung enthielt trotz dokumentierter Korrekturen im unteren Troubleshooting-, Beispiel- und Checklistenteil noch einzelne alte Formulierungen zu `contextWindow`, `context: fork`, RTK und absoluten Zielwerten. Diese portable Fassung entfernt diese Widersprüche vollständig.

## Wartungsregel

Vor einem Update Upstream und aktuelle Primärdokumentation erneut prüfen. Neue Aussagen erst nach Validierung übernehmen. Bestehende Qualitätsgrenzen niemals zugunsten einer behaupteten Einsparung abschwächen.
