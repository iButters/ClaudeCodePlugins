# Atomic Design Component Examples

## Atoms

### Button

```typescript
// atoms/Button/Button.types.ts
export type ButtonVariant = 'primary' | 'secondary' | 'ghost' | 'danger'
export type ButtonSize = 'sm' | 'md' | 'lg'

export interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: ButtonVariant
  size?: ButtonSize
  loading?: boolean
  leftIcon?: React.ReactNode
  rightIcon?: React.ReactNode
  fullWidth?: boolean
}
```

```typescript
// atoms/Button/Button.tsx
import { forwardRef } from 'react'
import { cn } from '@/utils/cn'
import { Spinner } from '@/atoms/Spinner'
import type { ButtonProps } from './Button.types'

export const Button = forwardRef<HTMLButtonElement, ButtonProps>(
  (
    {
      variant = 'primary',
      size = 'md',
      loading = false,
      leftIcon,
      rightIcon,
      fullWidth = false,
      disabled,
      className,
      children,
      ...props
    },
    ref
  ) => {
    const isDisabled = disabled || loading

    return (
      <button
        ref={ref}
        disabled={isDisabled}
        aria-disabled={isDisabled}
        aria-busy={loading}
        className={cn(
          'inline-flex items-center justify-center font-medium transition-colors',
          'focus:outline-none focus:ring-2 focus:ring-offset-2',
          'disabled:opacity-50 disabled:cursor-not-allowed',
          {
            // Variants
            'bg-primary-600 text-white hover:bg-primary-700 focus:ring-primary-500':
              variant === 'primary',
            'bg-neutral-100 text-neutral-900 hover:bg-neutral-200 focus:ring-neutral-500':
              variant === 'secondary',
            'bg-transparent text-neutral-700 hover:bg-neutral-100 focus:ring-neutral-500':
              variant === 'ghost',
            'bg-red-600 text-white hover:bg-red-700 focus:ring-red-500':
              variant === 'danger',
            // Sizes
            'text-sm px-3 py-1.5 rounded': size === 'sm',
            'text-base px-4 py-2 rounded-md': size === 'md',
            'text-lg px-6 py-3 rounded-lg': size === 'lg',
            // Full width
            'w-full': fullWidth,
          },
          className
        )}
        {...props}
      >
        {loading && <Spinner size="sm" className="mr-2" />}
        {!loading && leftIcon && <span className="mr-2">{leftIcon}</span>}
        {children}
        {!loading && rightIcon && <span className="ml-2">{rightIcon}</span>}
      </button>
    )
  }
)

Button.displayName = 'Button'
```

### Input

```typescript
// atoms/Input/Input.types.ts
export type InputSize = 'sm' | 'md' | 'lg'

export interface InputProps extends Omit<React.InputHTMLAttributes<HTMLInputElement>, 'size'> {
  size?: InputSize
  error?: boolean
  leftAddon?: React.ReactNode
  rightAddon?: React.ReactNode
}
```

```typescript
// atoms/Input/Input.tsx
import { forwardRef } from 'react'
import { cn } from '@/utils/cn'
import type { InputProps } from './Input.types'

export const Input = forwardRef<HTMLInputElement, InputProps>(
  ({ size = 'md', error = false, leftAddon, rightAddon, className, ...props }, ref) => {
    return (
      <div className="relative flex items-center">
        {leftAddon && (
          <div className="absolute left-3 text-neutral-500">{leftAddon}</div>
        )}
        <input
          ref={ref}
          aria-invalid={error}
          className={cn(
            'w-full border rounded-md transition-colors',
            'focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500',
            'disabled:bg-neutral-100 disabled:cursor-not-allowed',
            {
              'border-neutral-300 hover:border-neutral-400': !error,
              'border-red-500 focus:ring-red-500 focus:border-red-500': error,
              'text-sm py-1.5 px-3': size === 'sm',
              'text-base py-2 px-4': size === 'md',
              'text-lg py-3 px-5': size === 'lg',
              'pl-10': leftAddon,
              'pr-10': rightAddon,
            },
            className
          )}
          {...props}
        />
        {rightAddon && (
          <div className="absolute right-3 text-neutral-500">{rightAddon}</div>
        )}
      </div>
    )
  }
)

Input.displayName = 'Input'
```

## Molecules

### SearchBar

```typescript
// molecules/SearchBar/SearchBar.types.ts
export interface SearchBarProps {
  value?: string
  defaultValue?: string
  placeholder?: string
  onSearch?: (query: string) => void
  onChange?: (value: string) => void
  loading?: boolean
  className?: string
}
```

```typescript
// molecules/SearchBar/SearchBar.tsx
import { useState, useCallback } from 'react'
import { Button } from '@/atoms/Button'
import { Input } from '@/atoms/Input'
import { Icon } from '@/atoms/Icon'
import type { SearchBarProps } from './SearchBar.types'

export function SearchBar({
  value,
  defaultValue = '',
  placeholder = 'Search...',
  onSearch,
  onChange,
  loading = false,
  className,
}: SearchBarProps) {
  const [internalValue, setInternalValue] = useState(defaultValue)
  const isControlled = value !== undefined
  const currentValue = isControlled ? value : internalValue

  const handleChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const newValue = e.target.value
      if (!isControlled) {
        setInternalValue(newValue)
      }
      onChange?.(newValue)
    },
    [isControlled, onChange]
  )

  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault()
      onSearch?.(currentValue)
    },
    [currentValue, onSearch]
  )

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      if (e.key === 'Enter') {
        onSearch?.(currentValue)
      }
    },
    [currentValue, onSearch]
  )

  return (
    <form onSubmit={handleSubmit} className={className}>
      <div className="flex gap-2">
        <Input
          type="search"
          value={currentValue}
          onChange={handleChange}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          leftAddon={<Icon name="search" size="sm" />}
          aria-label="Search"
        />
        <Button type="submit" loading={loading} aria-label="Submit search">
          Search
        </Button>
      </div>
    </form>
  )
}
```

### FormField

```typescript
// molecules/FormField/FormField.types.ts
export interface FormFieldProps {
  label: string
  name: string
  error?: string
  hint?: string
  required?: boolean
  children: React.ReactElement
}
```

```typescript
// molecules/FormField/FormField.tsx
import { cloneElement } from 'react'
import { Label } from '@/atoms/Label'
import { Text } from '@/atoms/Text'
import type { FormFieldProps } from './FormField.types'

export function FormField({
  label,
  name,
  error,
  hint,
  required = false,
  children,
}: FormFieldProps) {
  const inputId = `field-${name}`
  const errorId = `${inputId}-error`
  const hintId = `${inputId}-hint`

  const describedBy = [error && errorId, hint && hintId].filter(Boolean).join(' ')

  return (
    <div className="flex flex-col gap-1.5">
      <Label htmlFor={inputId} required={required}>
        {label}
      </Label>

      {cloneElement(children, {
        id: inputId,
        name,
        error: !!error,
        'aria-describedby': describedBy || undefined,
        'aria-required': required,
      })}

      {hint && !error && (
        <Text id={hintId} size="sm" color="muted">
          {hint}
        </Text>
      )}

      {error && (
        <Text id={errorId} size="sm" color="error" role="alert">
          {error}
        </Text>
      )}
    </div>
  )
}
```

## Organisms

### Header

```typescript
// organisms/Header/Header.types.ts
export interface NavItem {
  id: string
  label: string
  href: string
  icon?: string
  badge?: string | number
}

export interface HeaderProps {
  logo?: React.ReactNode
  navItems?: NavItem[]
  user?: {
    name: string
    avatar?: string
  }
  onSearch?: (query: string) => void
  onLogout?: () => void
  className?: string
}
```

```typescript
// organisms/Header/Header.tsx
import { useState } from 'react'
import { Logo } from '@/atoms/Logo'
import { Avatar } from '@/atoms/Avatar'
import { Button } from '@/atoms/Button'
import { Icon } from '@/atoms/Icon'
import { NavLink } from '@/molecules/NavLink'
import { SearchBar } from '@/molecules/SearchBar'
import { Dropdown } from '@/molecules/Dropdown'
import type { HeaderProps } from './Header.types'

export function Header({
  logo,
  navItems = [],
  user,
  onSearch,
  onLogout,
  className,
}: HeaderProps) {
  const [mobileMenuOpen, setMobileMenuOpen] = useState(false)

  return (
    <header className={cn('bg-white border-b border-neutral-200', className)}>
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex items-center justify-between h-16">
          {/* Logo */}
          <div className="flex-shrink-0">
            {logo || <Logo />}
          </div>

          {/* Desktop Navigation */}
          <nav className="hidden md:flex items-center gap-1">
            {navItems.map((item) => (
              <NavLink
                key={item.id}
                href={item.href}
                icon={item.icon}
                badge={item.badge}
              >
                {item.label}
              </NavLink>
            ))}
          </nav>

          {/* Search */}
          {onSearch && (
            <div className="hidden md:block flex-1 max-w-md mx-8">
              <SearchBar onSearch={onSearch} />
            </div>
          )}

          {/* User Menu */}
          <div className="flex items-center gap-4">
            {user ? (
              <Dropdown
                trigger={
                  <button className="flex items-center gap-2">
                    <Avatar src={user.avatar} alt={user.name} size="sm" />
                    <span className="hidden lg:block">{user.name}</span>
                    <Icon name="chevron-down" size="sm" />
                  </button>
                }
                items={[
                  { label: 'Profile', href: '/profile' },
                  { label: 'Settings', href: '/settings' },
                  { type: 'divider' },
                  { label: 'Logout', onClick: onLogout },
                ]}
              />
            ) : (
              <Button variant="primary" href="/login">
                Sign In
              </Button>
            )}

            {/* Mobile Menu Button */}
            <button
              className="md:hidden p-2"
              onClick={() => setMobileMenuOpen(!mobileMenuOpen)}
              aria-expanded={mobileMenuOpen}
              aria-label="Toggle menu"
            >
              <Icon name={mobileMenuOpen ? 'x' : 'menu'} />
            </button>
          </div>
        </div>
      </div>

      {/* Mobile Navigation */}
      {mobileMenuOpen && (
        <nav className="md:hidden border-t border-neutral-200 py-4">
          <div className="px-4 space-y-2">
            {navItems.map((item) => (
              <NavLink
                key={item.id}
                href={item.href}
                icon={item.icon}
                className="block"
              >
                {item.label}
              </NavLink>
            ))}
          </div>
        </nav>
      )}
    </header>
  )
}
```

## Templates

### DashboardTemplate

```typescript
// templates/DashboardTemplate/DashboardTemplate.types.ts
export interface DashboardTemplateProps {
  header?: React.ReactNode
  sidebar?: React.ReactNode
  children: React.ReactNode
  footer?: React.ReactNode
  sidebarOpen?: boolean
  onSidebarToggle?: () => void
}
```

```typescript
// templates/DashboardTemplate/DashboardTemplate.tsx
import { cn } from '@/utils/cn'
import type { DashboardTemplateProps } from './DashboardTemplate.types'

export function DashboardTemplate({
  header,
  sidebar,
  children,
  footer,
  sidebarOpen = true,
  onSidebarToggle,
}: DashboardTemplateProps) {
  return (
    <div className="min-h-screen bg-neutral-50">
      {/* Header */}
      {header && (
        <div className="fixed top-0 left-0 right-0 z-40">
          {header}
        </div>
      )}

      <div className="flex pt-16">
        {/* Sidebar */}
        {sidebar && (
          <aside
            className={cn(
              'fixed left-0 top-16 bottom-0 z-30',
              'w-64 bg-white border-r border-neutral-200',
              'transition-transform duration-200 ease-in-out',
              {
                'translate-x-0': sidebarOpen,
                '-translate-x-full': !sidebarOpen,
              }
            )}
          >
            <div className="h-full overflow-y-auto p-4">
              {sidebar}
            </div>
          </aside>
        )}

        {/* Main Content */}
        <main
          className={cn(
            'flex-1 min-h-[calc(100vh-4rem)]',
            'transition-all duration-200 ease-in-out',
            {
              'ml-64': sidebar && sidebarOpen,
              'ml-0': !sidebar || !sidebarOpen,
            }
          )}
        >
          <div className="p-6">
            {children}
          </div>
        </main>
      </div>

      {/* Footer */}
      {footer && (
        <footer
          className={cn(
            'border-t border-neutral-200 bg-white',
            {
              'ml-64': sidebar && sidebarOpen,
              'ml-0': !sidebar || !sidebarOpen,
            }
          )}
        >
          {footer}
        </footer>
      )}
    </div>
  )
}

// Skeleton variant for loading state
DashboardTemplate.Skeleton = function DashboardTemplateSkeleton() {
  return (
    <div className="min-h-screen bg-neutral-50 animate-pulse">
      <div className="h-16 bg-neutral-200" />
      <div className="flex pt-16">
        <div className="w-64 h-[calc(100vh-4rem)] bg-neutral-200" />
        <div className="flex-1 p-6 space-y-4">
          <div className="h-8 bg-neutral-200 rounded w-1/4" />
          <div className="h-64 bg-neutral-200 rounded" />
        </div>
      </div>
    </div>
  )
}
```

## Pages

### DashboardPage

```typescript
// pages/Dashboard/DashboardPage.tsx
import { Suspense } from 'react'
import type { Metadata } from 'next'
import { DashboardTemplate } from '@/templates/DashboardTemplate'
import { Header } from '@/organisms/Header'
import { Sidebar } from '@/organisms/Sidebar'
import { StatsGrid } from '@/organisms/StatsGrid'
import { RecentActivity } from '@/organisms/RecentActivity'
import { mockStats, mockActivity, mockNavItems, mockUser } from './data/mock'

export const metadata: Metadata = {
  title: 'Dashboard | My App',
  description: 'View your dashboard and analytics',
  robots: 'noindex', // Authenticated pages shouldn't be indexed
}

export default function DashboardPage() {
  return (
    <DashboardTemplate
      header={
        <Header
          navItems={mockNavItems}
          user={mockUser}
          onSearch={handleSearch}
          onLogout={handleLogout}
        />
      }
      sidebar={
        <Sidebar
          items={mockSidebarItems}
          activeItem="dashboard"
        />
      }
    >
      <div className="space-y-6">
        <h1 className="text-2xl font-bold text-neutral-900">Dashboard</h1>

        <Suspense fallback={<StatsGrid.Skeleton />}>
          <StatsGrid stats={mockStats} />
        </Suspense>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <Suspense fallback={<Card.Skeleton />}>
            <RevenueChart data={mockRevenueData} />
          </Suspense>

          <Suspense fallback={<Card.Skeleton />}>
            <RecentActivity activities={mockActivity} />
          </Suspense>
        </div>
      </div>
    </DashboardTemplate>
  )
}

// Loading state
export function DashboardPageLoading() {
  return <DashboardTemplate.Skeleton />
}

// Error state
export function DashboardPageError({ error, reset }: { error: Error; reset: () => void }) {
  return (
    <DashboardTemplate>
      <div className="flex flex-col items-center justify-center h-64">
        <h2 className="text-xl font-semibold text-neutral-900">Something went wrong</h2>
        <p className="text-neutral-600 mt-2">{error.message}</p>
        <Button onClick={reset} className="mt-4">Try again</Button>
      </div>
    </DashboardTemplate>
  )
}
```

```typescript
// pages/Dashboard/data/mock.ts
export const mockStats = [
  {
    id: 'revenue',
    label: 'Total Revenue',
    value: 48250.00,
    change: 12.5,
    trend: 'up' as const,
    format: 'currency',
  },
  {
    id: 'users',
    label: 'Active Users',
    value: 2847,
    change: 8.3,
    trend: 'up' as const,
  },
  {
    id: 'orders',
    label: 'Orders',
    value: 384,
    change: -2.1,
    trend: 'down' as const,
  },
  {
    id: 'conversion',
    label: 'Conversion Rate',
    value: 3.24,
    change: 0.8,
    trend: 'up' as const,
    format: 'percentage',
  },
]

export const mockActivity = [
  {
    id: '1',
    user: { name: 'Sarah Johnson', avatar: '/avatars/sarah.jpg' },
    action: 'created a new project',
    target: 'Marketing Campaign Q4',
    timestamp: '2024-01-15T14:30:00Z',
  },
  {
    id: '2',
    user: { name: 'Mike Chen', avatar: '/avatars/mike.jpg' },
    action: 'completed task',
    target: 'Update landing page',
    timestamp: '2024-01-15T13:45:00Z',
  },
]

export const mockUser = {
  name: 'John Doe',
  avatar: '/avatars/john.jpg',
  email: 'john@example.com',
}
```
