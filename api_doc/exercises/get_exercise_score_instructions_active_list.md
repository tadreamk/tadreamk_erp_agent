# GET /exercise-score-instructions/active-list


Get a lightweight list of active score instructions for dropdown/select inputs.

**Response:**
```json
{
  "instructions": [
    { "id": "uuid", "title": "Instruction Title" }
  ]
}
```

**Errors:**
- `401` -- Not authenticated
- `403` -- No whitelist access to exercise section
