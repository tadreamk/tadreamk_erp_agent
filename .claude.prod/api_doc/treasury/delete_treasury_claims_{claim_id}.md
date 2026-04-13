# DELETE /treasury/claims/{claim_id}

Soft delete a funder claim. Only `draft` claims can be deleted. Requires `expense-management` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | The funder claim's unique identifier |

**Response:**
```json
{
  "message": "Claim deleted"
}
```

**Errors:**
- `400` — Only draft claims can be deleted
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Claim not found
