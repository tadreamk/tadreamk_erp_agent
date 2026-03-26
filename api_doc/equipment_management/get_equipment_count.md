# GET /equipment/count

Get count of equipment with optional filters. Requires `equipment-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by status |
| category | string | No | Filter by category |
| employee_username | string | No | Filter by assigned employee |
| search | string | No | Search by name or serial number |

**Response:**
```json
{
  "count": 42
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
