# GET /job-posts/{job_post_id}


Get single published job post by ID. Supports language selection for translated content.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| job_post_id | UUID | Job post ID |

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| lang | string | No | Language code: `en`, `zh`, `zh-TW` (default: `en`) |

**Response:** Full job post object. If `lang` is specified and translations exist, `title`, `description`, `responsibilities`, `requirements`, and `benefits` fields are replaced with the translated version.

**Errors:**
- `404` — Job post not found or not published

---

## Admin Endpoints (Whitelist: job-posts)
