---
description: Interaktiver UI-Kit Design-Wizard - erfasst Anforderungen und übergibt an Planner
argument-hint: "[optional: project-name]"
allowed-tools: ["AskUserQuestion", "Read", "Write", "TodoWrite", "Task"]
model: sonnet
---

# UI-Kit Design Wizard

Du führst den Benutzer durch einen strukturierten Prozess zur Definition eines UI-Kits. Sammle alle notwendigen Informationen in 3 Interaktionsrunden und übergib dann an den ui-kit-planner Agent.

## Projektinitialisierung

Projektname: ${1:-"Neues UI-Kit Projekt"}

Erstelle eine Todo-Liste zur Fortschrittsverfolgung:
1. Kontext und Zielgruppe erfassen
2. Design-Richtung definieren
3. Technisches Setup festlegen
4. Spezifikation erstellen
5. An ui-kit-planner übergeben

---

## Phase 1: Kontext und Zielgruppe

Verwende AskUserQuestion mit folgenden 4 Fragen:

**Frage 1 - Projekttyp:**
- header: "Projekttyp"
- question: "Welche Art von Anwendung soll das UI-Kit unterstützen?"
- multiSelect: false
- options:
  - label: "E-Commerce"
    description: "Online-Shop mit Produktkatalogen, Warenkorb und Checkout"
  - label: "SaaS Dashboard"
    description: "B2B-Anwendung mit Datenvisualisierung und komplexen Formularen"
  - label: "Portfolio/Marketing"
    description: "Präsentationsseite mit Hero-Sections und Content-Blöcken"
  - label: "Content/Blog"
    description: "Artikel-basiert mit Lesefluss und Medienintegration"

**Frage 2 - Zielgruppe:**
- header: "Zielgruppe"
- question: "Wer ist die primäre Zielgruppe?"
- multiSelect: false
- options:
  - label: "B2B Professionals"
    description: "Geschäftskunden die Effizienz und Professionalität erwarten"
  - label: "B2C Konsumenten"
    description: "Endverbraucher die Einfachheit und Emotion schätzen"
  - label: "Entwickler"
    description: "Technisches Publikum das Klarheit und Dokumentation braucht"
  - label: "Kreative"
    description: "Designer und Künstler die Innovation und Ausdruck suchen"

**Frage 3 - Primäres Gerät:**
- header: "Geräte"
- question: "Welches Gerät hat höchste Priorität?"
- multiSelect: false
- options:
  - label: "Mobile First"
    description: "Smartphones sind das Hauptgerät, Desktop sekundär"
  - label: "Desktop First"
    description: "Primär für große Bildschirme, Mobile als Fallback"
  - label: "Gleichwertig"
    description: "Beide Plattformen gleichermaßen wichtig"
  - label: "Touch Devices"
    description: "Tablets und Touch-Bildschirme im Fokus"

**Frage 4 - Bestehendes Branding:**
- header: "Branding"
- question: "Gibt es bereits ein Branding oder Corporate Design?"
- multiSelect: false
- options:
  - label: "Vollständig"
    description: "Farben, Typografie und Logo sind definiert"
  - label: "Teilweise"
    description: "Logo existiert, Rest ist flexibel"
  - label: "Nichts"
    description: "Komplette Freiheit bei der Gestaltung"
  - label: "Wird parallel entwickelt"
    description: "Branding-Prozess läuft gleichzeitig"

Speichere die Antworten aus Phase 1.

---

## Phase 2: Design-Richtung

Verwende AskUserQuestion mit folgenden 4 Fragen:

**Frage 1 - Design-Stil:**
- header: "Stil"
- question: "Welche Design-Richtung passt am besten?"
- multiSelect: false
- options:
  - label: "Modern/Minimal"
    description: "Viel Weißraum, klare Linien, reduzierte Elemente"
  - label: "Corporate/Professional"
    description: "Vertrauenswürdig, strukturiert, konservativ"
  - label: "Bold/Expressive"
    description: "Mutig, auffällig, starke Kontraste und große Typografie"
  - label: "Elegant/Luxury"
    description: "Raffiniert, hochwertig, subtile Details"

**Frage 2 - Farbstimmung:**
- header: "Farbwelt"
- question: "Welche Farbstimmung soll dominieren?"
- multiSelect: false
- options:
  - label: "Kühle Töne"
    description: "Blau, Grün, Grau - professionell und beruhigend"
  - label: "Warme Töne"
    description: "Orange, Rot, Gelb - einladend und energetisch"
  - label: "Neutral"
    description: "Schwarz, Weiß, Grau - zeitlos und flexibel"
  - label: "Lebendig"
    description: "Kräftige Primärfarben - jung und dynamisch"

**Frage 3 - Features:**
- header: "Features"
- question: "Welche Zusatzfeatures soll das UI-Kit enthalten?"
- multiSelect: true
- options:
  - label: "Dark Mode"
    description: "Automatische Unterstützung für dunkles Farbschema"
  - label: "Accessibility (WCAG)"
    description: "AAA-konform für maximale Barrierefreiheit"
  - label: "RTL Support"
    description: "Unterstützung für Rechts-nach-Links Sprachen"
  - label: "Animation System"
    description: "Konsistente Micro-Interactions und Transitions"

**Frage 4 - Animations-Präferenz:**
- header: "Animationen"
- question: "Wie viel Animation soll das UI-Kit bieten?"
- multiSelect: false
- options:
  - label: "Minimal"
    description: "Nur essentielle Feedback-Animationen"
  - label: "Moderat"
    description: "Subtile Transitions und Hover-Effekte"
  - label: "Umfangreich"
    description: "Reichhaltige Animationen mit Aufmerksamkeits-Effekten"
  - label: "Respects Motion"
    description: "Dynamisch basierend auf User-Präferenzen"

Speichere die Antworten aus Phase 2.

---

## Phase 3: Technisches Setup

Verwende AskUserQuestion mit folgenden 4 Fragen:

**Frage 1 - Framework:**
- header: "Framework"
- question: "Für welches Framework soll das UI-Kit erstellt werden?"
- multiSelect: false
- options:
  - label: "React"
    description: "JSX-Komponenten mit Hooks und Context API"
  - label: "Vue 3"
    description: "Composition API mit Single File Components"
  - label: "Svelte"
    description: "Kompilierte Komponenten mit minimaler Runtime"
  - label: "Framework-agnostisch"
    description: "Vanilla JS/CSS für maximale Kompatibilität"

**Frage 2 - CSS-Ansatz:**
- header: "CSS"
- question: "Welcher CSS-Ansatz soll verwendet werden?"
- multiSelect: false
- options:
  - label: "Tailwind CSS"
    description: "Utility-First mit Design-Tokens"
  - label: "CSS-in-JS"
    description: "Styled-Components oder Emotion"
  - label: "CSS Modules"
    description: "Scoped CSS mit lokalen Klassennamen"
  - label: "Vanilla CSS/SCSS"
    description: "Klassisches BEM mit SCSS-Variablen"

**Frage 3 - Komponentenumfang:**
- header: "Umfang"
- question: "Wie umfangreich soll das UI-Kit sein?"
- multiSelect: false
- options:
  - label: "Minimal"
    description: "10-15 Basis-Komponenten (Button, Input, Card, etc.)"
  - label: "Standard"
    description: "25-35 Komponenten inkl. Navigation und Formulare"
  - label: "Umfassend"
    description: "50+ Komponenten mit komplexen Patterns"
  - label: "Maßgeschneidert"
    description: "Spezifischer Umfang basierend auf Projektanforderungen"

**Frage 4 - Bestätigung:**
- header: "Bestätigen"
- question: "Soll ich mit diesen Einstellungen die Planung starten?"
- multiSelect: false
- options:
  - label: "Ja, starten"
    description: "Übergabe an ui-kit-planner zur detaillierten Planung"
  - label: "Einstellungen anpassen"
    description: "Zurück zum Anfang um Auswahl zu ändern"
  - label: "Zusammenfassung zeigen"
    description: "Alle Einstellungen nochmal auflisten"
  - label: "Als Vorlage speichern"
    description: "Einstellungen speichern ohne sofort zu planen"

Verarbeite die Bestätigung entsprechend.

---

## Phase 4: Verarbeitung und Übergabe

### Bei "Ja, starten":

Erstelle die UI-Kit-Spezifikation im folgenden Format und speichere sie:

**Datei: `.claude/ui-kit-spec.local.md`**

```yaml
---
project_name: [Projektname]
created: [Zeitstempel]
status: ready_for_planning
---
```

# UI-Kit Spezifikation

## Kontext
- **Projekttyp:** [Antwort]
- **Zielgruppe:** [Antwort]
- **Primäres Gerät:** [Antwort]
- **Bestehendes Branding:** [Antwort]

## Design-Richtung
- **Design-Stil:** [Antwort]
- **Farbstimmung:** [Antwort]
- **Features:** [Liste der gewählten Features]
- **Animations-Level:** [Antwort]

## Technisches Setup
- **Framework:** [Antwort]
- **CSS-Ansatz:** [Antwort]
- **Komponentenumfang:** [Antwort]

## Nächste Schritte
1. Token-System definieren
2. Basis-Komponenten designen
3. Komplexe Patterns erstellen
4. Dokumentation generieren

### Agent-Übergabe:

Starte den ui-kit-planner Agent mit der Task-Anweisung:

```
Plane das UI-Kit basierend auf der Spezifikation in .claude/ui-kit-spec.local.md.

Erstelle einen detaillierten Implementierungsplan mit:
1. Design-Token-Struktur (Farben, Spacing, Typografie)
2. Komponenten-Hierarchie und Abhängigkeiten
3. Dateistruktur und Benennungskonventionen
4. Implementierungsreihenfolge mit parallelen Execution Waves
5. Test- und Dokumentationsstrategie
```

### Bei "Einstellungen anpassen":
Beginne erneut bei Phase 1 und erlaube dem Benutzer, alle Fragen neu zu beantworten.

### Bei "Zusammenfassung zeigen":
Zeige alle bisherigen Antworten in einer übersichtlichen Liste und frage dann erneut nach Bestätigung.

### Bei "Als Vorlage speichern":
Speichere die Spezifikation in `.claude/ui-kit-templates/[projektname].md` und beende ohne Agent-Übergabe.

---

## Fehlerbehandlung

Falls AskUserQuestion keine Antworten liefert:

```
Es gab ein Problem bei der Erfassung deiner Antworten.

Alternativen:
1. Versuche es erneut mit /design-ui-kit
2. Beschreibe deine Anforderungen direkt in Textform
3. Nutze eine bestehende Vorlage aus .claude/ui-kit-templates/
```

---

## Beispiel-Workflow

Nach Abschluss aller Phasen:

```
## UI-Kit Spezifikation erstellt

### Zusammenfassung
- **Projekttyp:** SaaS Dashboard
- **Zielgruppe:** B2B Professionals
- **Design-Stil:** Modern/Minimal
- **Framework:** React mit Tailwind CSS
- **Umfang:** Standard (25-35 Komponenten)
- **Features:** Dark Mode, Accessibility

### Nächster Schritt
Übergabe an ui-kit-planner Agent zur detaillierten Planung...

[Task wird gestartet]
```
