# Agent Instructions

## API Documentation Context

Before responding to user queries related to the API, endpoints, data models, or integration:

1. **Scan the `api_doc/` folder** — Each module has its own subfolder with `index.md` (overview + endpoint table) and per-endpoint markdown files. Read the relevant `api_doc/<module>/index.md` first, then specific endpoint docs as needed. Example modules:
   - `health/`, `whitelist/`, `articles/`, `job_posts/`, `job_applications/`, `job_application_workflow/`
   - `employees/`, `employee_contracts/`, `personal_particular/`, `company_roles/`, `company_events/`
   - `tasks/`, `calendar/`, `notifications/`, `comments/`, `contact_directory/`
   - `leave_management/`, `payslip_workflow/`, `reimbursement_workflow/`, `expense_management/`
   - `onboarding/`, `templates/`, `technical_reports/`, `equipment_management/`, `exercises/`
   - `funding_opportunities/`, `funding_sources/`, `funding_utilization/`, `customer_management/`
   - `guide_quiz/`, `rachel_ai/`

2. **Use the documentation as the source of truth** — Base your answers on the specifications in `api_doc/`. Follow the documented request/response schemas, status workflows, and conventions.

3. **Cite specific docs when relevant** — If answering about a particular endpoint or module, reference the relevant `api_doc/<module>/` file and section to keep responses accurate and traceable.
