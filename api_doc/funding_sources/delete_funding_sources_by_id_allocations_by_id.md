# DELETE /funding-sources/{source_id}/allocations/{allocation_id}


Soft delete an expense category allocation from a funding source.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | Funding source ID |
| allocation_id | UUID | Allocation ID |

**Response:**
```json
{
  "message": "Allocation removed"
}
```

**Errors:**
- `400` -- Allocation does not belong to this funding source
- `404` -- Funding source not found
- `404` -- Allocation not found
