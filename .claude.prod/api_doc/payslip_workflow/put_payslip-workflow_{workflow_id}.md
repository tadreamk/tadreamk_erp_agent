# PUT /payslip-workflow/{workflow_id}

Update payslip field values. Only allowed when status is not `completed`. For hourly contracts, salary is auto-computed when `hours_worked` changes. Requires `payslip` whitelist access.

**Path Parameters:**
| Parameter | Type | Description |
|-----------|------|-------------|
| workflow_id | UUID | The payslip workflow's unique identifier |

**Request Body:**
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| field_values | object | Yes | Map of template field keys to values |

### User overrides

Four keys inside `field_values` act as manual overrides that survive `apply_hourly_computation`'s auto-recompute. Each follows the same rule: **if the submitted value is truthy AND strictly different from the value currently stored for that key, the user value wins**.

| Key | When to send | Effect |
|-----|--------------|--------|
| `mpf_relevant_income` | Finance wants to pin the stated relevant income | Overrides the recomputed sum of salary + allowance + bonus |
| `mpf_employee` | STEM scheme, deferred first-30-days, intern, voluntary exemption | Overrides `calculate_mpf()`'s employee contribution |
| `mpf_employer` | STEM scheme, deferred first-30-days, intern, voluntary exemption | Overrides `calculate_mpf()`'s employer contribution |
| `net_pay` | Finance manually states the disbursed amount | Overrides the auto `gross - mpf_employee` calculation |

MPF overrides are applied **before** `net_pay` is auto-recomputed, so a manual `mpf_employee` value correctly drives the auto net-pay without needing to also send `net_pay`.

Quirk: sending the same string as the stored value is a no-op (the override condition is `user_X != prev`). To pin an existing value against a forced recompute, send a stringly-different but numerically-equal value (e.g. `"0.0"` vs `"0"`).

**Response:** Updated payslip workflow object

**Errors:**
- `400` — Cannot edit a completed payslip
- `401` — Not authenticated
- `403` — Not on payslip whitelist
- `404` — Payslip workflow not found
