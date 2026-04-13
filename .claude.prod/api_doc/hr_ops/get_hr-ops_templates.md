# GET /hr-ops/templates

List active templates for the Create Workflow modal.

**Auth:** Requires `hr-ops` whitelist access.

**Response:** `200 OK`
```json
{
  "templates": [
    {
      "id": "uuid",
      "title": "Employee Warning Letter",
      "category": "disciplinary"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to hr-ops section
