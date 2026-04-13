# DELETE /bank-accounts/{account_id}

Soft-delete a bank account (sets is_active=False). Requires `bank-statements` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| account_id | UUID | Bank account ID |

**Response:** `200`
```json
{"message": "Deleted"}
```

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `404` — Bank account not found
