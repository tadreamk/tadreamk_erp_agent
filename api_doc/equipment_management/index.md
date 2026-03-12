# 46. Equipment Management

Manage company equipment (laptops, phones, monitors, software licenses, etc.) with full lifecycle tracking: creation, assignment, transfer, unassignment, and soft deletion.

**Base path:** `/equipment`

**Access control:** Whitelist `equipment-management` required for all endpoints except `GET /equipment/my` (authenticated users only).

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/equipment` | List all equipment with optional filters. | [get_equipment.md](./get_equipment.md) |
| `GET` | `/equipment/count` | Get total count of equipment matching the given filters. | [get_equipment_count.md](./get_equipment_count.md) |
| `GET` | `/equipment/my` | Get equipment assigned to the currently authenticated user. No whitelist require | [get_equipment_my.md](./get_equipment_my.md) |
| `GET` | `/equipment/{equipment_id}` | Get a specific equipment record by ID. | [get_equipment_by_id.md](./get_equipment_by_id.md) |
| `POST` | `/equipment` | Create a new equipment record. If `category` is `"Software"` and `renewal_date`  | [post_equipment.md](./post_equipment.md) |
| `PUT` | `/equipment/{equipment_id}` | Update an existing equipment record. For Software category items, calendar event | [put_equipment_by_id.md](./put_equipment_by_id.md) |
| `POST` | `/equipment/{equipment_id}/assign` | Assign equipment to an employee. Sends a notification and email to the assigned  | [post_equipment_by_id_assign.md](./post_equipment_by_id_assign.md) |
| `POST` | `/equipment/{equipment_id}/unassign` | Unassign equipment from its current employee. | [post_equipment_by_id_unassign.md](./post_equipment_by_id_unassign.md) |
| `POST` | `/equipment/{equipment_id}/transfer` | Transfer equipment from one employee to another. Sends a notification and email  | [post_equipment_by_id_transfer.md](./post_equipment_by_id_transfer.md) |
| `DELETE` | `/equipment/{equipment_id}` | Soft delete an equipment record. If the equipment has an associated calendar eve | [delete_equipment_by_id.md](./delete_equipment_by_id.md) |
