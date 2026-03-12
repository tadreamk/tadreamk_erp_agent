# PUT /job-post/{job_post_id}


Update an existing job post. All fields optional.

**Request Body:** Same fields as create, all optional. Additionally:
| Field | Type | Description |
|-------|------|-------------|
| translations | object | Translation data keyed by language code |
| translation_status | string | Translation status |

**Errors:**
- `404` — Job post not found
