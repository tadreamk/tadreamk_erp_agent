# GET /articles-public


List published articles. No authentication required.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| category | string | No | Filter by category |
| page | int | No | Page number (default: 1, min: 1) |
| limit | int | No | Items per page (default: 20, min: 1, max: 100) |

**Response:** Same pagination structure as admin list, but only returns articles with status `published`, sorted by `publish_date` descending.
