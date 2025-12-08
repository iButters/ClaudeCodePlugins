# Atomic Design Dependency Rules

## Import Hierarchy

### Valid Import Matrix

| From \ To | Atoms | Molecules | Organisms | Templates | Pages |
|-----------|-------|-----------|-----------|-----------|-------|
| **Atoms** | Same level only | - | - | - | - |
| **Molecules** | Yes | Same level only | - | - | - |
| **Organisms** | Yes | Yes | Same level only | - | - |
| **Templates** | Yes | Yes | Yes | Same level only | - |
| **Pages** | Yes | Yes | Yes | Yes | - |

### Import Validation Rules

```typescript
const LEVEL_ORDER = ['atom', 'molecule', 'organism', 'template', 'page']

function validateImport(fromLevel: string, toLevel: string): boolean {
  const fromIndex = LEVEL_ORDER.indexOf(fromLevel)
  const toIndex = LEVEL_ORDER.indexOf(toLevel)

  // Can only import from same level or lower
  return toIndex <= fromIndex
}

// Examples
validateImport('molecule', 'atom')      // true
validateImport('organism', 'molecule')  // true
validateImport('atom', 'molecule')      // false - INVALID
validateImport('molecule', 'organism')  // false - INVALID
```

## Circular Dependency Prevention

### Detection Algorithm

```typescript
function detectCycle(graph: Map<string, string[]>, start: string): boolean {
  const visited = new Set<string>()
  const recursionStack = new Set<string>()

  function dfs(node: string): boolean {
    visited.add(node)
    recursionStack.add(node)

    const deps = graph.get(node) || []
    for (const dep of deps) {
      if (!visited.has(dep) && dfs(dep)) return true
      if (recursionStack.has(dep)) return true
    }

    recursionStack.delete(node)
    return false
  }

  return dfs(start)
}
```

### Common Circular Patterns to Avoid

**Pattern 1: Peer Dependencies**
```typescript
// WRONG: Molecules depending on each other
// molecules/DropdownItem.tsx
import { Dropdown } from './Dropdown' // Creates cycle if Dropdown imports DropdownItem

// SOLUTION: Extract shared logic to atom or accept as children
import { ListItem } from '@/atoms/ListItem'
```

**Pattern 2: Parent-Child Cycles**
```typescript
// WRONG: Component importing its container
// molecules/TabPanel.tsx
import { Tabs } from '@/organisms/Tabs' // Tabs likely imports TabPanel

// SOLUTION: Use render props or children pattern
interface TabPanelProps {
  children: ReactNode
  isActive: boolean
}
```

## Cross-Level Communication

### Upward Communication (Child → Parent)

Use callbacks and events:

```typescript
// atoms/Button/Button.tsx
interface ButtonProps {
  onClick?: (event: MouseEvent) => void
}

// molecules/SearchBar/SearchBar.tsx
function SearchBar({ onSearch }) {
  return (
    <Button onClick={() => onSearch(query)}>Search</Button>
  )
}

// organisms/Header/Header.tsx
function Header() {
  const handleSearch = (query: string) => {
    // Handle search
  }
  return <SearchBar onSearch={handleSearch} />
}
```

### Downward Communication (Parent → Child)

Use props:

```typescript
// organisms/Form/Form.tsx
function Form() {
  const [isSubmitting, setIsSubmitting] = useState(false)

  return (
    <FormField disabled={isSubmitting} />
  )
}
```

### Sideways Communication (Same Level)

Use shared context or state management:

```typescript
// Context at organism level
const FormContext = createContext<FormState | null>(null)

// Multiple molecules access same context
function FormField() {
  const { errors } = useContext(FormContext)
  // ...
}

function FormActions() {
  const { isValid } = useContext(FormContext)
  // ...
}
```

## Shared Dependencies

### Design Tokens (Global)

All levels can import design tokens:

```typescript
// Any component
import { colors, spacing, typography } from '@/tokens'
```

### Utility Functions (Global)

Shared utilities are allowed at all levels:

```typescript
// Any component
import { cn, formatDate, debounce } from '@/utils'
```

### Type Definitions (Global)

Shared types are allowed at all levels:

```typescript
// Any component
import type { Size, Variant, ComponentProps } from '@/types'
```

## Enforcement Strategies

### ESLint Rule Configuration

```javascript
// .eslintrc.js
module.exports = {
  rules: {
    'import/no-restricted-paths': [
      'error',
      {
        zones: [
          // Atoms cannot import from molecules
          {
            target: './src/atoms/**/*',
            from: './src/molecules/**/*',
            message: 'Atoms cannot import from molecules'
          },
          // Atoms cannot import from organisms
          {
            target: './src/atoms/**/*',
            from: './src/organisms/**/*',
            message: 'Atoms cannot import from organisms'
          },
          // Molecules cannot import from organisms
          {
            target: './src/molecules/**/*',
            from: './src/organisms/**/*',
            message: 'Molecules cannot import from organisms'
          },
          // Add more zones as needed
        ]
      }
    ]
  }
}
```

### Import Path Aliases

```typescript
// tsconfig.json
{
  "compilerOptions": {
    "paths": {
      "@/atoms/*": ["./src/ui-kit/atoms/*"],
      "@/molecules/*": ["./src/ui-kit/molecules/*"],
      "@/organisms/*": ["./src/ui-kit/organisms/*"],
      "@/templates/*": ["./src/ui-kit/templates/*"],
      "@/pages/*": ["./src/ui-kit/pages/*"],
      "@/tokens": ["./src/ui-kit/tokens"],
      "@/utils/*": ["./src/utils/*"]
    }
  }
}
```

## Dependency Documentation

### Component Manifest

Each component should document its dependencies:

```typescript
// molecules/SearchBar/SearchBar.manifest.ts
export const manifest = {
  name: 'SearchBar',
  level: 'molecule',
  dependencies: {
    atoms: ['Button', 'Input', 'Icon'],
    molecules: [],
    external: ['react']
  },
  usedBy: ['Header', 'Sidebar', 'CommandPalette']
}
```

### Auto-Generated Dependency Graph

```
SearchBar (molecule)
├── Button (atom)
├── Input (atom)
└── Icon (atom)

Header (organism)
├── Logo (atom)
├── NavLink (molecule)
│   ├── Icon (atom)
│   └── Badge (atom)
├── SearchBar (molecule)
│   ├── Button (atom)
│   ├── Input (atom)
│   └── Icon (atom)
└── Avatar (atom)
```
