# GET /onboarding/count

Get count of onboarding workflows. Requires `onboarding` whitelist access.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| status | string | No | Filter by workflow status |
| hr_username | string | No | Filter by HR username |
| is_active | boolean | No | Filter by active status (default: true) |

**Response:**
```json
{
  "count": 42
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not on onboarding whitelist
