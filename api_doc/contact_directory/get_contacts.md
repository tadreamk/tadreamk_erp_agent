# GET /contacts


List all active employee contacts with optional search and department filtering.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by name, email, or username (default: empty) |
| department | string | No | Filter by department (default: empty) |

**Response:**
```json
{
  "contacts": [
    {
      "username": "john.doe",
      "full_name": "John Doe",
      "preferred_name": "Johnny",
      "position": "Software Engineer",
      "department": "Engineering",
      "work_email": "john.doe@company.com",
      "mobile_phone": "+65 9123 4567",
      "work_location": "Singapore HQ"
    }
  ],
  "total": 25
}
```

**Fields returned per contact:**
| Field | Type | Description |
|-------|------|-------------|
| username | string | Employee username |
| full_name | string | Full name (first + family name in English) |
| preferred_name | string or null | Employee's preferred/nickname |
| position | string or null | Job position from active contract |
| department | string or null | Department from active contract |
| work_email | string | Company work email |
| mobile_phone | string or null | Personal mobile phone number |
| work_location | string or null | Office/work location |

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access the contact directory
