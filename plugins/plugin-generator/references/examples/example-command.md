# Beispiel: Hochwertiger Command

Dieses Dokument zeigt eine Command-Datei, die alle Qualitätskriterien erfüllt.

## Das Beispiel

Dateiname: `.claude/commands/review-plugin.md`

```markdown
# Plugin-Qualitätsreview durchführen

Führt ein vollständiges Qualitätsreview aller Markdown-Dateien eines Plugins durch und erstellt einen priorisierten Report mit konkreten Verbesserungsvorschlägen.

## Parameter

- `$PLUGIN_PATH`: Pfad zum Plugin-Verzeichnis. Pflicht.
- `$FOCUS`: Fokus-Bereich für tiefere Analyse. Optional, Default: `all`. 
  Erlaubte Werte: `all`, `structure`, `content`, `clarity`, `consistency`.
- `$OUTPUT_FORMAT`: Format des Reports. Optional, Default: `markdown`. 
  Erlaubte Werte: `markdown`, `json`.

## Verhalten

1. **Dateierkennung**: Scanne `$PLUGIN_PATH` rekursiv nach `.md`-Dateien
2. **Kategorisierung**: Ordne jede Datei einem Typ zu (SKILL, Command, Agent, Reference, Template)
3. **Parallel-Review**: Führe die vier Spezialisten-Reviews gleichzeitig aus:
   - Struktur-Review: Frontmatter, Hierarchie, Syntax
   - Inhalt-Review: Vollständigkeit, Spezifität, Beispiele
   - Klarheits-Review: Ambiguitäten, Lesbarkeit
   - Konsistenz-Review: Widersprüche, Terminologie
4. **Synthese**: Aggregiere Ergebnisse, löse Konflikte, priorisiere Issues
5. **Report-Generierung**: Erstelle strukturierten Report im gewählten Format

## Beispiele

**Beispiel 1: Standard-Review**

Input:
```
/review-plugin ./my-plugin
```

Output:
```markdown
# Plugin Quality Report: my-plugin

## Gesamtbewertung

| Kategorie | Score | Status |
|-----------|-------|--------|
| Struktur | 4.5/5 | ✅ |
| Inhalt | 3.8/5 | ⚠️ |
| Klarheit | 4.2/5 | ✅ |
| Konsistenz | 4.0/5 | ✅ |
| **Gesamt** | **4.1/5** | **Gut** |

## Kritische Issues (0)

Keine kritischen Issues gefunden.

## Wichtige Issues (2)

1. **SKILL.md, Zeile 23**: Vager Qualifikator "verschiedene Formate"
   - Empfehlung: Ersetze durch konkrete Liste: "JSON, YAML und XML"

2. **agents/reviewer.md, Zeile 45**: Fehlendes Output-Format
   - Empfehlung: Füge Output-Format-Sektion hinzu
```

**Beispiel 2: Fokussierter Review**

Input:
```
/review-plugin ./my-plugin --focus=content
```

Output:
Detaillierter Inhalt-Review mit tieferer Analyse der Vollständigkeit, Spezifität und Beispiel-Qualität.

**Beispiel 3: JSON-Output**

Input:
```
/review-plugin ./my-plugin --output-format=json
```

Output:
```json
{
  "plugin": "my-plugin",
  "overall_score": 4.1,
  "categories": {
    "structure": {"score": 4.5, "status": "pass"},
    "content": {"score": 3.8, "status": "warning"},
    "clarity": {"score": 4.2, "status": "pass"},
    "consistency": {"score": 4.0, "status": "pass"}
  },
  "issues": [...]
}
```

## Fehlerbehandlung

| Fehler | Verhalten |
|--------|-----------|
| Plugin-Pfad existiert nicht | Fehlermeldung mit korrektem Pfad-Vorschlag |
| Keine .md-Dateien gefunden | Warnung, leerer Report |
| Ungültiger FOCUS-Wert | Fehlermeldung mit erlaubten Werten |
```

## Analyse: Warum dieses Beispiel die Kriterien erfüllt

### Pflicht-Elemente

| Element | Erfüllung |
|---------|-----------|
| Zweck-Beschreibung im ersten Absatz | ✓ Klar definiert |
| Parameter mit Typ, Pflicht/Optional, Default | ✓ Alle 3 Parameter dokumentiert |
| Verhaltens-Beschreibung | ✓ 5 nummerierte Schritte |
| Mindestens 1 Beispiel | ✓ 3 Beispiele |

### Qualitätsindikatoren

| Kriterium | Erfüllung |
|-----------|-----------|
| Dateiname entspricht Command | ✓ `review-plugin.md` |
| Beispiele zeigen Input UND Output | ✓ Vollständige Ein-/Ausgaben |
| Verschiedene Szenarien abgedeckt | ✓ Standard, Fokussiert, JSON |
| Fehlerbehandlung dokumentiert | ✓ Eigene Sektion |

### Inhaltliche Qualität

| Kriterium | Erfüllung |
|-----------|-----------|
| Imperativ in Beschreibung | ✓ "Führt... durch" |
| Konkrete Parameter-Werte | ✓ Erlaubte Werte explizit |
| Workflow nachvollziehbar | ✓ Klare Schrittfolge |
| Output-Format spezifiziert | ✓ Markdown und JSON gezeigt |
