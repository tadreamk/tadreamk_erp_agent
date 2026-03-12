# GET /equipment/count


Get total count of equipment matching the given filters.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status |
| category | string | No | Filter by category |
| employee_username | string | No | Filter by assigned employee username |
| search | string | No | Search across equipment fields |

**Response:**
```json
{
  "count": 42
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to equipment management
