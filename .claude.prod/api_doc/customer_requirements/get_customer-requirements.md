# GET /customer-requirements

List customer requirements. Requires `customer-requirements` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by dashboard status (`Draft`, `Active`, `Delivered`, `Archived`) |
| search | string | No | Case-insensitive substring match on title |
| skip | int | No | Offset (default 0) |
| limit | int | No | Page size (default 50, max 100) |

**Response:**
```json
[
  {
    "id": "uuid",
    "share_token": "abcdef123456",
    "title": "Example Requirement",
    "summary": "short dashboard description",
    "status": "Active",
    "share_mode": "edit",
    "created_by": "alannguyen",
    "created_at": "2026-04-16T10:00:00+00:00",
    "updated_at": "2026-04-16T12:00:00+00:00"
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No customer-requirements whitelist access
