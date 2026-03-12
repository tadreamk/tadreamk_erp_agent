# 65. Rachel AI API

AI assistant powered by Gemini LLM. Users send natural-language messages and receive AI-generated responses. Conversations are persisted and recent history is used as context for follow-up queries.

**Base path:** `/rachel-ai`

**Access control:** Authentication required. User must have `rachel-ai` whitelist access.

---

---

## Endpoints

| Method | Path | Description | Doc |
|--------|------|-------------|-----|
| `POST` | `/rachel-ai/chat` | Send a message to Rachel AI and receive a response. The last 5 conversations are | [post_rachel_ai_chat.md](./post_rachel_ai_chat.md) |
| `GET` | `/rachel-ai/history` | Get paginated conversation history for the current user, ordered by most recent  | [get_rachel_ai_history.md](./get_rachel_ai_history.md) |
