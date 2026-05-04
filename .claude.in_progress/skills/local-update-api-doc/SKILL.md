---
name: local-update-api-doc
description: Sync the local .claude.prod/api_doc/ directory with the latest API documentation
  from the fullstack ERP project. Use when user says "update api doc", "sync api doc",
  "refresh api doc", or "api-doc-update".
model: claude-sonnet-4-6
---

# API Doc Update

Replace the local `.claude.prod/api_doc/` directory with the latest version from the fullstack ERP project.

This command takes no arguments.

## Step 1: Remove existing api_doc

Delete the current `.claude.prod/api_doc/` directory:

```bash
rm -rf /Users/alan/Documents/projects/tadreamk_erp_agent/.claude.prod/api_doc
```

## Step 2: Copy latest api_doc from source

Copy the full `api_doc/` directory from the fullstack ERP project:

```bash
cp -r /Users/alan/Documents/projects/fullstack_erp/docs/api_doc /Users/alan/Documents/projects/tadreamk_erp_agent/.claude.prod/api_doc
```

## Step 3: Verify

Count the copied files and list the module directories:

```bash
find /Users/alan/Documents/projects/tadreamk_erp_agent/.claude.prod/api_doc -type f | wc -l
ls /Users/alan/Documents/projects/tadreamk_erp_agent/.claude.prod/api_doc/
```

## Step 4: Update erp-general-query skill

Read the list of module directories from the newly copied api_doc and update the "Available modules" block in `.claude.prod/skills/erp-general-query/SKILL.md`.

1. List the module directories: `ls /Users/alan/Documents/projects/tadreamk_erp_agent/.claude.prod/api_doc/`
2. Format them as a comma-separated list wrapped in a fenced code block.
3. Replace the existing `Available modules:` section (from the line `Available modules:` through the closing `` ``` ``) with the updated list.

## Step 5: Display Results

Report the sync result:

```
API doc updated — X files across Y modules synced from fullstack_erp/docs/api_doc.
erp-general-query skill updated with Y modules.
```
