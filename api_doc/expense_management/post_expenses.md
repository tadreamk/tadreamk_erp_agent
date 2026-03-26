# POST /expenses

Create a new manual expense. Requires `expense-management` whitelist.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Expense title |
| amount | decimal | Yes | Expense amount |
| currency | string | No | Currency (default: HKD) |
| expense_category_id | UUID | No | Expense category ID |
| description | string | No | Description |
| expense_date | date | No | Date of expense |
| source_type | string | No | Source type (default: manual) |
| funding_allocation | list | No | Funding source allocations |

**Response:** Created expense object

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
