# PUT /job-post/{job_post_id}/translations/{lang}


Update translation for a specific language. Only `zh` and `zh-TW` are supported.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| lang | string | Language code: `zh` or `zh-TW` |

**Request Body:** Object with translated fields (title, description, responsibilities, etc.)

**Errors:**
- `400` — Invalid language code
- `404` — Job post not found
