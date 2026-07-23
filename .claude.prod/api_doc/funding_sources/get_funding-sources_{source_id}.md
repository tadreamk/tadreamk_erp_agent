# GET /funding-sources/{source_id}

Get Funding Source. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | string |  |

**Response:**
```json
{
  "id": "uuid",
  "source_name": "string",
  "funding_type": "string",
  "provider": "string",
  "reference_no": "string",
  "description": "string",
  "total_approved": "string",
  "start_date": "date",
  "end_date": "date",
  "status": "string",
  "is_active": false,
  "created_at": "datetime",
  "created_by": "string",
  "created_by_preferred_name": "string",
  "updated_at": "datetime",
  "updated_by": "string",
  "updated_by_preferred_name": "string"
}
```

**Errors:**
- `422` — Validation Error
