package gaam_opa_experiment

# Only an illustrative policy predicate, not a GAAM trust decision.
default candidate_eligible := false

candidate_eligible if {
    input.contractVersion == "1"
    input.policy.revision == "demo-policy-1"
    input.policy.state == "current"
    input.policy.prohibited == false
    input.request.actor == input.delegation.delegate
    input.request.effect in input.authority.permittedEffects
    not input.request.effect in input.authority.prohibitedEffects
    input.request.effect in input.delegation.delegatedScope.effects
    input.authority.id == input.delegation.parentAuthority
    input.authority.subject == input.delegation.delegate
    input.authority.delegationPermitted == true
    input.authority.status == "active"
    input.delegation.status == "active"
    input.delegation.redelegation == "prohibited"
    input.authority.effectiveFrom <= input.evaluationTime
    input.evaluationTime < input.authority.effectiveUntil
    input.delegation.effectiveFrom <= input.evaluationTime
    input.evaluationTime < input.delegation.effectiveUntil
    input.evidence.state == "current"
    input.evidence.observedAt <= input.evaluationTime
    input.evaluationTime < input.evidence.freshUntil
    input.revocation.state == "active"
}
