# GET /customer-requirements/{id}

Fetch a single requirement by UUID. Requires `customer-requirements` whitelist.

**Response:**
```json
{
  "id": "uuid",
  "share_token": "abcdef123456",
  "title": "Example Requirement",
  "summary": "short dashboard description",
  "status": "Active",
  "share_mode": "edit",
  "created_by": "alannguyen",
  "is_active": true,
  "created_at": "2026-04-16T10:00:00+00:00",
  "updated_at": "2026-04-16T12:00:00+00:00"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No whitelist access
- `404` — Requirement not found or soft-deleted
