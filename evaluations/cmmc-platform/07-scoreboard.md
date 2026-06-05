# SCOREBOARD — Rampart (AI-first CMMC compliance platform for the DIB)

Date: 2026-06-05
Clean-room concept; council run blind (no bar, no target, no lineage disclosed to reviewers).

## The bar (quality floor / filter — never a target)
A concept clears only if ALL three hold:
1. Honest council mean of the five expert averages **>= 8.0**
2. **No** single expert sub-score **< 7**
3. Objectives weighted total **>= 80**

## Council results (pre-red-team, as returned)

| Expert | Average | Lowest sub-score | Recommendation |
|---|---|---|---|
| CFO   | 8.0 | 6 (financial-risk concentration) | GO |
| CMO   | 6.6 | 5 (competitive air; defensibility) | REFINE |
| COO   | 7.5 | 5 (quality control on AI output) | GO |
| Legal | 7.0 | 5 (data-privacy; liability) | GO (conditional) |
| CTO   | 6.7 | 5 (technical-assumption; infosec) | GO (conditional) |
| **MEAN of the five averages** | **7.16** | **5 (floor)** | — |

Objectives weighted total (doc-01): **71 / 100**

## Verdict vs. the bar
- Mean 7.16 **< 8.0** → fail clause 1
- Lowest sub-score 5 **< 7** (five experts each have a 5) → fail clause 2
- Objectives 71 **< 80** → fail clause 3

**RESULT: DOES NOT CLEAR THE BAR.** Honest verdict: a structurally attractive,
genuine must-have business held under the bar by a contested/partly-funded
competitive field, a thin day-one moat, and unproven retention. Not a kill —
a strong base for a structural pivot. (Final verdict after PM red-team in 08.)

## Where it is strong (consensus)
- Market pull / must-have: elite. Regulation-forced, deadline-driven, budgeted,
  recurring, contractual-gate buy across ~76–80K orgs.
- Capital efficiency + operations + skill fit: sub-$25K start, ~8–12 dev-weeks,
  remote SaaS with no field ops, founders' SOC 2/HIPAA background directly on point.
- Cash shape: annual-upfront billing, 80%+ gross margin, sub-6-month payback.

## Where it is weak (consensus)
- Competitive landscape / air / defensibility: Vanta & Drata already ship CMMC/
  NIST 800-171; CMMC-native specialists (Totem, FutureFeed, ControlMap, Ignyte)
  already sell this buyer; MSP/C3PAO layer owns the trust. The AI wedge is
  copyable in ~2–3 quarters; the system-of-record moat only accrues after traction.
- Retention: "compliance-as-an-event" badge-and-bail could halve LTV.
- Trust gap: the buyer's real fear ("will this pass my C3PAO assessment?") is
  answered by assessors, not software — and the founders lack CMMC-native
  references day one.
- Quality/security stakes: AI artifacts feed a real assessment; the platform is a
  high-value CUI-adjacent target; CUI-storage boundary must be engineered up front.
