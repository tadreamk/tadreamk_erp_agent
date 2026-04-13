# GET /funding-sources/{source_id}/available-categories

List expense categories not yet allocated to this funding source.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | The funding source's unique identifier |

**Auth:** Requires `funding-sources` whitelist access.

**Response:** `200 OK` — Array of `ExpenseCategoryResponse`
```json
[
  {
    "id": "uuid",
    "title": "Equipment",
    "description": "Equipment purchases",
    "is_active": true,
    "created_at": "2024-01-01T00:00:00",
    "updated_at": null,
    "updated_by": null
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on funding-sources whitelist
- `404` — Funding source not found
