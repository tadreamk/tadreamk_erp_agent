# PUT /treasury/claims/{claim_id}

Update a draft or submitted funder claim. Cannot update a `received` claim. Requires `expense-management` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| claim_id | UUID | The funder claim's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| expense_ids | list[UUID] | No | Updated list of expense IDs |
| total_amount | number | No | Updated total claim amount |
| expected_date | date | No | Updated expected date |
| note | string | No | Updated note |
| claim_reference | string | No | Updated external claim reference |

**Response:** Updated funder claim object

**Errors:**
- `400` — Cannot update a received claim
- `401` — Not authenticated
- `403` — Not authorized
- `404` — Claim not found
