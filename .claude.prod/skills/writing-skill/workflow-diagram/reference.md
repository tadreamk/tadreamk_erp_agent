# How to Write a Good Workflow Diagram

## Overview

A workflow diagram is a shared contract between the people who design a system and the people who build it. It answers three questions for every step: **who** acts, **what** they do, and **what the system does in response**. When these three things are clear, developers can implement without guessing, and stakeholders can review without asking.

This report uses the Customer Onboarding SOP as a worked example throughout — a six-stage flow involving a Customer, a Business Developer, a Marketer, and an R&D Team.

---

## The Diagram Format

Use a plain triple-backtick code block with no language tag. This renders monospaced in every markdown viewer and keeps the tree characters aligned.

```
Stage N - [Actor] Stage Title
  │
  │   (actions, inputs, system behaviour at this stage)
  │
  ▼
Stage N+1 - [Actor] Stage Title
```

| Symbol | Meaning |
|---|---|
| `│` | Vertical flow of time within a stage |
| `▼` | Transition to the next stage |
| `├──` | Branch — not the last option |
| `└──` | Branch — last option |
| `→` | Loop-back pointer to a named previous stage |

---

## Principle 1: Stage Titles, Not Navigation Paths

Each stage header has three parts: a sequential number, the actor in square brackets, and a short title naming what happens — not the menu path to get there.

**Wrong:**
```
[Marketer] ERP → Customer Onboarding → "New Registration Form"
```

**Right:**
```
Stage 1 - [Marketer] Initiate Registration Form
```

The title answers: *what is the actor doing at this stage?* Keeping navigation paths out of stage titles also means the diagram stays valid when the UI is reorganised.

---

## Principle 2: Name Every Actor

List all actors in a **People Involved** section before the diagram. Give each a concrete example name so the reader knows who `[Marketer]` is before they reach the first branch.

The phrase "currently" on a role signals that the role is expected to expand. This prevents a future reader from treating the example name as a permanent constraint.

---

## Principle 3: Branches Inline at the Decision Point

When a stage has multiple outcomes, show them as branches at that exact point using `├──[Label]──>` syntax. Label every branch with an action word in square brackets.

Two rules:
- **Happy path first** — the expected successful outcome uses `├──`; exceptional or terminal outcomes use `└──`.
- **Terminal branches say so explicitly** — if a branch ends the flow, write `(flow ends; ...)`. Never leave the reader wondering if the flow continues somewhere.

---

## Principle 4: Loop-backs Named Explicitly

When a rejection or error sends the actor back to a previous stage, write the return path inline on the branch and name the destination stage precisely.

A loop-back reuses an existing stage — it is not a new stage. Naming the destination removes ambiguity about where the flow resumes and makes cycles in the diagram traceable.

---

## Principle 5: Every Notification Inline

Every email or system notification appears at the exact step in the flow where it fires — never grouped at the end. Include the recipient, CC list, and a brief body description.

A consistent CC pattern across all emails signals a design rule, not an accident. A reader who sees it repeated will understand it as intentional.

---

## Principle 6: Prerequisites Outside the Diagram

Prerequisites are conditions that must already be true before the flow starts. They belong in a dedicated section above the diagram, not as the first step inside it.

If a prerequisite also needs to appear inside the diagram, mark it clearly as a pre-condition rather than an action. This makes it clear these items must already be true — the flow does not produce them.

---

## Complete Example — Customer Onboarding SOP

## People Involved

- **Customer** (e.g., Simon) — the external client who registers a project and makes the deposit payment
- **Business Developer** (e.g., currently Richard) — works with the customer on user requirements and storytelling before onboarding begins (prerequisite, not part of the system flow)
- **Marketer** (e.g., currently Richard) — internal staff who receives the registration, sets the deposit amount, and approves or declines the project
- **R&D Team** (e.g., Alan) — receives the automatically created task and builds the prototype on the dev server

The following is the full diagram from `docs/discussion/260506_customer_onboarding_sop.md`, applying all six principles:

```
Stage 1 - [Marketer] Initiate Registration Form
  │
  │   Prerequisites:
  │     ├── Business Developer and Customer have completed user requirements
  │     │   and storytelling sessions
  │     ├── Customer has sent a letter to the Business Developer confirming
  │     │   they are ready to subscribe
  │     └── Business Developer sends a request to the Marketer to initiate
  │         a registration form for the Customer
  │
  │   Marketer initiates a registration form and sends the link to the Customer
  │
  │   System sends an email to the Customer:
  │     └── CC: Marketer, Business Developer
  │         Body: registration form link
  │
  ▼
Stage 2 - [Customer] Submit Registration
  │     ├── Customer name
  │     ├── Project name
  │     ├── Email
  │     └── Optional information (e.g., notes, references)
  │
  │   Customer submits → sees on-screen notice:
  │     "Your project is under review. We will reply within xxx business days."
  │
  │   System sends a confirmation email to the Customer:
  │     └── CC: Marketer, Business Developer
  │         Body: project name, submission date, expected response time
  │
  ▼
Stage 3 - [Marketer] Review & Send Deposit Invoice
  │
  │   sees: customer name | project name | submission date
  │
  │   Marketer selects an invoice template and fills in:
  │     ├── Deposit amount
  │     ├── Project details
  │     └── Any additional notes
  │
  ├──[Submit]──> system sends email to Customer:
  │                 ├── Deposit invoice (from selected template)
  │                 ├── Greeting message
  │                 └── CC: Marketer, Business Developer
  │
  └──[Cancel]───> Marketer provides a cancellation reason
                    system sends email to Customer with the reason
                    CC: Marketer, Business Developer
                    (flow ends; re-engagement handled offline)
  │
  ▼
Stage 4 - [Customer] Payment & Proof of Transfer
  │
  │   Customer goes to their Customer Portal page
  │
  ├──[Accept]──> Customer makes payment
  │               Uploads transfer screenshot as proof of payment
  │               System sends confirmation email to Customer:
  │                 ├── Body: payment received, transferred to Marketer for next step
  │                 └── CC: Marketer, Business Developer, R&D Team
  │
  └──[Reject]──> Customer provides a rejection reason
                   system sends email to Marketer:
                   ├── Reason for rejection
                   └── CC: Customer, Business Developer
                   Marketer reviews the reason, refines the deposit amount,
                   and re-sends the updated invoice to the Customer
                   → returns to Stage 3 - [Marketer: Submit] stage
  │
  ▼
Stage 5 - [Marketer] Payment Verification
  │
  │   Marketer reviews the transfer screenshot in ERP
  │
  ├──[Accept]──> triggers R&D to start building
  │
  └──[Reject]──> system sends email to Customer:
                   ├── Body: payment not confirmed, please verify or resend
                   └── CC: Marketer, Business Developer
                   → returns to Stage 4 - [Customer: Payment & Proof of Transfer]
  │
  ▼
Stage 6 - [R&D] Build Prototype on Dev Server
  │
  │   User requirements and storytelling documents are linked automatically
  │
  │   When prototype is ready on dev:
  │
  │   System sends email to Customer:
  │     ├── Body: dev server URL and usage instructions
  │     └── CC: Marketer, Business Developer, R&D Team
  │
  ▼
Done — Customer can review the dev prototype; next steps handled offline.
```

---

## Checklist Before Finalising

- [ ] Every stage has a number, an actor, and a title (not a nav path)
- [ ] Every actor is listed in People Involved with an example name
- [ ] Every branch is labelled and the happy path comes first
- [ ] Every terminal branch says `(flow ends; ...)`
- [ ] Every loop-back names the destination stage
- [ ] Every notification shows recipient, CC list, and body summary
- [ ] Prerequisites are in a separate section, not inside the diagram steps
