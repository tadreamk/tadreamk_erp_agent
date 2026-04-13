# GET /leave/my-requests

Get the current user's leave requests. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status_filter | string | No | Filter by status |
| leave_type | string | No | Filter by leave type |
| page | int | No | Page number (default: 1) |
| limit | int | No | Max results (default: 50) |

**Response:**
```json
{
  "requests": [ { "...leave request..." } ],
  "total": 5,
  "page": 1,
  "limit": 50
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
