# GET /funding-utilization/summary


Get an overall summary of funding utilization across all active funding sources.

**Response:**
```json
{
  "total_approved": 1500000.00,
  "total_utilized": 875000.00,
  "total_remaining": 625000.00,
  "utilization_percentage": 58.33
}
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No access to funding utilization
