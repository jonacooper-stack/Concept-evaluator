---
name: business-objectives
description: Defines the founding objectives, constraints, and success criteria for the business being built, plus the evaluation rubric and scorecard used to assess every candidate idea against those criteria. Use this whenever a new business concept needs to be evaluated against the founders' goals, whenever a scorecard is needed to compare ideas, or whenever clarifying what this business is and is not supposed to be. Always consult this doc before running any expert evaluation — it is the source of truth for what "good" looks like.
---

# Business Objectives & Evaluation Rubric

This document defines what the founders are trying to build, the non-negotiable constraints, and how candidate ideas are scored. Every other expert agent (CFO, CMO, COO, Legal, CTO) and the synthesizing Product Manager agent reads from this doc as the source of truth.

## Use this doc to

1. Anchor every evaluation in the founders' actual goals — not generic "is this a good business" thinking.
2. Score candidate ideas against a consistent rubric so different concepts are directly comparable.
3. Disqualify ideas early that violate hard constraints, before deep expert review burns time.

## The business we're building

### Primary objective

A **bootstrapped lifestyle business** that generates strong, durable recurring income for the two cofounders, with optionality to grow into something larger — potentially a generational business that can be passed to children.

### Financial targets

- Within **24 months** of launch: generate **$1M+ in annual income to each cofounder** (i.e., ~$2M+ in distributable founder income annually, structure-dependent).
- **Recurring revenue is the spine** of the business. Subscription, contract, retainer, or other repeating-revenue models are strongly preferred over one-time transactional revenue.
- Path to scale beyond lifestyle income should exist but is not required at launch.

### Founder profile and capabilities

The business must be buildable using skills the founders already have or can reasonably acquire:

- General business and operations
- Marketing and go-to-market
- Software development
- Physical capability — willingness and ability to travel long distances, install equipment, do hands-on work in the field

The business **must not** require highly specialized credentials (e.g., medical licensure, PhD-level research, deep regulatory expertise the founders lack).

### Capital posture

- **Bootstrapped.** Very low upfront capital required. No outside equity raise assumed.
- Cash-flow positive as quickly as possible.
- No business that depends on a large pre-revenue capital outlay to be viable.

### Competitive posture

- **No dominant incumbent** that would crush a small entrant.
- Fragmented markets, sleepy incumbents, or underserved niches are ideal.
- Avoid markets where the obvious winning move is "raise $50M and outspend everyone."

### Probability of success

- Favor ideas with **high probability of meaningful success** over moonshots.
- A reliable $2M/year beats a 10% shot at $50M/year for this thesis.

## Hard constraints (any "no" here = automatic disqualification)

1. Cannot be launched with the founders' existing skills + reasonable learning curve.
2. Requires more than modest upfront capital (rough ceiling: well under what two founders can comfortably self-fund).
3. Has no plausible recurring revenue component.
4. Cannot plausibly reach ~$2M founder income within 24 months at reasonable scale assumptions.
5. Faces an incumbent or category leader that makes entry near-impossible.
6. Requires credentials, licenses, or specialized expertise the founders do not have and cannot reasonably acquire.

## Evaluation rubric

Every candidate idea is scored on the eight dimensions below, each on a **1–10 scale**. Scores roll up to a weighted total out of 100.

| # | Dimension | Weight | What a 10 looks like | What a 1 looks like |
|---|---|---|---|---|
| 1 | **Recurring revenue strength** | 15 | True subscription or contract revenue; >90% of revenue is repeating; high retention | Pure one-time transactions; no repeat dynamic |
| 2 | **Path to $2M founder income in 24mo** | 20 | Clear, conservative math gets there with reasonable unit economics and customer count | Requires heroic assumptions or doesn't get there at all |
| 3 | **Capital efficiency** | 10 | Launchable for low four/five figures; cash-flow positive fast | Needs significant capital before first revenue |
| 4 | **Skill fit with founders** | 10 | Uses exactly the founders' stack — business, marketing, software, hands-on field work | Needs credentials or expertise founders lack |
| 5 | **Competitive landscape** | 15 | Fragmented, sleepy, or underserved; no dominant player | Owned by a well-funded incumbent with strong moats |
| 6 | **Probability of success** | 10 | Proven demand, clear customer, low novelty risk | Speculative, requires market creation |
| 7 | **Scalability optionality** | 10 | Can stay lifestyle OR scale into something passable to children | Inherently capped, no growth lever |
| 8 | **Operational tractability** | 10 | Founders can run it as a two-person team for a long time | Requires large team or complex ops from day one |

**Scoring discipline:** A 5 is "honestly mediocre." A 7 is "good." A 9+ should be rare and earned. Resist the urge to score everything in the 6–8 band.

## Scorecard template

When evaluating an idea, the orchestrator (or any expert agent that needs a holistic view) produces this scorecard:

```
IDEA: <name>
ONE-LINE DESCRIPTION: <what it is>

HARD CONSTRAINT CHECK
- Buildable with founder skills? [Y/N + note]
- Low capital required? [Y/N + note]
- Recurring revenue component? [Y/N + note]
- Plausible $2M/founder in 24mo? [Y/N + note]
- No dominant incumbent? [Y/N + note]
- No specialized credentials required? [Y/N + note]
> If any answer is N: STOP. Disqualified. Move to next idea.

DIMENSION SCORES (1–10)
1. Recurring revenue strength:       [score]  — [one-line reason]
2. Path to $2M in 24mo:              [score]  — [one-line reason]
3. Capital efficiency:                [score]  — [one-line reason]
4. Skill fit:                         [score]  — [one-line reason]
5. Competitive landscape:             [score]  — [one-line reason]
6. Probability of success:            [score]  — [one-line reason]
7. Scalability optionality:           [score]  — [one-line reason]
8. Operational tractability:          [score]  — [one-line reason]

WEIGHTED TOTAL: [sum of (score × weight) / 10] / 100

TOP 3 STRENGTHS:
- ...

TOP 3 RISKS:
- ...

RECOMMENDATION: [Advance to expert review / Refine and resubmit / Drop]
```

## Thresholds

- **Weighted total ≥ 70** AND no dimension below 5 → advance to full expert council review.
- **Weighted total 55–69** → refine the concept and rescore; do not advance yet.
- **Weighted total < 55** OR any dimension at 3 or below → drop.

## How to use this with the expert agents

1. Run the candidate idea through the **scorecard above first**. If it clears the threshold, send it to the expert council.
2. Each expert (CFO, CMO, COO, Legal, CTO) evaluates independently using their own domain-specific rubric — they do not see each other's scores.
3. The **Product Manager agent** synthesizes all five expert outputs against this objectives doc and produces the final go / no-go / refine recommendation plus next-step artifacts.

## What this doc is NOT

- It is not a business plan.
- It is not a list of ideas.
- It is not a strategy document.

It is the **filter and yardstick**. Ideas, plans, and strategies live in other docs. This one only answers: "does this fit what we're trying to build, and how well?"
