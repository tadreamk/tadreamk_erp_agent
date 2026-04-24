# Renewal Contract Workflow API

Base prefixes: `/renewal-contract-workflow`, `/talent/renewal-contract-workflow`, `/talent/my-documents`.

Authentication: Required. HR access gated by the `renewal-contract-workflow` whitelist endpoint. The assigned CEO (matched on `ceo_username`) has full access to their workflows. The assigned employee accesses their workflow via the `/talent/` endpoints.

## Core CRUD (HR)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/renewal-contract-workflow` | List workflows (filters: `status`, `hr_username`, `employee_username`) |
| GET | `/renewal-contract-workflow/count` | Count workflows |
| GET | `/renewal-contract-workflow/{workflow_id}` | Fetch a workflow (HR, owning employee, or CEO) |
| POST | `/renewal-contract-workflow` | Create a new renewal workflow |
| PUT | `/renewal-contract-workflow/{workflow_id}` | Merge partial `field_values` (respects Signature Lock Rule) |
| DELETE | `/renewal-contract-workflow/{workflow_id}` | Soft-delete |

## Transitions

| Method | Path | Description |
|--------|------|-------------|
| POST | `/renewal-contract-workflow/{workflow_id}/send-to-talent` | `hr_input -> talent_input` (HR) |
| POST | `/renewal-contract-workflow/{workflow_id}/ceo-sign` | Capture CEO signature |
| POST | `/renewal-contract-workflow/{workflow_id}/ceo-reject` | `ceo_signature -> hr_input` with reason |
| POST | `/renewal-contract-workflow/{workflow_id}/finalize` | `ceo_signature -> completed` + contract insert + PDF upload + email |
| POST | `/renewal-contract-workflow/{workflow_id}/cancel` | Any non-completed -> `cancelled` (HR) |
| POST | `/renewal-contract-workflow/{workflow_id}/reopen` | `cancelled -> hr_input` (HR) |

## Internal Notes (HR + CEO only)

| Method | Path | Description |
|--------|------|-------------|
| GET | `/renewal-contract-workflow/{workflow_id}/notes` | List internal notes |
| POST | `/renewal-contract-workflow/{workflow_id}/notes` | Create a note |
| PUT | `/renewal-contract-workflow/{workflow_id}/notes/{note_id}` | Update (author only) |
| DELETE | `/renewal-contract-workflow/{workflow_id}/notes/{note_id}` | Delete (author only) |

## Talent Endpoints

| Method | Path | Description |
|--------|------|-------------|
| GET | `/talent/renewal-contract-workflow` | Active renewal for the logged-in employee (or null) |
| PUT | `/talent/renewal-contract-workflow` | Merge partial talent-side `field_values` |
| POST | `/talent/renewal-contract-workflow/sign` | Capture `talent_signature` (locks the document) |
| POST | `/talent/renewal-contract-workflow/submit` | `talent_input -> ceo_signature` |
| POST | `/talent/renewal-contract-workflow/decline` | `talent_input -> hr_input` + `[Talent Decline]` note |

## Unified Inbox

| Method | Path | Description |
|--------|------|-------------|
| GET | `/talent/my-documents` | Aggregator: talent-facing documents for the current user (renewal contracts wired, follow-ups to add onboarding etc.) |

## Conventions

- **Conflict on duplicate active workflow** — `POST /renewal-contract-workflow` returns `409 Conflict` if an active workflow already exists for the employee.
- **Signature Lock Rule** — once `talent_signature` is non-empty, only `ceo_*` keys (and the talent's own signature) can be merged via `PUT`.
- **Default roles** — `hr_username` defaults to the first active `head_of_hr`, `ceo_username` to the first active `ceo`, resolved via `company_role`.
