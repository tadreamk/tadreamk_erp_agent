# GET /admin/leave/balance/{employee_username}


Get the leave balance for a specific employee and leave type.

**Access control:** Whitelist `leave-management` required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| employee_username | string | Employee's username |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| leave_type | string | Yes | Leave type to check balance for |
| reference_date | date | No | Calculate balance as of this date (YYYY-MM-DD) |

**Response:**
```json
{
  "employee_username": "john.doe",
  "leave_type": "annual",
  "entitled": 14.0,
  "used": 3.0,
  "pending": 2.0,
  "available": 9.0,
  "from_date": "2026-01-01",
  "end_date": "2026-12-31"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not whitelisted for `leave-management`

---

## 34. Leave Amendment (Admin)

Administrative endpoints for reviewing and acting on employee-submitted leave amendment requests.

**Prefix:** `/admin/leave`

**Access control:** Whitelist `leave-management` required for all endpoints.
