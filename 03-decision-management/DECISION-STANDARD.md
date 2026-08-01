# Decision Management Standard

Version: 1.0-alpha  
Gültig ab: 2026-08-01

## Ziel

Bereits getroffene Entscheidungen müssen auffindbar, eindeutig, wirksam und änderbar sein, ohne dass frühere Stände verloren gehen.

## Entscheidungs-ID

Jede wesentliche Entscheidung erhält eine eindeutige ID:

`<PROJEKT>-DEC-<laufende Nummer>`

Beispiele:

- `AVV-DEC-001`
- `VILLA-DEC-001`
- `POS-DEC-001`

## Pflichtfelder

Jeder Entscheidungseintrag enthält:

- ID
- Titel
- Datum
- Status
- Kontext / Problem
- betrachtete Optionen
- Entscheidung
- Begründung
- Auswirkungen
- betroffene Anforderungen und Artefakte
- Verantwortlicher Entscheider
- Reversibilität
- Prüf- oder Wiedervorlagedatum, falls erforderlich
- ersetzt / ersetzt durch

## Statuswerte

- `PROPOSED` – vorgeschlagen, noch nicht freigegeben
- `ACCEPTED` – freigegeben und verbindlich
- `SUPERSEDED` – durch eine neuere Entscheidung ersetzt
- `REJECTED` – verworfen
- `DEPRECATED` – soll nicht mehr verwendet werden, bleibt historisch erhalten

## Verbindlichkeitsregel

Nur Entscheidungen mit Status `ACCEPTED` sind verbindlich. Sie dürfen weder im Chat noch bei einer neuen Umsetzung still verändert werden.

## Prüfung vor neuer Product-Owner-Frage

Vor jeder Entscheidungsfrage muss geprüft werden:

1. Ist das Thema bereits entschieden?
2. Deckt eine bestehende Leitentscheidung den Fall ab?
3. Entsteht tatsächlich eine neue Auswirkung oder ein Widerspruch?
4. Kann die Frage durch bestehende Akzeptanzkriterien beantwortet werden?

Nur wenn danach eine echte Lücke verbleibt, wird der Product Owner gefragt.

## Änderung einer Entscheidung

Eine akzeptierte Entscheidung wird nicht überschrieben. Stattdessen wird:

1. eine neue Decision-ID angelegt,
2. die alte Entscheidung auf `SUPERSEDED` gesetzt,
3. wechselseitig auf alte und neue Entscheidung verwiesen,
4. die Auswirkung auf Anforderungen, Backlog, Architektur, Tests und Dokumente geprüft.

## Entscheidungsklassen

### Klasse A – Product Owner erforderlich

- Vision, Zielgruppen und Produktumfang
- rechtlich, finanziell oder reputativ wesentliche Entscheidungen
- Branding, Name und Geschäftsmodell
- irreversible oder schwer reversible Änderungen
- wesentliche Termin-, Budget- oder Qualitätskonflikte

### Klasse B – innerhalb freigegebener Leitplanken delegierbar

- technische Umsetzungsmuster
- Dokumentstruktur
- Testmethoden
- interne Arbeitsreihenfolge
- redaktionelle Detailgestaltung ohne Änderung der Produktwirkung

### Klasse C – operativ

- Formatkorrekturen
- Ablageorte gemäß Standard
- eindeutige Fehlerkorrekturen ohne fachliche Änderung

## Decision Check

Vor jedem Lieferstand wird bestätigt:

- [ ] relevante ACCEPTED-Entscheidungen geprüft
- [ ] keine Entscheidung still überschrieben
- [ ] neue Entscheidungen dokumentiert
- [ ] ersetzte Entscheidungen korrekt verknüpft
- [ ] Auswirkungen in allen betroffenen Artefakten berücksichtigt
