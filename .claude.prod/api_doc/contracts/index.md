# Contracts API

Base prefixes:
- `/contract`
- `/contract/me`
- `/contracts`
- `/contracts/{contract_id}`

Authentication: See per-endpoint docs. Most endpoints require JWT (`Authorization: Bearer <token>`). Some require an endpoint whitelist.

| Method | Path | Auth | Description | File |
|--------|------|------|-------------|------|
| GET | /contract/me | Authenticated employee | List My Contracts | [get_contract_me.md](get_contract_me.md) |
| GET | /contract/me/{contract_id} | Authenticated employee | Get My Contract | [get_contract_me_{contract_id}.md](get_contract_me_{contract_id}.md) |
| GET | /contracts/ | `)
    rows, total = contract_queries.list_contracts_paginated(
        db,
        search=search,
        include_inactive_employees=include_inactive_employees,
        include_inactive_contracts=include_inactive_contracts,
        page=page,
        limit=limit,
    )
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=` whitelist | List Contracts | [get_contracts_.md](get_contracts_.md) |
| POST | /contracts/ | `)
    fields = payload.model_dump(exclude={` whitelist | Create Contract | [post_contracts_.md](post_contracts_.md) |
| GET | /contracts/{contract_id} | `)
    entry = get_contract_or_404_by_id(db, contract_id)
    log_sensitive_read(
        db,
        caller_username=user.username,
        endpoint=f` whitelist | Get Contract | [get_contracts_{contract_id}.md](get_contracts_{contract_id}.md) |
| PUT | /contracts/{contract_id} | `)
    contract = get_contract_or_404_by_id(db, contract_id)
    contract = contract_write_ops.update_contract(
        db,
        contract=contract,
        updated_by=user.username,
        fields=payload.model_dump(exclude_unset=True),
    )
    return APIResponse(
        success=True,
        message=` whitelist | Update Contract | [put_contracts_{contract_id}.md](put_contracts_{contract_id}.md) |
| POST | /contracts/{contract_id}/deactivate | `)
    contract = get_contract_or_404_by_id(db, contract_id)
    contract = contract_write_ops.deactivate_contract(db, contract=contract, caller=user.username)
    return APIResponse(
        success=True,
        message=` whitelist | Deactivate Contract | [post_contracts_{contract_id}_deactivate.md](post_contracts_{contract_id}_deactivate.md) |
| POST | /contracts/{contract_id}/reactivate | `)
    contract = get_contract_or_404_by_id(db, contract_id)
    try:
        contract = contract_write_ops.reactivate_contract(
            db, contract=contract, caller=user.username
        )
    except ContractReactivateError as exc:
        raise HTTPException(status_code=exc.status_code, detail=exc.message) from exc
    return APIResponse(
        success=True,
        message=` whitelist | Reactivate Contract | [post_contracts_{contract_id}_reactivate.md](post_contracts_{contract_id}_reactivate.md) |
