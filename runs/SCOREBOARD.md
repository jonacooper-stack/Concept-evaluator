# Deep-Dive Scoreboard (Stage 4 — full Opus council, red-teamed)

Quality floor (a FILTER applied to honest scores, never a target):
mean of five expert averages >= 8.0 AND no single sub-score < 7 AND objectives >= 80.

| # | Concept | CFO | CMO | COO | Legal | CTO | MEAN | Low sub | Obj/100 | Verdict |
|---|---------|-----|-----|-----|-------|-----|------|---------|---------|---------|
| 1 | A29 Compressed Air Optimization | 6.8 | 6.7 | 6.6 | 7.8 | 8.0 | 7.18 | 4 | 66 | NEAR-MISS |
| 2 | B5 ClaimSpeed (adjuster software) | 7.5 | 6.9 | 6.9 | 6.8 | 6.3 | 6.88 | 4 | 73 | NEAR-MISS |
| 3 | A14 Dehumidification white-label | 5.5 | 5.7 | 5.0 | 6.6 | 5.1 | 5.58 | 3 | 50 | FAIL |
| 4 | A4 Water Revenue-Recovery | 6.5 | 6.9 | 5.9 | 5.6 | 6.5 | 6.28 | 3 | 64 | FAIL |
| 5 | C10 Fractional Data Leader (SMB) | 6.4 | 5.7 | 5.9 | 6.8 | 6.1 | 6.20 | 3 | 55 | FAIL |

Scores shown are POST-red-team. "Low sub" = lowest single sub-score anywhere in the packet.

## Notes per concept
- **#1 A29 Compressed Air — NEAR-MISS.** Held back by Path-to-$2M-in-24mo (4): delivery is
  headcount-linear (every recurring dollar = one truck-roll survey), $2M needs ~200–400
  contracts + 4–5 techs, slips past 24 months at midpoint pricing. Plus sub-7 cluster
  (logistics, throughput, scaling, defensibility) from the field-service shape. Genuinely good
  $500k–$1M lifestyle business; wrong shape for a $2M/24mo mandate. Red-team widened the gap
  (mean 7.24→7.18). Structural refine: enterprise multi-site / IoT-SaaS layer / methodology licensing.
- **#2 B5 ClaimSpeed — NEAR-MISS.** Post-red-team mean 6.88, lowest sub-score 4 (CAT-season
  seasonality), objectives 73. Cleanest bootstrap economics of the field (~80% margin, budget-
  owning buyer, founder-market fit) but Path-to-$2M needs ~5–7% market penetration via a no-
  sales-team motion (base case ~$1M ARR = half target), the "carrier-ready/no-bounce-back"
  promise is unproven + a perpetual treadmill, defensibility thin vs Encircle/CompanyCam, and
  severe storm-season seasonality. Red-team widened the gap (6.92→6.88).
- **#3 A14 White-label mold monitoring — FAIL.** Post-red-team mean 5.58, lowest sub-score 3
  (COO quality-control, CTO maintenance), objectives 50. Deep council unmasked the triage's
  "white-label SaaS" framing: it's a hardware-fleet business (silent sensor failure in basement
  RF, reverse logistics, ~$1M inventory) + an uncontrolled two-stage B2B2C sale, against the
  founders' weakest skill (engineering 3-4/10) and low-effort preference. Red-team moved mean
  DOWN (5.62→5.58). Good salvageable insight (sell recurring revenue to contractors who own the
  customer) but needs a structural pivot — bundle into the job, partner the hardware.
- **#4 A4 Water Revenue-Recovery — FAIL.** Post-red-team mean 6.28, lowest sub-score 3 (Path-
  to-$2M), objectives 64. Genuinely sharp self-funding positioning into clean competitive air,
  but all five experts converge on the slow municipal procurement cycle (6-12mo board/RFP per
  deal) making ~45-180 contracts in 24 months unreachable; plus a contingent-fee/procurement
  legal cluster (uninsurable void-contract risk) and per-utility bespoke ETL that makes it a
  consulting practice in a SaaS costume. A strong $1-1.5M lifestyle business mis-cast as a
  $2M-each one. Re-clock to 36-48mo or restructure the customer/revenue model.
- **#5 C10 Fractional Data Leader — FAIL.** Post-red-team mean 6.20, lowest sub-score 3 (Path-
  to-$2M / throughput, tied), objectives 54.5 (below even the doc-01 advance floor of 55).
  Cleanest capital/recurring/legal profile of the whole field, but three experts (CFO, COO, CTO)
  independently derive the same founder-time ceiling: the product IS two founders' non-delegable
  senior judgment, capping them at ~20-40 retainers (~$0.6-0.7M each); reaching $2M each needs
  ~45-68, which requires diluting the advisory promise that justifies the price. Plus weak
  differentiation/defensibility and concentrated payroll-PII security liability. A genuine
  lifestyle practice; wrong shape for $2M/24mo. Red-team made it marginally worse (6.2→6.18).

---

## FINAL RESULT — 0 SHORTLIST qualifiers (an honest SUCCESS, per CLAUDE.md)

None of the 5 deep-dive candidates cleared the quality floor (mean >= 8.0 AND no sub-score < 7
AND objectives >= 80). The run explored 120 ideas, triaged honestly, and ran full rigorous
red-teamed council packets on the 5 finalists. Per CLAUDE.md: "A run that explores the field,
produces full rigorous packets, and finds ZERO qualifiers is a SUCCESS." We did not manufacture
a qualifier. Two NEAR-MISSES (closest), three FAILs.

### Ranked result
| Rank | Concept | Mean | Low sub | Obj | Verdict | The dimension that killed it |
|------|---------|------|---------|-----|---------|------------------------------|
| 1 | A29 Compressed Air Optimization | 7.18 | 4 | 66 | NEAR-MISS | Path-to-$2M (4): headcount-linear field service — every recurring $ = one truck-roll survey |
| 2 | B5 ClaimSpeed (adjuster software) | 6.88 | 4 | 73 | NEAR-MISS | Path-to-$2M + CAT seasonality (4): no-sales-team motion needs 5-7% market penetration |
| 3 | A4 Water Revenue-Recovery | 6.28 | 3 | 64 | FAIL | Path-to-$2M (3): slow municipal procurement makes 45-180 contracts in 24mo unreachable |
| 4 | C10 Fractional Data Leader | 6.20 | 3 | 55 | FAIL | Path-to-$2M / throughput (3): founder-time ceiling caps at ~$0.6-0.7M each |
| 5 | A14 White-label Mold Monitoring | 5.58 | 3 | 50 | FAIL | Hardware-fleet reality + uncontrolled two-stage sale vs founders' engineering gap |

### THE COMMON THREAD (the single most useful finding)
Every one of the five died primarily on the SAME dimension: **Path to $2M founder income in 24
months** (the 20-weight objective). Four of five scored it 3-4. The pattern is consistent and
diagnostic: each is a genuinely good, capital-light, recurring-revenue business that lands as a
$0.5M-$1.5M-each LIFESTYLE outcome, but the specific bar — ~$2M EACH within 24 MONTHS — is what
none could clear. The binding constraints recurred: (a) labor/founder-time-linear delivery that
can't outrun two people's hands; (b) slow B2B/B2G/board sales cycles; (c) thin defensibility in
copyable services. The $2M-in-24-months target, against a bootstrapped two-founder team, is the
real filter — not idea quality.

### How the 5 finalists differ (customer / market / revenue mechanism)
- A29: manufacturing plant managers / compressed-air energy waste / quarterly audit contract + savings-share.
- B5: independent insurance adjusters / claims-documentation SaaS / per-adjuster monthly seat.
- A4: municipal water districts / non-revenue-water / annual recovery contract (public procurement).
- C10: mid-market SMB execs / data/analytics leadership gap / monthly advisory retainer.
- A14: restoration contractors (channel) → homeowners / mold recurrence / per-home white-label monitoring subscription.
They are genuinely distinct across customer type (industrial / insurance / government / SMB-exec /
contractor-channel) and revenue mechanism (savings-share / SaaS seat / gov contract / advisory
retainer / white-label IoT subscription) — the diversity mandate held.

### Handoff notes (single biggest open question per NEAR-MISS, for a manual deep-dive)
- **A29 (closest):** Can you land FEWER, LARGER multi-compressor / multi-site enterprise accounts
  (~120 at ~$25k, or an IoT-monitoring SaaS layer) to break the one-survey-per-truck-roll linearity?
  If yes, the $2M math becomes defensible rather than heroic.
- **B5:** What is the real ACTIVE independent-adjuster denominator (30k or 80k?) and realized blended
  ARPU after a 50-customer pricing test — and does a firm-plan (multi-seat) emphasis compress the
  ~2,000-seat requirement enough to hit the window?

