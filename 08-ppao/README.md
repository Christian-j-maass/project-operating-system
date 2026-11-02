# PPAO: Dokumentation und Freigabestatus

Stand: 2. November 2026. Dieser Einstieg trennt historische Entwürfe, die dokumentierte Candidate-Fassung und die aktuelle Entscheidung über den Umfang des Merges.

## PPAO-DEC-001: Dokumentation ohne Aktivierung

| Feld | Festlegung |
| --- | --- |
| ID | PPAO-DEC-001 |
| Datum / Status | 02.11.2026 / ACCEPTED |
| Entscheider | Product Owner |
| Kontext / Problem | PR #1 enthält historische Design-, Architektur- und Pilotunterlagen. Ohne Kennzeichnung könnten frühere Aussagen als aktuelle Einsatzfreigabe gelesen werden. Effektiver Nutzen und Folgen des PPAO-Einsatzes müssen noch gemeinsam geklärt werden. |
| Betrachtete Optionen | Historische Unterlagen weiter als PR offen halten; als gekennzeichnete Dokumentation übernehmen; produktiven Einsatz freigeben. Gewählt ist ausschließlich die Dokumentationsübernahme. |
| Entscheidung | Die drei historischen Originaldokumente mit Statushinweisen und Verweisen übernehmen und PR #1 als Dokumentation mergen. PPAO nicht produktiv schalten. Vor einer gesonderten Einsatzentscheidung sind Nutzen und Konsequenzen gemeinsam im Detail zu klären. |
| Begründung | Entstehung und frühere Entscheidungen nachvollziehbar sichern und den Dokumentations-PR abschließen, ohne einen noch ungeklärten Einsatz vorwegzunehmen. |
| Auswirkungen | Dieser Merge erteilt keinen Auditauftrag, startet oder verlängert keinen Pilot und erlaubt keine neue Installation, automatische Aktivierung oder Produktivaktivierung. Vorhandene Candidate-Dateien, Adapter, Manifest- und Installationsstände werden durch diesen Lieferstand nicht verändert. |
| Betroffene Artefakte | Die drei unten verlinkten Originaldokumente, dieser Einstieg, der Repository-Einstieg und PR #1. |
| Reversibilität | Dokumentationsänderung ist versioniert rücknehmbar; die Originalhistorie bleibt erhalten. |
| Wiedervorlage | Nächste ausdrücklich beauftragte gemeinsame Nutzen- und Folgenklärung; kein automatischer Audit- oder Pilotstart. |
| Ersetzt / ersetzt durch | Keine historischen Sachentscheidungen werden gelöscht oder rückwirkend umgeschrieben. Damalige Pilotfreigaben werden durch diesen Merge nicht erneuert. Eine spätere Einsatzfreigabe benötigt eine eigene dokumentierte Entscheidung; sie liegt hier nicht vor. |

Quelle: ausdrücklicher Product-Owner-Auftrag vom 02.11.2026 zur Kennzeichnung, Verknüpfung und Dokumentationsübernahme, verbunden mit dem Auftrag, PPAO noch nicht produktiv zu schalten.

## Historische Originaldokumente

Die Originaltexte unterhalb der neuen Statushinweise bleiben unverändert. Angaben wie „freigegebene Pilot-Baseline“, „PPAO darf“ oder „nächste Schritte“ sind im damaligen zeitlichen Kontext zu lesen.

| Dokument | Historischer Stand | Einordnung |
| --- | --- | --- |
| [Designreview](PPAO_DESIGN_REVIEW_2026-08-20.md) | 20.08.2026 | Ursprüngliche 43 Entscheidungen und geplante Auditstruktur |
| [Konsolidierungsarchitektur](PPAO_CONSOLIDATION_ARCHITECTURE_2026-08-21.md) | 21.08.2026 | Verschlankung, Rollenabgrenzung und vorläufige Lastregeln |
| [Avenward-Shadow-Pilotplan](PPAO_AVENWARD_SHADOW_PILOT_2026-08-23.md) | Planung für 23.08.2026 | Historischer Pilotplan; kein Auftrag zur Fortsetzung oder Wiederholung |

## Aktuell dokumentierte Regeln

Diese Quellen beschreiben PPAO weiterhin als **Candidate – nicht final**. Sie sind Referenzen für eine spätere ausdrücklich beauftragte Klärung, keine Aktivierung durch ihre Verlinkung.

- [Candidate und Rollenbegrenzung](../09-capability-registry/skills/ppao-candidate/SKILL.md): ausdrücklicher Auftrag, zunächst lesend; kein Superagent, zweiter Projektleiter oder autonomer Änderungsagent.
- [Governancebaseline](../09-capability-registry/skills/ppao-candidate/references/governance-baseline.md): risikobasierte Tiefe, keine Wiedereröffnung akzeptierter Entscheidungen ohne materiell neue Evidenz und keine generelle Produktivaktivierung.
- [Auditvertrag](../09-capability-registry/skills/ppao-candidate/references/audit-contract.md): Findings und Gate-Status als Entscheidungshilfe, kein Ersatz für eine formale Freigabe.
- [Shadow-Regeln](../09-capability-registry/skills/ppao-candidate/references/shadow-mode.md): keine Verzögerung von Routinearbeit durch unnötige Methodendiskussionen oder Rückfragen; projektspezifische Grenzen nicht pauschal übertragen.
- [Entscheidungsstandard](../03-decision-management/DECISION-STANDARD.md): vor Rückfragen zuerst vorhandene Entscheidungen und Akzeptanzkriterien prüfen.

## Offene Nutzen- und Folgenklärung

**Berichteter Prüfpunkt:** Der Product Owner erinnert sich an durch PPAO ausgelöste Rückfragen, deren Auflösung aufwendig war. Konkrete Einzelfälle, Ursachen, Aufwand und Wirksamkeit damaliger Korrekturen sind in diesem Lieferstand nicht rekonstruiert. Eine gesicherte Ursachenzuordnung oder ein nachgewiesener Gesamtnutzen wird daraus nicht abgeleitet.

Für die spätere gemeinsame Klärung bleiben offen:

1. Frühere Rückfragen und Blockaden anhand konkreter Verläufe rekonstruieren: Was war entscheidungsrelevant, was bereits entschieden, was entstand durch eine Fehlanwendung oder widersprüchliche Regeln?
2. Tatsächlichen Zusatznutzen gegenüber der bestehenden Projektarbeit bestimmen: bestätigte zusätzliche Befunde und vermiedene Fehler gegen Rückfragen, Nacharbeit, Zeit- und Tokenaufwand abwägen; fehlende Messwerte offen lassen.
3. Grenzen und Konsequenzen eines möglichen Einsatzes bestimmen: wann eine lesende Prüfung hilfreich ist, wann sie laufende Arbeit stört und wie Empfehlungen von tatsächlichen Projekt- oder Releaseblockern getrennt werden.
4. Danach gesondert über weiteren Einsatz, engeren Umfang, Überarbeitung oder Verzicht entscheiden. Ein positiver Nutzen und eine Einsatzfreigabe werden nicht vorausgesetzt.

Dieser Dokumentationsmerge erledigt ausschließlich die Archivierung. Die vier Punkte sind offene Folgearbeit, kein gestarteter Audit und keine bereits beschlossene Methodikänderung.
