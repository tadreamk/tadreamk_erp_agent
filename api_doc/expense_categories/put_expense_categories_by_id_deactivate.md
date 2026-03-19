# PUT /expense-categories/{category_id}/deactivate

Deactivate an expense category (soft delete). Deactivated categories won't appear in default listings or dropdowns.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_id | UUID | Category ID |

**Response:**
```json
{
  "message": "Category 'Equipment' deactivated"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Category not found |
