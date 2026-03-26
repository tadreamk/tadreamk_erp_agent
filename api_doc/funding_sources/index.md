# Funding Sources API

Base prefix: `/funding-sources`

All endpoints require `funding-sources` whitelist.

| Method | Path | Description | File |
|--------|------|-------------|------|
| GET | /funding-sources/categories | List expense categories | [get_funding-sources_categories.md](get_funding-sources_categories.md) |
| GET | /funding-sources/grouped | List sources grouped by category | [get_funding-sources_grouped.md](get_funding-sources_grouped.md) |
| GET | /funding-sources | List funding sources | [get_funding-sources.md](get_funding-sources.md) |
| GET | /funding-sources/count | Get count | [get_funding-sources_count.md](get_funding-sources_count.md) |
| GET | /funding-sources/{source_id} | Get source by ID | [get_funding-sources_{source_id}.md](get_funding-sources_{source_id}.md) |
| POST | /funding-sources | Create funding source | [post_funding-sources.md](post_funding-sources.md) |
| PUT | /funding-sources/{source_id} | Update funding source | [put_funding-sources_{source_id}.md](put_funding-sources_{source_id}.md) |
| DELETE | /funding-sources/{source_id} | Delete funding source | [delete_funding-sources_{source_id}.md](delete_funding-sources_{source_id}.md) |
