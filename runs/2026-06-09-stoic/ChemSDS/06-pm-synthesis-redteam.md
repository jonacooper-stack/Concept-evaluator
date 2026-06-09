# SYNTHESIS — ChemSDS
Date: 2026-06-09
Council members reviewed: CFO, CMO, COO, Legal/Regulatory, CTO

## ONE-PARAGRAPH PM READ
ChemSDS reproduces the CMMC archetype almost line-for-line — a federal mandate (OSHA HazCom 2024 / GHS Rev 7) with hard dated deadlines (substances ~Jan 2026, mixtures ~Jul 2027) forces a recurring, budgeted, must-have buy from a fragmented base of small formulators that enterprise EHS platforms won't profitably serve and per-document consultancies won't productize. Capital-light, remote, no field ops; acquisition (outbound + distributor partnerships + deadline SEO + founder-led close) sits on the founders' edge. The honest tension: all three load-bearing assumptions — chemist-review-hours-per-SDS, the post-2027 recurring base, and an affordable/current hazard-data feed — are unverified and cheap to test, and the two experts closest to delivery (CTO, Legal) returned REFINE. The liability vector (an understated hazard classification a downstream worker relies on) is real and only insurable, not contractible-away.

## SCORE SUMMARY (POST-RED-TEAM)
Objectives scorecard weighted total: **75.0 / 100** (unchanged by red-team)
- Dim1 Market pull 8×20=160; Dim2 Recurring 7×15=105; Dim3 Competitive 8×15=120; Dim4 Path 7×15=105; Dim5 Probability 7×10=70; Dim6 Capital eff 8×10=80; Dim7 Op tractability 8×5=40; Dim8 Scalability 7×5=35; Dim9 Skill fit 7×5=35 → 750/10 = 75.0
- CFO average: **7.5** /10 (from 7.7)
- CMO average: **7.3** /10
- COO average: **7.6** /10 (from 7.7)
- Legal average: **6.5** /10
- CTO average: **6.6** /10
- Mean of five: **7.1 / 10**
- Lowest single sub-score anywhere: **3** (Legal dim 8, Liability exposure)
- Verdict split: 3 GO (CFO/CMO/COO) / 2 REFINE (Legal/CTO) — not unanimous.

## WHERE THE EXPERTS AGREE
- The demand is real and the shape is right — nobody disputes market pull (HazCom top-cited; dated deadlines; downstream buyers refuse non-compliant product).
- The chemist sign-off is THE hinge — CFO ("throughput/margin governor"), COO ("single point of failure"), CTO ("load-bearing"), Legal ("named credentialed reviewer is standard of care") all converge.
- All economics rest on three unverified numbers: real ARPU/tier mix, chemist-review-minutes-per-SDS, post-2027 recurring base — each [ASSUMED], each paired with a cheap experiment.
- Operationally/technically buildable by these founders (capital-light, remote, ~14–20 dev-week MVP, infosec in-wheelhouse).

## WHERE THE EXPERTS DISAGREE (PM calls)
- GO vs REFINE traces to whether the chemist + hazard-data + coverage chain holds. **Call: the REFINE frame is load-bearing** — CTO/Legal look directly at what decides "software with a thin expert layer" vs "expert-staffing shop with a software front end," and that resolves with cheap experiments that should run BEFORE meaningful spend.
- Liability: contractible nuisance (CFO/COO) vs model-defining (Legal 3, CTO "business-ending bug"). **Call: Legal holds** — a third-party bodily-injury tort isn't capped by an LOL clause the injured party never signed; insurable, but insurability must be PROVEN before build.
- Annuity question: "recurring by physics" (COO) vs thin post-wave base (CFO). **Call: CFO is right to flag** — low churn + a thin maintenance queue = sticky-but-shrinking ARPU, worse for the mo-24 figure than either states alone.

## RED-TEAM (mandatory)
Challenged the five highest sub-scores:
1. CFO dim 1 Capital efficiency 9→**8** (build needs a licensable hazard-data feed + paid chemist pre-revenue — more than the cleanest low-five-figure launches).
2. COO dim 3 Logistics 9 — **HELD** (literally zero logistics layer).
3. COO dim 9 Geographic/seasonality 9→**8** (real demand-timing concentration: 2026/2027 wave + March-1 EPCRA cycle; "no seasonality" oversells).
4. CMO dim 1 Positioning 8 — **HELD** (customer-legible with named contrasts; clarity, not defensibility, is what's scored).
5. CFO dim 6 Path-to-income 8→**7** (rides on [ASSUMED] $21.6K ARPU + unproven net margin — two stacked assumptions).
6. CTO dim 9 Scaling 8 — **HELD** (concrete architectural evidence).
- Result: CFO 7.7→**7.5**; COO 7.7→**7.6**; CMO/Legal/CTO unchanged. Mean 7.16→**7.1**. Objectives total unchanged at **75.0** (the cut CFO sub-scores mapped to objectives dims already independently scored at the lower values, so the scorecard was not inflated).

## TOP 5 RISKS (RANKED)
1. Chemist-review-minutes-per-SDS unknown, governs everything (COO/CTO/CFO) — if 2–3 hr not 0.5–1.0, FTE need triples, GM <45%, degrades to a staffing shop. Reduce: time 20–30 real docs before scaling past ~15–20 customers.
2. Third-party bodily-injury / failure-to-warn liability (Legal dim 8=3) — tort claim contracts can't cap. Reduce: two broker E&O + contingent-bodily-injury quotes before build; named reviewer + methodology + customer data warranties.
3. Post-2027 recurring base may be thin (CFO) — sticky-but-shrinking accounts. Reduce: measure re-authoring frequency; design retainer-plus-usage now.
4. Real ARPU/tier mix unproven; CAC on a scattered reluctant buyer (CMO/CFO). Reduce: 10 free gap-audits with real quotes; land ONE distributor-push partnership.
5. Hazard-data sourcing cost/currency (CTO). Reduce: 50-ingredient coverage test vs ECHA C&L + PubChem + one vendor quote before significant code.

## TOP 3 STRENGTHS
- A textbook must-have with an external enforcer (OSHA top-cited + dated deadlines + buyers refuse non-compliant product) — the CMMC archetype reproduced.
- A structurally vacated, defensible niche (enterprise platforms can't profitably come down-market; consultancies won't productize).
- Capital-light, remote, founder-fit delivery (~14–20 dev-week MVP, infosec in-wheelhouse, outbound/partner/deadline acquisition).

## THE BIGGEST OPEN QUESTION
Is this software-with-a-thin-expert-layer or an expert-labor shop with a software front end? It resolves to a single empirical number — minutes of credentialed-chemist review per machine-drafted SDS. Minutes → 70–80% GM and the ladder is reachable; hours → margin collapses and it's the labor-heavy consultancy the founders refuse to build. Cheap to measure; nothing meaningful should be spent until it is known.

## RECOMMENDATION: REFINE
Clears the doc-01 advance bar (objectives 75/100, mean 7.1, no dimension below the floor) but the GO verdict is unearned until four cheap, build-gating experiments land: (1) chemist-hours-per-SDS (median ≤1.0 hr), (2) insurability proof (two broker quotes), (3) hazard-data coverage (50-ingredient test + vendor quote), (4) real ARPU/tier mix + one distributor channel; plus (5) resolve the post-wave annuity question. Scope v1 to SDS authoring + labeling + portal; carve out/partner EPCRA Tier II and DOT/PHMSA Section 14. Target re-review 2026-07-31.

**Verdict vs the run's bar (objectives >75 AND each expert avg ≥7.5): FAIL.** Objectives 75.0 is not >75; and CMO 7.3, Legal 6.5, CTO 6.6 are below the 7.5 floor. The PM declined to soften REFINE to GO to match a near-line number — an honest near-miss, not a qualifier.
