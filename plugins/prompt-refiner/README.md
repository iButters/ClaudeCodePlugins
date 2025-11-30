# Prompt Refiner Plugin für Claude Code

Dieses Plugin verfeinert automatisch User-Prompts mit Claude Haiku, bevor sie an den Haupt-Agenten weitergeleitet werden.

## Features

- **Automatisches Prompt-Refinement**: Jeder User-Prompt wird von Haiku analysiert und mit kontextuellem Wissen angereichert
- **Slash-Command Erkennung**: Reine Slash-Commands wie `/help`, `/clear`, `/model` werden ignoriert
- **Projekt-Kontext**: Sammelt automatisch Git-Branch, kürzlich geänderte Dateien und Projekt-Typ
- **Minimale Latenz**: Haiku antwortet in ~200-500ms
- **Fail-Safe**: Bei Fehlern geht der Original-Prompt unverändert durch

## Installation

### Option 1: Lokale Installation

```bash
# Plugin-Verzeichnis kopieren
cp -r prompt-refiner ~/.claude/plugins/

# In Claude Code installieren
/plugin install ~/.claude/plugins/prompt-refiner
```

### Option 2: Direkt aus Verzeichnis

```bash
/plugin install /pfad/zu/prompt-refiner
```

## Voraussetzungen

- Python 3.8+
- `anthropic` Python-Paket: `pip install anthropic`
- Gültiger `ANTHROPIC_API_KEY` in der Umgebung

## Konfiguration

Das Verhalten kann in `scripts/refine_prompt.py` angepasst werden:

```python
# Modell (Standard: Haiku für Geschwindigkeit)
MODEL = "claude-haiku-4-5-20251001"

# Max Tokens für Refinement-Antwort
MAX_TOKENS = 1024

# System-Prompt für den Refiner
SYSTEM_PROMPT = """..."""
```

## Wie es funktioniert

1. **UserPromptSubmit Hook** feuert bei jeder User-Eingabe
2. **Slash-Command Check**: Reine Commands werden übersprungen
3. **Kontext-Sammlung**: Git-Info, Projekt-Typ werden erfasst
4. **Haiku-Aufruf**: Prompt wird analysiert und verfeinert
5. **Kontext-Injektion**: Zusätzlicher Kontext wird dem Prompt vorangestellt

## Beispiel

**User tippt:**
```
Fix den Login Bug
```

**Haiku fügt hinzu:**
```
[PROMPT-KONTEXT von Haiku]
- Bezieht sich wahrscheinlich auf die Authentifizierung
- Relevante Dateien: src/auth/*, src/middleware/session.ts
- Prüfe Error-Handling und Token-Validierung
- Das Projekt nutzt TypeScript mit Express
[/PROMPT-KONTEXT]
```

**Sonnet/Opus arbeitet** mit dem angereicherten Kontext.

## Ignorierte Eingaben

Diese werden **nicht** verfeinert:
- `/help`
- `/clear`
- `/model`
- `/init`
- `/compact --force`
- Leere Eingaben

Diese werden verfeinert:
- `/test src/utils.py` (hat Argumente)
- `/review Prüfe die Auth` (hat Text)
- Jeder normale Text

## Deaktivieren

```bash
/plugin disable prompt-refiner
```

## Lizenz

MIT
