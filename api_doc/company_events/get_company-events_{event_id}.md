# GET /company-events/{event_id}

Get details of a specific company event. Accessible by all employees.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| event_id | UUID | The event's unique identifier |

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "uuid",
    "title": "string",
    "description": "string",
    "location": "string",
    "start_time": "datetime",
    "end_time": "datetime",
    "participants": ["alice"],
    "reminder_at": "datetime",
    "created_by": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
- `404` — Company event not found
