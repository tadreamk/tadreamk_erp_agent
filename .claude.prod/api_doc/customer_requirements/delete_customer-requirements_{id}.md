# DELETE /customer-requirements/{id}

Soft-delete a requirement (sets `is_active = false`). The public URL for the share token returns 404 thereafter. Requires `customer-requirements` whitelist.

**Response:**
```json
{ "message": "Requirement deleted successfully" }
```

**Errors:** `401`, `403`, `404`.
