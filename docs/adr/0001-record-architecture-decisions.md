# 1. Record architecture decisions

Status: accepted

## Context

The worker's structural choices (no dependency on cairn-core, the committed proto stubs, NATS-only
transport, presigned object storage) are described in docs/ARCHITECTURE.md, which drifts as prose.

## Decision

Significant architecture decisions are recorded here as numbered ADRs (context, decision,
consequences). An ADR is never rewritten after acceptance; a later ADR supersedes it.

## Consequences

Structural changes come with an ADR in the same pull request. Decisions that predate this log stay
in docs/ARCHITECTURE.md until one of them is revisited.
