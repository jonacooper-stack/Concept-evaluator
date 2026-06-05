# SYNTHESIS — Member Engagement & Dues-Collection Overlay for Labor Unions
Date: 2026-06-05
Council members reviewed: CFO, CMO, COO, Legal/Regulatory, CTO

## ONE-PARAGRAPH PM READ

This is a genuinely well-shaped wedge sitting on top of a real, dated, regulation-forced pain: post-Janus, public-sector unions are legally compelled to re-sign members and collect dues off payroll, and most cannot. That is exactly the "painkiller, not vitamin" pull the objectives prize, and the income model (take-rate on a mandatory cash flow the customer is already moving) is structurally elegant. But four of five experts landed in REFINE (Legal is conditional, CTO is the lone conditional-GO), and they converge on the same three load-bearing doubts: (1) the differentiation is a feature bundle that Bonterra/ActionNetwork — non-sleepy comms incumbents who already own the union budget and already process payments — can copy in under a year; (2) the revenue model is a percentage take-rate on members' dues that union finance committees, accountable to members and ideologically allergic to "skimming," may negotiate to the floor or refuse outright; and (3) the founders show zero labor relationships and no evidence of a single union-director conversation, which is the entire gate in a slow, political, federated buyer. Underneath the "engagement overlay" framing, this is simultaneously a money-movement operation (TCPA + payments-ops + processor-freeze risk on politically charged money) and a relationship-gated enterprise sale into a finite, concentrated buyer set. The scores do not clear the bar before red-team, and they fall further after it.

## SCORE SUMMARY (pre-red-team)

- Objectives scorecard weighted total: **70 / 100** (lowest dimension: Probability of success = 5)
- CFO average:    6.9 / 10
- CMO average:    6.0 / 10
- COO average:    6.8 / 10
- Legal average:  5.9 / 10
- CTO average:    6.4 / 10
- **MEAN of the five averages: 6.40 / 10**
- **Lowest single sub-score anywhere: 4** (CFO #8 Financial risk concentration; CMO #10 Customer truth; Legal #5 Consumer protection complexity)

The bar requires MEAN > 8.0, no sub-score below 7, and objectives total ≥ 80. The concept fails all three before red-team even begins.

---

## MANDATORY RED-TEAM

Not a unanimous GO (CFO/CMO/COO REFINE, Legal conditional, CTO GO), but doc-07/CLAUDE.md require the red-team regardless. Highest sub-scores taken and each argued one point too high.

**1. CFO #2 Working-capital profile = 9 → LOWER to 8.** The 9 assumes a pristine in-transaction skim, but COO/Legal show a real money-movement op (ACH returns, chargebacks, reserves, processor holds). A processor underwriting union money at $100M+ will impose rolling reserves — working-capital drag the 9 ignores.

**2. COO #3 Logistics tractability = 9 → SURVIVES.** "Zero physical logistics, 50-state remote" measures field logistics squarely; on that axis it is genuinely clean. Lowering would manufacture a disagreement.

**3. Legal #4 Employment & contractor risk = 9 → SURVIVES.** Remote software team, no field workers, no 1099 misclassification — narrow and correct.

**4. CFO #1 Startup capital efficiency = 8 → LOWER to 7.** The true pre-revenue floor includes payments-ops + reconciliation ledger + per-state consent engine + tenant-isolation hardening before a large affiliate trusts it with $100M — more than "low five figures."

**5. CTO #1 Technical feasibility = 8 → LOWER to 7.** The 8 is explicitly contingent on deferring live legacy sync to CSV — an assumption the CTO itself flags as unverified ("MVP slips to a quarter+" if 5 unions reject CSV).

**Recomputed averages:** CFO 6.9 → **6.7**; COO **6.8**; Legal **5.9**; CTO 6.4 → **6.3**; CMO **6.0** (not lowered — already the lowest packet; its top score, Positioning 8, is well-evidenced).

**POST-RED-TEAM MEAN: (6.7 + 6.0 + 6.8 + 5.9 + 6.3) / 5 = 6.34 / 10.**
**Lowest single sub-score after red-team: still 4.**

---

## SCORE SUMMARY (post-red-team — verdict judged on these)

- Objectives weighted total: **70 / 100**
- CFO: **6.7** | CMO: **6.0** | COO: **6.8** | Legal: **5.9** | CTO: **6.3**
- **MEAN: 6.34 / 10** | **Lowest sub-score: 4**

## WHERE THE EXPERTS AGREE
- The pain is real, dated, budgeted (Janus 2018) — the heaviest-weighted market-pull, unanimous.
- This is secretly a money-movement + SMS-compliance operation, not a "lightweight overlay" (CFO/COO/Legal/CTO converge).
- The revenue event is decoupled from the sale — take-rate depends on digital-dues conversion the union controls; plan swings 3x on it.
- Differentiation is a feature bundle, copyable in <1yr by incumbents who own the customer.

## WHERE THE EXPERTS DISAGREE (PM call)
- CFO "path reachable" vs CMO "model collapses in finance committee." Call: **CMO load-bearing** — the CFO math is conditional on a take-rate the buyer's governance may reject; burden of proof unmet.
- CTO conditional-GO (feasibility 8) vs COO/Legal REFINE. Call: **COO/Legal load-bearing** — the hard part is operating a money-and-roster custodian on politically charged data atop processors that can cut you off, not the code.
- CFO/COO "scales with dues-dollars" vs CMO "few-thousand-body federated buyer." Call: **CMO load-bearing** — federalism resisting top-down mandate attacks the GTM thesis the revenue rests on.

## TOP 5 RISKS (RANKED)
1. Revenue model rejected by the buyer's own governance (percentage rake on dues) — CMO/CFO. Fix: flat per-member/per-transaction fee + 10 interviews.
2. TCPA litigation on high-volume SMS with missing consent provenance — Legal. Fix: consent/STOP as day-one infrastructure + contractual list-legality to union.
3. Founders have no labor relationships / no customer conversations — CMO (#10=4). Fix: 10 director interviews + named beachhead.
4. Processor/carrier freeze on politically sensitive money/messaging — CTO/COO/Legal. Fix: written acceptable-use + portability-by-design.
5. Throughput gap + revenue concentration — CFO. Fix: paid pilot proving ≥50% conversion in 9 mo + take-rate floor.

## TOP 3 STRENGTHS
- Regulation-forced, dated, existential demand (Janus; SEIU lost ~210K agency-fee payers).
- Structurally elegant, capital-light economics: take-rate on a mandatory cash flow, ~70–90% GM, near-zero working capital, no field ops.
- A real seam between sleepy records incumbents (UnionWare/Union Link) and comms CRMs, plus a compounding referenceable story in a tight community.

## THE BIGGEST OPEN QUESTION
Will unions actually let a third party take a percentage of members' dues — and can two founders with no labor relationships get into the room to find out? Both are cheap to test (10 interviews, a fee-structure probe) and both must be answered before any build.

## RECOMMENDATION: REFINE (decisively NOT GO)
Clears the objectives advance threshold (70 ≥ 70) but is nowhere near the win bar. Four of five experts at REFINE/conditional. Required changes are structural, so per CLAUDE.md anti-ratcheting a refined version must re-enter as a NEW clean-room candidate.

Changes that would move it toward GO:
1. Drop the percentage take-rate as primary line; default to flat per-member/per-transaction fee (CMO/CFO).
2. 10 union-director interviews + a named beachhead affiliate with a documented path-in (CMO #10).
3. One paid pilot showing ≥50% digital-dues conversion in 9 months (CFO/COO).
4. Written processor + carrier acceptable-use confirmation + portability-by-design (CTO/Legal/COO).
5. TCPA consent/opt-out + payments-ops as first-class day-one infrastructure; lock facilitator-not-transmitter (union merchant-of-record) architecture to avoid the ~49-state MTL trap (Legal/COO).

Target re-review: after 10 interviews + fee-structure validation + one written processor acceptable-use term — ~6–8 weeks of discovery, before any code.

---

## VERDICT AGAINST THE BAR: **FAIL**
- MEAN = 6.34 (needs > 8.0) — FAIL by a wide margin.
- Lowest sub-score = 4 (needs ≥ 7) — FAIL, in three places.
- Objectives total = 70 (needs ≥ 80) — FAIL.

Not a near-miss. Fails all three; the red-team moved the mean down (6.40 → 6.34), not up. No score adjusted to reach a verdict. A legitimately interesting painkiller worth one structural REFINE pass, but on the merits today it does not qualify.

## NEXT STEPS
- Founders — 10 structured union-director/finance-officer interviews (test %-vs-flat fee tolerance + federated mandate authority), ~4 weeks.
- Founders — name one 20–60K-member state affiliate + secure warm intro, ~4 weeks.
- Founders — written processor + carrier acceptable-use; confirm CSV-import acceptability with 5 unions, ~6 weeks.
- PM — if revenue restructured to flat fee + beachhead named, resubmit as a NEW clean-room one-pager (no lineage) for a fresh council round. Do not in-place ratchet.
