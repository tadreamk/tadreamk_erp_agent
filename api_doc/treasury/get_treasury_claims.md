# GET /treasury/claims

List funder claims with optional filtering. Requires `expense-management` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| funding_source_id | UUID | No | Filter by funding source |
| status | string | No | Filter by claim status |
| skip | integer | No | Pagination offset (default: 0) |
| limit | integer | No | Max results (default: 50, max: 100) |

**Response:** Array of funder claim objects

**Errors:**
- `401` — Not authenticated
- `403` — Not authorized
