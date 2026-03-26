# GET /admin/leave/requests/pending

Get pending leave requests awaiting approval. Requires `leave-management` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
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
- `403` — No leave-management whitelist access
