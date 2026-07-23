# GET /audit-log/stats

Get Audit Log Stats. Requires `)
    by_endpoint = audit_log_queries.count_by_endpoint(
        db, occurred_after=occurred_after, occurred_before=occurred_before
    )
    return {` whitelist.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| occurred_after | string | No |  |
| occurred_before | string | No |  |

**Response:**
```json
{
  "by_endpoint": {},
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
