# Plattformstatus – Claude und ChatGPT

Stand: 23.08.2026  
Registry: 0.1.0-candidate

## Aktueller Nachweis

| Capability | ChatGPT | Claude lokal | Claude Cloud | Bemerkung |
| --- | --- | --- | --- | --- |
| PPAO Candidate | installiert und verifiziert | Aktivierung offen | Aktivierung offen | Explizit aufrufbar; kein Superagent; nicht final |
| Token Optimization | installiert und verifiziert | Aktivierung offen | Aktivierung offen | Portable korrigierte Fassung liegt vor |
| TeachMe | dokumentiert | nicht aktuell verifiziert | nicht aktuell verifiziert | Paketierung folgt in Punkt 2 |
| GrillMe | dokumentiert | Recheck erforderlich | 19.08. historisch belegt | Paketierung/Erweiterung folgt |
| Vermenschlichen | dokumentiert | nicht aktuell verifiziert | nicht aktuell verifiziert | Paketierung/Erweiterung folgt |
| Projekt Neustart | dokumentiert | nicht aktuell verifiziert | nicht aktuell verifiziert | Paketierung folgt |
| Projektmanagement | dokumentiert | nicht aktuell verifiziert | nicht aktuell verifiziert | Paketierung folgt |
| kie.ai / higgsfield-skill | native Alternative: ImageGen | vom PO bestätigt | vom PO bestätigt | Higgsfield nur optionaler Fallback |

## Wichtigste Lücke

PPAO und Token Optimization besitzen jetzt einen gemeinsamen portablen Kern und sind in ChatGPT aktiv. Claude kennt beide nach aktueller Aussage des Product Owners noch nicht dauerhaft. Die lokale und die Cloud-Installation müssen getrennt aktiviert und verifiziert werden.

## Definition „installiert“

Eine Capability gilt nur als installiert, wenn die konkrete Oberfläche einen dauerhaften Nachweis liefert. Eine Skill-Liste in einer kurzlebigen Claude-Remote-Sitzung genügt nicht, wenn der Skill nur im Container liegt.

- **ChatGPT:** persönliche Skill-Installation gespeichert und nach Synchronisierung verifiziert.
- **Claude lokal:** Skill im persönlichen Claude-Skillverzeichnis vorhanden und in neuer lokaler Sitzung erkennbar.
- **Claude Cloud:** Skill in der claude.ai-Skillverwaltung gespeichert und in einer neuen Cloud-Sitzung erkennbar.

## Nächste operative Reihenfolge

1. PPAO Candidate und Token Optimization in Claude lokal aktivieren.
2. Beide getrennt in Claude Cloud aktivieren.
3. Installationsnachweise im Manifest auf `installed-verified` setzen.
4. Danach die fünf Kernskills paketieren und plattformweise ausrollen.
