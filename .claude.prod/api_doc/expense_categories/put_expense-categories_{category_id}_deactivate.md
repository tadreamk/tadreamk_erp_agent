# PUT /expense-categories/{category_id}/deactivate

Deactivate an expense category (soft delete). Requires `expense-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_id | UUID | The category's unique identifier |

**Response:**
```json
{
  "message": "Category 'Travel' deactivated"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
- `404` — Category not found
