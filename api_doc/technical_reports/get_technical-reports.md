# GET /technical-reports

List all technical reports. Requires `technical-reports` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by report status |
| search | string | No | Search by title or description |
| skip | integer | No | Pagination offset (default: 0) |
| limit | integer | No | Max results (default: 50, max: 100) |

**Response:** Array of technical report list objects

**Errors:**
- `401` — Not authenticated
- `403` — Not on technical-reports whitelist
