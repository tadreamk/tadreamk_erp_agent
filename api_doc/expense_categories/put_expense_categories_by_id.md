# PUT /expense-categories/{category_id}

Update an existing expense category. Only provided fields are updated. If changing the title, it must remain unique.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| category_id | UUID | Category ID |

**Request Body:**
```json
{
  "title": "Updated Title",
  "description": "Updated description"
}
```

All fields are optional.

**Response:**
```json
{
  "id": "uuid",
  "title": "Updated Title",
  "description": "Updated description",
  "is_active": true,
  "updated_by": "username",
  "updated_at": "2026-03-19T14:00:00+00:00"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | A category with this title already exists |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Category not found |
