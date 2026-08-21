# PPAO – Konsolidierungsarchitektur (verschlankt)

**Datum:** 2026-08-21  
**Status:** Candidate-Architektur / nicht live  
**Bezug:** Grill-Me Design Review Baseline vom 2026-08-20  
**Freigabestatus:** NICHT PRODUKTIV AKTIVIEREN ohne ausdrückliche PO-Freigabe.

## 1. Architekturentscheidung: Puzzle-/Orchestrator-Prinzip

PPAO wird bewusst **nicht** als Universal-Superagent implementiert. Er ist die übergeordnete Audit- und Orchestrierungsschicht und schaltet vorhandene spezialisierte Skills nur bei Bedarf zu.

Zielbild:

- **Project Operating System (POS):** Governance, Workflow, Decision Management, Definition of Ready/Done, Lessons Learned.
- **PPAO:** unabhängiger Auditor, Trigger- und Orchestrierungslogik, Findings, Priorisierung, Gate-Empfehlungen, Portfolio Patterns.
- **Grill Me:** eigenständiger Challenge-/Decision-Interview-Skill; wird von PPAO bei relevanten Entscheidungslücken oder High-Impact-Alternativen aufgerufen.
- **Teach Me:** eigenständiger Erklär-/Decision-Readiness-Skill; wird bei `CLARIFICATION REQUIRED` aufgerufen.
- **Token Optimization:** eigenständiger Spezialskill für Context-/Tokenökonomie; wird bei `CONTEXT EFFICIENCY REVIEW REQUIRED` aufgerufen.
- **ChatGPT / Claude Code / projektspezifische Agenten:** ausführende Ebene; PPAO dupliziert deren Implementierungslogik nicht.
- **Temporäre Specialist Reviewer:** nur bei echter Fachgrenze; keine persistenten neuen Agenten ohne nachgewiesenen Bedarf.

Prinzip: **Standard Setter → Executor → Auditor/Orchestrator.**

## 2. Was aus PPAO entfernt bzw. in Referenzen umgewandelt wird

PPAO enthält künftig nicht mehr die vollständige Fachlogik von Grill Me, Teach Me oder Token Optimization.

Stattdessen werden nur Trigger und Handoffs definiert:

- `GRILL_ME_REQUIRED` → Grill Me
- `DECISION_READINESS = CLARIFICATION_REQUIRED` → Teach Me
- `CONTEXT_EFFICIENCY_REVIEW_REQUIRED` → Token Optimization
- `SPECIALIST_REVIEW_REQUIRED:<domain>` → temporärer fachlicher Reviewer

Die Rückgabe dieser Skills wird durch PPAO in den Audit-Kontext integriert und auf Evidenz, Konflikte und Auswirkungen geprüft.

## 3. Project Operating System als Governance Source

PPAO soll bestehende POS-Regeln nicht duplizieren. Er liest die für das Projekt geltende Governance und prüft:

1. Wird sie eingehalten?
2. Ist sie noch angemessen?
3. Erzeugt sie unnötige Komplexität oder Last?
4. Widerspricht sie neueren expliziten PO-Entscheidungen oder besserer Evidenz?

PPAO darf Verbesserungen am POS empfehlen, aber bestehende Governance nicht selbst ändern.

## 4. Audit-Module statt neuer Agenten

Die PPAO-Prüfdimensionen bleiben als interne Module erhalten, nicht als eigenständige permanente Agenten:

- Purpose & Scope Review
- Requirements Review
- Decision Review
- Architecture Review
- Planning/Backlog Review
- Traceability Review
- QA/Validation Review
- Documentation Review
- Context Review (Trigger für Token Optimization)
- Governance Review
- Continuous Improvement Review
- Outcome/Value Review
- AI Workflow & Agent Governance Review
- Complexity/Simplification Review

Nur echte Expertise-Grenzen rechtfertigen einen temporären Specialist Reviewer.

## 5. Kritische Neubewertung der „maximal drei“-Regel

### 5.1 Zwei Regeln müssen getrennt werden

**A. Work-in-Progress-Limit (Projektsteuerung):** maximal drei aktive Arbeitspakete als organisatorischer Standard. Dies begrenzt Kontextwechsel und unfertige Parallelstränge.

**B. Runtime-Concurrency-Limit (technische Ausführung):** Anzahl tatsächlich gleichzeitig laufender Agenten/Subagenten/umfangreicher Tool-Workflows.

Diese Werte dürfen nicht gleichgesetzt werden. Drei aktive Arbeitspakete können sequenziell bearbeitet werden; umgekehrt kann ein einziges Arbeitspaket intern mehrere Subagenten starten und dadurch hohe technische Last erzeugen.

### 5.2 Kein belegter sicherer technischer Grenzwert „3“

Es gibt keinen belastbaren Beleg, dass drei parallele Claude-Code-Agenten technisch immer sicher sind. Öffentliche Fehlerberichte zeigen Kontextlimit-, Speicher-, Overload- und Aggregationsprobleme bereits bei drei oder wenigen parallelen Subagenten, insbesondere bei großem Parent-Kontext, großen Rückgaben oder vielen MCP-Verbindungen.

Daher gilt künftig:

> **3 ist ein absolutes Sicherheits-Cap für unsere Arbeitsweise, aber kein Zielwert und keine Sicherheitsgarantie.**

### 5.3 Dynamische Lastregel

PPAO/POS sollen für Claude-Code-nahe Workflows folgende Default-Regel verwenden:

- **1 paralleler Heavy-Agent:** Standard bei großem Repo, breiter Recherche, Architekturarbeit, großen Dateimengen oder hohem Kontext.
- **max. 2 parallele Medium-Agenten:** nur bei klar getrennten, schmal gescopten Aufgaben und begrenzten Rückgaben.
- **max. 3 parallele Light-Agenten:** nur bei unabhängigen, kleinen Aufgaben mit minimalem Kontext und kompaktem Ergebnisformat.
- **absolutes Cap: 3 gleichzeitig laufende Agenten/Subagenten** für die derzeitige Projektarbeitsweise, bis eigene Messdaten eine Änderung rechtfertigen.
- **keine rekursive Agenten-Fan-out-Kette** ohne explizite PO-Freigabe.

Wenn Lastklasse oder Kontextzustand unklar ist, wird konservativ die niedrigere Parallelität gewählt.

## 6. Lastklassen

### LIGHT

- eng begrenzte Datei-/Metadatenprüfung
- geringe Tool-Nutzung
- keine breite Recherche
- kompakte Rückgabe
- kaum geteilter Kontext

**zulässige Parallelität:** bis 3

### MEDIUM

- mehrere Dateien oder moderate Recherche
- relevante Abhängigkeiten
- mittlere Kontextmenge
- strukturierter Bericht

**zulässige Parallelität:** bis 2

### HEAVY

- Deep Audit
- große Repositories
- viele Dateien/Quellen
- Architektur-/Strategieanalyse
- breite Tool-Nutzung
- Specialist Review mit umfangreicher Evidenz
- großer Parent-Kontext

**zulässige Parallelität:** 1

## 7. Token-/Kontext-Schutzregeln

PPAO darf das Zuschalten eines Skills nicht automatisch als separaten parallelen Agenten interpretieren. Wo technisch möglich, wird ein Skill als fokussierte Capability im bestehenden Workflow genutzt.

Vor Parallelisierung wird geprüft:

1. Muss die Aufgabe überhaupt parallel laufen?
2. Sind die Teilaufgaben wirklich unabhängig?
3. Kann ein deterministisches Tool (Suche, grep, Skript, Test) die Aufgabe günstiger erledigen?
4. Welche minimale Kontextmenge benötigt jeder Agent?
5. Wie groß darf die Rückgabe sein?
6. Wie werden Zwischenergebnisse persistent gesichert, bevor weitere Agenten starten?
7. Muss Token Optimization zugeschaltet werden?

Schutzregeln:

- minimaler, aufgabenspezifischer Kontext statt vollständiger Projekt-Historie;
- keine unnötige Vererbung des vollständigen Parent-Kontexts;
- kompakte strukturierte Agentenrückgaben statt Volltranskripten;
- Ergebnisse zuerst persistent sichern/zusammenfassen, dann nächste Welle starten;
- bei wiederholten Context-/Overload-/Memory-Signalen Parallelität reduzieren;
- keine automatische Wiederholung eines gescheiterten breiten Fan-outs ohne Ursachenanalyse;
- Qualität darf durch Tokenoptimierung nicht materiell sinken.

## 8. PPAO Trigger für Token Optimization

PPAO setzt `CONTEXT_EFFICIENCY_REVIEW_REQUIRED`, wenn mindestens eines zutrifft:

- wiederholte Context-Limit-/Compaction-Probleme;
- große oder redundante Projektinstruktionen;
- mehrere Agenten laden dieselben Dateien/Quellen;
- ungewöhnlich große Agentenrückgaben;
- Deep Audit auf großem Repository;
- wiederholte Token-/Usage-Spitzen;
- Fan-out mit mehreren Medium/Heavy-Aufgaben;
- Tool-Aufgabe wäre deterministisch wesentlich günstiger lösbar.

Token Optimization liefert Optimierungsvorschläge; PPAO prüft anschließend, ob dadurch Qualität, Evidenz oder Governance gefährdet würden.

## 9. Revidierte PPAO-Rolle

PPAO ist künftig primär:

1. **Auditor** – erkennt Risiken, Gaps, Konflikte und Governance-Abweichungen.
2. **Orchestrator** – schaltet vorhandene Skills gezielt zu.
3. **Integrator** – führt deren Ergebnisse zu einer PO-Entscheidungsgrundlage zusammen.
4. **Gate Advisor** – gibt `PASS / PASS WITH CONDITIONS / HOLD / NOT READY / INSUFFICIENT EVIDENCE` als Empfehlung.
5. **Process Learner** – erkennt Portfolio Patterns und schlägt Verbesserungen vor.

PPAO ist ausdrücklich nicht:

- zweiter Projektleiter;
- zweiter Coding-Agent;
- Ersatz für Grill Me;
- Ersatz für Teach Me;
- Ersatz für Token Optimization;
- permanenter Security-/Architecture-/Research-Spezialist;
- autonomer Änderungsagent.

## 10. Konsequenz für PPAO v1.1.0 Candidate

Die Candidate-Spezifikation wird gegenüber der Design-Baseline verschlankt:

- bestehende Spezialskills werden referenziert statt dupliziert;
- POS wird als primäre Governance Source behandelt;
- Audit-Dimensionen werden als Module, nicht als neue Agenten modelliert;
- Specialist Reviewer werden temporär und nur bedarfsgetrieben zugeschaltet;
- D10 Context Engineering wird zu einem Audit-/Trigger-Modul für Token Optimization;
- AI Workflow & Agent Governance enthält die dynamische Lastregel;
- WIP-Limit und technische Concurrency werden getrennt;
- absoluter Runtime-Cap bleibt vorläufig 3, Default liegt je nach Lastklasse bei 1–2.

## 11. Noch offene Validierung

Vor produktiver Aktivierung müssen wir im Pilot messen:

- Context-/Compaction-Ereignisse;
- Abbruch-/Overload-/Memory-Fehler;
- Agentenparallelität je Lastklasse;
- Token-/Usage-Aufwand soweit technisch verfügbar;
- Größe der Rückgaben;
- Nutzen der Parallelisierung gegenüber sequenzieller Bearbeitung;
- False Positives und Audit-Nutzen.

Erst eigene Messdaten dürfen eine spätere Anhebung oder weitere Absenkung des Concurrency-Caps begründen.
