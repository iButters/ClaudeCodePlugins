# Technical Design

## Overview
[2-3 sentence architecture summary]

**Project:** [Name]
**Version:** 1.0
**Last Updated:** [Date]

## Architecture Decision Records

### ADR-1: [Decision Title]
**Decision:** [Chosen approach]
**Context:** [Why this decision was needed]
**Options Considered:**
- Option A: [pros/cons]
- Option B: [pros/cons]
**Rationale:** [Why chosen option]

### ADR-2: [Decision Title]
**Decision:** [Chosen approach]
**Rationale:** [Why]

## Tech Stack

| Layer | Technology | Version | Rationale |
|-------|------------|---------|-----------|
| Language | [e.g., TypeScript] | [5.x] | [Why] |
| Runtime | [e.g., Node.js] | [20.x] | [Why] |
| Framework | [e.g., Express] | [4.x] | [Why] |
| Database | [e.g., PostgreSQL] | [15.x] | [Why] |
| ORM | [e.g., Prisma] | [5.x] | [Why] |

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      Client Layer                        │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │   Web App   │  │  Mobile App │  │   CLI       │     │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘     │
└─────────┼────────────────┼────────────────┼─────────────┘
          │                │                │
          └────────────────┼────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                      API Layer                           │
│  ┌─────────────────────────────────────────────────┐    │
│  │              REST API / GraphQL                  │    │
│  └─────────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                    Service Layer                         │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐              │
│  │  Auth    │  │  Users   │  │  [Other] │              │
│  │ Service  │  │ Service  │  │ Service  │              │
│  └──────────┘  └──────────┘  └──────────┘              │
└─────────────────────────────────────────────────────────┘
                           │
┌──────────────────────────▼──────────────────────────────┐
│                    Data Layer                            │
│  ┌──────────────────┐  ┌──────────────────┐            │
│  │    PostgreSQL    │  │      Redis       │            │
│  │   (Primary DB)   │  │     (Cache)      │            │
│  └──────────────────┘  └──────────────────┘            │
└─────────────────────────────────────────────────────────┘
```

## Component Design

### Component: [Name]
**Responsibility:** [Single responsibility]
**Interfaces:**
- Input: [What it receives]
- Output: [What it produces]
**Dependencies:** [Other components]

### Component: [Name]
**Responsibility:** [Single responsibility]
**Dependencies:** [Other components]

## Data Model

### Entity: User
```
id: string (cuid)
email: string (unique)
name: string
password: string (hashed)
role: enum (USER, ADMIN)
createdAt: datetime
updatedAt: datetime
```

### Entity: [Other]
```
[Field definitions]
```

### Relationships
- User 1:N [Related Entity]

## API Design

### Endpoint: POST /api/users
**Purpose:** Create a new user
**Request:**
```json
{
  "email": "string",
  "password": "string",
  "name": "string"
}
```
**Response (201):**
```json
{
  "id": "string",
  "email": "string",
  "name": "string",
  "createdAt": "datetime"
}
```
**Errors:**
- 400: Validation error
- 409: Email already exists

### Endpoint: GET /api/users/:id
**Purpose:** Get user by ID
**Response (200):**
```json
{
  "id": "string",
  "email": "string",
  "name": "string"
}
```
**Errors:**
- 404: User not found

## Security Design

### Authentication
- Strategy: JWT tokens
- Token expiry: 1 hour
- Refresh token: 7 days

### Authorization
- Role-based access control (RBAC)
- Roles: USER, ADMIN

### Data Protection
- Passwords: bcrypt hashing
- Sensitive data: AES-256 encryption
- Transport: HTTPS only

## Deployment Architecture

### Environments
- Development: Local Docker
- Staging: [Cloud provider]
- Production: [Cloud provider]

### CI/CD
- GitHub Actions
- Automated tests on PR
- Deploy on merge to main

## Requirements Traceability

| Requirement | Component(s) | Notes |
|-------------|--------------|-------|
| R1 | [Component] | [How addressed] |
| R2 | [Component] | [How addressed] |
