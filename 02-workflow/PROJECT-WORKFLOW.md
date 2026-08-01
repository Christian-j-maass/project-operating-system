# Verbindlicher Projektworkflow

Version: 1.0-alpha  
Gültig ab: 2026-08-01

## 1. Projektstart

Vor fachlicher Detailarbeit werden mindestens angelegt:

- Projektauftrag und Zielbild
- In-Scope / Out-of-Scope
- Product Owner und Rollen
- Projekt-Repository
- erste Roadmap
- Product Backlog
- Decision Log
- Risikoregister
- Definition of Ready
- Definition of Done

Ohne diese Minimalstruktur darf nur explorative Vorarbeit erfolgen. Explorative Ergebnisse müssen ausdrücklich als vorläufig gekennzeichnet werden.

## 2. Verbindliche Quellenhierarchie

Bei Widersprüchen gilt folgende Reihenfolge:

1. freigegebene Baseline-Dokumente im Projekt-Repository
2. aktive Einträge im Decision Log
3. freigegebene Anforderungen und Issues
4. zuletzt dokumentierter Lieferstand
5. Chat-Verlauf

Chat-Erinnerungen dürfen keine dokumentierte Baseline still überschreiben.

## 3. Arbeitseingang

Jeder neue Auftrag wird vor Bearbeitung geprüft auf:

- bereits vorhandene Entscheidung
- Dublette oder Wiederholung
- Widerspruch zu Baselines
- Abhängigkeiten
- notwendige Product-Owner-Entscheidung
- erwartetes Ergebnisartefakt
- Akzeptanzkriterien

Nur echte Entscheidungslücken werden dem Product Owner vorgelegt.

## 4. Lieferzyklus

Jeder Arbeitszyklus folgt dieser Pipeline:

1. **Entscheidungsprüfung** – bestehende Regeln und Anforderungen prüfen
2. **Planung** – Ziel, Umfang, Abhängigkeiten und Akzeptanzkriterien festlegen
3. **Umsetzung** – Ergebnis oder Artefakt erstellen
4. **Qualitätsprüfung** – Inhalt, Konsistenz, Vollständigkeit und Risiken prüfen
5. **Dokumentation** – Entscheidungen, Änderungen und Ergebnisse aktualisieren
6. **Bericht** – Lieferstand, offene Punkte und nächste Priorität melden

Kein Schritt gilt als abgeschlossen, wenn die Dokumentation fehlt.

## 5. Begrenzung paralleler Arbeit

Standardmäßig dürfen höchstens drei aktive Arbeitspakete gleichzeitig bestehen:

- ein primäres Lieferpaket
- ein notwendiges Recherche- oder Abhängigkeitspaket
- ein Dokumentations- oder Qualitätspaket

Neue Themen werden in das Backlog aufgenommen, statt laufende Arbeit ungeplant zu verdrängen. Dringende Änderungen werden als Expedite gekennzeichnet und ihre Auswirkungen dokumentiert.

## 6. Sprint-Logik für die Zusammenarbeit mit KI

Empfohlene Sprintdauer: ein klar abgegrenzter Lieferstand statt starrer Kalenderwochen.

Ein Sprint enthält:

- Sprintziel
- ausgewählte Backlog-Einträge
- überprüfbare Ergebnisse
- Akzeptanzkriterien
- Abschlussbericht
- kurze Retrospektive bei relevanten Problemen oder neuen Erkenntnissen

## 7. Product-Owner-Kommunikation

Der Product Owner entscheidet insbesondere über:

- Prioritäten
- Produktumfang
- nicht reversible oder kostenrelevante Entscheidungen
- wesentliche Änderungen an Vision, Marke oder Geschäftsmodell
- Akzeptanz kritischer Risiken

Technische oder organisatorische Detailentscheidungen werden innerhalb freigegebener Leitplanken eigenständig vorbereitet und dokumentiert.

## 8. Änderungsmanagement

Eine bestehende Baseline darf nur geändert werden, wenn dokumentiert sind:

- Auslöser
- bisheriger Zustand
- neuer Zustand
- Begründung
- Auswirkungen
- betroffene Artefakte
- Freigabestatus
- Datum und Version

## 9. Abschluss eines Lieferstands

Ein Lieferstand ist erst fertig, wenn:

- Ergebnis erstellt ist
- Akzeptanzkriterien geprüft sind
- Widersprüche geklärt oder als offen markiert sind
- relevante Dokumente aktualisiert sind
- offene Risiken und Folgeaufgaben im Backlog stehen
- der Product Owner einen verständlichen Status erhält
