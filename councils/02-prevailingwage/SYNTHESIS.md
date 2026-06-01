# SYNTHESIS — ContractorPrevailingWage (Managed Certified-Payroll & Prevailing-Wage Compliance)
Date: 2026-06-01 · Verdict: **NEAR-MISS → REFINE** (strongest near-miss in the field)

## SCORE SUMMARY (post red-team)
- CFO 7.5 → **7.4** | CMO 7.5 → **7.4** | COO **6.8** | Legal **7.3** | CTO **6.7**
- **MEAN of five = 7.12** (vs bar 8.0) — misses by 0.88
- **Lowest sub-score anywhere = 5** (Legal liability, COO tooling-must-be-built, CTO third-party dependency, CTO maintenance treadmill) — vs floor 7
- **Objectives scorecard = ~78 / 100** (vs 80 PASS; above 70 advance floor)

## VERDICT vs THE BAR
NEAR-MISS — misses all three legs (mean, sub-score floor, objectives) but each gap is small and concentrated in buildable operational/technical drag, not demand. Closest the field has come to the CMMC archetype on the demand side.

## WHERE EXPERTS AGREE
- Demand is the real thing, not a vitamin: weekly, penalty-backed, perjury-signed, payment-gating, already-budgeted, near-involuntary retention; statutes cited (40 U.S.C. §3145, WH-347, 29 CFR Part 5) + 2023 DOL rule + IIJA/IRA tailwind. Strongest demand consensus in the field.
- Competitive air open, incumbents beatable (LCPtracker, Points North/eMARS, eBacon, Foundation, ADP bolt-on — DIY software/weak bolt-on/sleepy shops). No funded SaaS aggressor.
- The single hinge is delivery economics, stated five ways: the unproven per-project human-exception rate under a perjury-grade standard decides 70%-margin software service vs 50%-margin consultancy.
- The cheap pre-build experiment is agreed/identical: ingest first ~10 contractors' last month, measure true exception rate + minutes; 50-contact bid-award outbound pilot; 15–20 pricing interviews.

## WHERE EXPERTS DISAGREE (PM call)
- Margin/capacity optimism (CFO/COO) vs structural-cost skepticism (CTO) → **CTO frame load-bearing**: the jurisdiction/portal maintenance treadmill is a continuous cost that grows with state count; CFO/COO numbers are correct only conditional on narrow scope. → scope discipline (federal + 1–2 heavy states) is a launch precondition.
- Reach velocity: CMO intent-data optimism (positioning 9, wedge 8) vs CMO's own CAC realism (6) / customer truth (6) → **lower side load-bearing** until the 50-contact pilot returns a reply-to-close.
- Liability "insurable/second-order" (Legal) vs operational/reputational reality (COO) → MSA/insurance necessary but does not neutralize referral-channel chill from one publicized audit miss in a tight community.

## TOP 5 RISKS (ranked)
1. Delivery drifts software-leveraged → labor-intensive (the margin hinge; unverified ~15% exception rate; 25–30% would halve margin and ~double the mo24 count to 90–100).
2. Reach velocity into a low-trust, offline, slow buyer (governs mo12 ladder timing).
3. Jurisdiction/portal maintenance treadmill (un-API'd LCPtracker/state portals break silently; a silent failure withholds client payment).
4. E&O / FCA liability with referral-channel-chill as its sharp edge.
5. Willingness-to-pay at $300–$1,200/project/mo unvalidated (ladder rests on ~$3K/mo blended ARPU).

## TOP 3 STRENGTHS
- Best-in-field demand profile (forced, weekly, perjury-signed, payment-gating, budgeted; documented tailwind).
- Clean white space vs beatable incumbents; "we run it, you don't" + the open bid-award intent-data wedge no incumbent operationalizes.
- Near-ideal legal/operational shape: no license required, no consumer/special-category data, no field ops (logistics 9), obligation binds the customer; SOC 2 background makes security credible; capital-light, advance-billed.

## RED-TEAM (documented)
- CFO #4 Unit economics 8 → **7** (lands: rests on three [ASSUMED] inputs — CAC, ARPU, specialist ratio — the evidence rule caps it).
- CMO #8 Competitive air 9 → **8** (lands: CMO itself notes LCPtracker/Foundation could add a service arm; regulation-forced demand invites a funded entrant).
- CFO #6 Path-to-income (ladder) 8 → **held** (ladder, not $2M, closes on a small count even in the downside; override says don't penalize for missing $2M).
- COO #3 Logistics 9 held; COO #7 Throughput 8 held but flagged weakest (rests on assumed exception rate).
Recompute: mean 7.16 → **7.12**. Confirms, does not change, the verdict.

## PATH TO GO (not a structural rebuild — three pre-build experiments)
1. Exception-rate test: ingest 10 real contractors' last month; measure fraction of weekly per-project cycles needing human resolution + minutes each. The single gating number.
2. Bid-award outbound pilot: build SAM.gov/FPDS/state-DOT list; 50 founder-led contacts; measure reply→demo→close + price-flinch point; 15–20 pricing interviews.
3. Scope + liability scaffolding: commit to federal + 1–2 heavy states (CA/NY); verify wage-data sources + portal mechanics for those two before writing the rules engine; counsel papers the MSA (client certifies, liability capped at fees, consequential/FCA disclaimed, accuracy warranty) + confirms UPL boundary.

Proof metric by month 6: weekly specialist-hours per active contractor at 10+ live contractors. ≤~0.6 hr/contractor/wk (one FTE to ~27) → software thesis real → GO. Trending to 1.5+ → consultancy → re-price per project or narrow scope.
