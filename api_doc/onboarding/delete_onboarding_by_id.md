# DELETE /onboarding/{workflow_id}


Soft-delete an onboarding workflow (HR only). Sets `is_active` to `false`.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | Onboarding workflow ID |

**Response:**
```json
{
  "message": "Onboarding workflow deleted"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No whitelist access to onboarding section
- `404` — Onboarding workflow not found
