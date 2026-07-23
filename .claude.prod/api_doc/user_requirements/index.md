# User Requirements API

Base prefixes:
- `/user-requirements`
- `/user-requirements/annotations/{annotation_id}`
- `/user-requirements/{story_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /user-requirements | Authenticated | List Stories | [get_user-requirements.md](get_user-requirements.md) |
| POST | /user-requirements | Authenticated | Create Story | [post_user-requirements.md](post_user-requirements.md) |
| POST | /user-requirements/ai | Authenticated | Ai Create | [post_user-requirements_ai.md](post_user-requirements_ai.md) |
| POST | /user-requirements/annotations/{annotation_id}/ai-followup | Authenticated | Ai Followup | [post_user-requirements_annotations_{annotation_id}_ai-followup.md](post_user-requirements_annotations_{annotation_id}_ai-followup.md) |
| POST | /user-requirements/annotations/{annotation_id}/replies | Authenticated | Create Reply | [post_user-requirements_annotations_{annotation_id}_replies.md](post_user-requirements_annotations_{annotation_id}_replies.md) |
| PUT | /user-requirements/annotations/{annotation_id}/resolve | Authenticated | Resolve Annotation | [put_user-requirements_annotations_{annotation_id}_resolve.md](put_user-requirements_annotations_{annotation_id}_resolve.md) |
| DELETE | /user-requirements/{story_id} | Authenticated | Cancel Story | [delete_user-requirements_{story_id}.md](delete_user-requirements_{story_id}.md) |
| GET | /user-requirements/{story_id} | Authenticated | Get Story | [get_user-requirements_{story_id}.md](get_user-requirements_{story_id}.md) |
| PUT | /user-requirements/{story_id} | Authenticated | Update Story | [put_user-requirements_{story_id}.md](put_user-requirements_{story_id}.md) |
| POST | /user-requirements/{story_id}/ai-edit | Authenticated | Ai Prompt Edit | [post_user-requirements_{story_id}_ai-edit.md](post_user-requirements_{story_id}_ai-edit.md) |
| POST | /user-requirements/{story_id}/ai-edit-from-annotations | Authenticated | Ai Annotation Edit | [post_user-requirements_{story_id}_ai-edit-from-annotations.md](post_user-requirements_{story_id}_ai-edit-from-annotations.md) |
| GET | /user-requirements/{story_id}/annotations | Authenticated | List Annotations | [get_user-requirements_{story_id}_annotations.md](get_user-requirements_{story_id}_annotations.md) |
| POST | /user-requirements/{story_id}/annotations | Authenticated | Create Annotation | [post_user-requirements_{story_id}_annotations.md](post_user-requirements_{story_id}_annotations.md) |
| POST | /user-requirements/{story_id}/approve | Authenticated | Approve To Live | [post_user-requirements_{story_id}_approve.md](post_user-requirements_{story_id}_approve.md) |
| POST | /user-requirements/{story_id}/pick-up | Authenticated | Pick Up Story | [post_user-requirements_{story_id}_pick-up.md](post_user-requirements_{story_id}_pick-up.md) |
| POST | /user-requirements/{story_id}/ready-to-try | Authenticated | Ready To Try | [post_user-requirements_{story_id}_ready-to-try.md](post_user-requirements_{story_id}_ready-to-try.md) |
| POST | /user-requirements/{story_id}/submit | Authenticated | Submit Story | [post_user-requirements_{story_id}_submit.md](post_user-requirements_{story_id}_submit.md) |
