# Funding Utilization API

Read-only analytics endpoints that show how funding has been utilized across sources and expense categories. Provides summary totals, per-category breakdowns, per-source breakdowns, and detailed expense lists.

**Access control:** Whitelist `funding-sources` required for all endpoints (same whitelist as Funding Sources).

---

## 44. Funding Utilization

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/funding-utilization/summary` | Get an overall summary of funding utilization across all active funding sources. | [get_funding_utilization_summary.md](./get_funding_utilization_summary.md) |
| `GET` | `/funding-utilization/by-category` | Get utilization totals grouped by expense category. | [get_funding_utilization_by_category.md](./get_funding_utilization_by_category.md) |
| `GET` | `/funding-utilization/by-source` | Get utilization for each individual funding source. | [get_funding_utilization_by_source.md](./get_funding_utilization_by_source.md) |
| `GET` | `/funding-utilization/source/{funding_source_id}` | Get detailed utilization for a specific funding source, including a breakdown by | [get_funding_utilization_source_by_id.md](./get_funding_utilization_source_by_id.md) |
| `GET` | `/funding-utilization/source/{funding_source_id}/expenses` | Get recent expenses that have been allocated from a specific funding source. | [get_funding_utilization_source_by_id_expenses.md](./get_funding_utilization_source_by_id_expenses.md) |
