# LL-001 – Projektorganisation Avenward Veterans

Datum: 2026-08-01  
Status: Maßnahmen beschlossen  
Vertraulichkeitsstufe: öffentlich geeignete Prozesszusammenfassung

## Ausgangslage

Im Verlauf des Projekts wurden bereits getroffene Entscheidungen, vereinbarte Arbeitsweisen und frühere Analyseergebnisse mehrfach nicht zuverlässig in nachfolgenden Arbeitsschritten berücksichtigt. Die strukturierte Nutzung von GitHub als dauerhafte Projektdokumentation begann erst spät.

## Was gut lief

- klare und ambitionierte Produktvision
- hohe fachliche Tiefe und Qualitätsorientierung
- Product Owner traf Richtungsentscheidungen konsequent
- Bereitschaft, komplexe Anforderungen systematisch auszuarbeiten
- schrittweise Entwicklung eines Qualitäts-, Evidenz- und Datenschutzanspruchs
- Fehler wurden erkannt und offen angesprochen

## Was nicht gut lief

### 1. Entscheidungen blieben zu lange im Chat

**Wirkung:** Bereits geklärte Themen wurden erneut gefragt, diskutiert oder anders umgesetzt.

**Ursache:** Es fehlte anfangs ein konsequent gepflegtes Decision Log als verbindliche Quelle.

### 2. GitHub wurde zu spät als System-of-Record eingeführt

**Wirkung:** Wissen verteilte sich auf Chats, Einzeldateien und Erinnerungen. Migration und Rekonstruktion wurden notwendig.

**Ursache:** Die Projektinitialisierung startete direkt mit Produktinhalten, ohne vorherige Ablage- und Governance-Struktur.

### 3. Analyseaufbereitung war nicht durchgehend standardisiert

**Wirkung:** Umfang, Tiefe, Quellenstruktur und Ergebnisdarstellung wechselten; Ergebnisse mussten teilweise neu aufbereitet werden.

**Ursache:** Für Analysen fehlten zu Beginn verbindliche Templates und Akzeptanzkriterien.

### 4. Zu viele Themen wurden parallel geöffnet

**Wirkung:** Kontextwechsel, Prioritätsunklarheit und erhöhte Gefahr unvollständiger Dokumentation.

**Ursache:** Es gab keine wirksame Begrenzung paralleler Arbeit und keinen konsequenten Sprintfokus.

### 5. Fertigstellung und Dokumentation waren getrennt

**Wirkung:** Ein fachliches Ergebnis konnte als abgeschlossen erscheinen, obwohl Ablage, Status, Entscheidungslog oder Folgeaufgaben noch fehlten.

**Ursache:** Eine verbindliche Definition of Done wurde erst spät formuliert.

### 6. Product-Owner-Fragen wurden nicht immer vorab auf Dubletten geprüft

**Wirkung:** Der Product Owner musste bereits entschiedene Sachverhalte erneut bestätigen.

**Ursache:** Die verpflichtende Entscheidungskontrolle vor einer Frage war organisatorisch nicht abgesichert.

## Beschlossene Gegenmaßnahmen

| ID | Maßnahme | Verbindlichkeit | Erfolgsindikator |
|---|---|---|---|
| M-001 | GitHub-Repository und Minimal-Governance vor Detailarbeit einrichten | verpflichtend | kein Langzeitprojekt startet ausschließlich im Chat |
| M-002 | Jede wesentliche Entscheidung erhält eine ID und einen Status | verpflichtend | Entscheidungen sind eindeutig auffindbar |
| M-003 | Vor jeder Product-Owner-Frage erfolgt ein Decision Check | verpflichtend | keine vermeidbaren Wiederholungsfragen |
| M-004 | Maximal drei aktive Arbeitspakete gleichzeitig | Standard, Abweichung begründen | weniger Kontextwechsel und angefangene Nebenstränge |
| M-005 | Definition of Ready und Definition of Done anwenden | verpflichtend | keine Lieferung ohne Dokumentationsabschluss |
| M-006 | Einheitliches Analyse-Template verwenden | verpflichtend für größere Analysen | konsistente Quellen-, Annahmen- und Ergebnisstruktur |
| M-007 | Jeder Lieferzyklus endet mit Dokumentation und Statusbericht | verpflichtend | GitHub entspricht dem tatsächlichen Arbeitsstand |
| M-008 | Änderungen an Baselines nur über dokumentierte Change-Entscheidung | verpflichtend | keine stillen Überschreibungen |
| M-009 | Retrospektive nach relevanten Fehlern oder Meilensteinen | verpflichtend | Prozessfehler erzeugen nachweisbare Verbesserungen |

## Wirksamkeitsprüfung

Die Maßnahmen werden zunächst im Projekt Avenward Veterans praktisch getestet. Nach den nächsten drei größeren Lieferständen wird geprüft:

- Wurden bereits entschiedene Themen erneut gefragt?
- Stimmen Chat-Lieferstand und GitHub-Dokumentation überein?
- Sind offene Arbeiten eindeutig im Backlog sichtbar?
- Wurden neue Entscheidungen nachvollziehbar versioniert?
- Mussten Analysen wegen unklarer Aufbereitung neu erstellt werden?

## Zentrale Erkenntnis

Die fachliche Qualität allein sichert keinen verlässlichen Projektfortschritt. Bei langfristiger Zusammenarbeit mit KI müssen Kontext, Entscheidungen und Lieferstände aktiv in einem externen, versionierten System gesichert werden. GitHub ist deshalb nicht nur Code-Ablage, sondern das dauerhafte Projektgedächtnis.
