# Job Posts API

Public prefix: `/job-posts` (no auth required)
Admin prefix: `/job-post` (requires `job-posts` whitelist)

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /job-posts | None | List published job posts | [get_job-posts.md](get_job-posts.md) |
| GET | /job-posts/departments | None | Get departments from published posts | [get_job-posts_departments.md](get_job-posts_departments.md) |
| GET | /job-posts/job-types | None | Get available job types | [get_job-posts_job-types.md](get_job-posts_job-types.md) |
| GET | /job-posts/{job_post_id} | None | Get published job post by ID | [get_job-posts_{job_post_id}.md](get_job-posts_{job_post_id}.md) |
| GET | /job-post | `job-posts` whitelist | List all job posts (admin) | [get_job-post.md](get_job-post.md) |
| GET | /job-post/options | `job-posts` whitelist | Get form options | [get_job-post_options.md](get_job-post_options.md) |
| POST | /job-post | `job-posts` whitelist | Create a job post | [post_job-post.md](post_job-post.md) |
| GET | /job-post/{job_post_id} | `job-posts` whitelist | Get job post by ID | [get_job-post_{job_post_id}.md](get_job-post_{job_post_id}.md) |
| PUT | /job-post/{job_post_id} | `job-posts` whitelist | Update a job post | [put_job-post_{job_post_id}.md](put_job-post_{job_post_id}.md) |
| DELETE | /job-post/{job_post_id} | `job-posts` whitelist | Soft delete a job post | [delete_job-post_{job_post_id}.md](delete_job-post_{job_post_id}.md) |
| POST | /job-post/{job_post_id}/duplicate | `job-posts` whitelist | Duplicate a job post | [post_job-post_{job_post_id}_duplicate.md](post_job-post_{job_post_id}_duplicate.md) |
| POST | /job-post/{job_post_id}/publish | `job-posts` whitelist | Publish a draft post | [post_job-post_{job_post_id}_publish.md](post_job-post_{job_post_id}_publish.md) |
| POST | /job-post/{job_post_id}/close | `job-posts` whitelist | Close a published post | [post_job-post_{job_post_id}_close.md](post_job-post_{job_post_id}_close.md) |
| POST | /job-post/{job_post_id}/republish | `job-posts` whitelist | Republish a closed post | [post_job-post_{job_post_id}_republish.md](post_job-post_{job_post_id}_republish.md) |
| POST | /job-post/translate | `job-posts` whitelist | Translate content (preview) | [post_job-post_translate.md](post_job-post_translate.md) |
| POST | /job-post/{job_post_id}/translate | `job-posts` whitelist | Trigger background translation | [post_job-post_{job_post_id}_translate.md](post_job-post_{job_post_id}_translate.md) |
| GET | /job-post/{job_post_id}/translations | `job-posts` whitelist | Get translations | [get_job-post_{job_post_id}_translations.md](get_job-post_{job_post_id}_translations.md) |
| PUT | /job-post/{job_post_id}/translations/{lang} | `job-posts` whitelist | Update translation for lang | [put_job-post_{job_post_id}_translations_{lang}.md](put_job-post_{job_post_id}_translations_{lang}.md) |
