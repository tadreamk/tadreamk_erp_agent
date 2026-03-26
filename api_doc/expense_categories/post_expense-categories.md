# POST /expense-categories

Create a new expense category. Requires `expense-management` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Category title (must be unique) |
| description | string | No | Category description |

**Response:** Expense category object

**Errors:**
- `400` — A category with this title already exists
- `401` — Not authenticated
- `403` — No expense-management whitelist access
