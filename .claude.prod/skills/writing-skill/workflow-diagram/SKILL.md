---
name: workflow-diagram
description: >-
  Drafts and reviews ASCII workflow diagrams in markdown using box-drawing
  characters (stages, branches, notifications, loop-backs). Use when writing or
  editing SOPs, process specs, ERP flows, or when the user asks for workflow
  diagrams, process flows, stage diagrams, or "how to write a good workflow
  diagram".
---

# Workflow diagram (ASCII, markdown)

## When to apply

Use whenever the user wants a **multi-step business or system process** documented as a **single monospaced diagram** in markdown (not Mermaid unless they ask for it).

## Instructions

1. **Read** [reference.md](reference.md) for the full format, six principles, worked example (Customer Onboarding SOP), and final checklist.
2. **Apply** the rules when producing or editing diagrams:
   - Stage lines: `Stage N - [Actor] What happens` (never UI navigation paths).
   - **People Involved** before the diagram; example names per role; use *currently* when a role is provisional.
   - Branches at the decision: `├──[Action]──>` happy path first, `└──` last; terminal branches end with `(flow ends; …)`.
   - Loop-backs: name the **destination stage** explicitly; no duplicate stage numbers for the same logical step.
   - Emails/notifications: inline at the firing step (To/CC/body summary).
   - Prerequisites: section above the diagram or clearly marked preconditions, not mixed with normal steps.
3. Wrap the diagram in a **plain** fenced code block (triple backticks, **no** language tag) so alignment stays fixed-width.

## ERP source (optional)

Authoritative text originated as a TadReamk ERP **personal note** (`GET /personal-notes` / shared notes). A repo copy may exist at `docs/how-to-write-a-good-workflow-diagram.md` in `tadreamk_erp_agent`; the bundled [reference.md](reference.md) here is the same guidance for offline use.
