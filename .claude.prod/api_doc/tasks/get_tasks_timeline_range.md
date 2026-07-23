# GET /tasks/timeline/range

Get Tasks Timeline. Public endpoint (no auth).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| start | string | Yes | Start date of range (inclusive) |
| end | string | Yes | End date of range (inclusive) |

**Response:**
```json
{}
```

**Errors:**
- `422` — Validation Error
