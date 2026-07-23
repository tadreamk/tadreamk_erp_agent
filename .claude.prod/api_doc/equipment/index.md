# Equipment API

Base prefixes:
- `/equipment`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /equipment | Authenticated | List Equipment | [get_equipment.md](get_equipment.md) |
| POST | /equipment | Authenticated | Create Equipment | [post_equipment.md](post_equipment.md) |
| GET | /equipment/me | Authenticated employee | List My Equipment | [get_equipment_me.md](get_equipment_me.md) |
| GET | /equipment/{equipment_id} | Authenticated | Get Equipment | [get_equipment_{equipment_id}.md](get_equipment_{equipment_id}.md) |
| PUT | /equipment/{equipment_id} | Authenticated | Update Equipment | [put_equipment_{equipment_id}.md](put_equipment_{equipment_id}.md) |
