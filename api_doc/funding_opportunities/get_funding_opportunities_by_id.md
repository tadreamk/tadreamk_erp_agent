# GET /funding-opportunities/{opportunity_id}


Get full details of a specific funding opportunity.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| opportunity_id | UUID | Funding opportunity ID |

**Response:**
```json
{
  "id": "uuid",
  "opportunity_name": "Innovation Fund 2026",
  "funding_type": "government",
  "provider": "National Science Council",
  "description": "Annual innovation grant for technology companies",
  "estimated_amount": 250000.00,
  "application_url": "https://example.gov/apply",
  "application_deadline": "2026-06-30",
  "funding_start_date": "2026-09-01",
  "funding_end_date": "2027-08-31",
  "requirements": "Must be a registered technology company with < 200 employees",
  "status": "researching",
  "created_by": "admin_user",
  "created_at": "2026-02-01T10:00:00",
  "updated_at": "2026-03-05T14:20:00",
  "is_active": true
}
```

**Errors:**
- `404` -- Funding opportunity not found
