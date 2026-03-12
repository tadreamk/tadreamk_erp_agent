# DELETE /company-events/{event_id}


Delete a company event (soft delete). Requires `company-events` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| event_id | UUID | Company event unique identifier |

**Response:**
```json
{
  "success": true,
  "message": "Company event deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to manage company events
- `404` — Company event not found
- `500` — Failed to delete company event
