# POST /timesheet-workflow/{workflow_id}/reject

Manager rejects a submitted timesheet. Only the manager can reject. Status must be `submitted`.

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| workflow_id | uuid | Yes | Timesheet workflow ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| reason | string | No | Rejection reason |

**Response:**
```json
{
  "message": "Timesheet rejected",
  "status": "rejected"
}
```

**Errors:**
- `400` — Cannot reject at current status (must be `submitted`)
- `401` — Not authenticated
- `403` — Only the manager can reject
- `404` — Timesheet not found
