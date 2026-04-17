---
name: customer-requirement-draft
description: Draft a customer requirement document, create it via API, and return
  the public share URL. Use when user says "customer requirement", "draft requirement",
  "requirement doc", "create requirement", or "new customer requirement".
---

# Customer Requirement Draft

Draft a customer requirement document based on the user's query, create it in the ERP system, and return the public share link.

The user's request is: $ARGUMENTS

If the request is empty or unclear, ask the user to describe what the requirement document is about (e.g. the feature, project, or problem they need to document).

**Language detection:** Scan `$ARGUMENTS` for a language indicator:
- If the user mentions `chinese` / `中文` / `zh` → use **Simplified Chinese** (`zh-CN`). All section headings, placeholder text, and drafted content must be written in Simplified Chinese.
- If the user mentions `traditional chinese` / `繁體` / `zh-TW` → use **Traditional Chinese** (`zh-TW`).
- Otherwise → default to **English** (`en`).

The detected language applies to the entire document outline in Step 1 (headings, body text, placeholder lines such as `_待定义。_` for Chinese). The title and summary sent to the API in Step 2 must also be in the chosen language.

**Auth token** is loaded from the `WEBAPP_ACCESS_TOKEN` variable — first from `.env` in the current working directory, then from `~/.claude/.env` as a global fallback.
**API base URL**: `https://api-erp.tadreamk.com/api/v1`

## Timing

Record the wall-clock start time at the very beginning of Step 0 (before any work begins) using `date +%s%3N` (milliseconds). Record a per-step start time at the beginning of each step and compute its duration when the step finishes. Accumulate all durations for the final report in Step 3.

## Step 0: Load Token

Record step start time. Read `.env` in the current working directory and extract `WEBAPP_ACCESS_TOKEN`. If missing or empty, try `~/.claude/.env` as a fallback. If still missing, tell the user to set it in either `.env` (project-level) or `~/.claude/.env` (global) and stop.

## Step 1: Draft the Document Outline

Record step start time. Distribute the user's request into the outline structure below — only use information the user has provided. Do **not** invent, assume, or fill in content that is not present in the user's input. Leave a section's body as a single placeholder line if the user has not provided relevant information for it.

Write all headings, body text, and placeholder lines in the **language detected above**. Reference placeholders by language:
- English: `_To be defined._`
- Simplified Chinese: `_待定义。_`
- Traditional Chinese: `_待定義。_`

**English outline:**
```markdown
## Overview
## Background / Problem Statement
## Objectives
## Functional Requirements
## Non-Functional Requirements
## Acceptance Criteria
## Scope
**In scope:** / **Out of scope:**
## Stakeholders
## Timeline
## Notes / Open Questions
```

**Simplified Chinese outline (use these headings for zh-CN):**
```markdown
## 概述
## 背景 / 问题陈述
## 目标
## 功能需求
## 非功能需求
## 验收标准
## 范围
**范围内：** / **范围外：**
## 利益相关方
## 时间线
## 备注 / 待确认事项
```

**Traditional Chinese outline (use these headings for zh-TW):**
```markdown
## 概述
## 背景 / 問題陳述
## 目標
## 功能需求
## 非功能需求
## 驗收標準
## 範圍
**範圍內：** / **範圍外：**
## 利害關係人
## 時間線
## 備註 / 待確認事項
```

Also derive from the outline:
- **Title**: A concise document title drawn from the user's request (max 200 chars), in the chosen language
- **Summary**: 1–2 sentences paraphrasing the user's request (used as the dashboard description), in the chosen language

## Step 2: Create the Document via API

Record step start time. Create the document by POSTing to the API. Write the request body to a temp file to avoid shell escaping issues:

```bash
# Write body to temp file
cat > /tmp/cr_body.json <<'ENDJSON'
{
  "title": "<title from Step 1>",
  "summary": "<summary from Step 1>",
  "status": "Draft",
  "share_mode": "edit"
}
ENDJSON

# Create the requirement
curl -s -X POST "https://api-erp.tadreamk.com/api/v1/customer-requirements" \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d @/tmp/cr_body.json

# Clean up
rm /tmp/cr_body.json
```

From the response extract:
- `id` — UUID of the created requirement
- `share_token` — 12-character token used for the public share URL

**Error handling:**
- `401` / `403` — token expired or missing whitelist access; tell the user
- `422` — validation error; show the error detail

## Step 2b: Inject Markdown Body via WebSocket

Record step start time. The editor stores content as a Yjs collaborative document. Inject the markdown outline drafted in Step 1 by writing it to a temp file and running the shared script:

```bash
# Write the markdown outline to a temp file
cat > /tmp/cr_content.md <<'ENDMD'
<full markdown outline from Step 1>
ENDMD

# Run the injection script
python3 .claude.prod/scripts/inject_yjs_content.py <share_token> /tmp/cr_content.md

# Clean up
rm /tmp/cr_content.md
```

The script connects to the WebSocket, applies the current server Yjs state, replaces the `content` Y.Text with the markdown, and sends the binary update. The server persists the snapshot within ~10 s.

## Step 3: Display Results

Record step start time for any display work, then compute the total elapsed time (current time minus the global start recorded in Step 0).

Show the user:

```
Customer requirement created.

Title:   <title>
Summary: <summary>
Status:  Draft
Token:   <share_token>

Public URL: https://erp.tadreamk.com/shared/customer-requirements/<share_token>

--- Timing ---
Step 0  Load Token          <Xs>
Step 1  Draft Outline       <Xs>
Step 2  Create via API      <Xs>
Step 2b Inject Body (WS)    <Xs>
Step 3  Display Results     <Xs>
─────────────────────────────────
Total                       <Xs>
```

Then display the full markdown outline so the user can review it.

Remind the user they can open the Public URL to view and collaboratively edit the document in real time.
