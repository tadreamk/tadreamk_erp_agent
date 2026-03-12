# DELETE /equipment/{equipment_id}


Soft delete an equipment record. If the equipment has an associated calendar event (Software license renewal), the calendar event is also deleted.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | Equipment record ID |

**Response:**
```json
{
  "message": "Equipment deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to equipment management
- `404` — Equipment not found
