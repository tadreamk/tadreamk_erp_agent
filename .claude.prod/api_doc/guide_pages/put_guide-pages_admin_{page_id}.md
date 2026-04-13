# PUT /guide-pages/admin/{page_id}

Update an existing guide page. Requires `guide-pages` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| page_id | UUID | The guide page's unique identifier |

**Request Body:** (all fields optional, same as POST)

**Response:** Updated guide page object

**Errors:**
- `401` — Not authenticated
- `403` — No guide-pages whitelist access
- `404` — Guide page not found
