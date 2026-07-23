# POST /funding-sources

Create Funding Source. Requires authentication.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| source_name | string | Yes |  |
| funding_type | FundingTypeEnum | Yes |  |
| provider | string | Yes |  |
| reference_no | string | No |  |
| description | string | No |  |
| total_approved | number|string | Yes |  |
| start_date | string | Yes |  |
| end_date | string | No |  |
| status | _FundingStatusOnCreateEnum | No |  |

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
