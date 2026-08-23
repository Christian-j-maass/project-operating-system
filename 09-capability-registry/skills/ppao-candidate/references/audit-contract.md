# PPAO Audit Contract

## Auditdimensionen

- D01 Purpose & Objectives
- D02 Scope
- D03 Requirements
- D04 Decision Governance
- D05 Architecture / Solution Design
- D06 Planning & Backlog
- D07 Implementation Traceability
- D08 QA & Validation
- D09 Documentation
- D10 Context Engineering
- D11 Project Governance
- D12 Continuous Improvement
- D13 Outcome & Value Validation / Strategic Validity
- D14 AI Workflow & Agent Governance
- D15 Complexity & Simplification

Querschnitt: Evidence Quality, Tool/Agent Fitness, Dependency & Resilience, Assumptions, Focus/Scope Coherence, Value-for-Effort, Phase Awareness und Recommendation Outcome Tracking.

## Audit-Tiefe

- **Focused Review:** eng begrenzte Frage oder einzelne Änderung.
- **Standard Audit:** mehrere relevante Dimensionen mit risikobasierter Stichprobe.
- **Deep Audit:** breite, folgenreiche Prüfung; nur nach ausdrücklicher Freigabe.
- **Specialist Review:** echte Fachgrenze; liefert Evidenz, keine Änderungsrechte.

## Finding-Modell

Typen: `VIOLATION / RISK / GAP / CONFLICT / DEBT / OPTIMIZATION / QUESTION / HYPOTHETICAL RISK`.

Severity: `CRITICAL / HIGH / MEDIUM / LOW / INFO`.

Jedes wesentliche Finding enthält:

- Finding ID
- Type und Severity
- Finding
- Evidence
- Expected State
- Actual State
- Impact
- Recommendation
- Alternatives
- Confidence
- Project Owner Decision Required

Unbelegte adversariale Risiken als `HYPOTHETICAL RISK` kennzeichnen, nicht als Fakt.

## Gate-Status

- `PASS`
- `PASS WITH CONDITIONS`
- `HOLD`
- `NOT READY`
- `INSUFFICIENT EVIDENCE`

Ein Gate ist eine Empfehlung. Es ersetzt keine formale Entscheidung oder Freigabe des Project Owners.

## Evidenzsuffizienz

- `INSUFFICIENT`
- `SUFFICIENT WITH UNCERTAINTY`
- `SUFFICIENT`
- `SATURATED`

Weitere Recherche beenden, wenn der erwartete Zusatznutzen gering ist und die Entscheidung hinreichend abgesichert bleibt.

## Entscheidungs- und Risikostatus

- Decision readiness: `READY / CLARIFICATION REQUIRED`
- Risk: `RESOLVED / ACCEPTED / DEFERRED / REJECTED / MONITORED`
- Revalidation: `REVALIDATION REQUIRED`
- Strategic validity: `CONTINUE / ADJUST / PIVOT / PAUSE / STOP CANDIDATE`
- Stop rule: `CONTINUE / COMPLETE MINIMUM / ACCEPT CURRENT STATE / DEFER REMAINDER / STOP WORK`

## GitHub-Prüfregeln

- G01 README Consistency
- G02 Decision Traceability
- G03 Orphan Requirements
- G04 Orphan Implementation
- G05 Documentation Drift
- G06 Contradiction Detection
- G07 Stale Documents
- G08 Duplicate Sources of Truth
- G09 Issue Hygiene
- G10 PR Quality
- G11 Release Readiness
- G12 Repository Hygiene

Beurteile Angemessenheit nach Projekttyp, Phase, Risiko und Größe. Erzwinge keine mechanische Ordnerstruktur.
