# GET /customer-requirements/count

Return the count of active requirements matching the same filters as `GET /customer-requirements`.

**Query Parameters:** `status`, `search` (same semantics as the list endpoint).

**Response:**
```json
{ "count": 12 }
```

**Errors:** `401`, `403` (same as list).
