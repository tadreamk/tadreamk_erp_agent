# GET /admin/company-roles


List all company role assignments with pagination.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| limit | int | No | Max records to return (default: 100) |
| offset | int | No | Number of records to skip (default: 0) |

**Response:**
```json
{
  "company_roles": [
    {
      "id": "uuid",
      "username": "john.doe",
      "role_title": "head_of_hr",
      "role_description": "Head of Human Resources",
      "is_active": true,
      "created_at": "2025-06-01T00:00:00+00:00",
      "created_by": "admin.user"
    }
  ],
  "total": 10
}
```
