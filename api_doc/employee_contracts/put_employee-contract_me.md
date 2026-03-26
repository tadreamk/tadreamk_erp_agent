# PUT /employee-contract/me

Update employee contract data for the authenticated user. Requires authentication.

**Request Body:** (all fields optional, same as POST)

**Response:**
```json
{
  "message": "Employee contract updated",
  "employee_contract": { "...contract object..." }
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Employee contract record not found. Use POST to create.
