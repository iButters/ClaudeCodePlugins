# Atomic Design Best Practices

## Component Design Principles

### Single Responsibility

Each component should do one thing well:

```typescript
// GOOD - Single responsibility
function Avatar({ src, alt, size }: AvatarProps) {
  return <img src={src} alt={alt} className={`avatar avatar--${size}`} />
}

function UserInfo({ name, role }: UserInfoProps) {
  return (
    <div className="user-info">
      <span className="user-name">{name}</span>
      <span className="user-role">{role}</span>
    </div>
  )
}

// BAD - Multiple responsibilities
function AvatarWithInfo({ src, name, role, onEdit, onDelete }) {
  // Does too many things: display, edit, delete
}
```

### Composition Over Configuration

Prefer composable components over prop-heavy ones:

```typescript
// GOOD - Composable
<Card>
  <Card.Header>
    <Card.Title>Dashboard</Card.Title>
    <Card.Actions><Button>Edit</Button></Card.Actions>
  </Card.Header>
  <Card.Body>{content}</Card.Body>
</Card>

// BAD - Too many props
<Card
  title="Dashboard"
  showActions
  actionLabel="Edit"
  onActionClick={handleEdit}
  headerVariant="large"
  // ... many more props
/>
```

### Prop Drilling Prevention

Use context for deeply nested data:

```typescript
// GOOD - Context for shared state
const FormContext = createContext<FormState | null>(null)

function Form({ children }) {
  const [state, dispatch] = useReducer(formReducer, initialState)
  return (
    <FormContext.Provider value={{ state, dispatch }}>
      {children}
    </FormContext.Provider>
  )
}

function FormField({ name }) {
  const { state, dispatch } = useContext(FormContext)
  // Access form state directly
}

// BAD - Prop drilling
function Form({ children }) {
  const [values, setValues] = useState({})
  return React.Children.map(children, child =>
    cloneElement(child, { values, setValues }) // Drilling down
  )
}
```

## State Management

### State Location

| State Type | Location | Example |
|------------|----------|---------|
| UI State | Component | `isOpen`, `isHovered` |
| Form State | Form/Field | `value`, `error`, `touched` |
| Feature State | Context | Shopping cart, filters |
| Global State | Store | User session, theme |
| Server State | React Query/SWR | API data |

### Controlled vs Uncontrolled

Support both patterns:

```typescript
interface InputProps {
  // Controlled
  value?: string
  onChange?: (value: string) => void
  // Uncontrolled
  defaultValue?: string
  // Common
  name?: string
}

function Input({ value, onChange, defaultValue, ...props }: InputProps) {
  const [internalValue, setInternalValue] = useState(defaultValue ?? '')

  const isControlled = value !== undefined
  const currentValue = isControlled ? value : internalValue

  const handleChange = (e: ChangeEvent<HTMLInputElement>) => {
    const newValue = e.target.value
    if (!isControlled) {
      setInternalValue(newValue)
    }
    onChange?.(newValue)
  }

  return <input value={currentValue} onChange={handleChange} {...props} />
}
```

## Accessibility

### ARIA Attributes

```typescript
function Button({ children, disabled, loading, ...props }: ButtonProps) {
  return (
    <button
      disabled={disabled || loading}
      aria-disabled={disabled || loading}
      aria-busy={loading}
      {...props}
    >
      {loading ? <Spinner aria-hidden="true" /> : null}
      <span className={loading ? 'sr-only' : undefined}>{children}</span>
    </button>
  )
}
```

### Keyboard Navigation

```typescript
function Menu({ items }: MenuProps) {
  const [activeIndex, setActiveIndex] = useState(0)

  const handleKeyDown = (e: KeyboardEvent) => {
    switch (e.key) {
      case 'ArrowDown':
        e.preventDefault()
        setActiveIndex(i => Math.min(i + 1, items.length - 1))
        break
      case 'ArrowUp':
        e.preventDefault()
        setActiveIndex(i => Math.max(i - 1, 0))
        break
      case 'Enter':
      case ' ':
        e.preventDefault()
        items[activeIndex].onSelect?.()
        break
      case 'Escape':
        onClose?.()
        break
    }
  }

  return (
    <ul role="menu" onKeyDown={handleKeyDown}>
      {items.map((item, index) => (
        <li
          key={item.id}
          role="menuitem"
          tabIndex={index === activeIndex ? 0 : -1}
          aria-selected={index === activeIndex}
        >
          {item.label}
        </li>
      ))}
    </ul>
  )
}
```

### Focus Management

```typescript
function Modal({ isOpen, onClose, children }: ModalProps) {
  const modalRef = useRef<HTMLDivElement>(null)
  const previousActiveElement = useRef<Element | null>(null)

  useEffect(() => {
    if (isOpen) {
      previousActiveElement.current = document.activeElement
      modalRef.current?.focus()
    } else {
      (previousActiveElement.current as HTMLElement)?.focus()
    }
  }, [isOpen])

  // Trap focus inside modal
  const handleKeyDown = (e: KeyboardEvent) => {
    if (e.key === 'Tab') {
      const focusable = modalRef.current?.querySelectorAll(
        'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
      )
      // Focus trap logic...
    }
  }

  return (
    <div
      ref={modalRef}
      role="dialog"
      aria-modal="true"
      tabIndex={-1}
      onKeyDown={handleKeyDown}
    >
      {children}
    </div>
  )
}
```

## Performance

### Memoization

```typescript
// Memoize expensive computations
const processedData = useMemo(() =>
  data.filter(filterFn).sort(sortFn).slice(0, limit),
  [data, filterFn, sortFn, limit]
)

// Memoize callbacks passed to children
const handleClick = useCallback(() => {
  onSelect(item.id)
}, [item.id, onSelect])

// Memoize components that receive stable props
const MemoizedRow = memo(function Row({ data }: RowProps) {
  return <tr>...</tr>
})
```

### Code Splitting

```typescript
// Lazy load heavy components
const DataTable = lazy(() => import('@/organisms/DataTable'))
const Chart = lazy(() => import('@/organisms/Chart'))

function Dashboard() {
  return (
    <Suspense fallback={<Skeleton />}>
      <DataTable data={data} />
      <Chart data={chartData} />
    </Suspense>
  )
}
```

### Virtual Lists

```typescript
// For long lists, use virtualization
import { useVirtualizer } from '@tanstack/react-virtual'

function VirtualList({ items }: { items: Item[] }) {
  const parentRef = useRef<HTMLDivElement>(null)

  const virtualizer = useVirtualizer({
    count: items.length,
    getScrollElement: () => parentRef.current,
    estimateSize: () => 50,
  })

  return (
    <div ref={parentRef} style={{ height: '400px', overflow: 'auto' }}>
      <div style={{ height: virtualizer.getTotalSize() }}>
        {virtualizer.getVirtualItems().map(virtual => (
          <div
            key={virtual.key}
            style={{
              position: 'absolute',
              top: virtual.start,
              height: virtual.size,
            }}
          >
            {items[virtual.index].name}
          </div>
        ))}
      </div>
    </div>
  )
}
```

## Anti-Patterns to Avoid

### 1. Prop Explosion

```typescript
// BAD - Too many props
<Button
  label="Submit"
  icon="check"
  iconPosition="left"
  size="medium"
  variant="primary"
  fullWidth={true}
  rounded={true}
  shadow={true}
  loading={false}
  disabled={false}
  tooltip="Click to submit"
  tooltipPosition="top"
  // ... 20 more props
/>

// GOOD - Composable with sensible defaults
<Button variant="primary">
  <Icon name="check" />
  Submit
</Button>
```

### 2. Leaky Abstractions

```typescript
// BAD - Exposing implementation details
<DataTable
  onSqlQuery={handleSql}           // Leaking database
  reduxAction={updateTableAction}  // Leaking state management
  domRef={tableRef}                // Leaking DOM
/>

// GOOD - Clean interface
<DataTable
  data={data}
  columns={columns}
  onRowSelect={handleSelect}
  onSort={handleSort}
/>
```

### 3. Tight Coupling

```typescript
// BAD - Tightly coupled to specific data shape
function UserCard({ user }: { user: User }) {
  return (
    <div>
      <img src={user.profile.avatar.url} />  // Deeply nested access
      <span>{user.name.first} {user.name.last}</span>
    </div>
  )
}

// GOOD - Loosely coupled
interface UserCardProps {
  avatarUrl: string
  fullName: string
}

function UserCard({ avatarUrl, fullName }: UserCardProps) {
  return (
    <div>
      <img src={avatarUrl} />
      <span>{fullName}</span>
    </div>
  )
}
```

### 4. Premature Abstraction

```typescript
// BAD - Over-abstracted too early
function GenericCard<T extends object>({
  data,
  renderHeader,
  renderBody,
  renderFooter,
  headerComponent: HeaderComponent,
  bodyComponent: BodyComponent,
  // ... complex generic patterns for "flexibility"
})

// GOOD - Start simple, abstract when patterns emerge
function ProductCard({ product }: { product: Product }) {
  return (
    <Card>
      <Card.Image src={product.image} />
      <Card.Title>{product.name}</Card.Title>
      <Card.Price value={product.price} />
    </Card>
  )
}
```

### 5. Inconsistent Patterns

```typescript
// BAD - Inconsistent event naming
<Button onClick={handleClick} />     // onClick
<Input onValueChange={handleInput} /> // onValueChange
<Select whenChanged={handleSelect} /> // whenChanged

// GOOD - Consistent patterns
<Button onClick={handleClick} />
<Input onChange={handleInput} />
<Select onChange={handleSelect} />
```

## Documentation

### Component Documentation

```typescript
/**
 * Primary button component for user actions.
 *
 * @example
 * ```tsx
 * <Button variant="primary" onClick={handleSubmit}>
 *   Submit Form
 * </Button>
 * ```
 */
export interface ButtonProps {
  /**
   * Visual style variant
   * @default 'primary'
   */
  variant?: 'primary' | 'secondary' | 'ghost'

  /**
   * Button size
   * @default 'md'
   */
  size?: 'sm' | 'md' | 'lg'

  /**
   * Disables the button
   * @default false
   */
  disabled?: boolean

  /** Click event handler */
  onClick?: (event: MouseEvent) => void

  /** Button content */
  children: ReactNode
}
```

### README per Component

```markdown
# Button

Primary action button component.

## Usage

\`\`\`tsx
import { Button } from '@/atoms/Button'

<Button variant="primary" onClick={handleClick}>
  Click Me
</Button>
\`\`\`

## Props

| Prop | Type | Default | Description |
|------|------|---------|-------------|
| variant | `'primary' \| 'secondary' \| 'ghost'` | `'primary'` | Visual style |
| size | `'sm' \| 'md' \| 'lg'` | `'md'` | Button size |
| disabled | `boolean` | `false` | Disabled state |

## Accessibility

- Uses native `<button>` element
- Supports keyboard focus
- `aria-disabled` when disabled
```
