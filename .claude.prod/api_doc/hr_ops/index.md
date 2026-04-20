# HR Ops API

**Router files:**
- `backend/src/api/hr_ops_api.py` — HR-side endpoints (prefix `/hr-ops`, whitelist `hr-ops`)
- `backend/src/api/hr_ops_talent_api.py` — Talent-side endpoints (prefix `/talent/hr-ops`, JWT ownership)

---

## Endpoints

| Method | Path | Auth | Description |
|--------|------|------|-------------|
| GET | `/hr-ops/workflows` | hr-ops whitelist | List all HR Ops workflows |
| POST | `/hr-ops/workflows` | hr-ops whitelist | Create a new workflow |
| GET | `/hr-ops/workflows/{id}` | hr-ops whitelist | Get workflow detail + template |
| GET | `/hr-ops/templates` | hr-ops whitelist | List active templates for the Create modal |
| GET | `/talent/hr-ops/workflows` | JWT (own employee) | List employee's own workflows |
| GET | `/talent/hr-ops/workflows/{id}` | JWT (own employee) | Get employee workflow detail + template |
| POST | `/talent/hr-ops/workflows/{id}/submit` | JWT (own employee) | Submit completed field values |

---

## GET `/hr-ops/workflows`

**Auth:** `hr-ops` whitelist

**Query params:** `workflow_status` (optional), `page` (default 1), `limit` (default 50)

**Response:**
```json
{
  "workflows": [
    {
      "id": "uuid",
      "template_id": "uuid",
      "template_title": "Employee Handbook Acknowledgment v3",
      "employee_username": "alanshareteam",
      "hr_username": "alan",
      "status": "pending_input",
      "field_values": {},
      "pdf_url": "https://storage.googleapis.com/bucket/workflow.pdf",
      "submitted_at": null,
      "created_at": "2026-03-31T10:00:00Z",
      "updated_at": "2026-03-31T10:00:00Z",
      "is_active": true
    }
  ],
  "total": 1,
  "page": 1,
  "limit": 50
}
```

---

## POST `/hr-ops/workflows`

**Auth:** `hr-ops` whitelist

**Request body:**
```json
{
  "template_id": "uuid",
  "employee_username": "alanshareteam"
}
```

**Response:** Serialized workflow object (201 Created)

**Side effects:** In-app notification + email to employee (if `hr-ops` email setting enabled)

---

## GET `/hr-ops/workflows/{id}`

**Auth:** `hr-ops` whitelist

**Response:** Workflow object with additional `template` key containing full template with fields.

---

## GET `/talent/hr-ops/workflows`

**Auth:** JWT (cookie-based), returns only workflows where `employee_username == current user`

**Query params:** `page` (default 1), `limit` (default 50, max 200)

**Response:**
```json
{
  "workflows": [...],
  "total": 2,
  "page": 1,
  "limit": 50
}
```

---

## GET `/talent/hr-ops/workflows/{id}`

**Auth:** JWT, ownership check (403 if `employee_username != current user`)

**Response:** Workflow object with `template` key.

---

## POST `/talent/hr-ops/workflows/{id}/submit`

**Auth:** JWT, ownership check

**Request body:**
```json
{
  "field_values": {
    "family_name": "ShareTeam",
    "first_name": "Alan",
    "signature": "data:image/png;base64,..."
  }
}
```

**Response:** Updated workflow with `status: "completed"`

**Side effects:** In-app notification + email to HR (if `hr-ops` email setting enabled)

**Errors:**
- `400` — Workflow already submitted
- `403` — Not authorized
- `404` — Workflow not found
