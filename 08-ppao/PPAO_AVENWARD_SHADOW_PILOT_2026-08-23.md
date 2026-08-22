# PPAO – Avenward Veterans Shadow Pilot

**Geplanter Pilot:** nächste State-Analyse ab 2026-08-23  
**Status:** freigegebene Pilot-Baseline, PPAO weiterhin nicht produktiv/live  
**Projekt:** `Christian-j-maass/-avenward-veterans`  
**PPAO-Rolle:** Auditor + Orchestrator + Integrator, keine eigenständige Super-Agent-Implementierung

## 1. Ziel des Piloten

Der Pilot soll messen, ob PPAO bei der nächsten Avenward-State-Analyse den bestehenden Prozess effizienter macht, ohne die fachliche, technische oder evidenzbezogene Qualität zu senken und ohne vorhandenes Projektwissen zu gefährden.

Priorität der Optimierung:

1. **Qualität unverändert oder besser** – harte Nebenbedingung.
2. **Token-/Kontextverbrauch reduzieren.**
3. **Bearbeitungszeit reduzieren.**

Ein Erfolg liegt nur vor, wenn keine relevante Qualitätsregression entsteht.

## 2. Pilotmodus: Shadow Pilot

PPAO begleitet die bestehende Avenward-State-Analyse und auditiert bzw. orchestriert sie. Der etablierte Avenward-Workflow bleibt die operative Baseline.

PPAO darf im Pilot:

- projektspezifische Regeln und Quality Gates lesen und anwenden,
- Abweichungen, Risiken und Optimierungsmöglichkeiten identifizieren,
- vorhandene freigegebene Skills/Agenten bei echtem Bedarf zuschalten,
- selektives Retrieval und Context-Minimierung empfehlen,
- deterministische Prüfungen gegenüber LLM-Arbeit bevorzugen,
- am Ende einen Pilot-/Auditvergleich erstellen.

PPAO darf im Pilot nicht:

- bestehende Avenward-Qualitätsregeln abschwächen,
- neue dauerhafte Agents installieren,
- PPAO-Regeln während des laufenden Piloten verändern,
- State-Wellen parallelisieren,
- historische Daten oder Evidenz löschen,
- Entscheidungen still überschreiben,
- Qualitätsprüfungen zugunsten von Tokenersparnis überspringen.

## 3. Avenward Compatibility Layer

### 3.1 Regelpriorität

Für den Pilot gilt:

1. zwingende rechtliche, Security-, Datenschutz- und Datenintegritäts-Constraints,
2. aktuelle explizite Product-Owner-Entscheidung,
3. Avenward-spezifische freigegebene Governance, Decisions und Quality Gates,
4. Project Operating System,
5. generische PPAO-Regeln.

PPAO adaptiert sich an Avenward; Avenward wird nicht blind an PPAO angepasst.

### 3.2 Operational vs. Persistent Authority

Eine aktuelle explizite Product-Owner-Entscheidung gilt operativ sofort. Bis zur Dokumentation in GitHub wird sie als `DECISION VALID – GITHUB SYNC PENDING` geführt. GitHub bleibt das dauerhafte System of Record.

### 3.3 Grill Me / Teach Me

PPAO repliziert diese Skills nicht.

**Grill Me** wird nur zugeschaltet bei echter Entscheidungslücke, materiell neuer Evidenz, HIGH/CRITICAL Risiko, schwer reversibler Entscheidung, erheblichem Trade-off oder explizitem Wunsch des Product Owners.

**Teach Me** wird nur zugeschaltet, wenn eine wichtige Entscheidung ohne zusätzliche verständliche Einordnung nicht ausreichend decision-ready wäre.

Routine-State-Arbeit darf dadurch nicht mit unnötigen Rückfragen oder Methodendiskussionen verlangsamt werden.

### 3.4 Token Optimization

Token Optimization bleibt separater Spezialskill. PPAO kann ihn bei Bedarf aufrufen bzw. dessen Regeln anwenden lassen. Ziel ist weniger aktiver Kontext, nicht weniger gesichertes Wissen.

Tokenoptimierung darf niemals relevante Evidenz, historische Entscheidungen, Präzedenzfälle, Lessons Learned, Traceability oder Datenintegrität entfernen oder abschwächen.

## 4. Knowledge Preservation Gate

Vor jeder vorgeschlagenen Löschung, Archivierung, Verdichtung, Deduplizierung oder Entfernung aus dem aktiven Kontext ist zu prüfen:

- Ist die Information tatsächlich redundant?
- Enthält sie eine einzigartige Entscheidung?
- Enthält sie Evidenz oder einen Quellenbeleg?
- Enthält sie einen historischen Präzedenzfall?
- Enthält sie eine bekannte Fehlersituation oder Lesson Learned?
- Ist sie vollständig und verlässlich an anderer Stelle erhalten?
- Würde ihr Verlust spätere Revalidierung oder Rekonstruktion erschweren?

Mögliche Ergebnisse:

- `SAFE TO REMOVE`
- `SAFE TO ARCHIVE`
- `KEEP ACTIVE`
- `PRESERVE – UNIQUE KNOWLEDGE`
- `UNCERTAIN – DO NOT REMOVE`

Im Zweifel gilt `UNCERTAIN – DO NOT REMOVE`.

## 5. Concurrency- und Lastregel

### 5.1 Trennung WIP vs. Runtime

**WIP-Limit:** maximal drei aktive Arbeitspakete im Projekt; dies ist eine Projektsteuerungsregel.

**Runtime-Concurrency:** tatsächlich gleichzeitig rechnende KI-Agenten/Subagenten; dies ist eine technische Lastregel.

### 5.2 Globale Pilotgrenze

Absolute technische Obergrenze: **3 parallele Agenten**. Dies ist keine Sicherheitsgarantie, sondern ein Cap.

- `HEAVY`: 1 gleichzeitig
- `MEDIUM`: maximal 2 gleichzeitig
- `LIGHT`: maximal 3 gleichzeitig

Nach Memory-, Context- oder Overload-Problemen wird die Parallelität reduziert und nicht automatisch erneut hochgesetzt.

### 5.3 Avenward State Core Pipeline

Für den fachlichen Kern der State-Analyse gilt im Pilot verbindlich:

**Concurrency = 1.**

Die State-/Benefit-Kernpipeline bleibt sequenziell, weil kumulatives Präzedenzwissen über frühere States/Wellen ein dokumentierter Qualitätsmechanismus von Avenward ist.

Unabhängige Nebenprüfungen dürfen nur dann parallelisiert werden, wenn sie keinen gemeinsamen veränderlichen Kontext benötigen, keine Präzedenzkette unterbrechen und keine erhöhte Fehler-/Tokenlast erzeugen.

## 6. Safety Envelope

Während des Piloten gilt:

- keine historischen Daten löschen;
- keine Evidence Records entfernen;
- keine ACCEPTED Decisions überschreiben;
- keine Registerbereinigung ohne Knowledge Preservation Gate;
- keine neuen dauerhaften Agents installieren;
- keine State-Wellen parallel bearbeiten;
- keine Primärquellenpflicht abschwächen;
- keine Traceability-Anforderung entfernen;
- keine Quality Gates zugunsten von Geschwindigkeit oder Tokenersparnis überspringen;
- keine rekursiven Agent-Fan-outs ohne ausdrückliche Freigabe;
- keine destruktiven Git-Operationen als PPAO-Optimierung;
- keine PPAO-Methodikänderung während des laufenden Piloten.

## 7. Optimierungshebel, die ausdrücklich erlaubt sind

1. **Selective Retrieval:** nur relevante Decisions, Register, Präzedenzfälle und Quellen laden.
2. **Context Minimization:** große Dokumente gezielt durchsuchen statt vollständig zu laden, sofern kein Informationsverlust entsteht.
3. **Deterministic First:** Scripts, Tests, Grep/Find, Registry-Validatoren und andere deterministische Prüfungen vor LLM-Neuanalyse einsetzen.
4. **Duplicate Work Prevention:** vor neuer Recherche prüfen, ob belastbare aktuelle Evidenz bereits vorhanden ist.
5. **Result Compression:** Agentenresultate strukturiert und knapp in den Parent-Kontext zurückgeben; vollständige Evidenz bleibt im Repository/Quellartefakt erhalten.
6. **Existing-Agent Routing:** vorhandene Avenward-/globale Spezialagenten nur bei echtem Bedarf zuschalten; keine Funktionsduplikation in PPAO.
7. **Sequential Core / Parallel Periphery:** State-Kern sequenziell, nur wirklich unabhängige Randprüfungen parallel.

## 8. Messprotokoll

### 8.1 Vergleichsbasis

Primäre Baseline sind die **letzten drei hinreichend vergleichbaren State-/Benefit-Wellen** vor dem Pilot. Frühe Wellen mit deutlich anderem Reifegrad werden nicht als Hauptvergleich verwendet.

### 8.2 KPI-Priorität

Nur technisch belastbar messbare Werte werden als harte KPIs ausgewiesen. Nicht verlässlich messbare Werte werden als `NOT RELIABLY MEASURABLE` markiert und nicht geschätzt.

Zu erfassen, soweit verfügbar:

- Gesamttokens / Input+Output oder bestmöglicher plattformeigener Messwert,
- Bearbeitungsdauer vom Start bis zum validierten Abschluss,
- Anzahl größerer Context Loads,
- Anzahl und Typ der Agent-/Skill-Aufrufe,
- Peak Runtime-Concurrency,
- relevante Tool Calls,
- Anzahl vollständig bearbeiteter Benefits,
- Rule Tests: bestanden / gesamt,
- Typecheck/Lint/Build/Registry Validation: tatsächlicher Status,
- Evidence Quality / Primärquellenanforderung erfüllt,
- Traceability vollständig ja/nein,
- notwendige Rework-/Korrekturschleifen,
- PPAO Findings nach Severity,
- bestätigte vs. False-Positive-Findings,
- Quality Regression: Zielwert **0**.

### 8.3 Erfolgskriterien

Der Pilot gilt nur dann als positiv, wenn:

1. keine relevante Qualitätsregression vorliegt;
2. keine gesicherten Daten, Evidenz, Entscheidungen oder Präzedenzfälle verloren gehen;
3. mindestens ein nachvollziehbarer Effizienzgewinn bei Token-/Kontextverbrauch oder Bearbeitungszeit entsteht **oder** PPAO einen relevanten bisher unentdeckten Qualitäts-/Prozessbefund liefert, der den Zusatzaufwand rechtfertigt;
4. der PPAO-Zusatzaufwand nicht größer ist als der nachweisbare Nutzen.

## 9. Pilotablauf

1. Pilotversion und Compatibility Layer einfrieren.
2. Letzte drei vergleichbare Wellen als Baseline bestimmen.
3. State-Analyse nach bestehendem Avenward-Workflow starten.
4. PPAO im Shadow-Modus begleiten lassen.
5. State Core Pipeline strikt sequenziell ausführen.
6. Vorhandene Skills/Agenten nur trigger-basiert zuschalten.
7. Alle bestehenden Avenward Quality Gates unverändert ausführen.
8. Pilot-KPIs erfassen.
9. Nach Abschluss separaten PPAO Pilot Audit erstellen.
10. Erst danach Verbesserungen als PPAO-SIP oder POS/Avenward-Change-Vorschlag formulieren.

## 10. Freeze-Regel

Während der laufenden State-Welle wird die PPAO-Pilotmethodik nicht verändert. Beobachtete Verbesserungsmöglichkeiten werden gesammelt, aber erst nach Abschluss bewertet.

## 11. Entscheidungsstatus

Vom Product Owner bestätigt:

- **Shadow Pilot:** JA
- **Priorität Qualität → Tokenreduktion → Geschwindigkeit:** JA
- **Bestehende freigegebene Skills bedarfsgerecht zuschalten:** JA
- **Keine neuen Agents im Pilot:** JA
- **Avenward State Core Pipeline Concurrency = 1:** JA
- **PPAO bis auf Weiteres nicht generell live/produktiv schalten:** JA
