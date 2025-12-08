# Atomic Design Naming Conventions

## Component Names

### General Rules

1. **PascalCase** for component names
2. **Descriptive** - name describes what it is or does
3. **No prefixes** for level (don't use AtomButton, MoleculeSearchBar)
4. **No abbreviations** unless universally known (URL, API, ID)

### By Level

| Level | Pattern | Examples |
|-------|---------|----------|
| Atoms | Noun | `Button`, `Input`, `Icon`, `Avatar` |
| Molecules | Noun or NounNoun | `SearchBar`, `FormField`, `NavLink` |
| Organisms | Noun or SectionNoun | `Header`, `Sidebar`, `DataTable` |
| Templates | NounTemplate | `DashboardTemplate`, `AuthTemplate` |
| Pages | NounPage | `HomePage`, `SettingsPage` |

### Compound Components

Use dot notation for sub-components:

```typescript
// Card compound component
Card.Header
Card.Body
Card.Footer
Card.Image

// Usage
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Body>Content</Card.Body>
  <Card.Footer>Actions</Card.Footer>
</Card>
```

## File Names

### Component Files

```
ComponentName/
├── ComponentName.tsx         # Main component
├── ComponentName.types.ts    # TypeScript interfaces
├── ComponentName.styles.css  # Styles (or .module.css)
├── ComponentName.stories.tsx # Storybook stories
├── ComponentName.test.tsx    # Unit tests
└── index.ts                  # Public exports
```

### Naming Patterns

| File Type | Pattern | Example |
|-----------|---------|---------|
| Component | `{Name}.tsx` | `Button.tsx` |
| Types | `{Name}.types.ts` | `Button.types.ts` |
| Styles | `{Name}.styles.css` | `Button.styles.css` |
| CSS Modules | `{Name}.module.css` | `Button.module.css` |
| Stories | `{Name}.stories.tsx` | `Button.stories.tsx` |
| Tests | `{Name}.test.tsx` | `Button.test.tsx` |
| Hooks | `use{Name}.ts` | `useButton.ts` |
| Context | `{Name}Context.tsx` | `ThemeContext.tsx` |
| Utils | `{name}.utils.ts` | `button.utils.ts` |

## Props Naming

### Standard Props

| Purpose | Prop Name | Type |
|---------|-----------|------|
| Visual style | `variant` | `'primary' \| 'secondary' \| ...` |
| Size | `size` | `'sm' \| 'md' \| 'lg'` |
| Disabled state | `disabled` | `boolean` |
| Loading state | `loading` or `isLoading` | `boolean` |
| Full width | `fullWidth` | `boolean` |
| Children | `children` | `ReactNode` |
| Class extension | `className` | `string` |
| Click handler | `onClick` | `(event) => void` |
| Change handler | `onChange` | `(value) => void` |

### Event Handler Props

Use `on` prefix + event name:

```typescript
interface ButtonProps {
  onClick?: (event: MouseEvent) => void
  onFocus?: (event: FocusEvent) => void
  onBlur?: (event: FocusEvent) => void
  onKeyDown?: (event: KeyboardEvent) => void
}

interface InputProps {
  onChange?: (value: string) => void  // Simplified
  onInput?: (event: InputEvent) => void
  onSubmit?: (value: string) => void
}
```

### Boolean Props

Use positive naming, avoid negation:

```typescript
// GOOD
disabled?: boolean
visible?: boolean
loading?: boolean
checked?: boolean

// AVOID
notDisabled?: boolean  // Use disabled={false}
hidden?: boolean       // Use visible={false}
notLoading?: boolean   // Use loading={false}
```

### Render Props

Use `render` prefix or descriptive name:

```typescript
interface TableProps {
  renderHeader?: () => ReactNode
  renderRow?: (data: RowData) => ReactNode
  renderEmpty?: () => ReactNode
}

// Or component injection
interface TableProps {
  HeaderComponent?: ComponentType<HeaderProps>
  RowComponent?: ComponentType<RowProps>
}
```

## CSS Class Names

### BEM Convention

```
block__element--modifier

.button              // Block
.button__icon        // Element
.button--primary     // Modifier
.button--disabled    // Modifier
.button__icon--left  // Element + Modifier
```

### CSS Custom Properties

```css
/* Component-scoped variables */
.button {
  --button-padding: var(--spacing-3);
  --button-bg: var(--color-primary-500);
  --button-text: var(--color-white);

  padding: var(--button-padding);
  background: var(--button-bg);
  color: var(--button-text);
}

.button--secondary {
  --button-bg: var(--color-neutral-100);
  --button-text: var(--color-neutral-900);
}
```

### Tailwind Classes

Group by category:

```tsx
<button
  className={cn(
    // Layout
    'inline-flex items-center justify-center',
    // Sizing
    'px-4 py-2 min-w-[100px]',
    // Typography
    'text-sm font-medium',
    // Colors
    'bg-primary-500 text-white',
    // Borders
    'rounded-md border border-transparent',
    // States
    'hover:bg-primary-600 focus:ring-2 focus:ring-primary-300',
    'disabled:opacity-50 disabled:cursor-not-allowed',
    // Transitions
    'transition-colors duration-150',
    // Custom classes
    className
  )}
>
  {children}
</button>
```

## TypeScript Types

### Interface Naming

```typescript
// Component props: {Name}Props
interface ButtonProps { }
interface SearchBarProps { }

// State types: {Name}State
interface FormState { }
interface ModalState { }

// Context types: {Name}ContextValue
interface ThemeContextValue { }
interface AuthContextValue { }

// Event types: {Name}Event or On{Action}
type OnSearchEvent = (query: string) => void
type OnSelectEvent<T> = (item: T) => void
```

### Generic Type Parameters

```typescript
// Single generic: T
interface ListProps<T> {
  items: T[]
  renderItem: (item: T) => ReactNode
}

// Multiple generics: descriptive names
interface FormProps<TValues, TError> {
  initialValues: TValues
  onSubmit: (values: TValues) => void
  validate: (values: TValues) => TError | null
}
```

## Export Naming

### Index Files

```typescript
// atoms/Button/index.ts
export { Button } from './Button'
export type { ButtonProps, ButtonVariant, ButtonSize } from './Button.types'

// atoms/index.ts (barrel export)
export * from './Button'
export * from './Input'
export * from './Icon'
// etc.
```

### Named vs Default Exports

Prefer named exports for better IDE support:

```typescript
// PREFERRED - Named export
export function Button(props: ButtonProps) { }

// AVOID - Default export
export default function Button(props: ButtonProps) { }
```

## Storybook Naming

### Story Titles

```typescript
// atoms/Button/Button.stories.tsx
export default {
  title: 'Atoms/Button',  // Category/Name
  component: Button,
}

// molecules/SearchBar/SearchBar.stories.tsx
export default {
  title: 'Molecules/SearchBar',
  component: SearchBar,
}
```

### Story Names

```typescript
// Use descriptive names
export const Default: Story = { }
export const Primary: Story = { args: { variant: 'primary' } }
export const Secondary: Story = { args: { variant: 'secondary' } }
export const Small: Story = { args: { size: 'sm' } }
export const Large: Story = { args: { size: 'lg' } }
export const Disabled: Story = { args: { disabled: true } }
export const Loading: Story = { args: { loading: true } }
export const WithIcon: Story = { args: { leftIcon: <Icon name="star" /> } }
```

## Test Naming

### Test Files

```typescript
// Button.test.tsx
describe('Button', () => {
  describe('rendering', () => {
    it('renders children correctly', () => { })
    it('applies variant class', () => { })
    it('applies size class', () => { })
  })

  describe('interactions', () => {
    it('calls onClick when clicked', () => { })
    it('does not call onClick when disabled', () => { })
  })

  describe('accessibility', () => {
    it('has correct ARIA attributes', () => { })
    it('is keyboard accessible', () => { })
  })
})
```

### Data Test IDs

```tsx
<button data-testid="button-submit">Submit</button>
<input data-testid="input-email" />
<div data-testid="card-user-profile" />

// Pattern: {component}-{identifier} or {component}-{purpose}
```
