# PUT /expenses/{expense_id}/allocation

Update funding allocation for an expense. Requires `expense-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| expense_id | UUID | The expense's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| funding_allocation | list | Yes | List of funding source allocations |

Each allocation item:
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| funding_source_id | UUID | Yes | Funding source ID |
| amount | decimal | Yes | Amount allocated |

**Response:** Updated expense object

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
- `404` — Expense not found
