# Rachel AI API

Base prefixes:
- `/rachel-ai`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /rachel-ai/history | Public | Get History | [get_rachel-ai_history.md](get_rachel-ai_history.md) |
