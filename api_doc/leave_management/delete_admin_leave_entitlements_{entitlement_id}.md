# DELETE /admin/leave/entitlements/{entitlement_id}

Delete a leave entitlement. Requires admin authentication (head_of_hr or ceo).

**Path Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| entitlement_id | uuid | Yes | Entitlement ID |

**Response:**
```json
{
  "message": "Entitlement deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Admin access required
- `404` — Entitlement not found
- `500` — Failed to delete entitlement
