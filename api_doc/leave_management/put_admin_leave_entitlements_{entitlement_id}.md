# PUT /admin/leave/entitlements/{entitlement_id}

Update an existing leave entitlement. Requires admin authentication (head_of_hr or ceo).

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| entitlement_id | uuid | Yes | Entitlement ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| amount | float | No | Updated amount in days |
| from_date | date | No | Updated start date |
| end_date | date | No | Updated end date |
| notes | string | No | Updated notes |

**Response:**
```json
{
  "message": "Entitlement updated successfully",
  "entitlement": {
    "id": "uuid",
    "employee_username": "john_doe",
    "amount": 16.0
  }
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Admin access required
- `404` — Entitlement not found
