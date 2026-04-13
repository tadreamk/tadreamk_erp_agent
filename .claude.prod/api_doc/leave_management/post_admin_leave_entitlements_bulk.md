# POST /admin/leave/entitlements/bulk

Create entitlements for multiple employees at once. Requires admin authentication (head_of_hr or ceo).

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| employee_usernames | list[string] | Yes | List of employee usernames |
| leave_type | string | Yes | Leave type |
| amount | float | Yes | Entitlement amount in days |
| from_date | date | Yes | Start date |
| end_date | date | Yes | End date |
| notes | string | No | Optional notes |

**Response:**
```json
{
  "message": "Created 5 entitlements",
  "entitlements": [
    {
      "id": "uuid",
      "employee_username": "john_doe",
      "leave_type": "annual",
      "amount": 14.0
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Admin access required
