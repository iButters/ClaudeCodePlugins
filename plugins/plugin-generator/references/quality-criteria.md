# Qualitätskriterien für LLM-Instruktionen

Dieses Dokument definiert die empirisch validierten Qualitätskriterien, die alle generierten Plugin-Dateien erfüllen müssen. Die Kriterien basieren auf der Studie "Principled Instructions Are All You Need" (Bsharat et al., 2024) sowie dem RACCCA-Framework.

## Strukturelle Anforderungen

### Frontmatter-Qualität

Das YAML-Frontmatter einer SKILL.md erfüllt folgende Kriterien:

| Feld | Anforderung | Prüfkriterium |
|------|-------------|---------------|
| `name` | Kurz, beschreibend, lowercase mit Bindestrichen | 3-30 Zeichen, keine Sonderzeichen außer `-` |
| `description` | Umfassend, alle Trigger-Szenarien abdeckend | 100-500 Zeichen, enthält "Verwende wenn..." |

**Beispiel guter description:**
```yaml
description: Generiert API-Dokumentation aus Code-Kommentaren. Verwende diesen 
  Skill wenn der Nutzer (1) OpenAPI/Swagger-Specs erstellen möchte, (2) JSDoc 
  oder Docstrings in Dokumentation umwandeln will, (3) API-Endpunkte 
  dokumentieren möchte.
```

### Header-Hierarchie

Halte die Header-Hierarchie strikt ein:

```
# H1 - Titel (genau einmal, am Anfang)
## H2 - Hauptsektionen
### H3 - Untersektionen
#### H4 - Details (sparsam verwenden)
```

Sprünge wie H1 → H3 oder H2 → H4 sind nicht erlaubt.

### Delimiter-Verwendung

Verwende Delimiter konsistent für verschiedene Inhaltstypen:

| Inhaltstyp | Delimiter | Beispiel |
|------------|-----------|----------|
| Code | Triple-Backticks mit Sprache | ` ```python ` |
| Strukturierte Daten | XML-Tags | `<output_format>...</output_format>` |
| Wichtige Hinweise | Blockquotes | `> **Wichtig:** ...` |
| Sektions-Grenzen | Horizontale Linie | `---` |

## Inhaltliche Anforderungen

### Imperativ-Form

Formuliere alle Anweisungen im Imperativ:

| Falsch | Richtig |
|--------|---------|
| "Du sollst die Datei analysieren" | "Analysiere die Datei" |
| "Der Agent wird prüfen" | "Prüfe" |
| "Es soll validiert werden" | "Validiere" |

### Positive Formulierungen

Formuliere Anweisungen positiv statt negativ:

| Falsch | Richtig |
|--------|---------|
| "Verwende keine vagen Begriffe" | "Verwende präzise, konkrete Begriffe" |
| "Vergiss nicht die Beispiele" | "Füge Beispiele hinzu" |
| "Vermeide lange Sätze" | "Schreibe Sätze mit 15-25 Wörtern" |

### Verbotene vage Qualifikatoren

Diese Wörter indizieren mangelnde Spezifität und erfordern Konkretisierung:

```
einige, verschiedene, diverse, mehrere, etc., usw., und so weiter,
angemessen, geeignet, passend, gut, schlecht, richtig, falsch,
normalerweise, typischerweise, oft, manchmal, gelegentlich,
relativ, ziemlich, eher, gewissermaßen
```

**Transformation von vage zu spezifisch:**

| Vage | Spezifisch |
|------|------------|
| "einige Beispiele" | "3 Beispiele" |
| "angemessene Länge" | "200-500 Wörter" |
| "verschiedene Formate" | "JSON, YAML und Markdown" |

### Beispiel-Anforderungen

Beispiele müssen folgende Struktur aufweisen:

```markdown
**Beispiel: [Beschreibender Titel]**

Input:
[Konkreter Input]

Output:
[Erwarteter Output]

Erklärung:
[Warum dieses Output korrekt ist]
```

Mindestanforderungen:
- Komplexe Tasks: 3 Beispiele (Basis, Edge Case, Fehlerfall)
- Einfache Tasks: 1 Beispiel mit Input/Output

### Output-Format-Spezifikation

Jede Instruktion, die Output erwartet, definiert das Format explizit:

```markdown
## Output-Format

Strukturiere die Antwort als XML:

<review_result>
  <file name="[Dateiname]">
    <score category="[Kategorie]">[0-5]</score>
    <issues>
      <issue severity="critical|major|minor" line="[Zeile]">
        [Beschreibung]
      </issue>
    </issues>
  </file>
</review_result>
```

## RACCCA-Qualitätsdimensionen

Bewerte jede Instruktion anhand dieser sechs Dimensionen:

### Relevanz (R)
Prüffrage: Adressiert die Instruktion die Aufgabe direkt ohne Umwege?

| Score | Kriterium |
|-------|-----------|
| 5 | Jeder Satz trägt direkt zur Aufgabenerfüllung bei |
| 3 | Überwiegend relevant, einzelne Abschweifungen |
| 1 | Viel irrelevanter Inhalt, Kernaufgabe unklar |

### Accuracy (A)
Prüffrage: Sind alle Faktenaussagen und technischen Details korrekt?

| Score | Kriterium |
|-------|-----------|
| 5 | Alle Aussagen verifizierbar korrekt |
| 3 | Überwiegend korrekt, kleinere Ungenauigkeiten |
| 1 | Faktische Fehler, die zu Fehlverhalten führen |

### Completeness (C)
Prüffrage: Enthält die Instruktion alle notwendigen Informationen?

| Score | Kriterium |
|-------|-----------|
| 5 | Workflow vollständig, Edge Cases behandelt, Fehlerbehandlung definiert |
| 3 | Kernfunktion klar, einzelne Lücken bei Edge Cases |
| 1 | Wesentliche Schritte oder Informationen fehlen |

### Clarity (C)
Prüffrage: Ist jede Anweisung eindeutig und verständlich?

| Score | Kriterium |
|-------|-----------|
| 5 | Jede Anweisung hat genau eine plausible Interpretation |
| 3 | Überwiegend klar, einzelne mehrdeutige Stellen |
| 1 | Viele Ambiguitäten, verschiedene Interpretationen möglich |

### Coherence (C)
Prüffrage: Ist die Struktur logisch und konsistent?

| Score | Kriterium |
|-------|-----------|
| 5 | Logischer Aufbau, keine Widersprüche, konsistente Terminologie |
| 3 | Grundstruktur erkennbar, kleinere Inkonsistenzen |
| 1 | Unstrukturiert, widersprüchliche Aussagen |

### Appropriateness (A)
Prüffrage: Passt Detailgrad und Stil zur Aufgabe?

| Score | Kriterium |
|-------|-----------|
| 5 | Detailgrad optimal für Komplexität, Stil konsistent |
| 3 | Überwiegend angemessen, stellenweise zu viel/wenig Detail |
| 1 | Deutliches Missverhältnis zwischen Aufgabe und Darstellung |

## Red Flags

Diese Probleme erfordern sofortige Korrektur:

1. **Fehlende Output-Format-Spezifikation** bei Tasks mit strukturiertem Output
2. **Keine Beispiele** bei komplexen Tasks
3. **Widersprüchliche Anweisungen** innerhalb derselben Datei
4. **description im Frontmatter unter 100 Zeichen**
5. **Vage Qualifikatoren** in kritischen Anweisungen
6. **Fehlende Edge-Case-Behandlung** bei fehleranfälligen Operationen
7. **Inkonsistente Terminologie** für gleiche Konzepte

## Scoring-Schwellenwerte

| Gesamtscore | Bewertung | Aktion |
|-------------|-----------|--------|
| 4.5-5.0 | Exzellent | Freigabe ohne Änderungen |
| 3.5-4.4 | Gut | Freigabe mit optionalen Verbesserungen |
| 2.5-3.4 | Akzeptabel | Überarbeitung empfohlen |
| 1.5-2.4 | Mangelhaft | Überarbeitung erforderlich |
| 0-1.4 | Unzureichend | Grundlegende Neukonzeption nötig |
