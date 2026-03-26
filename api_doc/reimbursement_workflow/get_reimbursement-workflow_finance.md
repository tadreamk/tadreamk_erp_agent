# GET /reimbursement-workflow (Finance)

List all reimbursement workflows (Finance/HR view). Requires `reimbursement-workflow` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| employee_username | string | No | Filter by employee username |
| date_from | datetime | No | Filter by submission date from |
| date_to | datetime | No | Filter by submission date to |
| limit | integer | No | Max results (default: 50, max: 200) |
| offset | integer | No | Pagination offset (default: 0) |

**Response:** Array of reimbursement workflow list objects

**Errors:**
- `401` — Not authenticated
- `403` — Not on reimbursement-workflow whitelist
