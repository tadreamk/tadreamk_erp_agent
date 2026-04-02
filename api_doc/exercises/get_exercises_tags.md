# GET /exercises/tags

Get list of predefined tags available for exercises. Requires `exercise` whitelist.

**Response:**
```json
{
  "tags": ["frontend", "backend", "database", "machine-learning", "computer-vision", "nlp", "llm", "algorithms", "system-design", "generative-ai"]
}
```

**Errors:**
- `401` — Not authenticated
- `403` — No exercise whitelist access
