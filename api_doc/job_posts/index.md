# Job Posts API

Job posting system with multilingual support. Supports a status workflow (draft -> published -> closed), AI-powered translation to Chinese, and public listing for candidates.

**Departments:** Engineering, Design, Marketing, Sales, Human Resources, Finance, Operations, Legal, Customer Support, Product

**Job Types:** full_time, part_time, contract, internship (etc. — values from `JobType` enum)

**Status Workflow:**
- `draft` -> `published` (via `/publish`)
- `published` -> `closed` (via `/close`)
- `closed` -> `published` (via `/republish`)

---

## Public Endpoints (No Authentication)

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `GET` | `/job-posts` | List published job posts. No authentication required. | [get_job_posts.md](./get_job_posts.md) |
| `GET` | `/job-posts/departments` | Get list of unique departments from published job posts. | [get_job_posts_departments.md](./get_job_posts_departments.md) |
| `GET` | `/job-posts/job-types` | Get available job type options. | [get_job_posts_job_types.md](./get_job_posts_job_types.md) |
| `GET` | `/job-posts/{job_post_id}` | Get single published job post by ID. Supports language selection for translated  | [get_job_posts_by_id.md](./get_job_posts_by_id.md) |
| `GET` | `/job-post` | List all job posts with optional filtering. | [get_job_post.md](./get_job_post.md) |
| `GET` | `/job-post/options` | Get available options for job post creation form. | [get_job_post_options.md](./get_job_post_options.md) |
| `POST` | `/job-post` | Create a new job post. Created with status `draft`. | [post_job_post.md](./post_job_post.md) |
| `GET` | `/job-post/{job_post_id}` | Get a specific job post by ID. | [get_job_post_by_id.md](./get_job_post_by_id.md) |
| `PUT` | `/job-post/{job_post_id}` | Update an existing job post. All fields optional. | [put_job_post_by_id.md](./put_job_post_by_id.md) |
| `DELETE` | `/job-post/{job_post_id}` | Soft delete a job post (sets `is_active=false`). | [delete_job_post_by_id.md](./delete_job_post_by_id.md) |
| `POST` | `/job-post/{job_post_id}/duplicate` | Duplicate an existing job post. Creates a copy with "[Copy]" prefix in title and | [post_job_post_by_id_duplicate.md](./post_job_post_by_id_duplicate.md) |
| `POST` | `/job-post/{job_post_id}/publish` | Publish a draft job post. Sets `published_at` timestamp. | [post_job_post_by_id_publish.md](./post_job_post_by_id_publish.md) |
| `POST` | `/job-post/{job_post_id}/close` | Close a published job post. Sets `closed_at` timestamp. | [post_job_post_by_id_close.md](./post_job_post_by_id_close.md) |
| `POST` | `/job-post/{job_post_id}/republish` | Republish a closed job post. Updates `published_at` and clears `closed_at`. | [post_job_post_by_id_republish.md](./post_job_post_by_id_republish.md) |
| `POST` | `/job-post/translate` | Preview translation without saving. Uses Gemini AI to translate to zh and zh-TW. | [post_job_post_translate.md](./post_job_post_translate.md) |
| `POST` | `/job-post/{job_post_id}/translate` | Trigger background AI translation for a job post. Returns immediately; status ch | [post_job_post_by_id_translate.md](./post_job_post_by_id_translate.md) |
| `GET` | `/job-post/{job_post_id}/translations` | Get all translations for a job post. | [get_job_post_by_id_translations.md](./get_job_post_by_id_translations.md) |
| `PUT` | `/job-post/{job_post_id}/translations/{lang}` | Update translation for a specific language. Only `zh` and `zh-TW` are supported. | [put_job_post_by_id_translations_by_id.md](./put_job_post_by_id_translations_by_id.md) |
