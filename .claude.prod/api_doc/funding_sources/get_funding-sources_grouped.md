# GET /funding-sources/grouped

List all funding sources grouped by expense category. Requires `funding-sources` whitelist.

**Response:**
```json
[
  {
    "category_id": "uuid",
    "category_title": "Travel",
    "category_description": "Travel expenses",
    "total_allocated": 50000.0,
    "sources": [
      {
        "id": "uuid",
        "source_name": "Grant ABC",
        "funding_type": "Grant",
        "total_approved": 100000.0,
        "status": "active"
      }
    ]
  }
]
```

**Errors:**
- `401` — Not authenticated
- `403` — No funding-sources whitelist access
