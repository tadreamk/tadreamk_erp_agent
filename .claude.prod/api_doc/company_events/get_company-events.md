# GET /company-events

List all company events. Accessible by all employees.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search in title/description |
| start_date | date | No | Filter events starting on or after this date |
| end_date | date | No | Filter events ending on or before this date |
| skip | int | No | Offset (default: 0) |
| limit | int | No | Max results (default: 50, max: 100) |

**Response:**
```json
{
  "success": true,
  "data": [
    {
      "id": "uuid",
      "title": "string",
      "description": "string",
      "location": "string",
      "start_time": "datetime",
      "end_time": "datetime",
      "participants": ["alice", "bob"],
      "created_by": "string"
    }
  ],
  "total": 10
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an employee
