#!/usr/bin/env python3
"""
Prompt Refiner Hook für Claude Code
Verfeinert User-Prompts mit Claude Haiku für bessere Kontextualität.
Ignoriert reine Slash-Commands ohne zusätzlichen Text.
"""

import json
import os
import re
import subprocess
import sys

# ============================================================================
# KONFIGURATION
# ============================================================================

MODEL = "claude-haiku-4-5-20251001"
MAX_TOKENS = 1024

SYSTEM_PROMPT = """Du bist ein Prompt-Refiner für einen Coding-Agenten (Claude Code).

Deine Aufgabe ist es, den User-Prompt zu analysieren und zusätzlichen Kontext bereitzustellen, der dem Haupt-Agenten hilft, die Aufgabe besser zu verstehen.

Regeln:
1. Mache implizite Annahmen explizit
2. Identifiziere relevante technische Details aus dem Projekt-Kontext
3. Schlage vor, welche Dateien/Bereiche relevant sein könnten
4. Halte dich KURZ und PRÄGNANT (max 5-8 Zeilen)
5. Schreibe in der Sprache des Users
6. Füge KEINE neuen Aufgaben hinzu - nur Klarstellung der bestehenden
7. Wenn der Prompt bereits klar und vollständig ist, gib nur "SKIP" aus

Antworte NUR mit dem zusätzlichen Kontext, keine Erklärungen oder Meta-Kommentare."""

# ============================================================================
# HILFSFUNKTIONEN
# ============================================================================

def is_slash_command_only(prompt: str) -> bool:
    """
    Prüft ob der Prompt ein reiner Slash-Command ohne substantiellen Text ist.
    
    Beispiele die ignoriert werden:
    - /help
    - /clear
    - /model
    - /init
    
    Beispiele die NICHT ignoriert werden:
    - /test src/utils.py
    - /review Prüfe die Authentifizierung
    - Normaler Text ohne Slash
    """
    prompt = prompt.strip()
    
    # Leerer Prompt
    if not prompt:
        return True
    
    # Kein Slash-Command
    if not prompt.startswith('/'):
        return False
    
    # Slash-Command mit Argumenten?
    # Pattern: /command [optional whitespace] [argumente]
    parts = prompt.split(maxsplit=1)
    
    # Nur der Command ohne Argumente
    if len(parts) == 1:
        return True
    
    # Command mit Argumenten - prüfe ob Argumente substantiell sind
    args = parts[1].strip()
    
    # Wenn Argumente nur aus Flags bestehen (z.B. --help, -v), ignorieren
    if re.match(r'^(-{1,2}\w+\s*)+$', args):
        return True
    
    # Hat substantielle Argumente
    return False


def get_project_context() -> str:
    """Sammelt Projekt-Kontext für besseres Refinement."""
    context_parts = []
    
    project_dir = os.environ.get('CLAUDE_PROJECT_DIR', os.getcwd())
    
    # Git Branch
    try:
        result = subprocess.run(
            ['git', 'branch', '--show-current'],
            capture_output=True, text=True, timeout=5,
            cwd=project_dir
        )
        if result.returncode == 0 and result.stdout.strip():
            context_parts.append(f"Git-Branch: {result.stdout.strip()}")
    except Exception:
        pass
    
    # Kürzlich geänderte Dateien
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', 'HEAD~3', '--', '.'],
            capture_output=True, text=True, timeout=5,
            cwd=project_dir
        )
        if result.returncode == 0 and result.stdout.strip():
            files = result.stdout.strip().split('\n')[:5]
            context_parts.append(f"Kürzlich geändert: {', '.join(files)}")
    except Exception:
        pass
    
    # Projekt-Typ erkennen
    project_markers = {
        'package.json': 'Node.js/JavaScript',
        'pyproject.toml': 'Python',
        'Cargo.toml': 'Rust',
        'go.mod': 'Go',
        'pom.xml': 'Java/Maven',
        'build.gradle': 'Java/Gradle',
        'composer.json': 'PHP',
        'Gemfile': 'Ruby',
    }
    
    for marker, tech in project_markers.items():
        if os.path.exists(os.path.join(project_dir, marker)):
            context_parts.append(f"Projekt-Typ: {tech}")
            break
    
    return '\n'.join(context_parts) if context_parts else "Kein spezifischer Projekt-Kontext verfügbar"


def call_haiku(prompt: str, context: str) -> str:
    """Ruft Claude Haiku auf um den Prompt zu verfeinern."""
    try:
        import anthropic
    except ImportError:
        # Fallback wenn anthropic nicht installiert
        return ""
    
    try:
        client = anthropic.Anthropic()
        
        response = client.messages.create(
            model=MODEL,
            max_tokens=MAX_TOKENS,
            system=SYSTEM_PROMPT,
            messages=[{
                "role": "user",
                "content": f"""PROJEKT-KONTEXT:
{context}

USER-PROMPT:
{prompt}

Gib zusätzlichen Kontext für den Coding-Agenten."""
            }]
        )
        
        result = response.content[0].text.strip()
        
        # Wenn Haiku sagt der Prompt ist bereits klar
        if result.upper() == "SKIP" or len(result) < 10:
            return ""
        
        return result
        
    except Exception as e:
        # Bei Fehlern still scheitern - der Original-Prompt geht trotzdem durch
        sys.stderr.write(f"Haiku-Aufruf fehlgeschlagen: {e}\n")
        return ""


# ============================================================================
# HAUPTLOGIK
# ============================================================================

def main():
    # Hook-Input von stdin lesen
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        # Kein valides JSON - nichts tun
        sys.exit(0)
    
    prompt = input_data.get("prompt", "")
    
    # Prüfen ob es ein reiner Slash-Command ist
    if is_slash_command_only(prompt):
        # Nichts ausgeben, nichts tun
        sys.exit(0)
    
    # Projekt-Kontext sammeln
    context = get_project_context()
    
    # Haiku aufrufen für Refinement
    refined_context = call_haiku(prompt, context)
    
    # Wenn kein Refinement nötig/möglich
    if not refined_context:
        sys.exit(0)
    
    # Zusätzlichen Kontext ausgeben (wird dem Prompt vorangestellt)
    output = f"""[PROMPT-KONTEXT von Haiku]
{refined_context}
[/PROMPT-KONTEXT]"""
    
    print(output)
    sys.exit(0)


if __name__ == "__main__":
    main()
