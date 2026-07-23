# Job Posts API

Base prefixes:
- `/job-posts`
- `/job-posts/public`
- `/job-posts/{job_post_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /job-posts | Authenticated | List Job Posts | [get_job-posts.md](get_job-posts.md) |
| POST | /job-posts | Authenticated | Create Job Post | [post_job-posts.md](post_job-posts.md) |
| GET | /job-posts/public | Public | List Public Job Posts | [get_job-posts_public.md](get_job-posts_public.md) |
| GET | /job-posts/public/{job_post_id} | Public | Get Public Job Post | [get_job-posts_public_{job_post_id}.md](get_job-posts_public_{job_post_id}.md) |
| GET | /job-posts/{job_post_id} | Authenticated | Get Job Post | [get_job-posts_{job_post_id}.md](get_job-posts_{job_post_id}.md) |
| PUT | /job-posts/{job_post_id} | Authenticated | Update Job Post | [put_job-posts_{job_post_id}.md](put_job-posts_{job_post_id}.md) |
| POST | /job-posts/{job_post_id}/close | Public | Close Job Post | [post_job-posts_{job_post_id}_close.md](post_job-posts_{job_post_id}_close.md) |
| POST | /job-posts/{job_post_id}/publish | Public | Publish Job Post | [post_job-posts_{job_post_id}_publish.md](post_job-posts_{job_post_id}_publish.md) |
| POST | /job-posts/{job_post_id}/republish | Public | Republish Job Post | [post_job-posts_{job_post_id}_republish.md](post_job-posts_{job_post_id}_republish.md) |
