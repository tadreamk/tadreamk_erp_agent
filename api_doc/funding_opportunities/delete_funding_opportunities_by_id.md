# DELETE /funding-opportunities/{opportunity_id}


Soft delete a funding opportunity.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| opportunity_id | UUID | Funding opportunity ID |

**Response:**
```json
{
  "message": "Funding opportunity deleted successfully"
}
```

**Errors:**
- `404` -- Funding opportunity not found
