# POST /equipment


Create a new equipment record. If `category` is `"Software"` and `renewal_date` is provided, a calendar event is automatically created for license renewal tracking. If an `employee_username` is provided, a notification is sent to the assigned employee.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| name | string | Yes | Equipment name (1-255 chars) |
| category | string | Yes | Category: `Laptops`, `Phones`, `Keys`, `Parking`, `Monitors`, `Furniture`, `Software`, `Other` |
| serial_number | string | No | Serial/asset number (max 100 chars) |
| description | string | No | Additional description |
| purchase_date | date | No | Purchase date (YYYY-MM-DD) |
| purchase_price | decimal | No | Purchase price (>= 0) |
| warranty_until | date | No | Warranty expiration date |
| expense_management_id | UUID | No | FK to expense management record |
| employee_username | string | No | Assigned employee username |
| assigned_date | date | No | Assignment date |
| location | string | No | Physical location (max 255 chars) |
| status | string | No | Status (default: `available`). Values: `available`, `assigned`, `in_repair`, `reserved`, `retired`, `lost` |
| note | string | No | Additional notes |
| file_urls | string[] | No | List of document/photo URLs |
| license_key | string | No | Software license key (max 500 chars, Software category only) |
| total_seats | int | No | Number of license seats (>= 1, Software category only) |
| renewal_date | date | No | License renewal/expiration date (Software category only) |

**Response:**
```json
{
  "id": "uuid",
  "name": "Adobe Creative Cloud",
  "category": "Software",
  "serial_number": null,
  "description": "Team license",
  "purchase_date": "2025-01-01",
  "purchase_price": 599.99,
  "warranty_until": null,
  "expense_management_id": null,
  "employee_username": "jane.smith",
  "assigned_date": "2025-01-05",
  "location": null,
  "status": "assigned",
  "note": null,
  "file_urls": [],
  "license_key": "XXXX-XXXX-XXXX-XXXX",
  "total_seats": 5,
  "renewal_date": "2026-01-01",
  "calendar_event_id": "uuid",
  "updated_by": "admin",
  "created_at": "2025-01-01T08:00:00Z",
  "updated_at": null,
  "is_active": true,
  "employee_full_name": null
}
```

**Errors:**
- `400` — Employee username not found
- `401` — Not authenticated
- `403` — No access to equipment management
