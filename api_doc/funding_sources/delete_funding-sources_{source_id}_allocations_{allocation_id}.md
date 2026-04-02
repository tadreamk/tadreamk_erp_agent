# DELETE /funding-sources/{source_id}/allocations/{allocation_id}

Remove an expense category allocation from a funding source (soft delete).

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | The funding source's unique identifier |
| allocation_id | UUID | The allocation's unique identifier |

**Auth:** Requires `funding-sources` whitelist access.

**Response:** `200 OK`
```json
{
  "message": "Allocation removed"
}
```

**Errors:**
- `400` — Allocation does not belong to this funding source
- `401` — Not authenticated
- `403` — Not on funding-sources whitelist
- `404` — Funding source or allocation not found
