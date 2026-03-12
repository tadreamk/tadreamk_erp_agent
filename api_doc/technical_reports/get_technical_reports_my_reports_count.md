# GET /technical-reports/my-reports/count


Get count of technical reports submitted by the authenticated employee.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by report status |
| search | string | No | Search in report titles/descriptions |

**Response:**
```json
{
  "count": 5
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can submit technical reports
