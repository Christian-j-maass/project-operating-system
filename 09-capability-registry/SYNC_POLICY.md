# Synchronisations- und Governance-Policy

## Single Source of Truth

Die portable Kernlogik jeder Capability liegt nur unter `09-capability-registry/skills/<id>/`. Host-spezifische Unterschiede liegen unter `adapters/`. Manuell divergierende Vollkopien sind zu vermeiden.

## Portabilitätsziel

Gleichheit bedeutet:

- gleiche Rolle und fachliche Regeln,
- gleiche Qualitäts- und Freigabegrenzen,
- gleiche Eingabe-/Ausgabeverträge,
- gleiche Versions- und Evidenzbasis.

Nicht verlangt wird die technische Identität von Befehlen, Tools, Frontmatter-Feldern oder Connectoren.

## Statusregeln

- Status nur mit Datum und Nachweis erhöhen.
- `historically-verified-recheck` nicht als aktuelle Installation ausgeben.
- Lokale und Cloud-Installation getrennt führen.
- Dokumentierter Prompt ist kein installiertes Skill-Paket.
- Verfügbare Plattformfunktion ist kein Nachweis, dass die eigene Capability dort aktiviert ist.

## Versionierung

- Semantic Versioning verwenden.
- `candidate` bis zur ausdrücklichen Finalfreigabe beibehalten.
- Methodik während eines laufenden Audits oder Piloten nicht wechseln.
- Änderungen an PPAO zunächst als PPAO-SIP behandeln.

## Host-Adapter

- Claude-spezifische Invocation-, Tool- und Kontextfelder nur im Claude-Adapter führen.
- ChatGPT-spezifische UI-Metadaten nur im ChatGPT-Adapter führen.
- Keine nicht unterstützten Host-Felder in den portablen Kern übernehmen.
- Plattformdokumentation vor dauerhaften Konfigurationsänderungen erneut prüfen.

## Qualitätsgate

Vor jeder Synchronisierung prüfen:

1. Frontmatter und Dateistruktur valide.
2. Keine TODOs, widersprüchlichen Altregeln oder erfundenen Kommandos.
3. Fakten, Evidenz, Tests und Traceability unverändert oder besser.
4. Explizite Invocation- und Änderungsgrenzen erhalten.
5. Lizenz- und Herkunftsnachweise vorhanden.
6. Plattformstatus nach Installation erneut verifiziert.

## Product-Owner-Grenze

Keine autonome Finalisierung, Aktivierung von PPAO, Governance-Änderung oder Löschung von Projektwissen. Empfehlungen und Maßnahmenpakete zuerst zur Entscheidung vorlegen.
