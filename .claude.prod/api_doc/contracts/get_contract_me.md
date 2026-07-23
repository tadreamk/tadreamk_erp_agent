# GET /contract/me

List My Contracts. Requires authentication.

**Response:**
```json
{
  "entries": [
    {
      "id": "uuid",
      "position": "string",
      "start_date": "date",
      "employment_end_date": "date",
      "employment_type": "string",
      "contract_pay_type": "string",
      "is_active": false,
      "is_currently_effective": false
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
