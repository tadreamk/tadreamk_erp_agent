# Funding Sources API

Base prefixes:
- `/funding-sources`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /funding-sources | Authenticated | List Funding Sources | [get_funding-sources.md](get_funding-sources.md) |
| POST | /funding-sources | Authenticated | Create Funding Source | [post_funding-sources.md](post_funding-sources.md) |
| GET | /funding-sources/{source_id} | Authenticated | Get Funding Source | [get_funding-sources_{source_id}.md](get_funding-sources_{source_id}.md) |
| PUT | /funding-sources/{source_id} | Authenticated | Update Funding Source | [put_funding-sources_{source_id}.md](put_funding-sources_{source_id}.md) |
