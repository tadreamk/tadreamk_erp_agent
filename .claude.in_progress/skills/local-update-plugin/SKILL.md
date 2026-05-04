---
name: local-update-plugin
description: Sync .claude.prod assets (api_doc, skills, scripts, slides) to the
  tadreamk_erp_agent_plugin repo and bump the plugin version. Use when user says
  "update plugin", "sync plugin", "push to plugin", or "update-plugin".
model: claude-sonnet-4-6
---

# Update Plugin

Sync the production assets from `.claude.prod/` to the plugin repository and bump the version.

This command takes no arguments.

**Plugin directory**: `/Users/alan/Documents/projects/tadreamk_erp_agent_plugin/plugins/tadreamk-erp`
**Source directory**: `.claude.prod/`

## Step 1: Sync api_doc

Remove the existing `api_doc/` in the plugin and replace it with the one from `.claude.prod/`:

```bash
rm -rf /Users/alan/Documents/projects/tadreamk_erp_agent_plugin/plugins/tadreamk-erp/api_doc
cp -r .claude.prod/api_doc /Users/alan/Documents/projects/tadreamk_erp_agent_plugin/plugins/tadreamk-erp/api_doc
```

## Step 2: Sync skills

Remove the existing `skills/` in the plugin and replace it with the one from `.claude.prod/`:

```bash
rm -rf /Users/alan/Documents/projects/tadreamk_erp_agent_plugin/plugins/tadreamk-erp/skills
cp -r .claude.prod/skills /Users/alan/Documents/projects/tadreamk_erp_agent_plugin/plugins/tadreamk-erp/skills
```

## Step 3: Bump version

Read `/Users/alan/Documents/projects/tadreamk_erp_agent_plugin/plugins/tadreamk-erp/.claude-plugin/plugin.json` and increment the **minor** version by one, resetting the patch to 0. For example:
- `0.1.1` → `0.2.0`
- `0.3.5` → `0.4.0`
- `1.2.3` → `1.3.0`

Update the `"version"` field in `plugin.json` with the new version.

## Step 4: Display Results

Count the synced files and report:

```
Plugin updated:
  api_doc: X files across Y modules
  skills:  Z skills synced
  version: <old_version> → <new_version>

Plugin path: /Users/alan/Documents/projects/tadreamk_erp_agent_plugin/plugins/tadreamk-erp
```
