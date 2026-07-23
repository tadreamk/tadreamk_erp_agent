# Health API

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | / | Public | API root | [get_root.md](get_root.md) |
| GET | /health | Public | Health check | [get_health.md](get_health.md) |
