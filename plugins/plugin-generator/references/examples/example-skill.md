# Beispiel: Hochwertige SKILL.md

Dieses Dokument zeigt eine SKILL.md, die alle Qualitätskriterien erfüllt.

## Das Beispiel

```markdown
---
name: api-docs-generator
description: Generiert OpenAPI-Dokumentation aus Code-Kommentaren und 
  Funktionssignaturen. Verwende diesen Skill wenn der Nutzer (1) API-Dokumentation 
  aus bestehendem Code erstellen möchte, (2) OpenAPI/Swagger-Specs generieren will, 
  (3) JSDoc, Docstrings oder Typannotationen in Dokumentation umwandeln möchte, 
  (4) REST-Endpunkte dokumentieren will.
---

# API-Docs-Generator

Generiert strukturierte API-Dokumentation aus Code-Kommentaren und Typinformationen.

## Workflow

1. **Code-Analyse**: Scanne die Quelldateien nach dokumentierbaren Elementen 
   (Funktionen, Klassen, Endpunkte)
2. **Kommentar-Extraktion**: Extrahiere JSDoc, Docstrings oder XML-Kommentare
3. **Typ-Inferenz**: Leite Parametertypen aus Annotationen oder Kontext ab
4. **Schema-Generierung**: Erstelle OpenAPI-konforme Schemas für Request/Response
5. **Dokumentations-Synthese**: Kombiniere alle Informationen zur finalen Spec

## Unterstützte Formate

| Eingabe | Kommentar-Stil | Output |
|---------|----------------|--------|
| JavaScript/TypeScript | JSDoc (`/** */`) | OpenAPI 3.0 YAML |
| Python | Docstrings (`"""..."""`) | OpenAPI 3.0 YAML |
| Java | Javadoc (`/** */`) | OpenAPI 3.0 YAML |

## Code-Analyse

Identifiziere dokumentierbare Elemente anhand dieser Muster:

**REST-Endpunkte:**
```javascript
// Express.js
app.get('/users/:id', handler)    // → GET /users/{id}
app.post('/users', handler)       // → POST /users

// Decorator-basiert
@Get('/users/:id')                // → GET /users/{id}
@Post('/users')                   // → POST /users
```

**Funktionssignaturen:**
```python
def get_user(user_id: int) -> User:
    """
    Retrieve a user by ID.
    
    Args:
        user_id: The unique identifier of the user
        
    Returns:
        User object if found
        
    Raises:
        NotFoundError: If user does not exist
    """
```

## Output-Format

Generiere OpenAPI 3.0 YAML mit dieser Struktur:

```yaml
openapi: 3.0.0
info:
  title: [API-Name]
  version: [Version]
paths:
  /[endpoint]:
    [method]:
      summary: [Aus erster Kommentarzeile]
      description: [Aus vollständigem Kommentar]
      parameters:
        - name: [param-name]
          in: [path|query|header]
          schema:
            type: [Aus Typannotation]
      responses:
        '200':
          description: [Aus Returns-Sektion]
```

## Edge Cases

**Fehlende Kommentare:**
Generiere Platzhalter-Beschreibung aus Funktionsname:
`getUserById` → "Get user by id"

**Komplexe Typen:**
Erstelle separates Schema unter `components/schemas` und referenziere mit `$ref`.

**Mehrere HTTP-Methoden pro Pfad:**
Gruppiere unter demselben `path`-Eintrag.

## Referenzen

- **OpenAPI-Spezifikation**: Siehe `references/openapi-spec.md` für Schema-Details
- **Kommentar-Patterns**: Siehe `references/comment-patterns.md` für sprachspezifische Formate
```

## Analyse: Warum dieses Beispiel die Kriterien erfüllt

### Frontmatter-Qualität

| Kriterium | Erfüllung |
|-----------|-----------|
| name: lowercase mit Bindestrichen | ✓ `api-docs-generator` |
| description: 100-500 Zeichen | ✓ 298 Zeichen |
| description: enthält Trigger-Szenarien | ✓ 4 explizite "(1)...(4)" Trigger |

### Strukturelle Qualität

| Kriterium | Erfüllung |
|-----------|-----------|
| H1 nur einmal am Anfang | ✓ |
| Header-Hierarchie konsistent | ✓ H1 → H2 nur |
| Workflow mit nummerierten Schritten | ✓ 5 Schritte |
| Code-Beispiele mit Sprachangabe | ✓ javascript, python, yaml |

### Inhaltliche Qualität

| Kriterium | Erfüllung |
|-----------|-----------|
| Imperativ-Form | ✓ "Scanne", "Extrahiere", "Generiere" |
| Keine vagen Qualifikatoren | ✓ Konkrete Formate und Muster |
| Beispiele mit Input/Output | ✓ Code → OpenAPI Mapping |
| Edge Cases behandelt | ✓ Eigene Sektion |
| Output-Format spezifiziert | ✓ YAML-Struktur gezeigt |
| Referenzen zu anderen Dateien | ✓ 2 Reference-Verweise |

### RACCCA-Scores

| Dimension | Score | Begründung |
|-----------|-------|------------|
| Relevanz | 5 | Jede Sektion trägt zum Kernzweck bei |
| Accuracy | 5 | Technische Details korrekt (OpenAPI 3.0) |
| Completeness | 5 | Workflow vollständig, Edge Cases behandelt |
| Clarity | 5 | Eindeutige Anweisungen, konkrete Beispiele |
| Coherence | 5 | Logischer Aufbau, konsistente Terminologie |
| Appropriateness | 5 | Detailgrad passend zur Komplexität |
