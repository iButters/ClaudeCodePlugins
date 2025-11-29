# Agent Template

Verwende dieses Template für neue Agent-Definitionen.

---

## Template

```markdown
# [AGENT_NAME]

Du bist [ROLLE]. Deine Aufgabe ist [KERNAUFGABE].

## Fähigkeiten

- [FÄHIGKEIT_1]
- [FÄHIGKEIT_2]
- [FÄHIGKEIT_3]

## Constraints

- Beschränke dich auf [SCOPE]
- Delegiere [OUT_OF_SCOPE] an [DELEGATIONSZIEL]
- [WEITERE_EINSCHRÄNKUNG]

## Workflow

1. **[PHASE_1]**: [PHASE_1_BESCHREIBUNG]
2. **[PHASE_2]**: [PHASE_2_BESCHREIBUNG]
3. **[PHASE_3]**: [PHASE_3_BESCHREIBUNG]
4. **[PHASE_4]**: [PHASE_4_BESCHREIBUNG]

## Bewertungskriterien

| Kriterium | Score 5 | Score 3 | Score 1 |
|-----------|---------|---------|---------|
| [KRITERIUM_1] | [EXZELLENT] | [AKZEPTABEL] | [UNZUREICHEND] |
| [KRITERIUM_2] | [EXZELLENT] | [AKZEPTABEL] | [UNZUREICHEND] |

## Output-Format

<[OUTPUT_TAG]>
  <file name="[DATEINAME]">
    <score category="[KATEGORIE]">[SCORE]</score>
    <issues>
      <issue severity="critical|major|minor" line="[ZEILE]">
        [BESCHREIBUNG]
      </issue>
    </issues>
    <recommendations>
      [EMPFEHLUNGEN]
    </recommendations>
  </file>
</[OUTPUT_TAG]>
```

---

## Platzhalter

| Platzhalter | Beschreibung | Beispiel |
|-------------|--------------|----------|
| `[AGENT_NAME]` | Beschreibender Name des Agents | `Struktur-Review-Agent` |
| `[ROLLE]` | Expertise-Beschreibung | `Experte für Dokumentenstruktur` |
| `[KERNAUFGABE]` | Hauptaufgabe in einem Satz | `die strukturelle Korrektheit von MD-Dateien zu prüfen` |
| `[FÄHIGKEIT_X]` | Konkrete, messbare Fähigkeit | `Frontmatter-Validierung nach YAML-Standard` |
| `[SCOPE]` | Erlaubter Arbeitsbereich | `strukturelle Aspekte` |
| `[OUT_OF_SCOPE]` | Was der Agent nicht tun soll | `inhaltliche Bewertungen` |
| `[DELEGATIONSZIEL]` | Wer stattdessen zuständig ist | `den Inhalt-Agent` |
| `[PHASE_X]` | Name einer Workflow-Phase | `Frontmatter-Validierung` |
| `[KRITERIUM_X]` | Bewertungskriterium | `Header-Hierarchie` |
| `[OUTPUT_TAG]` | XML-Tag für Output | `structure_review` |

## Anpassungshinweise

1. **Rollen-Definition**: Formuliere die Rolle so, dass sie klar von anderen Agents abgegrenzt ist. Vermeide Überschneidungen.

2. **Fähigkeiten**: Liste 3-5 konkrete Fähigkeiten. Jede Fähigkeit sollte messbar oder überprüfbar sein.

3. **Constraints**: Definiere klare Grenzen, um Scope-Creep zu verhindern. Benenne explizit, was delegiert wird.

4. **Workflow**: Strukturiere den Workflow in 3-5 Phasen. Jede Phase sollte ein klares Ergebnis produzieren.

5. **Bewertungskriterien**: Definiere 2-4 Kriterien mit klaren Beschreibungen für verschiedene Score-Levels.

6. **Output-Format**: Verwende XML für strukturierte Outputs. Passe die Struktur an die spezifischen Anforderungen des Agents an.

## Wann SubAgents einsetzen

Erstelle SubAgents nur wenn:
- Der Agent mehr als 5 verschiedene Wissensdomänen abdecken muss
- Natürliche Domänen-Grenzen existieren (z.B. pro Dateityp)
- Maker-Checker-Validierung erforderlich ist

SubAgents erben das Output-Format des Haupt-Agents.

## Checkliste vor Fertigstellung

- [ ] Rolle klar von anderen Agents abgegrenzt
- [ ] Fähigkeiten konkret und messbar
- [ ] Constraints verhindern Scope-Creep
- [ ] Workflow-Phasen sind logisch und vollständig
- [ ] Bewertungskriterien mit klaren Score-Definitionen
- [ ] Output-Format ist strukturiert und maschinenlesbar
