# Cross-Round Scoreboard

**Goal:** Find 2+ DISTINCT concepts clearing SHORTLIST bar: mean of five expert averages > 8.0 AND no sub-score < 7 AND objectives >= 80, on honest red-teamed scores.

**Bound:** 3 generation rounds OR 12 concepts deep-dived, whichever first.

## Deep-dive results

| # | Concept | Round | CFO | CMO | COO | Legal | CTO | Mean (post-RT) | Low sub | Obj | Verdict |
|---|---------|-------|-----|-----|-----|-------|-----|----------------|---------|-----|---------|
| 1 | SecureControls Defense Tier-2 (NIST 800-171/SPRS) | 1 | 7.7 | 7.6 | 7.5 | 7.3 | 7.7 | **7.56** | 5 (Legal priv/liab) | 79.5 | FAIL / near-miss |
| 2 | ClearWater Water Ops (EPA LCRI) | 1 | 7.6 | 6.5 | 7.4 | 7.4 | 8.1 | **7.40** | 4 (CFO path-to-income) | 69 | FAIL |
| 3 | CosmeticMoCRA Ops (FDA MoCRA) | 1 | 7.5 | 7.0 | 7.2 | 7.5 | 7.8 | **7.40** | 6 (many) | 73.5 | NEAR-MISS |

## Concepts deep-dived: 3 / 12 bound
## Generation rounds completed: 1 (in progress) / 3 bound
## Clears so far: 0 / 2 needed

## Round 1 failure-mode notes (seed for Round 2 generation)
- **Liability tail kills it**: FCA / attestation-spillover exposure where the firm advises on a government representation drives Legal privacy+liability to 5s. AVOID concepts where the provider is a witness/contribution target in the customer's regulatory enforcement, or where the provider custodies highly sensitive regulated data (CUI/PHI/cardholder) that makes it an extinction-grade breach target. Favor concepts where the provider handles low-sensitivity business data and the liability cleanly rests on the customer.
- **Strong-tech encroachment caps competition**: even in a "sleepy incumbent" niche, if Vanta/Drata/horizontal-GRC can add the framework down-market, competitive dimension caps ~6. Favor niches with domain-specific data/workflow a horizontal SaaS can't templatize, or where the buyer will never operate a self-serve dashboard.
- **Labor-gated onboarding flattens the income curve**: judgment-heavy onboarding (110-control assessment) makes each marginal account need a hire, capping the $500K rung. Favor concepts with lighter/templatable onboarding and steeper renewal-year cost decline.
- **NEW (C2): Low-ACV × slow buyer = unreachable income ladder.** A ~$ thousands ACV sold to dispersed, board-vote government/municipal buyers needs heroic close velocity (~15/mo) to hit $300K/founder. AVOID tiny-ACV public-entity buyers unless ARPU is $8K+ AND there is a batch/channel multiplier. Favor PRIVATE businesses with budget authority and a single decision-maker, ACV >= ~$10–15K.
- **NEW (C2): Free government-adjacent substitute poisons willingness-to-pay.** State Rural Water Association circuit riders deliver the same compliance help free. AVOID niches where a free/subsidized program (extension office, association circuit rider, govt technical-assistance) already serves the need.
- **NEW (C2): A single funded vertical player (120Water) caps the competition score** even amid sleepy incumbents. Re-confirm no funded vertical SaaS owns mindshare in the niche.
- **NEW (C3): Free/self-serviceable underlying filing caps WTP + recurrence depth.** When the core obligation is a FREE government portal submission (MoCRA registration) that a CM can absorb, willingness-to-pay and year-2 retention are at risk. Favor mandates where the work is genuinely hard, ongoing, and NOT a one-time free portal submission.

## STRUCTURAL FINDING after 3 deep-dives (drives Round 2 seeding)
All three "managed-compliance-service" concepts landed in a tight 7.40–7.56 mean band — NONE cleared >8.0. The ceiling is structural, not idiosyncratic:
- **Differentiation & Defensibility reliably score ~6** — a productized managed service is copyable; the moat is relationships/positioning, not structure. To break >8.0 need a STRUCTURAL moat: proprietary data, network/pooled effects, switching cost that compounds, or becoming the operational system-of-record (not just compliance paperwork).
- **Liability reliably scores 5–6** when the provider advises on a government attestation/representation (FCA, FDA, export). Need concepts where liability cleanly rests on the customer / a third party, OR where the deliverable is operational not attestational.
- **Recurrence/margin dips to 6** when value is front-loaded (one-time onboarding) or labor-gated. Need intrinsic, high-frequency recurring cadence with declining renewal-year cost.
ROUND 2 SEED: keep the forced-buy/sleepy-incumbent spine BUT add at least one structural-moat mechanism (pooled membership / network, proprietary dataset, or operational system-of-record the customer runs their business on), clean liability (customer-owned or operational not attestational), higher ACV ($10K+), private decision-maker buyer, intrinsic high-frequency recurrence.

## Round-1 4th deep-dive: PICK SWAP
ExportShield ITAR/EAR (triage #4, consensus 8) is a NEAR-DUPLICATE of Concept 1's failure mode (defense supply chain + severe-penalty attestation liability tail). CLAUDE.md: drop near-duplicates of failed concepts. SUBSTITUTING DOTDrug Consortium Ops (triage #5, consensus 8) as Concept 4 — distinct sector, cleaner administrative liability (labs/MROs do testing), and a pooled-membership structure that tests whether a mild network/scale effect lifts defensibility above the 6 ceiling.
