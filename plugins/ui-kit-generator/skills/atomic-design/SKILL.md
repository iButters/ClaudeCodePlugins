---
name: Atomic Design
description: This skill should be used when the user asks about "atomic design methodology", "component hierarchy", "atoms molecules organisms", "design system structure", "component composition", "when to create atoms vs molecules", "component dependencies", "UI component architecture", "design system organization", or needs guidance on structuring components according to Atomic Design principles.
version: 0.1.0
---

# Atomic Design Methodology for UI-Kit Generation

## Overview

Atomic Design is a methodology for creating design systems with a clear hierarchy. Components are organized into five distinct levels, each building upon the previous.

**The Five Levels:**
1. **Atoms** - Foundational building blocks
2. **Molecules** - Simple component combinations
3. **Organisms** - Complex UI sections
4. **Templates** - Page-level layouts
5. **Pages** - Concrete instances with real content

## Level Definitions

### Atoms (Level 1)

The smallest, indivisible UI elements that can't be broken down further.

**Characteristics:**
- Single responsibility
- No dependencies on other components (except design tokens)
- Highly reusable across entire application
- Stateless or minimal internal state

**Examples:**
| Component | Purpose | Props |
|-----------|---------|-------|
| Button | User actions | variant, size, disabled |
| Input | Text entry | type, placeholder, value |
| Label | Text annotation | htmlFor, required |
| Icon | Visual symbols | name, size, color |
| Badge | Status indicators | variant, children |
| Avatar | User images | src, alt, size, fallback |
| Spinner | Loading state | size |
| Divider | Visual separation | orientation |

**File Structure:**
```
atoms/
├── Button/
│   ├── Button.tsx
│   ├── Button.types.ts
│   ├── Button.styles.css
│   ├── Button.stories.tsx
│   ├── Button.test.tsx
│   └── index.ts
```

### Molecules (Level 2)

Simple combinations of atoms that form functional units.

**Characteristics:**
- Composed of 2-5 atoms
- Single, focused purpose
- Imports atoms, never duplicates them
- May have controlled state

**Examples:**
| Component | Atoms Used | Purpose |
|-----------|------------|---------|
| SearchBar | Input + Button + Icon | Search functionality |
| FormField | Label + Input + Text | Form input with label/error |
| NavLink | Icon + Text + Badge | Navigation item |
| Card | Box + Text + Button | Content container |
| Dropdown | Button + List + Icon | Selection menu |
| Tooltip | Box + Text | Contextual information |

**Composition Rule:**
```tsx
// CORRECT - Import atoms
import { Button } from '@/atoms/Button'
import { Input } from '@/atoms/Input'
import { Icon } from '@/atoms/Icon'

export function SearchBar() {
  return (
    <div className="search-bar">
      <Icon name="search" />
      <Input placeholder="Search..." />
      <Button>Go</Button>
    </div>
  )
}

// WRONG - Duplicating atom code
export function SearchBar() {
  return (
    <div className="search-bar">
      <svg>...</svg>  {/* Don't recreate Icon */}
      <input />       {/* Don't recreate Input */}
      <button>Go</button>  {/* Don't recreate Button */}
    </div>
  )
}
```

### Organisms (Level 3)

Complex UI sections composed of molecules and atoms.

**Characteristics:**
- Form distinct sections of interface
- May include multiple molecules and atoms
- Handle section-level state and logic
- Can be standalone UI regions

**Examples:**
| Component | Composition | Purpose |
|-----------|-------------|---------|
| Header | Logo + NavLinks + SearchBar + Avatar | Page header |
| Sidebar | NavLinks + Dividers + UserCard | Side navigation |
| DataTable | Table + Pagination + Filters | Data display |
| Modal | Overlay + Card + Buttons | Dialog windows |
| Form | FormFields + Buttons | Data entry |
| CommentThread | Comments + Input + Buttons | Discussion |

**State Management:**
```tsx
export function DataTable({ data, columns }) {
  // Organism manages complex state
  const [sortBy, setSortBy] = useState(null)
  const [filters, setFilters] = useState({})
  const [page, setPage] = useState(1)

  const processedData = useMemo(() =>
    applyFiltersAndSort(data, filters, sortBy),
    [data, filters, sortBy]
  )

  return (
    <div className="data-table">
      <TableFilters filters={filters} onChange={setFilters} />
      <Table data={processedData} columns={columns} />
      <Pagination page={page} onChange={setPage} />
    </div>
  )
}
```

### Templates (Level 4)

Page-level layouts that define content structure without specific content.

**Characteristics:**
- Define page structure and zones
- Use slots/children for content injection
- Framework for consistent page layouts
- No concrete content, only structure

**Examples:**
| Template | Layout Zones | Use Case |
|----------|--------------|----------|
| DashboardTemplate | Header + Sidebar + Main + Footer | Admin panels |
| AuthTemplate | Logo + Form + Links | Login/Register |
| MarketingTemplate | Hero + Sections + CTA | Landing pages |
| SettingsTemplate | Tabs + Content | Config pages |
| ArticleTemplate | Header + Content + Sidebar | Blog posts |

**Slot Pattern:**
```tsx
interface DashboardTemplateProps {
  header?: ReactNode
  sidebar?: ReactNode
  children: ReactNode
  footer?: ReactNode
}

export function DashboardTemplate({
  header,
  sidebar,
  children,
  footer
}: DashboardTemplateProps) {
  return (
    <div className="dashboard-layout">
      {header && <header className="layout-header">{header}</header>}
      <div className="layout-body">
        {sidebar && <aside className="layout-sidebar">{sidebar}</aside>}
        <main className="layout-main">{children}</main>
      </div>
      {footer && <footer className="layout-footer">{footer}</footer>}
    </div>
  )
}
```

### Pages (Level 5)

Concrete instances of templates filled with real content.

**Characteristics:**
- Use templates as structure
- Contain actual data and content
- Handle page-level logic and data fetching
- Include SEO metadata

**Examples:**
| Page | Template Used | Content |
|------|---------------|---------|
| HomePage | MarketingTemplate | Hero, Features, Testimonials |
| DashboardPage | DashboardTemplate | Stats, Charts, Activity |
| ProductListPage | CatalogTemplate | Products, Filters, Pagination |
| SettingsPage | SettingsTemplate | Profile, Security, Prefs |

## Dependency Rules

### Import Direction

Components can only import from lower levels:

```
Pages      → Templates, Organisms, Molecules, Atoms
Templates  → Organisms, Molecules, Atoms
Organisms  → Molecules, Atoms
Molecules  → Atoms
Atoms      → Design Tokens only
```

### Forbidden Patterns

```tsx
// FORBIDDEN: Atom importing from Molecule
// atoms/Button/Button.tsx
import { FormField } from '@/molecules/FormField' // ❌

// FORBIDDEN: Molecule importing from Organism
// molecules/SearchBar/SearchBar.tsx
import { Header } from '@/organisms/Header' // ❌

// FORBIDDEN: Circular dependencies
// organisms/Sidebar/Sidebar.tsx
import { Dashboard } from '@/templates/Dashboard' // ❌
```

### Valid Import Examples

```tsx
// atoms/Button/Button.tsx
import { colors, spacing } from '@/tokens' // ✅

// molecules/FormField/FormField.tsx
import { Label } from '@/atoms/Label' // ✅
import { Input } from '@/atoms/Input' // ✅
import { Text } from '@/atoms/Text' // ✅

// organisms/Header/Header.tsx
import { Logo } from '@/atoms/Logo' // ✅
import { NavLink } from '@/molecules/NavLink' // ✅
import { SearchBar } from '@/molecules/SearchBar' // ✅

// templates/Dashboard/DashboardTemplate.tsx
import { Header } from '@/organisms/Header' // ✅
import { Sidebar } from '@/organisms/Sidebar' // ✅
```

## Generation Workflow

### Wave-Based Execution

Components are generated in waves based on dependency level:

```
Wave 1: Atoms (parallel)
   ↓ complete
Wave 2: Molecules (parallel)
   ↓ complete
Wave 3: Organisms (parallel)
   ↓ complete
Wave 4: Templates (parallel)
   ↓ complete
Wave 5: Pages (parallel)
```

### Dependency Graph

Before generation, analyze dependencies:

```typescript
interface ComponentNode {
  name: string
  level: 'atom' | 'molecule' | 'organism' | 'template' | 'page'
  dependencies: string[]
}

const dependencyGraph: ComponentNode[] = [
  { name: 'Button', level: 'atom', dependencies: [] },
  { name: 'Input', level: 'atom', dependencies: [] },
  { name: 'SearchBar', level: 'molecule', dependencies: ['Button', 'Input', 'Icon'] },
  { name: 'Header', level: 'organism', dependencies: ['Logo', 'NavLink', 'SearchBar'] },
]
```

## Decision Guide

### When to Create an Atom

- Component has single responsibility
- Used in 3+ different contexts
- Cannot be broken into smaller parts
- Has no dependencies on other components

### When to Create a Molecule

- Combines 2-5 atoms into functional unit
- Represents a single UI pattern
- Used in multiple organisms
- Would be awkward to inline in organism

### When to Create an Organism

- Forms a distinct UI section
- Requires internal state management
- Could be reused on multiple pages
- Contains complex interaction logic

### When to Create a Template

- Defines page structure
- Used by multiple pages
- Contains layout logic only
- No specific content

## Additional Resources

- **`references/dependency-rules.md`** - Detailed import validation rules
- **`references/naming-conventions.md`** - Component naming standards
- **`references/best-practices.md`** - Common patterns and anti-patterns
- **`examples/component-examples.md`** - Code examples for each level
