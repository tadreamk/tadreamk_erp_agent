# GET /contacts

Get all active employee contacts for the directory. Requires employee authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search by name, username, or email |
| department | string | No | Filter by department |

**Response:**
```json
{
  "contacts": [
    {
      "username": "alice",
      "full_name": "Alice Wong",
      "preferred_name": "Alice",
      "position": "Software Engineer",
      "department": "Engineering",
      "work_email": "alice@company.com",
      "mobile_phone": "+852 1234 5678",
      "work_location": "Hong Kong"
    }
  ],
  "total": 10
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Only employees can access the contact directory
