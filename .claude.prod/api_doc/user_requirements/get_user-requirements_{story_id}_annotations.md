# GET /user-requirements/{story_id}/annotations

List Annotations. Requires authentication.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| story_id | string |  |

**Response:**
```json
{
  "items": [
    {
      "id": "string",
      "story_id": "string",
      "start_offset": 0,
      "end_offset": 0,
      "highlighted_text": "string",
      "comment": "string",
      "is_ai_generated": false,
      "is_resolved": false,
      "resolved_by": "string",
      "resolved_by_preferred_name": "string",
      "resolved_at": "datetime",
      "created_by": "string",
      "created_by_preferred_name": "string",
      "created_at": "datetime",
      "suggested_answers": [
        "string"
      ],
      "replies": [
        {
          "id": {},
          "parent_annotation_id": {},
          "comment": {},
          "is_ai_generated": {},
          "created_by": {},
          "created_by_preferred_name": {},
          "created_at": {}
        }
      ]
    }
  ],
  "total": 0
}
```

**Errors:**
- `422` — Validation Error
