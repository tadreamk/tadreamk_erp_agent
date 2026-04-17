# POST /customer-requirements/{id}/rotate-token

Regenerate the public share token so the old `/shared/customer-requirements/{old_token}` URL returns 404 and a new URL replaces it. Requires `customer-requirements` whitelist.

**Request body:** empty.

**Response:**
```json
{ "share_token": "NEWTOKEN5678" }
```

**Errors:** `401`, `403`, `404`.
