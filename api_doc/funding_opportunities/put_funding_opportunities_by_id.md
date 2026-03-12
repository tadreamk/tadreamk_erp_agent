# PUT /funding-opportunities/{opportunity_id}


Update an existing funding opportunity. Only provided fields are updated.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| opportunity_id | UUID | Funding opportunity ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| opportunity_name | string | No | Name (1-255 chars) |
| funding_type | string | No | Type: `government`, `corporate`, `internal`, `donation`, `investment` |
| estimated_amount | decimal | No | Estimated funding amount (>= 0) |
| provider | string | No | Organization providing the fund (max 255 chars) |
| description | string | No | Description |
| application_url | string | No | URL to application portal (max 500 chars) |
| application_deadline | date | No | Deadline to submit application |
| funding_start_date | date | No | Expected funding period start |
| funding_end_date | date | No | Expected funding period end (must be >= funding_start_date) |
| requirements | string | No | Eligibility requirements |
| status | string | No | Status: `researching`, `submitted`, `awarded`, `rejected`, `expired`, `closed` |

**Response:** Updated funding opportunity object.

**Errors:**
- `400` -- A funding opportunity with this name already exists
- `404` -- Funding opportunity not found
