# website-bauen – Befund und Verifikation

Stand 18.10.2026. Änderung auf dem bestehenden PR-2-Branch, kein zweiter Skill
und keine Installation. Upstream ist über Commit und SHA-256 im Manifest fixiert;
kein semantischer Release-Tag und keine Lizenzdatei im geprüften Checkout.
Der bestehende Paket-Builder verarbeitet nur `skills/`; externe Referenzen werden
absichtlich nicht kopiert oder umgeschrieben.

## Nachweisbare Architektur

- Avenward `.claude/agents/` enthält category-migration-proposer,
  dependency-hardening, legal-conflict-resolver, newsletter-drafter,
  quarterly-benefit-review, session-guardian. Kein ausdrücklich benannter
  Design-Agent. Avenwards CLAUDE.md enthält keine website-bauen-Laderegel.
- Globale Agentendateien auf Christians Rechner sind nicht zugänglich.
- Die Work-Sitzung listet website-bauen; SKILL.md wurde erfolgreich gelesen.
  Diese bereitgestellte Fassung hat nicht dasselbe Frontmatter wie der aktuelle
  Upstream. Deshalb weder Commitgleichheit noch globale Persistenz behaupten.
- Upstream erlaubt expliziten Claude-Aufruf `/website-bauen` und beschreibt
  automatische Relevanzauswahl. Das ist eine Auswahlmöglichkeit, keine Garantie.
- Claude `skills:` lädt Inhalte beim Subagent-Start vor, wenn verfügbar und nicht
  deaktiviert. Fehlende/deaktivierte Skills können übersprungen werden. Deshalb
  Ladebeleg und Blockerregel. Ein Skillname in einem Register aktiviert nichts.
- Die neue Root-CLAUDE.md gilt nur im Registry-Repository. Übernahme in einen
  tatsächlich vorhandenen globalen Design-Agenten oder ein anderes Projekt bleibt
  offen, bis dessen Konfiguration und Regeln geprüft werden können.

## Lokale Prüfung ohne Installation (auf Christians Rechner)

1. Claude-Code-Version und aktiven Projektpfad notieren. Persönliche Skills unter
   `~/.claude/skills/`, Projekt-Skills unter `.claude/skills/` und Plugin-Skills
   prüfen; bei Symlinks Ziel auflösen. Auch `~/.agents/skills/website-bauen`
   als mögliches Ziel des Skills-Installers prüfen. Keine Zugangsdaten ausgeben.
2. Alle website-bauen-Kandidaten und gleichnamigen Commands prüfen. SKILL.md,
   referenzierte Phasen/Vorlagen, Git-Commit oder Dateihash festhalten. Nicht
   erneut `npx ... skills add` ausführen. Bei Konflikt zuerst aktive Quelle klären.
3. `~/.claude/agents/`, `.claude/agents/`, Plugins und `--agents`-Startparameter
   auf den tatsächlichen Design-Agenten prüfen. Dessen vorhandene `skills`-Liste
   um website-bauen ergänzen; vorhandene Tools und Fähigkeiten erhalten.
   `disable-model-invocation`, skillOverrides und Skill-Tool-Rechte prüfen.
4. Root-Regel aus diesem Repository in die geltenden Anweisungen übernehmen,
   nachdem dortige Prioritäten geprüft wurden. Neue Sitzung starten, Tests unten
   ausführen und Lade-/Debugnachweis sichern. Erst dann Status erhöhen.

## Laufzeit-Abnahme (noch nicht ausgeführt)

Pro Umgebung Version, Zeitpunkt, aktive Quelle, Agent und Ladebeleg erfassen.
In einem Wegwerfprojekt mit vorhandener WEBSITE-STATUS.md testen:

| Fall | Auftrag | Erwartung |
| --- | --- | --- |
| Explizit | `/website-bauen status` | Skill geladen, Status gelesen, keine Änderungen |
| Automatisch | Neue Firmenwebsite erstellen | Ladebeleg vor erster fachlicher Arbeit |
| Änderung | Navigation der vorhandenen Website verbessern | passende Phase, kein Neustart |
| Optimierung | Website auf mobile Barrierefreiheit prüfen | passende Phase, bestehende Entscheidungen erhalten |
| Negativ | Nur Prettier aktualisieren | kein Website-Prozess |
| Negativ | Benefit-Anspruchsdaten aktualisieren | kein Website-Prozess |
| Agent | gleichen Website-Auftrag an tatsächlichen Design-Agenten | voller Skill vorgeladen, Quelle belegt |
| Fehlt | Skill im Testprofil deaktivieren/entfernen | konkreter Blocker, keine Installation |
| Persistenz | neue unabhängige Sitzung | Quelle und Skill erneut verfügbar |

Claude lokal, Claude Code web/Cloud und claude.ai separat erfassen; lokale
Installation wird nicht als Cloud-Installation gewertet. Bei ChatGPT natürlichen
expliziten Skillnamen nutzen; `$website-bauen` ist die Upstream-Codex-Syntax,
keine zugesicherte ChatGPT-Slash-Command-Schnittstelle. Eine bestandene statische
Prüfung beweist keine Modellentscheidung und keine Ausführung im fremden Host.

## Quellen

- https://github.com/Julian-Ivanov/website-bauen/tree/ee7c4cbfa3fd2e7c2e169b2831f4218a27edc9ca
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/sub-agents#preload-skills-into-subagents
- https://github.com/Christian-j-maass/-avenward-veterans/tree/main/.claude/agents
- https://github.com/Christian-j-maass/-avenward-veterans/blob/main/CLAUDE.md
