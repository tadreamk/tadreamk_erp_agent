# GET /funding-sources/{source_id}


Get full details of a single funding source.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | Funding source ID |

**Response:**
```json
{
  "id": "uuid",
  "source_name": "Government Grant 2026",
  "funding_type": "government",
  "provider": "Ministry of Finance",
  "reference_no": "GOV-2026-001",
  "description": "Annual government funding allocation",
  "total_approved": 500000.00,
  "start_date": "2026-01-01",
  "end_date": "2026-12-31",
  "status": "active",
  "funding_opportunity_id": "uuid-or-null",
  "created_by": "admin_user",
  "created_at": "2026-01-10T08:00:00",
  "updated_at": "2026-02-15T10:30:00",
  "is_active": true
}
```

**Errors:**
- `404` -- Funding source not found
