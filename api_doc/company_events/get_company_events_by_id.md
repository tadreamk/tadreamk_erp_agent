# GET /company-events/{event_id}


Get full company event details. All employees can view. Response includes `can_edit` and `can_delete` permission flags based on the viewer's whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| event_id | UUID | Company event unique identifier |

**Response:**
```json
{
  "success": true,
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "title": "Company Town Hall",
    "description": "Quarterly all-hands meeting",
    "location": "Main Conference Room",
    "start_time": "2026-03-20T09:00:00+00:00",
    "end_time": "2026-03-20T11:00:00+00:00",
    "participants": ["john.doe", "jane.smith"],
    "participant_details": [
      {
        "username": "john.doe",
        "name": "DOE John",
        "department": "Engineering",
        "work_email": "john.doe@company.com"
      }
    ],
    "participant_count": 2,
    "created_by": "admin",
    "created_by_name": "ADMIN User",
    "updated_by": null,
    "updated_by_name": null,
    "created_at": "2026-03-10T08:00:00+00:00",
    "updated_at": null,
    "is_active": true,
    "reminder_at": "2026-03-19T09:00:00+00:00",
    "reminder_sent": false,
    "can_edit": true,
    "can_delete": true
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access this resource
- `404` — Company event not found
