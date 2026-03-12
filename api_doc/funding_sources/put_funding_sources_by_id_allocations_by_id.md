# PUT /funding-sources/{source_id}/allocations/{allocation_id}


Update the allocated amount for an existing allocation.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| source_id | UUID | Funding source ID |
| allocation_id | UUID | Allocation ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| allocated_amount | decimal | Yes | New amount to allocate (>= 0) |

**Response:** Updated allocation object (same shape as POST response).

**Errors:**
- `400` -- Allocation does not belong to this funding source
- `400` -- Total allocation would exceed approved amount. Available: {amount}
- `404` -- Funding source not found
- `404` -- Allocation not found
