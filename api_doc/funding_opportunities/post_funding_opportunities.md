# POST /funding-opportunities


Create a new funding opportunity.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| opportunity_name | string | Yes | Name of the opportunity (1-255 chars) |
| funding_type | string | Yes | Type: `government`, `corporate`, `internal`, `donation`, `investment` |
| estimated_amount | decimal | Yes | Estimated funding amount (>= 0) |
| provider | string | No | Organization providing the fund (max 255 chars) |
| description | string | No | Description of the opportunity |
| application_url | string | No | URL to application portal (max 500 chars) |
| application_deadline | date | No | Deadline to submit application (YYYY-MM-DD) |
| funding_start_date | date | No | Expected funding period start (YYYY-MM-DD) |
| funding_end_date | date | No | Expected funding period end (YYYY-MM-DD, must be >= funding_start_date) |
| requirements | string | No | Eligibility requirements |
| status | string | No | Status (default: `researching`). Options: `researching`, `submitted`, `awarded`, `rejected`, `expired`, `closed` |

**Response:** Full funding opportunity object (same shape as GET by ID).

**Errors:**
- `400` -- A funding opportunity with this name already exists
- `400` -- Validation error (e.g., funding_end_date < funding_start_date)
- `401` -- Not authenticated
- `403` -- No access to funding opportunities management
