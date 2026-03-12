# PUT /equipment/{equipment_id}


Update an existing equipment record. For Software category items, calendar events for license renewal are automatically synced. If the category changes away from Software, related calendar events and license fields are cleaned up.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| equipment_id | UUID | Equipment record ID |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | No | Equipment name (1-255 chars) |
| category | string | No | Category |
| serial_number | string | No | Serial/asset number (max 100 chars) |
| description | string | No | Additional description |
| purchase_date | date | No | Purchase date |
| purchase_price | decimal | No | Purchase price (>= 0) |
| warranty_until | date | No | Warranty expiration date |
| expense_management_id | UUID | No | FK to expense management record |
| employee_username | string | No | Assigned employee username |
| assigned_date | date | No | Assignment date |
| location | string | No | Physical location (max 255 chars) |
| status | string | No | Status |
| note | string | No | Additional notes |
| file_urls | string[] | No | List of document/photo URLs |
| license_key | string | No | Software license key (max 500 chars) |
| total_seats | int | No | Number of license seats (>= 1) |
| renewal_date | date | No | License renewal/expiration date |

**Response:** Same as `GET /equipment/{equipment_id}`.

**Errors:**
- `400` — Employee username not found
- `401` — Not authenticated
- `403` — No access to equipment management
- `404` — Equipment not found
