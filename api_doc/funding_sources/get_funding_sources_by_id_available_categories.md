# GET /funding-sources/{source_id}/available-categories


List expense categories that have not yet been allocated to this funding source. Useful for populating dropdowns when creating new allocations.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | Funding source ID |

**Response:**
```json
[
  {
    "id": "uuid",
    "title": "Travel & Transportation",
    "description": "Business travel and transportation expenses",
    "created_at": "2026-01-01T00:00:00",
    "updated_at": null,
    "updated_by": null
  }
]
```

**Errors:**
- `404` -- Funding source not found
