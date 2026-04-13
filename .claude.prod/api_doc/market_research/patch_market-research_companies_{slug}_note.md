# PATCH /market-research/companies/{slug}/note

Update the internal note for a market research company. Requires `market-research` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | URL-friendly company identifier |

**Request Body:**
| Field | Type | Description |
|-------|------|-------------|
| note | string or null | Internal note content |

**Response:** `MarketResearchDetailResponse` — full company profile with updated note.

**Errors:**
- `401` — Not authenticated
- `403` — No market-research whitelist access
- `404` — Company not found
