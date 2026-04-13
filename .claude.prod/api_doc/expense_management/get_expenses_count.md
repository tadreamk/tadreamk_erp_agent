# GET /expenses/count

Get count of expenses with optional filters. Requires `expense-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status |
| expense_category_id | UUID | No | Filter by category |
| source_type | string | No | Filter by source type |
| q | string | No | Word-split text search across note, category name, and employee username |

**Response:**
```json
{
  "count": 42
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
