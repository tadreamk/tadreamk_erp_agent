# DELETE /treasury/claims/{claim_id}

Delete a draft claim. Only draft claims can be deleted.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | Claim ID |

**Response:**
```json
{
  "message": "Claim deleted"
}
```

**Error Codes:**
| Code | Description |
|------|-------------|
| 400 | Only draft claims can be deleted |
| 401 | Not authenticated |
| 403 | Not authorized |
| 404 | Claim not found |
