---
name: token-optimization
description: "Token- und Kontexteffizienz für ChatGPT/Codex und Claude verbessern, ohne Qualität zu reduzieren. Verwenden bei Tokenverbrauch, Kosten, Budget, Effizienz, Kontextfenster, Context Bloat, Cache, Compaction, großen Dateien, wiederholter Recherche, langen Tool-Ausgaben, unnötigen Agenten oder formalen Effizienzvergleichen. Auch bei entsprechenden Symptomen anwenden. Evidenz, Tests, Traceability und vollständige Liefergegenstände immer bewahren."
---

# Token Optimization

## Qualitätsgrenze

**Reduziere Verschwendung, niemals notwendige Analyse.** Optimiere Wiederholung, Transport, Kontextlast und Ausführungs-Overhead. Reduziere nicht:

- erforderliche Recherche oder Quellenprüfung,
- relevante Dateien oder Gegenargumente,
- Tests, Qualitätssicherung oder Traceability,
- Unsicherheiten und Risikohinweise,
- fachliche Tiefe entscheidungsrelevanter Inhalte,
- Vollständigkeit von Berichten, Dokumenten und anderen Liefergegenständen.

Bei einem Konflikt zwischen geringeren Tokens und höherer fachlicher Sicherheit gewinnt die fachliche Sicherheit.

## Verschwendungsachsen

Prüfe vier Hauptursachen:

1. **Wiederholung und Cache-Verlust** – identische Informationen mehrfach laden oder ungünstig neu verarbeiten.
2. **Kontextaufblähung** – zu große Dateien, Historien, Toollisten oder irrelevante Quellen in den aktiven Kontext bringen.
3. **Unpassende Rechenintensität** – Modell, Reasoning Effort oder Agentenanzahl über dem Aufgabenbedarf wählen.
4. **Verbose Ein- und Ausgaben** – vollständige Logs, Diffs oder Transkripte transportieren, obwohl ein gezielter Ausschnitt genügt.

## Arbeitsablauf

### 1. Akzeptanzkriterien festhalten

- Ziel, Pflichtumfang, Qualitätsgates und nicht verhandelbare Constraints bestimmen.
- Vor Optimierung klären, was vollständig erhalten bleiben muss.
- Für einen formalen Vergleich `references/measurement-protocol.md` lesen.

### 2. Verbrauchstreiber lokalisieren

- Nur tatsächlich verfügbare Plattformmetriken verwenden.
- Große Context Loads, wiederholte Dateilesevorgänge, lange Tool-Ausgaben, unnötige Tools und Agenten identifizieren.
- Nicht messbare Größen als `NOT RELIABLY MEASURABLE` markieren; keine Werte schätzen.

### 3. Selektives Retrieval anwenden

- Dateinamen, Indizes, Überschriften und Suchmuster zuerst verwenden.
- Nur relevante Abschnitte laden; bei inhaltlicher Verwendung die erforderliche Primärstelle vollständig genug lesen.
- Zusammenfassungen als Wegweiser, nicht als Ersatz der entscheidungsrelevanten Quelle behandeln.
- Bereits vorhandene aktuelle Evidenz prüfen, bevor neue Recherche gestartet wird.

### 4. Deterministisch zuerst prüfen

- Suche, Parser, Validatoren, Tests, Lint, Typecheck, Diffs und andere deterministische Werkzeuge vor wiederholter LLM-Interpretation einsetzen, wenn sie dieselbe Frage zuverlässig beantworten.
- Erst Übersicht oder Statistik ausgeben; vor Freigabe, Commit oder fachlichem Review die notwendige Vollansicht prüfen.
- Warnungen und Fehler nicht durch globale Filter unsichtbar machen.

### 5. Tool-Ausgaben begrenzen

- Befehle auf relevante Pfade, Zeilen, Treffer oder letzte Einträge beschränken.
- Erfolgreiche Routineausgaben zusammenfassen; bei Fehlern die relevanten Details zeigen.
- Recherche-Rohmaterial persistent sichern, statt es in voller Länge im Hauptkontext zu halten.
- Zwischenkommunikation knapp halten; Liefergegenstände vollständig ausarbeiten.

### 6. Agenten proportional einsetzen

- Nicht delegieren, wenn kumulatives Präzedenzwissen der Qualitätsmechanismus ist.
- Nur unabhängige, eng begrenzte Aufgaben parallelisieren.
- Minimalen aufgabenspezifischen Kontext und kompaktes Ergebnisformat vorgeben.
- Deterministisches Werkzeug vor zusätzlichem Agenten bevorzugen.
- Qualitäts-, Sicherheits- und Plattformgrenzen für Parallelität einhalten.

### 7. Sitzungen und dauerhafte Anweisungen begrenzen

- Lange Sitzungen an fachlich sinnvollen Übergabepunkten schneiden.
- Entscheidungsrelevante Informationen vor Compaction oder Sitzungswechsel persistent sichern.
- Dauerhafte Projektdateien auf Fakten und kurze Regeln beschränken; Verfahren in Skills und Referenzen auslagern.
- Host-spezifische Befehle oder Einstellungen erst nach Prüfung der aktuellen Dokumentation ändern; dafür `references/platform-notes.md` lesen.

### 8. Wirkung verifizieren

- Nach der Optimierung dieselben Qualitätsgates ausführen.
- Verbrauch, Laufzeit, Rework und Ergebnisqualität gegen eine vergleichbare Baseline stellen.
- Nur nachweisbare Effizienzgewinne berichten.
- Maßnahme zurückweisen oder anpassen, wenn Evidenz, Tests, Vollständigkeit oder Entscheidungsqualität sinken.

## Änderungsgrenze

- Wende reversible, aufgabenspezifische Begrenzungen wie gezielte Suche oder kompakte Tool-Ausgabe direkt an.
- Schlage dauerhafte Konfigurations-, Governance-, Modell-, Agenten- oder Workflowänderungen zuerst mit Wirkung und Risiko vor.
- Lösche, archiviere oder verdichte kein Projektwissen ohne Wissensschutzprüfung und erforderliche Freigabe.

## Plattformtrennung

Halte den fachlichen Kern identisch, aber erfinde keine gemeinsamen Kommandos. ChatGPT/Codex und Claude besitzen unterschiedliche Mess-, Skill-, Agenten- und Konfigurationsmechanismen. Lies `references/platform-notes.md`, sobald eine konkrete Host-Einstellung, ein Befehl oder eine Installationsfrage betroffen ist.

## Quellenstatus

Diese Fassung basiert auf dem geprüften, gepflegten Avenward-Fork des MIT-lizenzierten Upstream-Skills und entfernt verbliebene widersprüchliche Altanweisungen. Lies `references/source-and-corrections.md` bei Updates, Quellenfragen oder einem Abgleich mit der früheren Claude-Fassung.
