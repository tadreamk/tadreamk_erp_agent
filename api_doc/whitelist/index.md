# Whitelist API

Base prefix: `/whitelist`

Authentication: Required. Most endpoints require `whitelist` admin access. `/my-endpoints` requires only authentication.

| Method | Path | Description |
|--------|------|-------------|
| GET | `/whitelist/my-endpoints` | Get current user's accessible endpoints |
| GET | `/whitelist/endpoints` | Get list of valid ERP endpoints |
| GET | `/whitelist/stats` | Get whitelist statistics by endpoint |
| GET | `/whitelist/` | List whitelist entries with filtering and pagination |
| GET | `/whitelist/entry/{whitelist_id}` | Get a single whitelist entry by ID |
| GET | `/whitelist/user/{username}` | Get user's accessible endpoints |
| POST | `/whitelist/` | Create a new whitelist entry |
| POST | `/whitelist/bulk` | Create multiple whitelist entries for a user |
| PUT | `/whitelist/{whitelist_id}` | Update a whitelist entry |
| DELETE | `/whitelist/{whitelist_id}` | Deactivate (soft delete) a whitelist entry |

## Endpoint Documentation

- [GET /whitelist/my-endpoints](get_whitelist_my-endpoints.md)
- [GET /whitelist/endpoints](get_whitelist_endpoints.md)
- [GET /whitelist/stats](get_whitelist_stats.md)
- [GET /whitelist/](get_whitelist.md)
- [GET /whitelist/entry/{whitelist_id}](get_whitelist_entry_{whitelist_id}.md)
- [GET /whitelist/user/{username}](get_whitelist_user_{username}.md)
- [POST /whitelist/](post_whitelist.md)
- [POST /whitelist/bulk](post_whitelist_bulk.md)
- [PUT /whitelist/{whitelist_id}](put_whitelist_{whitelist_id}.md)
- [DELETE /whitelist/{whitelist_id}](delete_whitelist_{whitelist_id}.md)
