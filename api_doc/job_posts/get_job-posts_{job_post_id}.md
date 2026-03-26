# GET /job-posts/{job_post_id}

Get a single published job post by ID. Supports language selection for translated content. No authentication required.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | The job post's unique identifier |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| lang | string | No | Language code (en, zh, zh-TW) — default: en |

**Response:** Full job post object with localized content if available

**Errors:**
- `404` — Job post not found or not published
