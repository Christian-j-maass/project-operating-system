# Project Operating System

Version: 1.1-alpha

Status: Aufbau  
Owner / Product Owner: Christian Maass  
Prozessverantwortung: Scrum Master / ChatGPT

## Zweck

Dieses Repository ist die verbindliche Quelle für die gemeinsame Projektarbeitsweise mit ChatGPT und GitHub. Es enthält wiederverwendbare Standards, Checklisten, Entscheidungsregeln, Lessons Learned und Vorlagen für langfristige Projekte.

## Leitziele

- Entscheidungen dürfen nicht verloren gehen oder ohne dokumentierte Änderung überschrieben werden.
- Der Product Owner wird nur bei echten Entscheidungslücken einbezogen.
- Ergebnisse werden versioniert, nachvollziehbar und projektübergreifend wiederverwendbar dokumentiert.
- ChatGPT dient der Analyse und Umsetzung; GitHub dient als dauerhafte System-of-Record.
- Arbeit wird in kleinen, prüfbaren Lieferständen organisiert.

## Verbindliche Grundregel

Eine Entscheidung, Anforderung oder Arbeitsweise gilt erst dann als dauerhaft gesichert, wenn sie im zuständigen Projekt-Repository oder in diesem Repository dokumentiert wurde. Chat-Inhalte allein gelten nicht als belastbare Projektdokumentation.

## Einstieg in die Zusammenarbeit

Der kurze gemeinsame Kern steht in [AGENTS.md](AGENTS.md). Die
[Entscheidung POS-DEC-001](03-decision-management/POS-DEC-001-VERIFIED-COLLABORATION.md)
dokumentiert die beauftragte Umsetzung vom 17.11.2026. Die neueste ausdrückliche
Nutzerentscheidung gilt sofort; ihre dauerhafte Dokumentation wird nachgeführt.

- [Einbindung, Plattformstatus und ChatGPT-Anleitung](07-project-adoption/COLLABORATION-ADOPTION.md)
- [Kopiertext für persönliche ChatGPT-Anweisungen](07-project-adoption/CHATGPT-INSTRUCTIONS.txt)
- [Drei Anwendungsproben und Grenzen des Wirksamkeitsnachweises](04-quality/COLLABORATION-PILOT.md)

Die Repository-Einbindung ist vom kontoweiten oder projektübergreifenden Rollout
zu unterscheiden. Die vorhandenen PPAO-Grenzen gelten weiterhin. Dieser
Lieferstand macht aus der Alpha-Fassung keine allgemein abgenommene Version 1.0.

## Struktur

- `01-governance/` – Rollen, Verantwortlichkeiten und Grundregeln
- `02-workflow/` – verbindlicher Projekt- und Sprintablauf
- `03-decision-management/` – Entscheidungs- und Änderungsmanagement
- `04-quality/` – Definition of Ready, Definition of Done und Qualitätsprüfungen
- `05-lessons-learned/` – dokumentierte Ursachen, Maßnahmen und Wirksamkeitskontrolle
- `06-templates/` – wiederverwendbare Vorlagen
- `07-project-adoption/` – Übernahme des Standards in konkrete Projekte
- [`08-ppao/`](08-ppao/README.md) – historische PPAO-Dokumentation und aktuelle Entscheidung: Dokumentationsübernahme ohne Aktivierung
- `09-capability-registry/` – dokumentierte plattformübergreifende Capability- und Candidate-Fassungen

## Aktueller Sicherheitshinweis

Dieses Repository ist zum Zeitpunkt der Initialisierung öffentlich. Daher dürfen hier keine personenbezogenen, vertraulichen, rechtlich sensiblen oder geschäftskritischen Projektinformationen abgelegt werden. Für interne Projektdetails muss das Repository auf **private** gestellt oder ein separates privates Repository genutzt werden.

## Geltungsbereich

Der Standard soll schrittweise auf folgende Projekte angewendet werden:

1. Avenward Veterans
2. Villa Paraguay
3. Apokalyptische Zuflucht / Silo
4. zukünftige langfristige Projekte

## Versionsprinzip

- `alpha`: Standard befindet sich im Aufbau.
- `beta`: Standard wird in mindestens einem Projekt praktisch getestet.
- `1.0`: Standard ist abgenommen und verbindlich.

Änderungen am Standard werden über einen dokumentierten Change-Eintrag nachvollziehbar gemacht.
