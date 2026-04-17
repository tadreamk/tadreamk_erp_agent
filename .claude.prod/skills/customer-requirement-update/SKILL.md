---
name: customer-requirement-update
description: Update an existing customer requirement document by merging new details
  or update points into the current content, then re-injecting via WebSocket. Use
  when user says "update requirement", "update customer requirement", "add details to requirement",
  "fill in requirement", or provides a share token with update points.
---

# Customer Requirement Update

Fetch the current content of an existing customer requirement document, merge the user's update points into it, re-inject the result via WebSocket, and optionally update title/summary/status via the REST API.

The user's input is: $ARGUMENTS

If `$ARGUMENTS` is empty or has no identifiable share token, ask the user to provide:
1. The share token or public URL of the document to update
2. The update points or additional details to incorporate

## Input format

`$ARGUMENTS` may contain:
- A **share token** (12-char alphanumeric, e.g. `mpcplK0XCcoA`) or a **full public URL** (`https://erp.tadreamk.com/shared/customer-requirements/<token>`)
- Followed by the **update instructions** — free-form bullet points, sentences, or structured details to merge into the document

Examples:
```
mpcplK0XCcoA add non-functional: page load under 2s, 99.9% uptime, HTTPS only
https://erp.tadreamk.com/shared/customer-requirements/mpcplK0XCcoA stakeholders: Alan (owner), Lisa (staff), Tom (staff); timeline: 3 months MVP
mpcplK0XCcoA status: In Review. Payment gateway: Stripe. Hosting: Vercel + Supabase.
```

Extract the share token:
- If a full URL is present: take the last path segment as the token
- Otherwise: take the first whitespace-delimited token that is exactly 12 alphanumeric characters

Everything after the token is the **update payload**.

## Language detection

Scan the **update payload** for a language indicator:
- `chinese` / `中文` / `zh` → **Simplified Chinese** (`zh-CN`)
- `traditional chinese` / `繁體` / `zh-TW` → **Traditional Chinese** (`zh-TW`)
- Otherwise → match the **language already used in the existing document** (detected in Step 2)

## Timing

Record the wall-clock start time at the very beginning of Step 0 using `python3 -c "import time; print(int(time.time()*1000))"`. Record a per-step start time at the beginning of each step and compute its duration when the step finishes.

## Step 0: Load Token

Record step start time. Read `.env` in the current working directory and extract `WEBAPP_ACCESS_TOKEN`. If missing, try `~/.claude/.env` as a fallback. If still missing, tell the user to set it and stop.

## Step 1: Resolve Share Token

Record step start time. Parse `$ARGUMENTS` as described above to extract:
- `share_token` — the 12-character document token
- `update_payload` — everything remaining (the update instructions)

If no valid share token is found, ask the user to provide one and stop.

## Step 2: Fetch Current Document

Record step start time. Run two operations in parallel:

**2a — Fetch metadata** (no auth needed):
```bash
curl -s "https://api-erp.tadreamk.com/api/v1/customer-requirements/public/<share_token>"
```
Extract from the response:
- `id` — UUID (needed for optional PUT in Step 4)
- `title` — current title
- `share_token` — confirm it matches

**2b — Read current markdown body via WebSocket**:
```bash
python3 .claude.prod/scripts/read_yjs_content.py <share_token>
```
Capture stdout as `current_content`.

If `current_content` is empty or blank, the document body has not been set yet — treat it as an empty outline and proceed.

## Step 3: Merge Update Points

Record step start time. Analyse `current_content` and `update_payload`, then produce `updated_content` by applying the following rules:

1. **Preserve structure** — keep the existing section headings and all content that is not being changed.
2. **Fill placeholders** — if the user supplies information for a section currently marked `_To be defined._` (or its Chinese equivalents), replace the placeholder with the provided content formatted consistently with the rest of the document.
3. **Append new information** — if the user provides information that extends an existing section, append it to that section rather than overwriting it.
4. **Status / title / summary changes** — if the update payload mentions a new title, summary, or status (`Draft` → `In Review` → `Approved` → `Delivered`), note these separately as `new_title`, `new_summary`, `new_status` for Step 4; do NOT embed them as body text.
5. **Language consistency** — write all new content in the document's detected language.
6. **Do not invent** — only use information explicitly present in `update_payload`. Leave remaining placeholders as-is.

After merging, show the user a concise diff-style summary of what changed (e.g. "Filled: Non-Functional Requirements, Stakeholders. Updated: Timeline.") before proceeding.

## Step 4: Re-inject Body via WebSocket

Record step start time. Write `updated_content` to a temp file and run the injection script:

```bash
cat > /tmp/cr_update_content.md <<'ENDMD'
<updated_content from Step 3>
ENDMD

python3 .claude.prod/scripts/inject_yjs_content.py <share_token> /tmp/cr_update_content.md

rm /tmp/cr_update_content.md
```

## Step 4b: Update Metadata via REST (if changed)

Record step start time (skip and record 0 ms if no metadata changed). If `new_title`, `new_summary`, or `new_status` were identified in Step 3, PATCH the document via PUT:

```bash
TOKEN=$(grep WEBAPP_ACCESS_TOKEN .env | cut -d'=' -f2 | tr -d '[:space:]')

cat > /tmp/cr_update_meta.json <<ENDJSON
{
  "title": "<new_title or existing title>",
  "summary": "<new_summary or existing summary>",
  "status": "<new_status or existing status>"
}
ENDJSON

curl -s -X PUT "https://api-erp.tadreamk.com/api/v1/customer-requirements/<id>" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/cr_update_meta.json

rm /tmp/cr_update_meta.json
```

**Error handling:**
- `401` / `403` — token expired or missing whitelist; inform the user
- `404` — document not found or deleted
- `422` — validation error; show the detail

## Step 5: Display Results

Record step start time and compute total elapsed time (current ms minus global start ms).

Show the user:

```
Customer requirement updated.

Title:      <title>
Status:     <status>
Token:      <share_token>
Changes:    <concise list: e.g. "Filled: Non-Functional Requirements, Stakeholders | Updated: Timeline | Status: Draft → In Review">

Public URL: https://erp.tadreamk.com/shared/customer-requirements/<share_token>

--- Timing ---
Step 0  Load Token          <Xs>
Step 1  Resolve Token       <Xs>
Step 2  Fetch Document      <Xs>
Step 3  Merge Updates       <Xs>
Step 4  Re-inject Body      <Xs>
Step 4b Update Metadata     <Xs>
Step 5  Display Results     <Xs>
─────────────────────────────────
Total                       <Xs>
```

Then display the **full updated markdown** so the user can review it.

Remind the user they can open the Public URL to view and collaboratively edit the document in real time.
