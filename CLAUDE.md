# Website-Aufgaben: Skill laden und nachweisen

Bei Website-Erstellung, vollständiger Überarbeitung, ausdrücklichem Aufruf von
`website-bauen` oder Fortsetzung über `WEBSITE-STATUS.md`: vor fachlicher Arbeit
`website-bauen` laden. Bei gezielten Website-Änderungen und Optimierungen nur die
passende Phase nutzen; keinen neuen Gesamtprozess starten. Reine Dependency- oder
Benefit-Datenpflege und Design außerhalb von Websites lösen den Skill nicht aus.

Vor der Arbeit Verfügbarkeit prüfen. Quelle/aufgelösten Skillpfad, Version soweit
nachweisbar und geladene Phase im Arbeitsbericht nennen. Ist der Skill nicht
verfügbar oder deaktiviert, die abhängige Website-Arbeit mit einem konkreten
Blocker anhalten; keine automatische Installation und keinen Ersatz als angeblich
geladenen Skill ausgeben. Bestehende Installation zuerst prüfen, nie duplizieren.
Bei vorhandenem Status fortsetzen; bestehende Entscheidungen und Projektregeln
beachten. Ein expliziter Status-Aufruf bleibt lesend.

Bei Übergabe an einen vorhandenen Website-/Design-Subagenten muss dessen
Konfiguration `skills: [website-bauen]` enthalten (bestehende Skills erhalten) und
seine Startanweisung dieselbe Verfügbarkeitsprüfung verlangen. Kein neuer Agent
ist durch diese Regel installiert. Erfolgreiches Vorladen benötigt einen
Laufzeitnachweis; eine YAML-Zeile allein genügt nicht.

Nachweise und offene Umgebungstests:
`09-capability-registry/WEBSITE_BAUEN_VERIFICATION.md`.
