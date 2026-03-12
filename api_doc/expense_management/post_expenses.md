# POST /expenses


Create a new manual expense.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| expense_category_id | UUID | Yes | FK to expense category |
| total_value | decimal | Yes | Total expense amount (>= 0) |
| note | string | No | Additional notes |
| file_urls | string[] | No | List of supporting document URLs (default: []) |

**Response:** Full expense object (same shape as GET by ID).

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to expense management
