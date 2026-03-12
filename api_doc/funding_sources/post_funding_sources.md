# POST /funding-sources


Create a new funding source.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| source_name | string | Yes | Name of the funding source (1-255 chars) |
| funding_type | string | Yes | Type: `government`, `corporate`, `internal`, `donation`, `investment` |
| total_approved | decimal | Yes | Total approved amount (must be > 0) |
| provider | string | No | Organization providing the fund (max 255 chars) |
| reference_no | string | No | External reference number (max 100 chars) |
| description | string | No | Description of the funding |
| start_date | date | No | Funding period start date (YYYY-MM-DD) |
| end_date | date | No | Funding period end date (YYYY-MM-DD, must be >= start_date) |
| status | string | No | Status: `active` (default), `completed` |
| funding_opportunity_id | UUID | No | Link to a funding opportunity (if converted from one) |

**Response:** `201 Created` -- Full funding source object (same shape as GET by ID).

**Errors:**
- `400` -- Funding source with this name already exists
- `400` -- Validation error (e.g., end_date < start_date)
- `401` -- Not authenticated
- `403` -- No access to funding sources management
