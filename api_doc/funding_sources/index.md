# Funding Sources & Allocation API

Manage funding sources (government, corporate, internal, donation, investment) and allocate budgets across expense categories. Supports status tracking, date-bounded funding periods, and grouped views by category.

**Access control:** Whitelist `funding-sources` required for all endpoints.

---

## 41. Funding Sources

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/funding-sources` | List all funding sources with optional filters and pagination. | [get_funding_sources.md](./get_funding_sources.md) |
| `GET` | `/funding-sources/count` | Get count of funding sources matching optional filters. | [get_funding_sources_count.md](./get_funding_sources_count.md) |
| `GET` | `/funding-sources/categories` | List all expense categories available for filtering/allocation. | [get_funding_sources_categories.md](./get_funding_sources_categories.md) |
| `GET` | `/funding-sources/grouped` | List all funding sources grouped by expense category. | [get_funding_sources_grouped.md](./get_funding_sources_grouped.md) |
| `GET` | `/funding-sources/{source_id}` | Get full details of a single funding source. | [get_funding_sources_by_id.md](./get_funding_sources_by_id.md) |
| `POST` | `/funding-sources` | Create a new funding source. | [post_funding_sources.md](./post_funding_sources.md) |
| `PUT` | `/funding-sources/{source_id}` | Update an existing funding source. Only provided fields are updated. | [put_funding_sources_by_id.md](./put_funding_sources_by_id.md) |
| `DELETE` | `/funding-sources/{source_id}` | Soft delete a funding source. | [delete_funding_sources_by_id.md](./delete_funding_sources_by_id.md) |
| `GET` | `/funding-sources/{source_id}/allocations` | List all expense category allocations for a funding source. | [get_funding_sources_by_id_allocations.md](./get_funding_sources_by_id_allocations.md) |
| `GET` | `/funding-sources/{source_id}/available-categories` | List expense categories that have not yet been allocated to this funding source. | [get_funding_sources_by_id_available_categories.md](./get_funding_sources_by_id_available_categories.md) |
| `POST` | `/funding-sources/{source_id}/allocations` | Add an expense category allocation to a funding source. If a previously soft-del | [post_funding_sources_by_id_allocations.md](./post_funding_sources_by_id_allocations.md) |
| `PUT` | `/funding-sources/{source_id}/allocations/{allocation_id}` | Update the allocated amount for an existing allocation. | [put_funding_sources_by_id_allocations_by_id.md](./put_funding_sources_by_id_allocations_by_id.md) |
| `DELETE` | `/funding-sources/{source_id}/allocations/{allocation_id}` | Soft delete an expense category allocation from a funding source. | [delete_funding_sources_by_id_allocations_by_id.md](./delete_funding_sources_by_id_allocations_by_id.md) |
