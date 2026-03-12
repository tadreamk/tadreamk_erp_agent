# DELETE /funding-sources/{source_id}


Soft delete a funding source.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | Funding source ID |

**Response:**
```json
{
  "message": "Funding source deleted"
}
```

**Errors:**
- `404` -- Funding source not found

---

## 42. Funding Allocation

Manage how a funding source's approved budget is distributed across expense categories. Total allocations across all categories cannot exceed the source's `total_approved` amount.
