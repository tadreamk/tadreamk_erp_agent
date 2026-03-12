# GET /exercises/tags


Get the predefined list of valid tags.

**Response:**
```json
{
  "tags": [
    "frontend",
    "backend",
    "database",
    "machine-learning",
    "computer-vision",
    "nlp",
    "llm",
    "algorithms",
    "system-design",
    "generative-ai"
  ]
}
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
