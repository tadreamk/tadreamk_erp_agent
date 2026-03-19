---
name: guide-page-draft
description: Generate a guide page in Markdown, saving it locally as a draft for
  review before uploading. Use when user says "write a guide page", "guide page
  draft", "draft guide page", "create guide page", or "generate guide page".
disable-model-invocation: true
---

# Guide Page Draft

Generate a guide page in Markdown and save it locally as a draft for review before uploading.

The user's request is: $ARGUMENTS

If the request is empty or unclear, ask the user to describe what guide page they want written. Example:
```
/guide-page-draft Write a guide page about how to submit a leave request
```

## Step 1: Determine Metadata

Based on the user's request, determine the following:

1. **filename** — Derive from the topic. Use lowercase kebab-case (e.g., `how-to-submit-leave`, `equipment-request-guide`). This will also be used as the **slug**.
2. **title** — A clear, descriptive title (max 255 chars).
3. **section** — Ask the user to select a section using the AskUserQuestion tool. Suggest relevant options based on the topic, e.g.: `General`, `HR`, `Finance`, `IT`, `Operations`, `Onboarding`. The user can also type a custom section name.
4. **sort_order** — Default to `0`. Ask the user if they want a specific display order within the section.

## Step 2: Write the Guide Page Content

Generate a professional, employee-facing guide page in **Markdown** format:

- Write clear, actionable content appropriate for an internal company knowledge base
- Use H2 (`##`) and H3 (`###`) headings to organize sections
- Include step-by-step instructions where appropriate
- Use bullet lists and numbered lists as needed
- Include tips, notes, or warnings using bold text (e.g., **Note:** or **Important:**)
- Keep the tone professional but approachable
- Do NOT include the title as an H1 heading in the content — the title is stored separately in metadata

**Markdown formatting rules:**
- **Bullet lists**: Do NOT put blank lines between consecutive list items. Write them as tight lists.
- **Numbered lists**: Same rule — no blank lines between items.

## Step 3: Save Files Locally

Create the output directory if it doesn't exist: `data/guide_pages/`

Save two files:

1. **`data/guide_pages/{filename}.md`** — The Markdown content body only (no title H1)
2. **`data/guide_pages/{filename}_meta.json`** — Metadata file with this structure:
   ```json
   {
     "slug": "how-to-submit-leave",
     "title": "How to Submit a Leave Request",
     "section": "HR",
     "sort_order": 0,
     "is_active": true
   }
   ```

## Step 4: Summary

Display a summary to the user:
- Guide page title
- Slug / filename
- Section and sort order
- Local path (`data/guide_pages/{filename}.md`)
- A preview of the first few lines of content
- Remind the user they can review/edit the files, then run `/guide-page-upload` to publish
