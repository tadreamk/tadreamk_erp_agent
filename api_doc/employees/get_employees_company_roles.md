# GET /employees/company-roles


Get all active company roles with employee name details. Enriches each role record with `family_name` and `given_name` from the personal particulars table.

**Response:**
```json
{
  "roles": [
    {
      "id": "uuid",
      "username": "john.doe",
      "role_title": "head_of_hr",
      "role_description": "Head of Human Resources",
      "is_active": true,
      "family_name": "Doe",
      "given_name": "John"
    }
  ],
  "total": 10
}
```
