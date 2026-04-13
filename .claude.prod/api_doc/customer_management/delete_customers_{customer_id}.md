# DELETE /customers/{customer_id}

Soft delete a customer record. Requires `customer-management` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| customer_id | UUID | The customer's unique identifier |

**Response:**
```json
{
  "message": "Customer deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No customer-management whitelist access
- `404` — Customer not found
