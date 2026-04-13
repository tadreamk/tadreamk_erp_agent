# DELETE /tasks/recurrences/{recurrence_id}

Delete a recurrence template. Manager only.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| recurrence_id | string | The recurrence's unique identifier |

**Auth:** Requires `tasks` whitelist access and manager role on the recurrence.

**Response:** `200 OK`
```json
{
  "status": 200,
  "message": "Recurrence deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access / Only managers can perform this action
- `404` — Recurrence not found
