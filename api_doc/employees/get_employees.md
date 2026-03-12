# GET /employees


Get all employees with filtering and pagination. Returns employee list enriched with contract details (full name, position, department, start date).

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search filter across employee fields |
| include_inactive | bool | No | Include inactive employees (default: false) |
| department | string | No | Filter by department |
| page | int | No | Page number (default: 1) |
| limit | int | No | Items per page (default: 50) |

**Response:**
```json
{
  "employees": [
    {
      "id": "uuid",
      "username": "john.doe",
      "work_email": "john.doe@company.com",
      "manager_username": "jane.smith",
      "is_active": true,
      "created_at": "2025-06-01T00:00:00",
      "full_name": "DOE John",
      "position": "Software Engineer",
      "department": "Engineering",
      "start_date": "2025-06-01"
    }
  ],
  "total": 42,
  "page": 1,
  "limit": 50
}
```
