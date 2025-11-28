# Wave [N]: [Description]

## Status

- **State:** ⬜ Pending | 🔄 In Progress | ✅ Complete
- **Dependencies:** Wave [N-1] | None
- **Tasks:** [X] total, [Y] complete
- **Started:** -
- **Completed:** -

## Task Summary

| ID | Task | Type | Status | Effort | Review |
|----|------|------|--------|--------|--------|
| T1 | Database Schema | database | ⬜ | M | - |
| T2 | Auth Setup | backend | ⬜ | M | - |
| T3 | Frontend Init | frontend | ⬜ | S | - |

---

## T1: Database Schema

**Type:** database
**Component:** Data Layer
**Priority:** P1
**Effort:** M

**Description:**
Set up database schema with Prisma. Create initial migrations for all core entities.

**Subtasks:**
- [ ] 1.1: Initialize Prisma with PostgreSQL
- [ ] 1.2: Define User model with auth fields
- [ ] 1.3: Define [Entity] model
- [ ] 1.4: Define relationships
- [ ] 1.5: Create initial migration
- [ ] 1.6: Add seed data script

**Acceptance Criteria:**
- [ ] Schema matches design.md data model (R1.1)
- [ ] All required fields present (R1.2)
- [ ] Migration runs without errors (R1.3)
- [ ] Seed data creates valid test records (R1.4)

**Files:**
- `prisma/schema.prisma` (new)
- `prisma/migrations/[timestamp]_init/` (new)
- `prisma/seed.ts` (new)
- `package.json` (modify - add prisma scripts)

**Status:** ⬜ Not Started
**Completed:** -
**Review:** -
**Notes:** -

---

## T2: Auth Setup

**Type:** backend
**Component:** Authentication
**Priority:** P1
**Effort:** M

**Description:**
Implement authentication system with JWT tokens and secure password handling.

**Subtasks:**
- [ ] 2.1: Install auth dependencies (bcrypt, jsonwebtoken)
- [ ] 2.2: Create auth utility functions
- [ ] 2.3: Implement register endpoint
- [ ] 2.4: Implement login endpoint
- [ ] 2.5: Create auth middleware
- [ ] 2.6: Add token refresh logic

**Acceptance Criteria:**
- [ ] Passwords securely hashed (R2.1)
- [ ] JWT tokens generated correctly (R2.2)
- [ ] Auth middleware protects routes (R2.3)
- [ ] Token refresh works (R2.4)

**Files:**
- `src/utils/auth.ts` (new)
- `src/middleware/authMiddleware.ts` (new)
- `src/routes/auth.ts` (new)
- `src/controllers/authController.ts` (new)

**Status:** ⬜ Not Started
**Completed:** -
**Review:** -
**Notes:** -

---

## T3: Frontend Init

**Type:** frontend
**Component:** UI Foundation
**Priority:** P1
**Effort:** S

**Description:**
Initialize frontend project with React, routing, and base layout components.

**Subtasks:**
- [ ] 3.1: Create React app with Vite
- [ ] 3.2: Set up React Router
- [ ] 3.3: Create base layout component
- [ ] 3.4: Add Tailwind CSS
- [ ] 3.5: Create placeholder pages

**Acceptance Criteria:**
- [ ] App builds without errors (R3.1)
- [ ] Routing works between pages (R3.2)
- [ ] Tailwind classes apply correctly (R3.3)

**Files:**
- `frontend/src/App.tsx` (new)
- `frontend/src/components/Layout.tsx` (new)
- `frontend/src/pages/Home.tsx` (new)
- `frontend/src/pages/Login.tsx` (new)
- `frontend/tailwind.config.js` (new)

**Status:** ⬜ Not Started
**Completed:** -
**Review:** -
**Notes:** -

---

## Wave Completion Checklist

Before marking wave complete:

- [ ] All tasks have status ✅
- [ ] All reviews passed
- [ ] All acceptance criteria verified
- [ ] index.md updated with new counts
- [ ] No blocking issues remain
- [ ] Ready for Wave [N+1]

## Execution Log

| Time | Event | Details |
|------|-------|---------|
| - | Wave started | - |
| - | T1 started | - |
| - | T1 completed | - |
| - | Wave completed | - |
