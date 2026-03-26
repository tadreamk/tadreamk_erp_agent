# PUT /expense-categories/{category_id}/reactivate

Reactivate a previously deactivated expense category. Requires `expense-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_id | UUID | The category's unique identifier |

**Response:**
```json
{
  "message": "Category 'Travel' reactivated"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No expense-management whitelist access
- `404` — Category not found
