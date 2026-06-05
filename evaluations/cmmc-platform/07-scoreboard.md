# SCOREBOARD — Rampart (AI-first CMMC compliance platform for the DIB)

Date: 2026-06-05
Clean-room concept; council run blind (no bar, no target, no lineage disclosed to reviewers).

## The bar (quality floor / filter — never a target)
A concept clears only if ALL three hold:
1. Honest council mean of the five expert averages **>= 8.0**
2. **No** single expert sub-score **< 7**
3. Objectives weighted total **>= 80**

## Council results — pre- and post-red-team

| Expert | Avg (returned) | Avg (post-red-team) | Lowest sub-score | Recommendation |
|---|---|---|---|---|
| CFO   | 8.0 | 7.6 | 6 (financial-risk concentration) | GO |
| CMO   | 6.6 | 6.6 | 5 (competitive air; defensibility) | REFINE |
| COO   | 7.5 | 7.2 | 5 (quality control on AI output) | GO |
| Legal | 7.0 | 6.8 | 5 (data-privacy; liability) | GO (conditional) |
| CTO   | 6.7 | 6.7 | 5 (technical-assumption; infosec) | GO (conditional) |
| **MEAN of the five averages** | **7.16** | **6.98** | **5 (floor)** | — |

Objectives weighted total (doc-01): orchestrator **71 / 100**; PM independent re-read **68 / 100**.

Red-team cuts (all downward): COO logistics 10→8; CFO cash-flow-self-funding 9→8;
Legal regulatory-trajectory 8→7. Survived on evidence: CFO working-capital 9, CFO
startup-capital 9, Legal licensing 9, Legal employment 9.

## Verdict vs. the bar (post-red-team)
- Mean 6.98 **< 8.0** → fail clause 1 (by a full point)
- Lowest sub-score 5 **< 7** (five sub-scores at 5) → fail clause 2
- Objectives 68–71 **< 80** → fail clause 3

**RESULT: DOES NOT CLEAR THE BAR. Verdict: NEAR-MISS → REFINE.** A structurally
attractive, genuine must-have business held under the bar by a contested/partly-funded
competitive field, a thin day-one moat, an unaddressed trust/channel reality, and
unproven retention. Not a kill — a strong base for a structural pivot. The red-team
moved every adjusted score DOWN, not up. Full synthesis + documented red-team in
08-synthesis-redteam.md.

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
