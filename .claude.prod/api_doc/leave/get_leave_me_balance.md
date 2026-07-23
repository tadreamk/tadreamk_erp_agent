# GET /leave/me/balance

Get My Balance. Requires authentication.

**Response:**
```json
{
  "balances": [
    {
      "leave_type": "string",
      "entitled": "string",
      "used": "string",
      "pending": "string",
      "available": "string",
      "is_monthly_limit": false,
      "monthly_limit": "string",
      "monthly_used": "string"
    }
  ]
}
```

**Errors:**
- `401` — Not authenticated
- `404` — Not found
