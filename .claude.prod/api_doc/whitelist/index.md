# Whitelist API

Base prefixes:
- `/whitelist`
- `/whitelist/entry`
- `/whitelist/user`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /whitelist/ | Authenticated | Get Whitelist Entries | [get_whitelist_.md](get_whitelist_.md) |
| POST | /whitelist/ | Authenticated | Create Whitelist Entry | [post_whitelist_.md](post_whitelist_.md) |
| POST | /whitelist/bulk | Authenticated | Create Whitelist Entries Bulk | [post_whitelist_bulk.md](post_whitelist_bulk.md) |
| GET | /whitelist/endpoints | Authenticated | Get Valid Endpoints | [get_whitelist_endpoints.md](get_whitelist_endpoints.md) |
| GET | /whitelist/entry/{whitelist_id} | Authenticated | Get Whitelist Entry | [get_whitelist_entry_{whitelist_id}.md](get_whitelist_entry_{whitelist_id}.md) |
| GET | /whitelist/my-endpoints | Authenticated | Get My Endpoints | [get_whitelist_my-endpoints.md](get_whitelist_my-endpoints.md) |
| GET | /whitelist/stats | Authenticated | Get Whitelist Stats | [get_whitelist_stats.md](get_whitelist_stats.md) |
| GET | /whitelist/user/{username} | Authenticated | Get User Endpoints | [get_whitelist_user_{username}.md](get_whitelist_user_{username}.md) |
| DELETE | /whitelist/{whitelist_id} | Authenticated | Deactivate Whitelist Entry | [delete_whitelist_{whitelist_id}.md](delete_whitelist_{whitelist_id}.md) |
| PUT | /whitelist/{whitelist_id} | Authenticated | Update Whitelist Entry | [put_whitelist_{whitelist_id}.md](put_whitelist_{whitelist_id}.md) |
