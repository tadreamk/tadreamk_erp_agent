# DELETE /bank-statements/{statement_id}

Delete a bank statement and all its lines (cascade). Requires `bank-statements` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| statement_id | UUID | Bank statement ID |

**Response:** `200`
```json
{"message": "Deleted"}
```

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `404` — Statement not found
