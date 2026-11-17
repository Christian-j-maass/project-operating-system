# Anwendungsproben und Wirksamkeitsvergleich

Stand: 17.11.2026 · Standard: 1.1-alpha

## Aussagegrenze

Die folgenden drei Fälle wurden in diesem Auftrag als lesende beziehungsweise
synthetische Anwendungsproben im selben Chat-Kontext bearbeitet. Die Ergebnisse
sind Selbstprüfungen, keine unabhängigen Modellläufe. Es existieren noch keine
gepaarten Vorher-/Nachher-Läufe und keine gemessenen Token- oder Zeitersparnisse.
Eine höhere Ergebnisqualität gegenüber dem bisherigen Standard ist damit nicht
nachgewiesen. Die technische Prüfung der Dateien wird davon getrennt geführt.

Ausgangsstand: Repository-Commit `4ee78b4142652cea1da787b406fac727d438d941`.
Kandidat: abgegrenzter Lieferstand mit der
[Entscheidung POS-DEC-001](../03-decision-management/POS-DEC-001-VERIFIED-COLLABORATION.md).

## Fall 1: Verfügbarkeit und Einsatzfreigabe unterscheiden

**Auftrag:** Darf PPAO aufgrund eines älteren Plattformnachweises automatisch
produktiv eingesetzt werden?

**Eingabe:** Die [Plattformübersicht](../09-capability-registry/PLATFORM_STATUS.md)
nennt mit historischem Stand eine Installation und aktive Verfügbarkeit. Die
neuere [Entscheidung PPAO-DEC-001 vom 02.11.2026](../08-ppao/README.md) erlaubt
nur die Dokumentationsübernahme und ausdrücklich keine Produktivaktivierung.

**Bearbeitetes Ergebnis:** Nein. Der ältere Nachweis betrifft Verfügbarkeit;
die neuere ausdrückliche Entscheidung begrenzt den zulässigen Einsatz. PPAO
bleibt Candidate und wird durch diesen Auftrag nicht produktiv aktiviert.
Ein aktueller Installationsstand in anderen Oberflächen ist nicht geprüft.

**Kriterien / Selbstprüfung:** Aktuellere Entscheidung angewandt; Installation
von Freigabe getrennt; Quellen genannt; keine Aktivierung behauptet. Erfüllt.
Diese Fallantwort ist keine neue PPAO-Prüfung oder Produktivfreigabe.

## Fall 2: Vergleich nach Gesamtpreis und belegter Variante

**Auftrag:** Welche Angebote erfüllen eine Grenze von 300 Euro einschließlich
Versand für das vorgegebene Modell in Größe 54?

**Eingabe:** Vollständig synthetische Daten, keine realen Händlerangebote:

| Angebot | Artikel | Versand | Modell / Größe 54 tatsächlich bestellbar |
| --- | --- | --- | --- |
| A | 279,00 Euro | 24,90 Euro | laut Fallvorgabe bestätigt |
| B | 289,00 Euro | 9,90 Euro | laut Fallvorgabe bestätigt |
| C | 269,00 Euro | 0,00 Euro | Größe 54 nicht verifiziert |

**Bearbeitetes Ergebnis:** Nur B erfüllt die Vorgabe: 298,90 Euro insgesamt.
A liegt mit 303,90 Euro über der Grenze. C liegt rechnerisch bei 269,00 Euro,
ist wegen der ungeklärten Größe aber kein bestätigter Treffer. Es wurde kein
reales Angebot recherchiert oder eine tatsächliche Lieferbarkeit behauptet.

**Kriterien / Selbstprüfung:** Versand eingerechnet; Grenze korrekt angewandt;
ungeklärte Variante ausgeschlossen; synthetische Angaben gekennzeichnet. Erfüllt.
Die beiden entscheidenden Summen sind zusätzlich mit Dezimalrechnung zu prüfen.

## Fall 3: Erstellung und Prüfung eines Medienexports trennen

**Auftrag:** Ist eine Audiokorrektur abgeschlossen, wenn das Mischprojekt geändert
wurde und ein Exportpfad genannt ist, der fertige Export aber weder zur Messung
noch zum Anhören vorliegt?

**Eingabe:** Synthetische Statusbeschreibung. Vorgabe: Musik bleibt im Vordergrund
und wird bei Geräuschen nicht abgesenkt. Keine abspielbare Datei bereitgestellt.

**Bearbeitetes Ergebnis:** Die Bearbeitung ist beschrieben, die Ergebnisabnahme
ist offen. Ohne zugänglichen fertigen Export lässt sich weder die Lautstärke
noch ein unerwünschtes Absenken bestätigen. Nächster Schritt ist, den verfügbaren
Export zu beschaffen und die Geräuschübergänge mit Hörprobe und passenden
technischen Messungen zu kontrollieren. Der Fall wird nicht als fertige
Medienkorrektur ausgegeben; es wird keine erneute Produktionsfreigabe erfunden.

**Kriterien / Selbstprüfung:** Keine erfundene Hörprobe; offenes Kriterium
benannt; konkreter Prüfschritt; keine unnötige Freigabefrage. Erfüllt.
Eine echte Medienprüfung wurde in dieser Anwendungsprobe nicht ausgeführt.

## Praktischer Vorher-/Nachher-Vergleich: noch offen

Für jeden der drei Fälle Ausgangsstandard und Kandidat mit identischer Eingabe,
gleichen Quellenständen und möglichst derselben Modell-/Toolkonfiguration in
getrennten frischen Kontexten bearbeiten. Die eine Antwort wird dem anderen
Lauf nicht vorgegeben. Tatsächliche Ausgaben und Prüfnachweise aufbewahren.

| Messgröße | Ausgangsstandard | Kandidat | Wertung |
| --- | --- | --- | --- |
| Erfüllte Pflichtkriterien / ausgelassene Anforderungen | noch nicht gemessen | noch nicht gemessen | keine Qualitätsverschlechterung zulässig |
| Fachliche Fehler und unbelegte Aussagen | noch nicht gemessen | noch nicht gemessen | keine kritische Regression zulässig |
| Notwendige Korrekturschleifen | noch nicht gemessen | noch nicht gemessen | konkreter Nutzen bei weniger Nacharbeit |
| Wiederholte oder unnötige Nutzerfragen | noch nicht gemessen | noch nicht gemessen | vorhandene Freigaben werden berücksichtigt |
| Zeit / Token / Kosten, soweit wirklich verfügbar | noch nicht gemessen | noch nicht gemessen | fehlende Werte bleiben offen |

Die drei Fälle sind ein kleiner Praxistest, keine statistisch belastbare
Allgemeinaussage. Zusätzliche Agenten oder neue globale Konfigurationen werden
nicht allein wegen bestandener Anwendungsproben ausgerollt. Zuerst belastbare
Vergleichsdaten erfassen und Qualität mindestens erhalten.

## Technischer Prüfnachweis dieses Lieferstands

Lokale Prüfungen vom 17.11.2026 am abgegrenzten Änderungspaket:

| Kriterium | Methode / geprüfter Stand | Ergebnis | Grenze |
| --- | --- | --- | --- |
| Verlässlicher Ausgangsstand | Alle 28 Ausgangsdateien gegen ihre Git-Blob-SHAs am genannten Baseline-Commit geprüft | bestanden | Kein unabhängiger Plattformlauf |
| Vorhandene Fähigkeiten erhalten | Bestehende Registry-Unittests mit temporärem Paket-Build für Claude und ChatGPT ausgeführt | 3 Tests bestanden | Paket-Build ist kein Installations- oder Aktivierungsnachweis |
| Begrenzter Änderungsumfang | 5 vorhandene Dateien geändert und 6 neue Dateien ergänzt; übrige Ausgangsdateien verglichen | bestanden | Zusätzlicher Remote-Diff im Pull Request erforderlich |
| Bestehende Regeln bewahrt | 22 PPAO-/Registry-Dateien bytegleich; bisherige Website-Anweisung nach Entfernen des neuen Imports bytegleich | bestanden | Laufzeit in fremden Oberflächen offen |
| Interne Dokumentverweise | 26 relative Links der geänderten und neuen Dokumente auf vorhandene Ziele aufgelöst | bestanden | Kein automatischer Beweis für Abruf oder Befolgung durch einen Agenten |
| Kompakter persönlicher Kopiertext | Zeichen gezählt | 1.180 Zeichen ohne abschließenden Zeilenumbruch | Speicherung im Nutzerkonto offen |
| Rechenbeispiel | Beide entscheidenden Summen mit Decimal nachgerechnet | 303,90 und 298,90 Euro bestätigt | Synthetische Angebote, keine Händlerprüfung |

Der abschließende Remote-Diff und die Übernahme werden am tatsächlichen GitHub-
Lieferstand im Pull Request nachgewiesen. Plattform-Laufzeittests und kontoweite
Einstellungen werden davon getrennt im
[Einbindungsstatus](../07-project-adoption/COLLABORATION-ADOPTION.md) geführt.
