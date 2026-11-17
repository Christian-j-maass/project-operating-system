# Definition of Ready und Definition of Done

Version: 1.1-alpha · aktualisiert am 17.11.2026

Gemeinsamer Einstieg: [AGENTS.md](../AGENTS.md).
Diese Checklisten werden proportional zum Auftrag verwendet. Eine Routinekorrektur
benötigt keinen vollständigen Audit oder zusätzliche Freigaberunde.

## Definition of Ready

Ein Arbeitspaket darf umgesetzt werden, wenn:

- [ ] Ziel und erwarteter Nutzen verständlich sind
- [ ] Umfang und Abgrenzung feststehen
- [ ] relevante Entscheidungen und Baselines geprüft wurden
- [ ] Akzeptanzkriterien vorliegen
- [ ] notwendige Quellen, Dateien und Abhängigkeiten verfügbar sind
- [ ] offene Product-Owner-Entscheidungen geklärt oder ausdrücklich als Annahme markiert sind
- [ ] gewünschtes Ergebnisformat feststeht
- [ ] Risiken und mögliche Seiteneffekte identifiziert sind
- [ ] das Arbeitspaket klein genug für einen prüfbaren Lieferstand ist

## Definition of Done

Ein Arbeitspaket ist abgeschlossen, wenn:

- [ ] das vereinbarte Ergebnis vollständig erstellt wurde
- [ ] alle Akzeptanzkriterien geprüft wurden
- [ ] Fakten, Annahmen und Unsicherheiten sauber getrennt sind
- [ ] keine bekannten Widersprüche zu akzeptierten Entscheidungen bestehen
- [ ] relevante Qualitätsprüfungen erfolgt sind
- [ ] Entscheidungen, Änderungen und neue Erkenntnisse dokumentiert wurden
- [ ] betroffene Backlog-, Risiko- und Statusinformationen aktualisiert wurden
- [ ] das Ergebnis auffindbar und versioniert abgelegt ist
- [ ] der Lieferstand für den Product Owner verständlich zusammengefasst wurde
- [ ] Folgeaufgaben ausdrücklich erfasst wurden

## Nachweis der Ergebnisprüfung

Für wesentliche Lieferstände je Akzeptanzkriterium dokumentieren:

| Kriterium | Methode | Artefakt / Version | Ergebnis | Grenze / offener Nachweis |
| --- | --- | --- | --- | --- |
| Konkrete überprüfbare Anforderung | Tatsächlich ausgeführte Prüfung | Eindeutige Datei, Commit oder Export | bestanden / nicht bestanden / offen / nicht anwendbar | Nicht ausgeführte Umgebungstests oder verbleibende Unsicherheit |

Ein Erstellungsauftrag, eine Dateiexistenz, ein grüner Build oder eine erneute
Textdurchsicht belegen nicht automatisch die Produktwirkung. Selbstprüfung und
unabhängige Begutachtung werden getrennt bezeichnet. Nach einer Korrektur werden
die betroffene Anforderung und mögliche Rückwirkungen auf frühere Anforderungen
geprüft. Ein Lieferstand kann als teilweise geliefert gemeldet werden; offene
Prüfungen werden nicht still als bestanden gewertet.

## Zusätzliche DoD für Analyse und Recherche

- [ ] Fragestellung und Untersuchungsumfang sind dokumentiert
- [ ] Quellen und Prüfdatum sind nachvollziehbar
- [ ] Schätzungen sind als Schätzungen gekennzeichnet
- [ ] konkurrierende Befunde oder Unsicherheiten werden genannt
- [ ] Schlussfolgerungen sind von Rohbefunden getrennt
- [ ] entscheidungstragende Aussagen sind direkt durch die angegebenen Quellen gedeckt; konkurrierende Modellantworten gelten nicht als Quellenbeleg
- [ ] die Aufbereitung entspricht dem vereinbarten Format

## Zusätzliche DoD für Software

- [ ] Implementierung entspricht den Anforderungen
- [ ] relevante Tests wurden erstellt oder durchgeführt
- [ ] Fehlerfälle und Eingabevalidierung wurden berücksichtigt
- [ ] Datenschutz, Sicherheit und Barrierefreiheit wurden geprüft, soweit relevant
- [ ] Dokumentation und Startanleitung wurden aktualisiert
- [ ] Änderungen sind in einem nachvollziehbaren Commit enthalten
- [ ] Release- oder Änderungsnotiz ist vorbereitet
- [ ] die betroffene Nutzerfunktion wurde passend zum Risiko geprüft; nicht verfügbare Geräte- und Tenant-Prüfungen sind offen ausgewiesen

## Zusätzliche DoD für Präsentationen und Dokumente

- [ ] Zahlen, Begriffe, Versionsstände und Quellen stimmen überein
- [ ] Inhalt und Gestaltung unterstützen die Zielgruppe
- [ ] keine veralteten Entwürfe werden als final dargestellt
- [ ] Dateiname, Datum und Version sind eindeutig
- [ ] Export wurde visuell geprüft
- [ ] nach Korrekturen wurden Vollständigkeit und bereits akzeptierte Gestaltung erneut an den betroffenen Exportseiten geprüft

## Zusätzliche DoD für Audio und Video

- [ ] der tatsächlich ausgegebene Export wurde angehört beziehungsweise angesehen
- [ ] vereinbarte Lautstärkeverhältnisse, Übergänge, Bewegungen und Kontinuität sind am Export geprüft
- [ ] bei relevanten Mischungsänderungen wurden verfügbare technische Messungen mit der Hörprobe abgeglichen
- [ ] fehlender Zugriff auf Ton, Export oder Abspielumgebung ist ausdrücklich als Prüfgrenze dokumentiert
