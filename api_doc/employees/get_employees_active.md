# GET /employees/active


Get active employees for picker/dropdown selection. Returns minimal fields plus name from personal particulars.

**Query Parameters:**
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| search | string | No | Search filter |
| limit | int | No | Max results (default: 50) |

**Response:**
```json
{
  "employees": [
    {
      "id": "uuid",
      "username": "john.doe",
      "work_email": "john.doe@company.com",
      "family_name": "Doe",
      "given_name": "John"
    }
  ]
}
```
