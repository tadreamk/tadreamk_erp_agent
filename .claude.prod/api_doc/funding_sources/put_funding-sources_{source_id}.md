# PUT /funding-sources/{source_id}

Update Funding Source. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | string |  |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| source_name | string | No |  |
| funding_type | FundingTypeEnum | No |  |
| provider | string | No |  |
| reference_no | string | No |  |
| description | string | No |  |
| total_approved | number|string | No |  |
| start_date | string | No |  |
| end_date | string | No |  |
| status | FundingStatusEnum | No |  |

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
