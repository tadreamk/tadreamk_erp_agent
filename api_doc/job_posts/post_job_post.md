# POST /job-post


Create a new job post. Created with status `draft`.

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| title | string | Yes | Job title (1-200 chars) |
| department | string | Yes | Department (1-100 chars) |
| job_type | JobType | Yes | Employment type |
| location | string | No | Job location (max 200 chars) |
| job_slogan | string | No | Brief tagline |
| about_us | string | No | Company info |
| experience | decimal | No | Years of experience required |
| application_deadline | datetime | No | Application closing date |
| description_en | string | No | Job description (English) |
| responsibilities_en | string[] | No | List of responsibilities |
| requirements_en | string[] | No | List of requirements |
| benefits_en | string[] | No | List of benefits |
| preferred_qualifications_en | string[] | No | Preferred qualifications |

**Response:**
```json
{
  "message": "Job post created successfully",
  "job_post": { "..." : "..." }
}
```
