# GET /technical-reports/my-reports/count

Get the count of technical reports for the authenticated employee. Requires employee authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by report status |
| search | string | No | Search by title or description |

**Response:**
```json
{
  "count": 7
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
