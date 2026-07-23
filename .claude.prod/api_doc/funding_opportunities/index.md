# Funding Opportunities API

Base prefixes:
- `/funding-opportunities`
- `/funding-opportunities/{opportunity_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /funding-opportunities | Authenticated | List Funding Opportunities | [get_funding-opportunities.md](get_funding-opportunities.md) |
| POST | /funding-opportunities | Authenticated | Create Funding Opportunity | [post_funding-opportunities.md](post_funding-opportunities.md) |
| GET | /funding-opportunities/{opportunity_id} | Authenticated | Get Funding Opportunity | [get_funding-opportunities_{opportunity_id}.md](get_funding-opportunities_{opportunity_id}.md) |
| PUT | /funding-opportunities/{opportunity_id} | Authenticated | Update Funding Opportunity | [put_funding-opportunities_{opportunity_id}.md](put_funding-opportunities_{opportunity_id}.md) |
| PUT | /funding-opportunities/{opportunity_id}/stage | Authenticated | Update Funding Opportunity Stage | [put_funding-opportunities_{opportunity_id}_stage.md](put_funding-opportunities_{opportunity_id}_stage.md) |
