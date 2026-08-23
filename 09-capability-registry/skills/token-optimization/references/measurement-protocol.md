# Measurement Protocol

## Grundsatz

Tokenersparnis nur als Verbesserung ausweisen, wenn die fachliche Qualität nicht materiell sinkt. Nicht verfügbare Messwerte als `NOT RELIABLY MEASURABLE` kennzeichnen und niemals schätzen.

## Baseline festlegen

1. Aufgaben mit vergleichbarem Scope, Reifegrad und Qualitätsniveau auswählen.
2. Modell, Plattform, Datum, relevante Tools und Skill-Version dokumentieren.
3. Verbindliche Qualitätsgates und erwartete Liefergegenstände vorab festhalten.
4. Historische Werte nur als Vergleich, nicht als allgemeines Versprechen behandeln.

## Messwerte

Soweit technisch zuverlässig verfügbar erfassen:

- Input- und Output-Tokens oder bestmöglichen nativen Verbrauchswert
- Bearbeitungsdauer bis zum validierten Abschluss
- Zahl und Umfang größerer Context Loads
- Tool-, Agenten- und Skill-Aufrufe
- Peak Runtime-Concurrency
- vollständig bearbeitete Objekte oder Arbeitseinheiten
- Tests, Typecheck, Lint, Build und Registry Validation
- Evidence Quality und Traceability
- Korrektur- und Rework-Schleifen
- Qualitätsregressionen und bestätigte Findings

## Vergleich

- Gleiche oder hinreichend vergleichbare Aufgaben gegenüberstellen.
- Änderungen an Modell, Plattform, Datenlage und Scope offenlegen.
- Effizienzgewinn getrennt nach Kontext, Ausgabe, Laufzeit und Arbeitsaufwand berichten.
- Keine Scheingenauigkeit verwenden.
- Einsparung verwerfen, wenn Tests, Evidenz, Vollständigkeit oder Entscheidungsqualität schlechter werden.

## Avenward-Vergleichsbasis

Für den PPAO-/Token-Optimization-Pilot gelten die letzten drei hinreichend vergleichbaren State-/Benefit-Wellen als primäre Baseline. Vom Product Owner genannte historische Vergleichswerte:

- netto 7 Stunden Bearbeitungszeit,
- 27 % der wöchentlichen Claude-Tokens,
- gleiche Qualität als harte Nebenbedingung.

Behandle diese Werte als projektspezifische Vergleichsbasis, nicht als bereits bewiesenes Einsparziel. Zielwert für Quality Regression: **0**.
