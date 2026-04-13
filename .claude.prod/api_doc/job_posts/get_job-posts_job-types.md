# GET /job-posts/job-types

Get list of available job type options. No authentication required.

**Response:**
```json
{
  "job_types": [
    { "value": "full_time", "label": "Full Time" },
    { "value": "part_time", "label": "Part Time" },
    { "value": "contract", "label": "Contract" },
    { "value": "internship", "label": "Internship" }
  ]
}
```
