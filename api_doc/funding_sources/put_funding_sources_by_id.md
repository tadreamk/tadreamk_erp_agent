# PUT /funding-sources/{source_id}


Update an existing funding source. Only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | Funding source ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| source_name | string | No | Name (1-255 chars) |
| funding_type | string | No | Type: `government`, `corporate`, `internal`, `donation`, `investment` |
| total_approved | decimal | No | Total approved amount (must be > 0) |
| provider | string | No | Organization providing the fund (max 255 chars) |
| reference_no | string | No | External reference number (max 100 chars) |
| description | string | No | Description |
| start_date | date | No | Funding period start date |
| end_date | date | No | Funding period end date (must be >= start_date) |
| status | string | No | Status: `active`, `completed` |
| funding_opportunity_id | UUID | No | Link to a funding opportunity |

**Response:** Updated funding source object.

**Errors:**
- `400` -- Funding source with this name already exists
- `400` -- end_date must be >= start_date
- `404` -- Funding source not found
