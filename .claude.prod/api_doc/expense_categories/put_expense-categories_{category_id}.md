# PUT /expense-categories/{category_id}

Update an existing expense category. Requires `expense-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_id | UUID | The category's unique identifier |

**Request Body:** (all fields optional)
| Field | Type | Description |
|-------|------|-------------|
| title | string | Category title (must be unique) |
| description | string | Category description |

**Response:** Updated expense category object

**Errors:**
- `400` — A category with this title already exists
- `401` — Not authenticated
- `403` — No expense-management whitelist access
- `404` — Category not found
