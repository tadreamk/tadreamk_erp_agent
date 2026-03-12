# GET /company-events


List all company events with optional search and date filters. All employees can view.

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| search | string | No | null | Search by title |
| start_date | date | No | null | Filter events starting on or after this date |
| end_date | date | No | null | Filter events ending on or before this date |
| skip | int | No | 0 | Number of records to skip (min: 0) |
| limit | int | No | 50 | Items per page (1-100) |

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "title": "Company Town Hall",
      "location": "Main Conference Room",
      "start_time": "2026-03-20T09:00:00+00:00",
      "end_time": "2026-03-20T11:00:00+00:00",
      "participant_count": 25,
      "created_by": "admin",
      "created_by_name": "ADMIN User",
      "created_at": "2026-03-10T08:00:00+00:00"
    }
  ],
  "total": 12
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access this resource
