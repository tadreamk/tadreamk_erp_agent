# DELETE /company-events/{event_id}

Delete a company event (soft delete). Requires `company-events` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| event_id | UUID | The event's unique identifier |

**Response:**
```json
{
  "success": true,
  "message": "Company event deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No company-events whitelist access
- `404` — Company event not found
- `500` — Failed to delete company event
