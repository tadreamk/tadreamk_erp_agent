# GET /employee/me

Get the current employee's own profile. Requires authentication.

**Response:**
```json
{
  "id": "uuid",
  "username": "alice",
  "work_email": "alice@company.com",
  "contract_id": "uuid",
  "personal_particular_id": "uuid",
  "onboarding_id": "uuid",
  "is_active": true
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Employee profile not found
