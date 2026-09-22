---
title: "Collective Authority Exercise"
nav_exclude: true
normative_status: Informative
---

# Collective Authority Exercise

**Status:** informative future-evolution pressure test; not part of the v0.9.2 normative baseline.

## Problem

Some authority belongs to a principal whose exercise requires several controllers
to act under a composition rule. A 2-of-3 threshold is the minimal example. The
three controllers are not three independent holders of the authority: the
governed principal is the authority holder and the controllers participate in
one bounded authority exercise.

This distinction matters when a protocol or implementation can authenticate
every controller but has not established the current composition rule that makes
their acts authoritative as a collective.

## Required distinctions

A future GAAM projection for collective authority must keep the following
propositions separate:

1. **Authority principal** — the accountable holder/source of the authority.
2. **Controller/member identity** — who may participate in exercising it.
3. **Membership state** — which controllers currently qualify.
4. **Exercise rule** — the threshold, quorum, approval, or other composition rule.
5. **Authority exercise** — the exact action the collective is attempting.
6. **Composition evidence** — evidence that the current rule was satisfied by
   distinct qualifying participants for that exact action.

A controller's valid identity, credential, or signature MUST NOT be treated as
independent possession of the collective authority.

## Pressure-test outcomes

| Case | Expected |
|---|---|
| Current 2-of-3 rule, current membership, two distinct exact-action approvals | PERMIT |
| Only one qualifying member under a current 2-of-3 rule | DENY |
| Two valid member approvals but composition-rule evidence is missing | INDETERMINATE |
| Approvals rely on stale membership | DENY |
| Approvals rely on a stale exercise rule | DENY |
| Same member appears twice under a 2-of-3 rule | DENY |

The machine-readable companion fixture is
`experimental/examples/collective-authority-pressure-cases.json`.

## Initial disposition

The existing Authority-at-Commitment concepts already provide the important
principal/actor, current-state, approval-binding, fail-safe, and evidence
semantics. The pressure test therefore does **not** justify a new canonical
authority type at this stage.

The residual gap is narrower: GAAM does not yet expose a first-class normative
model for membership plus an authority-exercise composition rule. This remains
an informative future-evolution concern pending independent implementation and
interoperability evidence.

## Boundary

This concept does not prescribe threshold cryptography, multisignature formats,
DID/controller representation, Trust Tasks party encoding, or protocol wire
messages. Those are downstream realization choices.
