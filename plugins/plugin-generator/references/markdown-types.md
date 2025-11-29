# Markdown-Dateitypen für Claude Code Plugins

Dieses Dokument spezifiziert die Anforderungen für jeden Markdown-Dateityp in Claude Code Plugins.

## Übersicht der Dateitypen

| Dateityp | Pfad | Zweck |
|----------|------|-------|
| SKILL.md | `[skill-name]/SKILL.md` | Haupt-Instruktionen und Workflow |
| Command | `.claude/commands/[name].md` | Slash-Command-Definition |
| Agent | `agents/[name].md` | Agent-Definition mit Rolle und Fähigkeiten |
| Reference | `references/[name].md` | Dokumentation und Nachschlagewerk |
| Template | `templates/[name].md` | Wiederverwendbare Vorlagen |

## SKILL.md

### Pflicht-Elemente

```yaml
---
name: [skill-name]
description: [Umfassende Beschreibung mit allen Trigger-Szenarien]
---
```

```markdown
# [Skill-Titel]

[Ein-Satz-Zusammenfassung des Skill-Zwecks]

## Workflow

1. [Schritt 1]
2. [Schritt 2]
...

## [Weitere Sektionen nach Bedarf]
```

### Qualitätsindikatoren

| Kriterium | Minimum | Optimal |
|-----------|---------|---------|
| description-Länge | 100 Zeichen | 200-400 Zeichen |
| Workflow-Schritte | 3 | 5-7 |
| Referenzen zu Bundled Resources | Alle vorhandenen | Alle vorhandenen |
| Beispiele | 1 pro komplexem Konzept | 2-3 pro Konzept |

### Struktur-Template

```markdown
---
name: [lowercase-mit-bindestrichen]
description: [Was der Skill tut]. Verwende diesen Skill wenn der Nutzer 
  (1) [Trigger 1], (2) [Trigger 2], (3) [Trigger 3].
---

# [Skill-Name als Titel]

[Kurze Zweckbeschreibung in 1-2 Sätzen.]

## Workflow

1. **[Schritt-Name]**: [Beschreibung]
2. **[Schritt-Name]**: [Beschreibung]
3. **[Schritt-Name]**: [Beschreibung]

## [Kernkonzept-Sektion]

[Erklärung des wichtigsten Konzepts]

## Referenzen

- **[Referenz-Name]**: Siehe `references/[datei].md` für [Zweck]
```

## Command

### Pflicht-Elemente

Jede Command-Datei definiert einen Slash-Command, den der Nutzer aufrufen kann.

```markdown
# [Command-Beschreibung]

[Was der Command tut und wann er verwendet wird]

## Parameter

- `$PARAM1`: [Beschreibung] (Pflicht/Optional, Default: [Wert])

## Verhalten

[Detaillierte Beschreibung des Command-Verhaltens]

## Beispiel

Input: `/[command-name] [beispiel-parameter]`
Output: [Erwartetes Ergebnis]
```

### Qualitätsindikatoren

| Kriterium | Anforderung |
|-----------|-------------|
| Dateiname | Entspricht Command-Name ohne Slash |
| Zweck-Beschreibung | Erste Zeile nach Header erklärt Zweck |
| Parameter-Dokumentation | Jeder Parameter mit Typ, Pflicht/Optional, Default |
| Beispiel | Mindestens 1 vollständiges Input/Output-Beispiel |

### Struktur-Template

```markdown
# [Kurze Beschreibung des Commands]

Dieser Command [Zweck in einem Satz].

## Parameter

- `$PARAM1`: [Beschreibung]. Pflicht.
- `$PARAM2`: [Beschreibung]. Optional, Default: `[wert]`.

## Verhalten

1. [Schritt 1]
2. [Schritt 2]
3. [Schritt 3]

## Beispiele

**Beispiel 1: [Szenario-Name]**

Input:
```
/[command] [parameter-werte]
```

Output:
[Beschreibung oder Beispiel des Outputs]
```

## Agent

### Pflicht-Elemente

Agent-Dateien definieren spezialisierte Agenten mit klarer Rolle und Fähigkeiten.

```markdown
# [Agent-Name]

[Rollen-Definition in 1-2 Sätzen]

## Fähigkeiten

- [Fähigkeit 1]
- [Fähigkeit 2]

## Constraints

- [Einschränkung 1]
- [Einschränkung 2]

## Workflow

1. [Schritt 1]
2. [Schritt 2]

## Output-Format

[Spezifikation des erwarteten Outputs]
```

### Qualitätsindikatoren

| Kriterium | Anforderung |
|-----------|-------------|
| Rollen-Definition | Klar abgegrenzt von anderen Agents |
| Fähigkeiten | Konkret, messbar, nicht vage |
| Constraints | Verhindern Scope-Creep |
| Output-Format | Strukturiert, maschinenlesbar |

### Struktur-Template

```markdown
# [Agent-Name]

Du bist [Rolle]. Deine Aufgabe ist [Kernaufgabe].

## Fähigkeiten

- [Konkrete Fähigkeit 1 mit messbarem Outcome]
- [Konkrete Fähigkeit 2 mit messbarem Outcome]

## Constraints

- Beschränke dich auf [Scope]
- Delegiere [Out-of-Scope-Tasks] an [anderen Agent/Nutzer]

## Workflow

1. **[Phase 1]**: [Beschreibung]
2. **[Phase 2]**: [Beschreibung]
3. **[Phase 3]**: [Beschreibung]

## Output-Format

<[output_tag]>
  <[element]>[Beschreibung]</[element]>
</[output_tag]>
```

## Reference

### Pflicht-Elemente

Reference-Dateien dienen als Nachschlagewerk und werden bei Bedarf geladen.

```markdown
# [Referenz-Titel]

[Kurze Beschreibung des Inhalts und wann diese Referenz zu konsultieren ist]

## [Hauptsektion 1]

[Inhalt]

## [Hauptsektion 2]

[Inhalt]
```

### Qualitätsindikatoren

| Kriterium | Anforderung |
|-----------|-------------|
| Einleitung | Erklärt wann/warum diese Referenz relevant ist |
| Struktur | Logisch gegliedert, schnell durchsuchbar |
| Tiefe | Detaillierter als SKILL.md |
| Redundanz | Keine Duplikation mit SKILL.md |

### Struktur-Template

```markdown
# [Referenz-Titel]

Diese Referenz dokumentiert [Thema]. Konsultiere sie wenn [Anwendungsfälle].

## [Hauptkonzept 1]

[Detaillierte Erklärung]

### [Unterkonzept 1.1]

[Details]

## [Hauptkonzept 2]

[Detaillierte Erklärung]

## Schnellreferenz

| [Spalte 1] | [Spalte 2] | [Spalte 3] |
|------------|------------|------------|
| [Wert] | [Wert] | [Wert] |
```

## Template

### Pflicht-Elemente

Template-Dateien sind Vorlagen, die kopiert und angepasst werden.

```markdown
# [Template-Name]

[Beschreibung wofür dieses Template verwendet wird]

## Template

[Das eigentliche Template mit Platzhaltern in eckigen Klammern]

## Platzhalter

- `[PLATZHALTER_1]`: [Beschreibung, was hier eingesetzt wird]
- `[PLATZHALTER_2]`: [Beschreibung, was hier eingesetzt wird]

## Anpassungshinweise

[Hinweise zur korrekten Verwendung des Templates]
```

### Qualitätsindikatoren

| Kriterium | Anforderung |
|-----------|-------------|
| Platzhalter-Format | Konsistent, klar erkennbar `[UPPERCASE_MIT_UNTERSTRICHEN]` |
| Dokumentation | Jeder Platzhalter erklärt |
| Vollständigkeit | Template ist ohne Änderungen syntaktisch valide |
| Anpassungshinweise | Erklären optionale vs. pflicht Anpassungen |

### Struktur-Template

```markdown
# [Template-Name]

Verwende dieses Template für [Anwendungsfall].

---

## Template

```[sprache]
[Template-Inhalt mit [PLATZHALTERN]]
```

---

## Platzhalter

| Platzhalter | Beschreibung | Beispiel |
|-------------|--------------|----------|
| `[PLATZHALTER_1]` | [Was hier eingesetzt wird] | `beispiel-wert` |

## Anpassungshinweise

1. [Hinweis 1]
2. [Hinweis 2]
```

## Cross-Dateityp-Konsistenz

### Namenskonventionen

| Element | Konvention | Beispiel |
|---------|------------|----------|
| Skill-Name | lowercase-mit-bindestrichen | `api-docs-generator` |
| Command-Dateiname | lowercase-mit-bindestrichen | `generate-docs.md` |
| Agent-Dateiname | lowercase-mit-bindestrichen | `structure-agent.md` |
| Platzhalter | UPPERCASE_MIT_UNTERSTRICHEN | `[API_ENDPOINT]` |

### Referenzierung zwischen Dateien

Verwende relative Pfade für Verweise:

```markdown
Siehe `references/quality-criteria.md` für Details.
Führe `scripts/validate.py` aus.
Verwende das Template in `templates/skill-template.md`.
```

### Terminologie-Konsistenz

Definiere zentrale Begriffe einmalig und verwende sie konsistent:

| Konzept | Bevorzugter Begriff | Vermeide |
|---------|---------------------|----------|
| Markdown-Instruktionsdatei | "Instruktions-Datei" | "Prompt-Datei", "MD-File" |
| Qualitätsprüfung | "Review" | "Check", "Validierung", "Audit" |
| Bewertungszahl | "Score" | "Note", "Wert", "Rating" |
