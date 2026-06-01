# Deep-Dive Scoreboard (Stage 4 — full Opus council, red-teamed)

Quality floor (a FILTER applied to honest scores, never a target):
mean of five expert averages >= 8.0 AND no single sub-score < 7 AND objectives >= 80.

| # | Concept | CFO | CMO | COO | Legal | CTO | MEAN | Low sub | Obj/100 | Verdict |
|---|---------|-----|-----|-----|-------|-----|------|---------|---------|---------|
| 1 | A29 Compressed Air Optimization | 6.8 | 6.7 | 6.6 | 7.8 | 8.0 | 7.18 | 4 | 66 | NEAR-MISS |
| 2 | B5 ClaimSpeed (adjuster software) | 7.5 | 6.9 | 6.9 | 6.8 | 6.3 | 6.88 | 4 | 73 | NEAR-MISS |
| 3 | A14 Dehumidification white-label | 5.5 | 5.7 | 5.0 | 6.6 | 5.1 | 5.58 | 3 | 50 | FAIL |
| 4 | A4 Water Revenue-Recovery | 6.5 | 6.9 | 5.9 | 5.6 | 6.5 | 6.28 | 3 | 64 | FAIL |
| 5 | C10 Fractional CDO for SMBs | — | — | — | — | — | — | — | — | pending |

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
