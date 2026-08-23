# Installation und Verifikation

## Grundsatz

Claude lokal, Claude Cloud und ChatGPT sind drei getrennte Installationsnachweise. Ein Paket an einer Stelle aktiviert es nicht automatisch überall.

## Pakete bauen

Vom Repository-Root:

```bash
python 09-capability-registry/scripts/build_skill_packages.py --target all
```

Ausgabe:

- `09-capability-registry/dist/claude/<skill>/`
- `09-capability-registry/dist/chatgpt/<skill>/`

ZIP-Dateien nur für einen ausdrücklich benötigten Upload erzeugen:

```bash
python 09-capability-registry/scripts/build_skill_packages.py --target claude --zip
```

## Claude lokal

1. Claude-Paket bauen.
2. Skillordner nach `~/.claude/skills/<skill>/` kopieren; unter Windows entspricht dies normalerweise `%USERPROFILE%\.claude\skills\<skill>\`.
3. Neue lokale Claude-Code-Sitzung öffnen.
4. Skillliste prüfen und beide Skills explizit testen.
5. PPAO muss nur explizit aufrufbar sein; die Claude-Fassung enthält `disable-model-invocation: true`.

## Claude Cloud

1. Claude-ZIP ausdrücklich bauen.
2. Jeden Skill getrennt in der claude.ai-Skillverwaltung hochladen.
3. Neue Cloud-Sitzung starten und Verfügbarkeit prüfen.
4. Persistenz in einer weiteren neuen Sitzung bestätigen.
5. Erst danach den Manifeststatus auf `installed-verified` setzen.

Der Upload ist eine kontoabhängige Benutzeraktion. Eine Installation in einem kurzlebigen Remote-Container gilt nicht als Cloud-Persistenznachweis.

## ChatGPT

Die beiden Pakete wurden am 23.08.2026 als persönliche Skills installiert und nach der Speicherung verifiziert. Bei einer Neuinstallation die ChatGPT-Fassung aus `dist/chatgpt/` verwenden und anschließend die Skillverwaltung aktualisieren.

## Funktionstests

### PPAO Candidate

Aufruf: `PPAO: Prüfe dieses Projekt zunächst ausschließlich lesend.`

Erwartet:

- Kennzeichnung `Candidate – nicht final`;
- Rolle Auditor/Orchestrator/Integrator;
- Bestandsaufnahme mit Belegen vor Empfehlungen;
- keine operative Änderung ohne Freigabe;
- keine Superagenten- oder automatische Implementierungslogik.

### Token Optimization

Aufruf: `Prüfe diesen Workflow auf Token- und Kontextverschwendung, ohne die Qualität zu reduzieren.`

Erwartet:

- Qualitätsgrenze zuerst;
- messbare statt erfundener Einsparwerte;
- selektives Retrieval und deterministische Prüfungen;
- keine veralteten `contextWindow`- oder `context: fork`-Empfehlungen;
- vollständige Evidenz, Tests und Liefergegenstände.

## Statusaktualisierung

Nach jeder Installation Datum, Oberfläche, Version und Verifikationsnachweis in `capability-manifest.json` ergänzen. Nie mehrere Oberflächen aus einem einzigen Test ableiten.
