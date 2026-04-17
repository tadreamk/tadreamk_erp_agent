# POST /customer-requirements/public/{token}/format

Reformat the current editor text into well-structured Markdown via Google Gemini. **No authentication.** Shares the 60 req/min/IP rate limit with the other public endpoints.

**Path parameter:** `token` — the 12-character share token.

**Request body:**
```json
{ "content": "raw text to reformat" }
```

Max input: 100 KB (UTF-8 encoded).

**Response:**
```json
{ "formatted": "# Reformatted\n\n- well-structured\n- markdown\n..." }
```

**Behaviour:**

- Gemini is called with a fixed system prompt instructing it to rewrite the input as GFM Markdown while preserving all original meaning. No commentary is added.
- The frontend replaces the Yjs `Y.Text` in a single transaction when this call succeeds, so every open tab converges on the rewritten content.
- Wrapping ` ```markdown ... ``` ` fences are stripped server-side if the model returns them.

**Errors:**
- `400` — input exceeds 100 KB (`FormatTooLargeError`)
- `404` — token unknown / soft-deleted / `disabled`
- `429` — IP rate limit exceeded
- `502` — LLM call failure (network error, no candidates, or safety block)
