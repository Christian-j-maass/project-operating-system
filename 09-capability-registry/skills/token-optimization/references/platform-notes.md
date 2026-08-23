# Platform Notes

## Gemeinsamer Kern

- Halte dauerhafte Anweisungen kurz und verlagere Verfahren in Skills und Referenzen.
- Lade nur aufgabenrelevante Dateien, Tools und Skills.
- Trenne plattformneutrale Qualitätsregeln von Host-Kommandos und Einstellungen.
- Prüfe aktuelle offizielle Dokumentation, bevor dauerhafte Konfigurationsänderungen empfohlen werden.

## ChatGPT und Codex

- Nutze Progressive Disclosure: kurze Skill-Metadaten, fokussierte SKILL.md, Referenzen nur bei Bedarf.
- Suche zunächst gezielt nach Dateinamen, Überschriften und relevanten Mustern; lies danach die erforderlichen Originalstellen.
- Halte Zwischenmeldungen und Tool-Ausgaben knapp, Lieferdokumente jedoch vollständig.
- Nutze verfügbare native Verbrauchsmetriken; erfinde keine Tokenwerte, wenn die Oberfläche keine zuverlässigen Daten liefert.
- Beachte die aktuellen Plattformregeln zu Agenten, Parallelität, Berechtigungen und Dateioperationen.

## Claude und Claude Code

- Verwende `/context`, `/plugin`, `/skills` oder `/compact` nur, wenn die eingesetzte Claude-Code-Version diese Befehle unterstützt.
- Empfehle keinen `contextWindow`-Schlüssel in `settings.json`, solange er nicht in der aktuellen offiziellen Einstellungsreferenz der eingesetzten Version dokumentiert ist.
- `context: fork` ist in aktuellen Claude-Code-Skills gültiges Frontmatter für isolierte Subagent-Ausführung. Nutze es nur für eine explizite, in sich ausführbare Aufgabe; der isolierte Skill erhält nicht automatisch den Gesprächsverlauf.
- Behandle experimentelle Conversation-Forks und das Skill-Frontmatter `context: fork` nicht als dasselbe Feature. Prüfe Versionsvoraussetzungen und Kontextvererbung in der aktuellen Primärdokumentation.
- Behandle Compaction als potenziell verlustbehaftete Verdichtung. Sichere entscheidungsrelevante Details vorher persistent.
- Halte `CLAUDE.md` auf dauerhafte Projektfakten und kurze Regeln begrenzt; lagere lange Verfahren in Skills aus.
- Konfiguriere Skills, Tools und MCPs möglichst vor einer Arbeitssitzung; ändere dauerhafte Konfiguration nicht beiläufig mitten in einer kritischen Analyse.

## Providerneutralität

Optimiere den Workflow, nicht für eine einzelne Anbieterbehauptung. Dokumentiere Host-spezifische Abweichungen und behalte gemeinsame Akzeptanzkriterien für Claude und ChatGPT bei.
