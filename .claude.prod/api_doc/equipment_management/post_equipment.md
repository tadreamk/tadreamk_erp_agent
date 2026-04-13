# POST /equipment

Create a new equipment record. Requires `equipment-management` whitelist.

If the category is "Software" and `renewal_date` is provided, a calendar event is created automatically.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Equipment name |
| category | string | Yes | Category (Laptops, Phones, Keys, Parking, Monitors, Furniture, Software, Other) |
| serial_number | string | No | Serial/asset number |
| description | string | No | Description |
| purchase_date | date | No | Purchase date |
| purchase_price | decimal | No | Purchase price |
| warranty_until | date | No | Warranty expiration date |
| expense_management_id | UUID | No | Linked expense ID |
| employee_username | string | No | Assigned employee |
| assigned_date | date | No | Assignment date |
| location | string | No | Physical location |
| status | string | No | Status (default: available) |
| note | string | No | Additional notes |
| file_urls | list[string] | No | Document/photo URLs |
| license_key | string | No | Software license key (Software only) |
| total_seats | int | No | License seat count (Software only) |
| renewal_date | date | No | License renewal date (Software only) |

**Response:** Equipment object

**Errors:**
- `401` — Not authenticated
- `403` — No equipment-management whitelist access
- `400` — Employee not found (if employee_username provided)
