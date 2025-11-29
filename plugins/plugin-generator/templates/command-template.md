# Command Template

Verwende dieses Template für neue Slash-Command-Definitionen.

---

## Template

```markdown
# [COMMAND_BESCHREIBUNG]

[ZWECK_EINZEILER]

## Parameter

- `$[PARAM_1]`: [PARAM_1_BESCHREIBUNG]. Pflicht.
- `$[PARAM_2]`: [PARAM_2_BESCHREIBUNG]. Optional, Default: `[DEFAULT_WERT]`.

## Verhalten

1. **[PHASE_1]**: [PHASE_1_BESCHREIBUNG]
2. **[PHASE_2]**: [PHASE_2_BESCHREIBUNG]
3. **[PHASE_3]**: [PHASE_3_BESCHREIBUNG]

## Beispiele

**Beispiel 1: [SZENARIO_NAME]**

Input:
```
/[COMMAND_NAME] [BEISPIEL_PARAMETER]
```

Output:
[OUTPUT_BESCHREIBUNG_ODER_BEISPIEL]

## Fehlerbehandlung

| Fehler | Verhalten |
|--------|-----------|
| [FEHLER_1] | [VERHALTEN_1] |
| [FEHLER_2] | [VERHALTEN_2] |
```

---

## Platzhalter

| Platzhalter | Beschreibung | Beispiel |
|-------------|--------------|----------|
| `[COMMAND_BESCHREIBUNG]` | Kurze Beschreibung als H1-Titel | `Plugin-Qualitätsreview durchführen` |
| `[ZWECK_EINZEILER]` | Was der Command tut, 1 Satz | `Analysiert alle MD-Dateien eines Plugins.` |
| `[PARAM_X]` | Parametername in UPPERCASE | `PLUGIN_PATH` |
| `[PARAM_X_BESCHREIBUNG]` | Was der Parameter bewirkt | `Pfad zum Plugin-Verzeichnis` |
| `[DEFAULT_WERT]` | Default-Wert für optionale Parameter | `all` |
| `[PHASE_X]` | Name einer Verarbeitungsphase | `Dateierkennung` |
| `[COMMAND_NAME]` | Name des Commands ohne Slash | `review-plugin` |
| `[FEHLER_X]` | Beschreibung eines Fehlerfalls | `Pfad existiert nicht` |
| `[VERHALTEN_X]` | Reaktion auf den Fehler | `Fehlermeldung mit Vorschlag` |

## Anpassungshinweise

1. **Dateiname**: Speichere die Datei als `[COMMAND_NAME].md` im Verzeichnis `.claude/commands/`.

2. **Parameter**: Entferne die Parameter-Sektion falls der Command keine Parameter hat. Füge weitere Parameter hinzu falls nötig.

3. **Verhalten**: Passe die Anzahl der Phasen an die Komplexität des Commands an (Minimum 2, empfohlen 3-5).

4. **Beispiele**: Füge bei komplexen Commands 2-3 Beispiele hinzu, die verschiedene Parameterkombinationen zeigen.

5. **Fehlerbehandlung**: Dokumentiere mindestens die 2 wahrscheinlichsten Fehlerfälle.

## Checkliste vor Fertigstellung

- [ ] Dateiname entspricht Command-Name
- [ ] Alle Parameter mit Pflicht/Optional und Default dokumentiert
- [ ] Mindestens 1 vollständiges Input/Output-Beispiel
- [ ] Fehlerbehandlung für häufige Fehlerfälle definiert
- [ ] Alle Anweisungen im Imperativ
