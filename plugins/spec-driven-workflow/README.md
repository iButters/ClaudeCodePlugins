# Spec-Driven Workflow Plugin v2.2.0

Ein vollständiges Claude Code Plugin für spezifikationsgetriebene Softwareentwicklung.

## Was ist neu in v2.2?

### Git-Integration
- `--git` Flag bei `/spec-execute` für automatische Commits nach Wave-Completion
- `--git-push` Flag für Commit + Push
- Strukturierte Commit-Messages mit Task-Übersicht

### Wave Reports
- Automatische Report-Generierung nach jeder Wave
- Reports in `.specs/[project]/reports/wave-N-report.md`
- Enthält Tasks, Files, Review-Ergebnisse

### Bug Tracking mit EARS
- `/spec-bug` - Bugs mit EARS "Unwanted Behavior" Pattern melden
- `/spec-bugs` - Alle Bugs auflisten
- `/spec-bug-wave` - Bug-Fix Wave aus offenen Bugs erstellen
- Eigene `wave-bugfix-N.md` Dateien für Bug-Fixes

### Feature Management mit EARS
- `/spec-feature` - Feature Requests mit allen EARS Patterns
- `/spec-features` - Feature Backlog anzeigen
- `/spec-feature-to-tasks` - Feature in Tasks/Waves konvertieren
- Traceability zwischen Features und Tasks

## Was war neu in v2.1?

### Wave-basierte Task-Struktur
- Tasks werden in separate Wave-Dateien aufgeteilt
- `tasks/index.md` für Übersicht
- `tasks/wave-N.md` für detaillierte Tasks
- Bessere Skalierbarkeit für große Projekte (1000+ Zeilen Task-Pläne)

## Was wurde korrigiert?

### Alte Version (v1.0) - Probleme:
1. ❌ Verwendete `.skill`-Format statt Plugin-Format
2. ❌ Keine echten Slash Commands (nur Dokumentation)
3. ❌ Keine echten Subagents (nur Beschreibungen)
4. ❌ Relative Pfade funktionierten nicht

### Neue Version (v2.0) - Korrekturen:
1. ✅ Vollständiges Plugin mit `.claude-plugin/plugin.json`
2. ✅ Echte Slash Commands in `commands/`
3. ✅ Echte Subagents in `agents/` mit korrektem Format
4. ✅ Skill für Auto-Aktivierung in `skills/`
5. ✅ Modell-Konfiguration pro Aufgabentyp

## Plugin-Struktur

```
spec-driven-workflow/
├── .claude-plugin/
│   └── plugin.json              # Plugin-Manifest
├── commands/                    # Slash Commands
│   ├── spec-start.md           # /spec-start
│   ├── spec-idea.md            # /spec-idea
│   ├── spec-requirements.md    # /spec-requirements
│   ├── spec-design.md          # /spec-design
│   ├── spec-tasks.md           # /spec-tasks
│   ├── spec-execute.md         # /spec-execute [--git]
│   ├── spec-status.md          # /spec-status
│   ├── spec-review.md          # /spec-review
│   ├── spec-bug.md             # /spec-bug (NEU)
│   ├── spec-bugs.md            # /spec-bugs (NEU)
│   ├── spec-bug-wave.md        # /spec-bug-wave (NEU)
│   ├── spec-feature.md         # /spec-feature (NEU)
│   ├── spec-features.md        # /spec-features (NEU)
│   └── spec-feature-to-tasks.md # /spec-feature-to-tasks (NEU)
├── agents/                      # Subagents
│   ├── backend-executor.md     # Sonnet 4.5
│   ├── frontend-executor.md    # Sonnet 4.5
│   ├── database-executor.md    # Sonnet 4.5
│   ├── test-executor.md        # Sonnet 4.5
│   ├── docs-executor.md        # Haiku 4.5
│   ├── requirements-reviewer.md # Opus 4.5
│   ├── architecture-reviewer.md # Opus 4.5
│   ├── code-quality-reviewer.md # Opus 4.5
│   └── task-orchestrator.md    # Opus 4.5
├── skills/
│   └── spec-driven-workflow/
│       └── SKILL.md            # Auto-Aktivierung
└── assets/
    └── templates/              # Spec-Templates
        ├── idea.md
        ├── requirements.md
        ├── design.md
        ├── bug.md              # Bug-Report Template (NEU)
        ├── feature.md          # Feature-Request Template (NEU)
        ├── wave-report.md      # Wave-Report Template (NEU)
        ├── bugs-index.md       # Bug-Index Template (NEU)
        └── features-index.md   # Feature-Index Template (NEU)
```

## Modell-Zuordnung

| Aufgabe | Modell | Grund |
|---------|--------|-------|
| Planung (spec-idea, spec-design, spec-tasks) | Opus 4.5 | Tiefe Analyse |
| Review (alle *-reviewer) | Opus 4.5 | Gründliche Prüfung |
| Dokumentation (docs-executor) | Haiku 4.5 | Effizient für Text |
| Implementation (alle anderen) | Sonnet 4.5 | Ausgewogen |

Alle Modelle verwenden Extended Thinking.

## Installation

### Option 1: Manuell

1. Entpacke `spec-driven-workflow-plugin.zip`

2. Kopiere den Ordner zu deinem Claude Code Projekt:
   ```bash
   # Projekt-lokal
   cp -r spec-driven-workflow/ .claude/
   
   # ODER global
   cp -r spec-driven-workflow/ ~/.claude/
   ```

3. Struktur nach Installation:
   ```
   .claude/
   ├── commands/
   │   ├── spec-start.md
   │   └── ...
   ├── agents/
   │   ├── backend-executor.md
   │   └── ...
   └── skills/
       └── spec-driven-workflow/
           └── SKILL.md
   ```

### Option 2: Als Plugin (via Marketplace)

Falls du einen eigenen Marketplace hast:

1. Lade das ZIP in deinen Marketplace
2. In Claude Code: `/plugin install spec-driven-workflow@your-marketplace`

## Verwendung

### Workflow starten

```bash
# Mit Slash Command
/spec-start my-app

# Oder natürliche Sprache
"Ich möchte eine Todo-App bauen"
```

### Kompletter Workflow

```
1. /spec-start my-app      → Projekt initialisieren
2. /spec-idea              → Idee verfeinern
3. /spec-requirements      → EARS Requirements generieren
4. /spec-design            → Technische Architektur
5. /spec-tasks             → Implementation Tasks planen
6. /spec-execute           → Orchestrierte Ausführung
7. /spec-status            → Fortschritt prüfen
8. /spec-review [task-id]  → Manuelle Review
```

### Subagents

Die Subagents werden automatisch verwendet:

- Bei `/spec-execute` → Executors für Implementation
- Nach Tasks → Reviewers für Qualitätsprüfung
- Bei komplexer Planung → task-orchestrator

## Slash Commands

### Core Workflow
| Command | Beschreibung | Modell |
|---------|--------------|--------|
| `/spec-start [name]` | Projekt initialisieren | Sonnet |
| `/spec-idea` | Idee durch Dialog verfeinern | Opus |
| `/spec-requirements` | EARS Requirements generieren | Opus |
| `/spec-design` | Technische Architektur erstellen | Opus |
| `/spec-tasks` | Implementation Tasks planen (Wave-Dateien) | Opus |
| `/spec-execute` | Nächste pending Wave ausführen | Sonnet + Subagents |
| `/spec-execute wave 2` | Bestimmte Wave ausführen | Sonnet + Subagents |
| `/spec-execute T5` | Einzelnen Task ausführen | Sonnet + Subagents |
| `/spec-execute --git` | Wave ausführen + Commit | Sonnet + Subagents |
| `/spec-execute --git-push` | Wave ausführen + Commit + Push | Sonnet + Subagents |
| `/spec-status` | Projekt-Status anzeigen | Sonnet |
| `/spec-review T5` | Manuelles Review eines Tasks | Opus |

### Bug Tracking (NEU in v2.2)
| Command | Beschreibung | Modell |
|---------|--------------|--------|
| `/spec-bug` | Bug mit EARS Notation melden | Sonnet |
| `/spec-bugs` | Alle Bugs auflisten | Sonnet |
| `/spec-bug-wave` | Bug-Fix Wave erstellen | Sonnet |

### Feature Management (NEU in v2.2)
| Command | Beschreibung | Modell |
|---------|--------------|--------|
| `/spec-feature` | Feature mit EARS anfordern | Sonnet |
| `/spec-features` | Feature Backlog anzeigen | Sonnet |
| `/spec-feature-to-tasks` | Feature in Tasks konvertieren | Opus |

## Subagents

### Executors (Implementation)

| Agent | Typ | Modell |
|-------|-----|--------|
| backend-executor | APIs, Server, Business Logic | Sonnet 4.5 |
| frontend-executor | UI, Components, Styling | Sonnet 4.5 |
| database-executor | Schema, Migrations, Queries | Sonnet 4.5 |
| test-executor | Unit/Integration Tests | Sonnet 4.5 |
| docs-executor | README, API Docs, Comments | Haiku 4.5 |

### Reviewers (Quality)

| Agent | Prüft | Modell |
|-------|-------|--------|
| requirements-reviewer | EARS Kriterien | Opus 4.5 |
| architecture-reviewer | design.md Compliance | Opus 4.5 |
| code-quality-reviewer | Security, Performance | Opus 4.5 |

### Orchestration

| Agent | Aufgabe | Modell |
|-------|---------|--------|
| task-orchestrator | Parallele Koordination | Opus 4.5 |

## Projekt-Struktur (generiert)

```
.specs/
├── my-app/
│   ├── idea.md              # Projektkonzept
│   ├── requirements.md      # EARS Requirements
│   ├── design.md            # Technische Architektur
│   ├── tasks/               # Implementation Plan (Wave-basiert)
│   │   ├── index.md         # Übersicht & Fortschritt
│   │   ├── wave-1.md        # Foundation Tasks
│   │   ├── wave-2.md        # Core Features
│   │   ├── wave-N.md        # Weitere Waves
│   │   └── wave-bugfix-N.md # Bug-Fix Waves (NEU)
│   ├── reports/             # Wave Reports (NEU)
│   │   ├── wave-1-report.md
│   │   └── wave-N-report.md
│   ├── bugs/                # Bug Tracking (NEU)
│   │   ├── index.md
│   │   ├── BUG-001.md
│   │   └── BUG-NNN.md
│   └── features/            # Feature Backlog (NEU)
│       ├── index.md
│       ├── FEAT-001.md
│       └── FEAT-NNN.md
└── steering/
    └── project-rules.md     # Projektübergreifende Regeln
```

### Wave-basierte Tasks

Tasks werden in separate Wave-Dateien aufgeteilt:
- **index.md** - Übersicht, Fortschritt, Task-Index
- **wave-N.md** - Detaillierte Tasks pro Wave (~150-200 Zeilen)

Vorteile:
- Kleiner Context beim Ausführen (`/spec-execute wave 2` lädt nur `wave-2.md`)
- Keine Konflikte bei parallelen Updates
- Bessere Übersichtlichkeit bei großen Projekten

## EARS Notation

Requirements verwenden EARS (Easy Approach to Requirements Syntax):

| Pattern | Syntax | Verwendung |
|---------|--------|------------|
| **Event-Driven** | `WHEN [trigger] THE SYSTEM SHALL [behavior]` | User-Aktionen |
| **Unwanted Behavior** | `IF [condition] THEN THE SYSTEM SHALL [behavior]` | Bugs, Fehler |
| **State-Driven** | `WHILE [state] THE SYSTEM SHALL [behavior]` | Zustände |
| **Optional** | `WHERE [feature] THE SYSTEM SHALL [behavior]` | Feature-Flags |

### Bug Reports mit EARS (NEU)

```
Expected: WHEN [action] THE SYSTEM SHALL [correct behavior]
Actual:   IF [condition] THEN THE SYSTEM [unwanted behavior]
Fix:      WHEN [action] THE SYSTEM SHALL [corrected behavior]
```

## Beispiel

```
> /spec-start task-manager

✅ Project "task-manager" initialized!

📁 Created:
.specs/
├── task-manager/
│   ├── idea.md          ← Start here
│   ├── requirements.md
│   ├── design.md
│   └── tasks/           ← Wave-basiert
│       └── (nach /spec-tasks)
└── steering/
    └── project-rules.md

🚀 Next: /spec-idea

> /spec-tasks

✅ Task plan created for "task-manager"

📁 Created:
.specs/task-manager/tasks/
├── index.md      (overview)
├── wave-1.md     (3 tasks)
├── wave-2.md     (5 tasks)
└── wave-3.md     (2 tasks)

📊 Summary:
- Total Tasks: 10
- Waves: 3

🚀 Next: /spec-execute

> /spec-execute wave 1

🚀 Executing Wave 1: Foundation
   Tasks: T1, T2, T3 (parallel)
   ...
```

## Fehlerbehebung

### Commands werden nicht erkannt

Prüfe, dass die Dateien im richtigen Verzeichnis sind:
```bash
ls ~/.claude/commands/  # oder .claude/commands/
```

### Subagents werden nicht verwendet

Prüfe die agents/ Ordner:
```bash
ls ~/.claude/agents/  # oder .claude/agents/
```

### Skill wird nicht aktiviert

Prüfe den skills/ Ordner:
```bash
ls ~/.claude/skills/spec-driven-workflow/SKILL.md
```

## Lizenz

MIT
