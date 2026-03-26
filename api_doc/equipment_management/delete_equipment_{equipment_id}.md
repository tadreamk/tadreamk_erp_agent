# DELETE /equipment/{equipment_id}

Soft delete an equipment record. If the equipment has an associated calendar event, it is also deleted. Requires `equipment-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | The equipment's unique identifier |

**Response:**
```json
{
  "message": "Equipment deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
- `404` — Equipment not found
