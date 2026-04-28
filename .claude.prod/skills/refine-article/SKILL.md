---
name: refine-article
description: Refine an article for grammar, punctuation, and clarity without
  changing its content. Works on a local markdown file the user points at OR on
  a live published article fetched by URL/slug (which is then re-uploaded). Use
  when the user says "refine article", "polish article", "grammar check",
  "proofread article", "clean up article", "fix grammar", or pastes an article
  URL with refinement intent.
---

# Refine Article

Refine an article so it reads as grammatically correct, idiomatic, and well-punctuated — **without** changing its content, structure, or tone. The skill operates in one of two modes depending on what the user provides:

- **File mode** — refine one or more local markdown files in place. The user points at the files; the skill does not assume any particular directory layout.
- **Live mode** — fetch a published article from the API by slug or public URL, refine it, and PUT the refined content + translations back to the API.

The user's request is: $ARGUMENTS

`$ARGUMENTS` may be:
- A **public URL** — `https://tadreamk.com/magazine/<section>/<slug>` or `https://tadreamk.com/news/<slug>` → live mode
- A **slug for a live article** with explicit live intent (e.g. `live setting-up-mpf` or `published setting-up-mpf`) → live mode
- A **path to a markdown file** (e.g. `notes/draft.md`) → file mode, refine that single file
- Empty — ask the user whether they want to refine a file (which path?) or a live article (which URL?), then continue

If multiple file paths are passed, refine each independently.

## Scope of changes (read this first)

This skill is **non-rewriting**. Apply only the kinds of edits a careful copy-editor would make:

**Allowed**
- Fix spelling, typos, subject-verb agreement, tense consistency, article (a/an/the) usage, pronoun agreement
- Fix punctuation (commas, periods, quotation marks, hyphens, em-dashes), capitalisation, and spacing
- Replace awkward or ambiguous phrasing with a clearer wording that preserves meaning
- Tighten redundant words ("in order to" → "to") only when the meaning is unchanged
- For Chinese (zh, zh-TW): fix typos, punctuation (use full-width 。，：；「」『』（）), incorrect characters, and Mainland-vs-Taiwan vocabulary mismatches. zh-TW must use Traditional characters and Taiwan-localised terminology; zh must use Simplified characters

**Not allowed**
- Adding new facts, examples, claims, or sentences that weren't in the source
- Removing sentences or sections, or merging/splitting paragraphs in a way that changes structure
- Reordering sections, headings, or list items
- Changing tone (e.g. casual → formal) or voice
- Translating between languages, or swapping technical terms for different ones
- Changing or "improving" markdown formatting beyond fixing broken syntax (do NOT promote H3 → H2, add bullets, etc.)
- Touching anything inside fenced code blocks (` ``` `), inline code (`` ` ``), URLs, image paths, or HTML tags
- Replacing proper nouns, brand names, person names, or product names

If a sentence is **technically correct but you would phrase it differently**, leave it alone. The bar is "is this an error or genuinely confusing?", not "is this how I would write it?".

## Step 0: Resolve Mode and Target

Inspect `$ARGUMENTS` and pick exactly one mode.

**`mode = "live"`** if `$ARGUMENTS` contains:
- a URL starting with `https://tadreamk.com/magazine/` or `https://tadreamk.com/news/` — extract the **last path segment** as the slug, OR
- the keyword `live` / `published` / `online` / `remote` followed by a slug.

**`mode = "file"`** if `$ARGUMENTS` is one or more file paths. Confirm each path exists; if any does not, list the missing ones and ask.

If `$ARGUMENTS` is empty or ambiguous, ask the user once whether to refine a local file (request a path) or a live article (request a URL or slug).

State the resolved mode out loud (one short line) before continuing, e.g.:
- `Mode: file — notes/draft.md`
- `Mode: live — slug "setting-up-mpf" via https://tadreamk.com/magazine/erp/setting-up-mpf`

## Step 1: Load Source

### File mode

Read each target file's full content. Keep the originals in memory (`original_<path>`) for the diff summary in Step 5.

### Live mode

Live mode uses **`WEBAPP_ACCESS_TOKEN`** for both the download (GET) and the re-upload (PUT) — load it once at the start of this step and reuse it.

**Load the token.** Read `WEBAPP_ACCESS_TOKEN` from `.env` in the current working directory; if missing, fall back to `~/.claude/.env`. If still missing, tell the user to set it in either file and stop — without the token the skill cannot fetch or update the article.

```bash
TOKEN=$(grep WEBAPP_ACCESS_TOKEN .env 2>/dev/null | cut -d'=' -f2 | tr -d '[:space:]')
if [ -z "$TOKEN" ]; then
  TOKEN=$(grep WEBAPP_ACCESS_TOKEN ~/.claude/.env 2>/dev/null | cut -d'=' -f2 | tr -d '[:space:]')
fi
```

**Resolve the slug to a UUID and fetch the article body.** The public-by-slug endpoint is the only one that takes a slug, so call it first to obtain the `id`. Pass the bearer token on this call too — the endpoint accepts it, and using the same token everywhere keeps live mode token-scoped end to end:

```bash
curl -s "https://api-erp.tadreamk.com/api/v1/articles-public/<slug>" \
  -H "Authorization: Bearer $TOKEN"
```

Extract from the response:
- `id` — UUID, needed for the PUT in Step 4
- `slug`, `title`, `summary`, `content`, `category`, `author`, `read_time`, `cover_image_url`, `status`
- `translations` — a dict that may contain `zh` and `zh-TW` keys, each with `title`, `summary`, `content`

Treat the response as the **single source of truth**. Live mode does not touch the local filesystem at any point.

**Errors**
- `404` → slug is wrong or the article is not published; surface and stop.
- `401` / `403` → the token is invalid or missing the articles whitelist; surface and stop.

Keep the originals in memory (`original_en_*`, `original_zh_*`, `original_zh-TW_*`) for the diff summary in Step 5.

## Step 2: Refine

Refine each text body independently using the rules in the **Scope of changes** section above. Do this work **inline** (do not call external grammar APIs).

For each body:
1. Walk the markdown paragraph by paragraph.
2. **Skip protected regions verbatim** — fenced code blocks, inline code spans, link/image URLs, HTML tags, and the literal text inside `![...](...)` URL portions must be copied through unchanged.
3. Apply only the edits allowed in the Scope section. Preserve heading levels, list markers, blank-line structure, and bold/italic emphasis.
4. Preserve image-with-caption blocks exactly:
   ```markdown
   ![Diagram description|center](https://...)

   *Brief description of what the diagram shows*
   ```
   You may correct grammar inside the alt text or italic caption, but do not change the URL or the `|center` modifier.

If a paragraph has no errors, output it byte-identical to the input.

In **live mode**, also refine the article's `title` and `summary`, and the `title` / `summary` inside each present translation locale (`zh`, `zh-TW`).

**Language-specific notes**
- **English** — favour standard written English. Do not Americanise British spelling or vice-versa; match whatever the source already uses. If the source mixes both, pick the dominant style and align stragglers.
- **Simplified Chinese (`zh`)** — use Mainland Simplified characters and Mainland-standard terminology. Use full-width punctuation (`。，：；「」（）`).
- **Traditional Chinese (`zh-TW`)** — use Traditional characters and Taiwan-localised terminology (e.g. 軟體 not 軟件, 程式 not 程序 in the software sense). Use full-width punctuation. The CJK quote convention for zh-TW is 「」 / 『』.

## Step 3: Write Back (file mode)

Skip this step in live mode.

Write each refined file back to its original path, overwriting the source.

## Step 4: Re-upload (live mode)

Skip this step in file mode.

PUT the refined fields back using the same `$TOKEN` loaded in Step 1. Always include `title`, `summary`, `content`, and `translations` together in the same PUT to keep them consistent.

```bash
cat > /tmp/refine_article_put.json <<'ENDJSON'
{
  "title": "<refined English title>",
  "summary": "<refined English summary>",
  "content": "<refined English content>",
  "translations": {
    "zh": {
      "title": "<refined zh title>",
      "summary": "<refined zh summary>",
      "content": "<refined zh content>"
    },
    "zh-TW": {
      "title": "<refined zh-TW title>",
      "summary": "<refined zh-TW summary>",
      "content": "<refined zh-TW content>"
    }
  }
}
ENDJSON

curl -s -X PUT "https://api-erp.tadreamk.com/api/v1/articles/<article_id>" \
  -H "Authorization: Bearer $TOKEN" \
  -H "Content-Type: application/json" \
  -d @/tmp/refine_article_put.json

rm /tmp/refine_article_put.json
```

Use the temp-file pattern (`-d @file.json`) — the markdown content contains characters that break inline shell quoting.

If a translation locale (`zh` or `zh-TW`) was missing in the GET response, omit it from the `translations` object in the PUT. Never invent a translation that didn't exist.

**Error handling**
- `401` / `403` — token missing or article not writable; surface the message and stop.
- `404` — article id no longer exists; surface and stop.
- `422` — validation error; show the detail.

## Step 5: Report

Count changed lines per body (a line counts as changed if its trimmed content differs from the original).

### File mode

```
Refined file(s):

notes/draft.md       — 7 lines changed
notes/draft_zh.md    — no changes needed

Highlights:
- Fixed subject-verb agreement in 2 paragraphs
- Replaced half-width punctuation with full-width (zh)
- Tightened opening sentence
```

### Live mode

```
Refined live article: <slug>  (id: <article_id>)

Title (en)           — updated
Summary (en)         — updated
Content (en)         — 9 lines changed
Title (zh)           — no change
Summary (zh)         — updated
Content (zh)         — 5 lines changed
Title (zh-TW)        — updated
Summary (zh-TW)      — updated
Content (zh-TW)      — 5 lines changed

Highlights:
- Fixed two run-on sentences in the English body
- Replaced half-width commas with full-width in zh-TW
- Tightened English summary

Public URL: https://tadreamk.com/<category-path>/<slug>
```

Compute the public URL using the same category-to-prefix mapping used by `/article-upload`:

| Category | URL prefix |
|---|---|
| `TadReamk AI` | `https://tadreamk.com/magazine/ai/` |
| `TadReamk Design` | `https://tadreamk.com/magazine/design/` |
| `IP Law` | `https://tadreamk.com/magazine/law/` |
| `News` | `https://tadreamk.com/news/` |
| `TadReamk-AIGC` | `https://tadreamk.com/magazine/aigc/` |
| `TadReamk-ERP` | `https://tadreamk.com/magazine/erp/` |

If a body had **zero** changes, say so explicitly (e.g. `Content (zh) — no change`) so the user knows it was reviewed.

The "Highlights" list should be 3–6 short bullets describing the **kinds** of fixes made. Do not list every individual edit.

## Notes

- **Idempotency** — running this skill twice on the same article should be a no-op the second time. If it isn't, the first pass overstepped the Scope rules.
- **No translation drift** — refining English must not pull in zh/zh-TW phrasing, and vice versa. Each language is refined against its own text only.
- **Live mode does not touch the local filesystem.** It reads from the API and writes back to the API.
- **File mode does not call the API.** It refines the file in place; nothing is uploaded.
- **Off-limits in both modes** — never re-render diagrams or modify `category`, `author`, `read_time`, `cover_image_url`, `status`, or any non-text field.
