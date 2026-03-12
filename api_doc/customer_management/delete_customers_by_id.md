# DELETE /customers/{customer_id}


Soft delete a customer record.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| customer_id | UUID | Customer record ID |

**Response:**
```json
{
  "message": "Customer deleted successfully"
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No access to customer management
- `404` — Customer not found
