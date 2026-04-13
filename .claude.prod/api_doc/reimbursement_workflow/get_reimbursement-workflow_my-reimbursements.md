# GET /reimbursement-workflow/my-reimbursements

Get reimbursement workflows for the authenticated user. Requires authentication.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |

**Response:** Array of reimbursement workflow list objects

**Errors:**
- `401` — Not authenticated
