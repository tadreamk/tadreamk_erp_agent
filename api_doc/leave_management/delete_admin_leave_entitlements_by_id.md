# DELETE /admin/leave/entitlements/{entitlement_id}


Permanently delete a leave entitlement.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| entitlement_id | UUID | Leave entitlement ID |

**Response:**
```json
{
  "message": "Entitlement deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — Not an admin user
- `404` — Leave entitlement not found
- `500` — Failed to delete entitlement
