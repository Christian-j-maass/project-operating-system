# Einbindung des gemeinsamen Arbeitsstandards

Version: 1.1-alpha · Stand: 17.11.2026

Kernquelle ist [AGENTS.md](../AGENTS.md). Fachregeln bleiben im jeweiligen
Projekt. Der [Umsetzungsauftrag](../03-decision-management/POS-DEC-001-VERIFIED-COLLABORATION.md)
erlaubt dieses abgegrenzte Paket; eine Dateiablage ist kein Laufzeitnachweis.

## Umsetzungs- und Nachweisgrenzen

| Oberfläche / Bereich | Einbindung in diesem Paket | Nachweisgrenze |
| --- | --- | --- |
| Project Operating System | AGENTS.md als kurzer Kern; Workflow, Entscheidungen und DoD verknüpft | Datei- und Inhaltsprüfung im aktuellen Lieferstand; keine Behauptung eines automatischen Ladens in jeder Oberfläche |
| Codex im Repository | AGENTS.md im Repository-Root | Frische unabhängige Codex-Sitzung mit Lade- und Verhaltenstest noch offen |
| Claude Code im Repository | CLAUDE.md importiert AGENTS.md; bisherige Website-Regeln bleiben enthalten | Keine lokale oder Cloud-Claude-Sitzung verfügbar; tatsächliche Anwendung offen |
| GitHub Copilot im Repository | .github/copilot-instructions.md verweist auf den gemeinsamen Kern | Keine Copilot-Laufzeitprüfung; kein Nachweis für Microsoft 365 Copilot |
| Dieser ChatGPT-Dialog | Nutzerauftrag und gelesener Standard liegen im laufenden Kontext vor | Keine unabhängige Prüfung und kein Beleg für dauerhafte kontoweite Einstellung |
| Neue ChatGPT-Chats | Kompakter persönlicher Kopiertext vorbereitet | Kontoeinstellung kann mit den verfügbaren Werkzeugen nicht geschrieben werden; einmalige Nutzeraktion nötig |
| Bestehende Fachagenten / Fachprojekte | Fachliche Prüfkriterien im gemeinsamen Standard beschrieben | Weitergehender Rollout erst nach den vergleichbaren Praxisfällen; keine pauschale Agentenumstellung |
| PPAO | Bestehende Candidate- und Aufrufgrenzen referenziert | PPAO-DEC-001 bleibt gültig; keine Produktivaktivierung |

Die älteren Installationsaussagen in der Capability-Registry sind kein Nachweis
für einen aktuellen globalen Rollout. Ein bestehender Änderungsstopp für
produktive Claude-Konfigurationen wird durch diese Dokumentation nicht pauschal
aufgehoben. Das Paket installiert weder globale Konfigurationen noch Skills.

## Einmaliger Schritt für persönliche ChatGPT-Anweisungen

Damit die Grundregeln auch in neuen Chats als persönliche Vorgabe hinterlegt
sind, ist der [Kopiertext](CHATGPT-INSTRUCTIONS.txt) vorbereitet. Er ist eine
kompakte, bewusst begrenzte Ableitung der Version 1.1-alpha und kein zweiter
vollständiger Standard. Änderungen künftig mit der Kernquelle abgleichen.

1. Den Kopiertext öffnen und den vollständigen Text markieren und kopieren.
2. In ChatGPT über das Profil die Einstellungen öffnen.
3. Unter Personalisierung die benutzerdefinierten beziehungsweise persönlichen
   Anweisungen öffnen. Bezeichnungen können je Oberfläche abweichen.
4. Den Text zu vorhandenen sinnvollen Anweisungen ergänzen; bestehende persönliche
   Angaben nicht ungeprüft ersetzen. Falls das Feld bereits voll ist, den
   vorhandenen Text zunächst gemeinsam kürzen statt Vorgaben zu verlieren.
5. Speichern beziehungsweise die Übernahme der Einstellung bestätigen und einen
   neuen Chat öffnen.
6. Einen kleinen Test stellen: „Ein Anbieter kostet 279 Euro plus 24,90 Euro
   Versand, meine Grenze beträgt 300 Euro. Ist das Angebot passend? Welche
   Angaben fehlen gegebenenfalls?“ Erwartet: 303,90 Euro, daher über der Grenze;
   keine erfundene Lieferbarkeit, kein Kauf ohne Auftrag.

Der Test prüft ein konkretes Verhalten. Dass ChatGPT die Regeln lediglich
wiedergeben kann, beweist keine zuverlässige Einhaltung. Kontostatus erst nach
tatsächlicher Bestätigung aktualisieren. In diesem Auftrag ist die Speicherung
der persönlichen Einstellung nicht nachgewiesen.

## Plattformprüfung bei verfügbarem Zugriff

Zunächst dieses Repository in einer frischen Sitzung öffnen. Ohne Vorladen aus
dem laufenden Dialog feststellen, welche Anweisungsdateien tatsächlich im
Kontext liegen. Anschließend die drei Fälle aus dem
[Pilotprotokoll](../04-quality/COLLABORATION-PILOT.md) bearbeiten. Oberfläche,
Version, Commit, Datum, sichtbaren Ladebeleg und Verhalten festhalten.

Bei Übernahme in andere Projekte dort vorhandene Anweisungen und neueste
Entscheidungen zuerst lesen. Nur die fehlende Einbindung ergänzen und bestehende
Fachregeln bewahren. Den gemeinsamen Kern versioniert referenzieren oder gezielt
importieren; einen bloßen Link nicht als garantierten automatischen Abruf
ausgeben. Kein externer Import bei jedem Routineauftrag, wenn die passende
Version bereits im aktuellen Kontext nachgewiesen ist.

Bei Microsoft 365 Copilot gelten die bankinternen Berechtigungen, verfügbaren
Funktionen und Instruktionsgrenzen. Der stabile Six-Sigma-Agent wird durch dieses
Paket nicht verändert. Eine Tenant-Abnahme bleibt eine gesonderte Prüfung.

## Geprüfte technische Quellen

Dokumentation abgerufen am 17.11.2026; diese Quellen beschreiben die Plattform,
nicht die Installation im Konto des Product Owners:

- [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- [OpenAI: persönliche Vorgaben](https://learn.chatgpt.com/docs/personalize)
- [Anthropic: CLAUDE.md und Dateiimporte](https://code.claude.com/docs/en/memory)
- [GitHub: unterstützte Instruktionsarten und Oberflächengrenzen](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions)
