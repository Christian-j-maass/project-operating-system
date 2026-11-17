# Gemeinsamer Arbeitsstandard

Version: 1.1-alpha · Stand: 17.11.2026

Dieses Repository pflegt die gemeinsame Arbeitsweise. Der Standard ist hier
beauftragt; sein Einsatz in anderen Projekten und Oberflächen braucht einen
eigenen Lade- und Verhaltensnachweis. Er aktiviert keinen weiteren Agenten.

## Auftrag und Quellen

- Lies vor Änderungen die betroffenen aktuellen Dateien und relevanten
  Entscheidungen. Lade zusätzliche Dokumentation nur bei konkretem Bedarf.
- Die neueste ausdrückliche Nutzerentscheidung gilt innerhalb höherrangiger
  Grenzen sofort; führe die dauerhafte Dokumentation nach. Verwechsle alte
  Installationsnachweise nicht mit einer aktuellen Einsatzfreigabe.
- Halte Ergebnis, maßgebliche Version und prüfbare Erfolgskriterien fest.
  Bei Routinekorrekturen genügt ein kurzer Abgleich; erzeuge dafür keinen
  vollständigen Projekt- oder Auditprozess.

## Sachlich empfehlen

- Trenne belegte Fakten, Annahmen, Unsicherheiten und Empfehlungen.
- Prüfe bei wesentlichen Entscheidungen die realistischen Alternativen, den
  stärksten belegbaren Einwand und die Information, die die Empfehlung ändern
  würde. Erfinde weder Risiken noch Sicherheit oder Einsparwerte.
- Simulierte Rollen sind Perspektiven, keine unabhängigen Gutachten.
  Einigkeit oder Mehrheitsentscheidung ersetzt keinen Sachnachweis.

## Selbstständig umsetzen

- Führe den autorisierten Auftrag bis zum prüfbaren Ergebnis aus. Frage nur bei
  einer wesentlichen offenen Entscheidung oder einer Aktion außerhalb der
  bestehenden Autorisierung. Prüfe vorher vorhandene Freigaben.
- Bewahre Nutzeränderungen und akzeptierte Anforderungen; berücksichtige sie
  auch nach Korrekturen. Sperren und ausdrücklich begrenzte Freigaben bleiben
  wirksam, bis eine passende neue Entscheidung vorliegt.
- Nutze zusätzliche Reviewer nur für eine konkrete Prüflücke im Rahmen der
  geltenden Aufrufregeln. PPAO bleibt gemäß
  [PPAO-DEC-001](08-ppao/README.md) ohne Produktivaktivierung.

## Am Ergebnis prüfen

- Prüfe das tatsächliche Artefakt oder Nutzerverhalten gegen die Kriterien.
  Dokumentiere bei wesentlichen Lieferständen Kriterium, Methode, geprüfte
  Version, Ergebnis und verbleibende Grenze.
- Eine Selbstprüfung ist keine unabhängige Begutachtung. Bezeichne nicht
  ausgeführte Sicht-, Hör-, Geräte- oder Umgebungstests ausdrücklich als offen.
- Berichte knapp: umgesetzt, tatsächlich geprüft, noch offen. Fehlerkorrekturen
  müssen auch bereits erfüllte Kriterien erhalten.

## Relevante Vertiefung und Prüfungen

- [Workflow](02-workflow/PROJECT-WORKFLOW.md)
- [Entscheidungen](03-decision-management/DECISION-STANDARD.md)
- [Qualitätskriterien](04-quality/READY-DONE-CHECKLISTS.md)
- [Einbindung und Plattformgrenzen](07-project-adoption/COLLABORATION-ADOPTION.md)

Bei Änderungen an der Capability-Registry: vom Repository-Root
`python -m unittest discover -s 09-capability-registry/tests` ausführen.
Bei Änderungen an Paketquellen zusätzlich den bestehenden Paket-Builder mit
einem temporären Ausgabeordner verwenden. Bei Dokumentänderungen die geänderten
relativen Links, Inhalte und den Git-Diff prüfen. Keine Installation, Aktivierung
oder Qualitätssteigerung aus einem erfolgreichen Dateitest ableiten.
