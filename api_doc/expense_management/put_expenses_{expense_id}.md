# PUT /expenses/{expense_id}

Update an existing expense. Requires `expense-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | The expense's unique identifier |

**Request Body:** (all fields optional, same as POST plus `title: string` — optional, overrides the auto-generated title)

**Response:** Updated expense object

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
- `404` — Expense not found
