# PUT /customer-requirements/{id}

Partial update on an existing requirement. Requires `customer-requirements` whitelist.

**Request body (all fields optional):**
```json
{
  "title": "Renamed Requirement",
  "summary": "new summary",
  "status": "Delivered",
  "share_mode": "disabled"
}
```

**Response:** `CustomerRequirementResponse`.

**Errors:** `401`, `403`, `404`, `422`.
