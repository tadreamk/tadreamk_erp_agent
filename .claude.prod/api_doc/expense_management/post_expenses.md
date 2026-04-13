# POST /expenses

Create a new manual expense. Requires `expense-management` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| expense_category_id | UUID | Yes | FK to expense_categories |
| total_value | decimal | Yes | Total expense amount (>= 0) |
| note | string | No | Additional notes |
| file_urls | list[string] | No | Supporting document URLs (default: []) |

**Response:** Created expense object

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
