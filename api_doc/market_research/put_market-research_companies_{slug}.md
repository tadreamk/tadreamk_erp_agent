# PUT /market-research/companies/{slug}

Update a market research company by slug. Requires `market-research` whitelist.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| slug | string | URL-friendly company identifier |

**Request Body:** (all fields optional)
| Field | Type | Description |
|-------|------|-------------|
| name | string | Company name |
| linkedin_url | string | LinkedIn URL |
| tagline | string | Company tagline |
| description | string | Company description |
| industry | string | Industry category |
| location_city | string | City |
| location_country | string | Country code |
| founded | int | Year founded |
| company_size | string | Employee range |
| linkedin_members | int | LinkedIn member count |
| followers | int | LinkedIn followers |
| website | string | Primary website |
| website_alt | string | Secondary website |
| phone | string | Phone number |
| email | string | Primary email |
| email_alt | string | Secondary email |
| contact_person | string | Contact person |
| hkstp_url | string | HKSTP profile URL |
| hkstp_category | string | HKSTP category |
| hkstp_address | string | HKSTP address |
| specialties | array | Specialties list |
| industries_served | array | Industries served |
| hashtags | array | LinkedIn hashtags |
| people | array | Key people |
| strengths | array | Identified strengths |
| weaknesses | array | Identified weaknesses |
| it_ai_service_opportunities | array | IT/AI opportunity objects |
| best_entry_points | array | Best entry point objects |
| potential_score | int | Raw potential score |
| potential_tier | int | Tier 1-5 |
| potential_score_reason | string | Score explanation |
| note | string | Internal staff note |
| scraped_at | date | Date data was scraped |

**Response:** `MarketResearchDetailResponse` — full updated company profile.

**Errors:**
- `400` — No fields to update
- `401` — Not authenticated
- `403` — No market-research whitelist access
- `404` — Company not found
