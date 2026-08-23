# PPAO Shadow Mode

## Bewährtes Muster vom 23.08.2026

Der erfolgreiche Einsatz erfolgte als explizit beauftragter Personal-Context-/PPAO-Abgleich für **Avenward Veterans** während paralleler Arbeit von Claude an Iowa/Wave 68.

Verbindliches Verhalten:

- ausschließlich den genannten Projektkontext verwenden;
- laufende parallele Arbeit zuerst erkennen und respektieren;
- zunächst nur lesen und vorhandene Nutzeränderungen bewahren;
- keine Merges, PR-Schließungen, Branch-Wechsel oder externen Aktionen ohne ausdrückliche Freigabe;
- zuerst kurze Bestandsaufnahme mit Belegen liefern;
- danach konkrete nächste Prüfschritte nennen;
- keine Routinearbeit durch unnötige Methodendiskussionen oder Rückfragen verzögern.

## Verallgemeinerbarer Shadow-Ablauf

1. Projekt und Trennung von anderen Vorhaben bestätigen.
2. Git-/Arbeitsstatus, parallele Aktivitäten und Kollisionsrisiken prüfen.
3. Nur direkt hilfreichen früheren Kontext laden.
4. Aktuelle Evidenz gegen frühere Entscheidungen und Baselines abgleichen.
5. Abweichungen und Risiken dokumentieren, ohne operative Änderungen.
6. Empfehlungen und nächste Prüfschritte ausgeben.
7. Erst nach neuer ausdrücklicher Freigabe in einen Umsetzungsmodus wechseln.

## Avenward-spezifische Pilotgrenzen

- Qualität unverändert oder besser als harte Nebenbedingung.
- State-/Benefit-Kernpipeline sequenziell (`Concurrency = 1`).
- Keine State-Wellen parallelisieren.
- Keine Evidence Records, Entscheidungen, Präzedenzfälle oder Registerinformationen entfernen.
- Alle bestehenden Quality Gates unverändert ausführen.
- Token- oder Zeitgewinn niemals durch Qualitätsreduktion erkaufen.

Übertrage diese Avenward-Regeln nicht automatisch auf andere Projekte. Leite dort projektspezifische Grenzen aus der geltenden Governance ab.
