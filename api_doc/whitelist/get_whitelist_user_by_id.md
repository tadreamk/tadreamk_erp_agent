# GET /whitelist/user/{username}


Get a specific user's accessible endpoints.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| username | string | Target username |

**Response:**
```json
{
  "username": "john.doe",
  "endpoints": ["task", "job-posts"]
}
```
