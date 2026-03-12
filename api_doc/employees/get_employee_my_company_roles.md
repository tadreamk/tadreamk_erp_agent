# GET /employee/my-company-roles


Get the current authenticated user's active company roles.

**Response:**
```json
{
  "roles": [
    {
      "title": "head_of_hr",
      "description": "Head of Human Resources"
    }
  ]
}
```

**Errors:**
- `401` -- Not authenticated

---

## 19. Employees (Admin / HR)

Base path: `/employees`

**Access control:** Whitelist `employees` required for all endpoints.
