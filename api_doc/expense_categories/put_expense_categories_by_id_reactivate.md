# PUT /expense-categories/{category_id}/reactivate

Reactivate a previously deactivated expense category.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_id | UUID | Category ID |

**Response:**
```json
{
  "message": "Category 'Equipment' reactivated"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Category not found |
