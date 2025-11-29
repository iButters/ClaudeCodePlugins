---
name: plugin-generator
description: Creates complete Claude Code plugins from natural language descriptions
  and validates them through specialized review agents. Use this skill when the user
  (1) wants to create a new plugin or skill, (2) describes a plugin idea and needs
  help with implementation, (3) wants to have existing plugin files quality-checked,
  (4) wants feedback on instruction markdown files, (5) wants to understand quality
  criteria for good LLM instructions.
---

# Plugin-Generator

Erstellt qualitativ hochwertige Claude Code Plugins und validiert sie durch ein Multi-Agenten-Review-System.

## Workflow

1. **Anforderungsanalyse**: Extrahiere Kernfunktionalität, Trigger-Szenarien und benötigte Ressourcen aus der Nutzerbeschreibung

2. **Strukturplanung**: Bestimme die erforderlichen Dateitypen basierend auf dem Anforderungsprofil:
   - SKILL.md (immer erforderlich)
   - Commands (bei benutzerauslösbaren Aktionen)
   - Agents (bei spezialisierten Sub-Tasks)
   - References (bei umfangreicher Dokumentation)
   - Templates (bei wiederverwendbaren Vorlagen)

3. **Generierung**: Erstelle alle Dateien unter Einhaltung der Qualitätskriterien aus `references/quality-criteria.md`

4. **Review-Durchführung**: Führe die 4 Spezialisten-Reviews parallel aus:
   - Struktur-Review mit `agents/structure-agent.md`
   - Inhalt-Review mit `agents/content-agent.md`
   - Klarheits-Review mit `agents/clarity-agent.md`
   - Konsistenz-Review mit `agents/consistency-agent.md`

5. **Synthese**: Aggregiere die Review-Ergebnisse mit `agents/synthesis-agent.md` zu einem priorisierten Report

6. **Iteration**: Überarbeite das Plugin basierend auf dem Review-Feedback

## Entscheidungsbaum für Dateitypen

Bestimme die erforderlichen Dateien anhand dieser Fragen:

**Commands erstellen?**
- Gibt es benutzerauslösbare Aktionen mit Parametern? → Ja
- Soll der Nutzer Slash-Commands verwenden können? → Ja

**Agents erstellen?**
- Gibt es spezialisierte Sub-Tasks mit eigener Logik? → Ja
- Benötigt der Skill verschiedene Perspektiven oder Reviews? → Ja

**References erstellen?**
- Gibt es umfangreiche Dokumentation, die den Kontext sprengt? → Ja
- Existieren Spezifikationen oder Standards, die referenziert werden? → Ja

**Templates erstellen?**
- Gibt es wiederverwendbare Strukturen, die kopiert werden sollen? → Ja
- Soll der Output ein bestimmtes Format haben? → Ja

## Qualitätskriterien-Kurzreferenz

Jede generierte Datei erfüllt diese Mindestanforderungen:

**Frontmatter (SKILL.md):**
- `name`: 3-30 Zeichen, lowercase, Bindestriche erlaubt
- `description`: 100-500 Zeichen, enthält mindestens 3 Trigger-Szenarien mit "(1)...(2)...(3)..."

**Struktur:**
- Genau ein H1-Header am Anfang
- Keine Header-Sprünge (H1→H3 ist ein Fehler)
- Konsistente Delimiter-Verwendung

**Inhalt:**
- Imperativ-Form für alle Anweisungen ("Analysiere", nicht "Du sollst analysieren")
- Keine vagen Qualifikatoren ("einige", "verschiedene", "etc.")
- Mindestens 1 Beispiel bei komplexen Konzepten
- Output-Format spezifiziert bei strukturiertem Output

**Vollständigkeit:**
- Workflow mit nummerierten Schritten
- Edge Cases dokumentiert
- Fehlerbehandlung bei fehleranfälligen Operationen

Für detaillierte Kriterien siehe `references/quality-criteria.md`.

## Review-Prozess

Das Review-System besteht aus 4 spezialisierten Agenten, die parallel arbeiten:

| Agent | Fokus | Output |
|-------|-------|--------|
| Struktur-Agent | Frontmatter, Header, Syntax, Referenzen | `<structure_review>` |
| Inhalt-Agent | Vollständigkeit, Spezifität, Beispiele | `<content_review>` |
| Klarheits-Agent | Ambiguitäten, Pronomen, Lesbarkeit | `<clarity_review>` |
| Konsistenz-Agent | Terminologie, Widersprüche, Cross-Datei | `<consistency_review>` |

Der Synthese-Agent aggregiert die Ergebnisse zu einem priorisierten Markdown-Report.

## Scoring-System

| Gesamtscore | Status | Aktion |
|-------------|--------|--------|
| 4.5-5.0 | ✅ Exzellent | Freigabe ohne Änderungen |
| 4.0-4.4 | ✅ Gut | Freigabe mit optionalen Verbesserungen |
| 3.5-3.9 | ⚠️ Akzeptabel | Überarbeitung empfohlen |
| 2.5-3.4 | ⚠️ Mangelhaft | Überarbeitung erforderlich |
| 0-2.4 | ❌ Unzureichend | Grundlegende Neukonzeption nötig |

Gewichtung der Kategorien:
- Struktur: 15%
- Inhalt: 35%
- Klarheit: 30%
- Konsistenz: 20%

## Beispiel: Plugin-Generierung

**Nutzeranfrage:**
"Ich brauche ein Plugin, das mir hilft, Git-Commit-Messages zu schreiben."

**Analyse:**
- Kernfunktionalität: Commit-Message-Generierung
- Trigger: Code-Änderungen beschreiben, Commit vorbereiten
- Benötigte Dateien: SKILL.md, 1 Command, 1 Reference

**Generierte Struktur:**
```
commit-helper/
├── SKILL.md
├── .claude/commands/
│   └── generate-commit.md
└── references/
    └── conventional-commits.md
```

**Generierte SKILL.md (Auszug):**
```markdown
---
name: commit-helper
description: Generiert konventionskonforme Git-Commit-Messages aus 
  Code-Änderungsbeschreibungen. Verwende diesen Skill wenn der Nutzer 
  (1) eine Commit-Message für Änderungen benötigt, (2) den Conventional 
  Commits Standard einhalten möchte, (3) Hilfe bei der Formulierung 
  von Commit-Beschreibungen braucht.
---

# Commit-Helper

Generiert strukturierte Git-Commit-Messages nach dem Conventional Commits Standard.

## Workflow

1. **Änderungs-Analyse**: Identifiziere Art der Änderung (feat, fix, docs, etc.)
2. **Scope-Bestimmung**: Bestimme den betroffenen Bereich des Codes
3. **Message-Generierung**: Erstelle Commit-Message nach Conventional Commits
4. **Validierung**: Prüfe Message auf Formatkonformität
```

## Referenzen

- **Qualitätskriterien**: Siehe `references/quality-criteria.md` für alle Bewertungskriterien
- **Dateityp-Spezifikationen**: Siehe `references/markdown-types.md` für Anforderungen pro Dateityp
- **Beispiele**: Siehe `references/examples/` für hochwertige Beispiel-Dateien

## Templates

Verwende diese Templates als Ausgangspunkt:

- **SKILL.md**: `templates/skill-template.md`
- **Commands**: `templates/command-template.md`
- **Agents**: `templates/agent-template.md`

## Edge Cases

**Sehr einfache Plugins (nur SKILL.md):**
Generiere nur SKILL.md mit integriertem Workflow. Verzichte auf Commands, Agents und References, wenn der Skill in unter 100 Zeilen vollständig beschrieben werden kann.

**Komplexe Plugins (>5 Dateien):**
Aktiviere SubAgents für den Inhalt-Review. Erstelle einen separaten SubAgent pro Dateityp, um die Review-Qualität zu erhöhen.

**Review-only-Modus:**
Falls der Nutzer nur ein Review bestehender Dateien wünscht, überspringe die Generierungs-Schritte und starte direkt mit dem Review-Prozess.
