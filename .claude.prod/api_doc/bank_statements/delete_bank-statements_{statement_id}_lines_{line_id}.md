# DELETE /bank-statements/{statement_id}/lines/{line_id}

Delete a transaction line. Requires `bank-statements` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| statement_id | UUID | Bank statement ID |
| line_id | UUID | Line ID |

**Response:** `200`
```json
{"message": "Deleted"}
```

**Errors:**
- `401` — Not authenticated
- `403` — No bank-statements whitelist access
- `404` — Line not found (or does not belong to this statement)
