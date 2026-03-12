# GET /onboarding/count


Get count of onboarding workflows matching filters (HR only).

**Query Parameters:**
| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| status | string | No | — | Filter by workflow status |
| hr_username | string | No | — | Filter by assigned HR username |
| is_active | bool | No | `true` | Filter by active/inactive |

**Response:**
```json
{
  "count": 12
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
