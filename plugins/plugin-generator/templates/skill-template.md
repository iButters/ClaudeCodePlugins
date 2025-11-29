# SKILL.md Template

Verwende dieses Template als Ausgangspunkt für neue SKILL.md-Dateien.

---

## Template

```markdown
---
name: [SKILL_NAME]
description: [KURZE_BESCHREIBUNG]. Verwende diesen Skill wenn der Nutzer 
  (1) [TRIGGER_1], (2) [TRIGGER_2], (3) [TRIGGER_3].
---

# [SKILL_TITEL]

[EINZEILER_ZWECKBESCHREIBUNG]

## Workflow

1. **[SCHRITT_1_NAME]**: [SCHRITT_1_BESCHREIBUNG]
2. **[SCHRITT_2_NAME]**: [SCHRITT_2_BESCHREIBUNG]
3. **[SCHRITT_3_NAME]**: [SCHRITT_3_BESCHREIBUNG]
4. **[SCHRITT_4_NAME]**: [SCHRITT_4_BESCHREIBUNG]
5. **[SCHRITT_5_NAME]**: [SCHRITT_5_BESCHREIBUNG]

## [HAUPTKONZEPT_SEKTION]

[ERKLÄRUNG_DES_KERNKONZEPTS]

[TABELLE_ODER_LISTE_MIT_DETAILS]

## [BEISPIEL_SEKTION]

**Beispiel: [SZENARIO_NAME]**

Input:
```[SPRACHE]
[BEISPIEL_INPUT]
```

Output:
```[SPRACHE]
[BEISPIEL_OUTPUT]
```

## Edge Cases

**[EDGE_CASE_1]:**
[BEHANDLUNG_1]

**[EDGE_CASE_2]:**
[BEHANDLUNG_2]

## Referenzen

- **[REFERENZ_1_NAME]**: Siehe `references/[DATEI_1].md` für [ZWECK_1]
- **[REFERENZ_2_NAME]**: Siehe `references/[DATEI_2].md` für [ZWECK_2]
```

---

## Platzhalter

| Platzhalter | Beschreibung | Beispiel |
|-------------|--------------|----------|
| `[SKILL_NAME]` | Lowercase mit Bindestrichen, 3-30 Zeichen | `api-docs-generator` |
| `[KURZE_BESCHREIBUNG]` | Was der Skill tut, ohne "Verwende wenn" | `Generiert API-Dokumentation aus Code` |
| `[TRIGGER_1-3]` | Konkrete Szenarien, die den Skill auslösen | `API-Dokumentation erstellen möchte` |
| `[SKILL_TITEL]` | Name als Titel, kann Leerzeichen enthalten | `API-Docs-Generator` |
| `[EINZEILER_ZWECKBESCHREIBUNG]` | Maximal 1 Satz | `Erstellt OpenAPI-Specs aus Kommentaren.` |
| `[SCHRITT_X_NAME]` | Kurzer Name im Imperativ | `Code-Analyse` |
| `[SCHRITT_X_BESCHREIBUNG]` | Was in diesem Schritt passiert | `Scanne Quelldateien nach Endpunkten` |
| `[HAUPTKONZEPT_SEKTION]` | Titel der wichtigsten inhaltlichen Sektion | `Unterstützte Formate` |
| `[EDGE_CASE_X]` | Beschreibung des Sonderfalls | `Fehlende Kommentare` |
| `[BEHANDLUNG_X]` | Wie der Edge Case behandelt wird | `Generiere Platzhalter aus Funktionsname` |

## Anpassungshinweise

1. **Frontmatter-description**: Erweitere um weitere Trigger falls nötig. Ziel: 200-400 Zeichen.

2. **Workflow-Schritte**: Passe Anzahl an Komplexität an (Minimum 3, Maximum 7). Entferne oder ergänze Schritte.

3. **Sektionen nach Workflow**: Füge themenspezifische Sektionen hinzu, die für den Skill relevant sind. Mögliche Sektionen:
   - Unterstützte Formate
   - Konfiguration
   - Output-Format
   - Validierung

4. **Beispiele**: Bei komplexen Skills füge 2-3 Beispiele hinzu, die verschiedene Szenarien abdecken.

5. **Edge Cases**: Dokumentiere mindestens die 2 häufigsten Sonderfälle.

6. **Referenzen**: Entferne diese Sektion falls keine Reference-Dateien existieren. Füge für jede vorhandene Reference einen Eintrag hinzu.

## Checkliste vor Fertigstellung

- [ ] description enthält mindestens 3 explizite Trigger-Szenarien
- [ ] Alle Anweisungen im Imperativ formuliert
- [ ] Keine vagen Qualifikatoren (einige, verschiedene, etc.)
- [ ] Mindestens 1 konkretes Beispiel mit Input/Output
- [ ] Edge Cases dokumentiert
- [ ] Alle existierenden Reference-Dateien verlinkt
