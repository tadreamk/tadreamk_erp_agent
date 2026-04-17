# TadReamk ERP Agent

An AI Agent project for interacting with the [TadReamk ERP System](https://erp.tadreamk.com) via natural language commands. The agent leverages Claude Code skills to automate common ERP workflows — writing and publishing articles, managing tasks, generating diagrams, and more.

## Project Structure

```
.claude.prod/api_doc/        # API documentation for all ERP modules
.claude.prod/skills/         # Claude Code skills for ERP operations
.claude.prod/scripts/        # Utility scripts (slide export, branding, Yjs injection)
.claude.prod/slides/         # Vite + React slide generator for article diagrams
.claude.prod/requirements.txt  # Python dependencies for all scripts under .claude.prod/scripts/
data/                        # Local drafts (articles, tasks) before uploading
```

## Available Skills

The skills below are included as examples to demonstrate how an AI agent can interact with the ERP API. You can modify them or create your own skills under `.claude.prod/skills/` to fit your workflow. Each skill is a folder with a `SKILL.md` file that defines the agent's behavior. See the [Claude Code skills documentation](https://docs.anthropic.com/en/docs/claude-code/skills) for details.

### Articles
- `/article-draft` — Generate a full article with diagram and translations (EN, zh, zh-TW)
- `/article-video-draft` — Generate an article with embedded video and translations
- `/article-upload` — Publish a local draft to GCS and the ERP database

### Tasks
- `/task-overview` — View active tasks for the configured user
- `/task-detail <slug>` — View task details by slug
- `/task-draft` — Create a local task draft
- `/task-add` — Upload a task draft to the ERP
- `/task-update <slug>` — Update an existing task

## Setup

### 1. Configure `.env`

Create a `.env` file at the project root with the following variables. All three are required for the Claude Code skills to work:

```
WEBAPP_ACCESS_TOKEN=<your ERP API token>
ARTICLE_AUTHOR_NAME=<your name>
TASK_USERNAME=<your ERP username>
```

| Variable | Used by | Description |
|----------|---------|-------------|
| `WEBAPP_ACCESS_TOKEN` | All skills | Bearer token for authenticating with the TadReamk ERP API (`api-erp.tadreamk.com`). Obtain from the ERP admin panel. |
| `ARTICLE_AUTHOR_NAME` | `/article-draft`, `/article-video-draft` | Author name displayed on published articles (e.g., `"Huu-Thanh Nguyen"`). |
| `TASK_USERNAME` | `/task-draft`, `/task-overview` | Your ERP username. Used to assign you as task manager and to filter your active tasks. |

### 2. Install Python dependencies

All Python packages required by scripts under `.claude.prod/scripts/` are listed in `.claude.prod/requirements.txt`. Install them with:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r .claude.prod/requirements.txt
playwright install chromium
```

> `playwright` is used only for slide export and is not listed in `requirements.txt` since it requires a separate browser install step.

### 3. Install Node dependencies (for React slides)

```bash
cd .claude.prod/slides && npm install
```
