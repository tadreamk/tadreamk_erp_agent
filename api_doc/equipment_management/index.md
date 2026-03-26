# Equipment Management API

Base prefix: `/equipment`

Most endpoints require `equipment-management` whitelist. `GET /equipment/my` only requires authentication.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /equipment | `equipment-management` whitelist | List all equipment | [get_equipment.md](get_equipment.md) |
| GET | /equipment/count | `equipment-management` whitelist | Get equipment count | [get_equipment_count.md](get_equipment_count.md) |
| GET | /equipment/my | Authenticated | Get my assigned equipment | [get_equipment_my.md](get_equipment_my.md) |
| GET | /equipment/{equipment_id} | `equipment-management` whitelist | Get equipment by ID | [get_equipment_{equipment_id}.md](get_equipment_{equipment_id}.md) |
| POST | /equipment | `equipment-management` whitelist | Create equipment | [post_equipment.md](post_equipment.md) |
| PUT | /equipment/{equipment_id} | `equipment-management` whitelist | Update equipment | [put_equipment_{equipment_id}.md](put_equipment_{equipment_id}.md) |
| POST | /equipment/{equipment_id}/assign | `equipment-management` whitelist | Assign equipment to employee | [post_equipment_{equipment_id}_assign.md](post_equipment_{equipment_id}_assign.md) |
| POST | /equipment/{equipment_id}/unassign | `equipment-management` whitelist | Unassign equipment | [post_equipment_{equipment_id}_unassign.md](post_equipment_{equipment_id}_unassign.md) |
| POST | /equipment/{equipment_id}/transfer | `equipment-management` whitelist | Transfer equipment to another employee | [post_equipment_{equipment_id}_transfer.md](post_equipment_{equipment_id}_transfer.md) |
| DELETE | /equipment/{equipment_id} | `equipment-management` whitelist | Delete equipment | [delete_equipment_{equipment_id}.md](delete_equipment_{equipment_id}.md) |
