# GET /expenses/{expense_id}

Get a specific expense by ID. Requires `expense-management` whitelist or CEO role.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | The expense's unique identifier |

**Response:** Full expense object including `title` (string, nullable — auto-generated on creation, editable) and funding allocation details

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
- `404` — Expense not found
