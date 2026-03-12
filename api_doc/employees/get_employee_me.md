# GET /employee/me


Get the current authenticated employee's profile.

**Response:**
```json
{
  "id": "uuid",
  "username": "john.doe",
  "work_email": "john.doe@company.com",
  "contract_id": "uuid",
  "personal_particular_id": "uuid",
  "onboarding_id": "uuid",
  "is_active": true
}
```

**Errors:**
- `401` -- Not authenticated
- `404` -- Employee profile not found
