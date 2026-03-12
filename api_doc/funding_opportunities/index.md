# Funding Opportunities API

Track and manage potential funding opportunities through their lifecycle -- from research and application to award or rejection. Opportunities can later be converted into active funding sources.

**Access control:** Whitelist `funding-opportunities` required for all endpoints.

---

## 43. Funding Opportunities

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/funding-opportunities` | List all funding opportunities with optional filters and pagination. | [get_funding_opportunities.md](./get_funding_opportunities.md) |
| `GET` | `/funding-opportunities/count` | Get count of funding opportunities matching optional filters. | [get_funding_opportunities_count.md](./get_funding_opportunities_count.md) |
| `GET` | `/funding-opportunities/{opportunity_id}` | Get full details of a specific funding opportunity. | [get_funding_opportunities_by_id.md](./get_funding_opportunities_by_id.md) |
| `POST` | `/funding-opportunities` | Create a new funding opportunity. | [post_funding_opportunities.md](./post_funding_opportunities.md) |
| `PUT` | `/funding-opportunities/{opportunity_id}` | Update an existing funding opportunity. Only provided fields are updated. | [put_funding_opportunities_by_id.md](./put_funding_opportunities_by_id.md) |
| `DELETE` | `/funding-opportunities/{opportunity_id}` | Soft delete a funding opportunity. | [delete_funding_opportunities_by_id.md](./delete_funding_opportunities_by_id.md) |
