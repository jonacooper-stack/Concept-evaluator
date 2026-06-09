# SYNTHESIS — FranAudit
Date: 2026-06-09
Council members reviewed: CFO, CMO, COO, Legal/Regulatory, CTO

## ONE-PARAGRAPH PM READ
FranAudit is one of the most market-pull-positive concepts this council has seen: a federally mandated (16 CFR Part 436), annually recurring, revenue-gating buy with a literally enumerable, publicly-dated prospect list (CA DFPI, WA, MN, WI registries) and sleepy hourly-billing incumbents disinclined to productize. The demand spine and wedge mirror the CMMC archetype almost beat-for-beat. But two structural hazards are priced too lightly by the bullish reviews: (1) the core deliverable — drafting/amending the FDD, judging materiality, responding to examiner comment letters — is the practice of law, and the legally defensible structure (attorney owns the client relationship and economics to avoid UPL and Rule 5.4 fee-splitting) directly erodes the margin and client-ownership the thesis depends on; and (2) the Dec-31 fiscal-year-end clustering compresses ~70% of the book into one ~8-week March–April window, a labor spike that mathematically exceeds two founders before month 24 and overloads the single sign-off attorney. A real painkiller, but NOT a clean GO — the gap between the compliant version and the profitable version is unanswered, and it lives in Legal's domain.

## SCORE SUMMARY (POST-RED-TEAM)
Objectives weighted total: **71.5 / 100** (pre-red-team 73.0)
- Dim1 Market pull 9×20=180; Dim2 Recurring 8×15=120; Dim3 Competitive 7×15=105; Dim4 Path 6×15=90 (cut from 7 in red-team); Dim5 Probability 6×10=60; Dim6 Capital eff 8×10=80; Dim7 Op tractability 5×5=25; Dim8 Scalability 6×5=30; Dim9 Skill fit 5×5=25 → 715/10 = 71.5
- CFO average: **7.3** /10 (from 7.4)
- CMO average: **7.7** /10
- COO average: **6.0** /10
- Legal average: **4.8** /10
- CTO average: **7.2** /10 (from 7.4)
- Mean of five: **6.60 / 10**
- Lowest sub-score anywhere: **3** (Legal — Industry burden, Licensing, Liability, Jurisdictional — a cluster, not a one-off).

## WHERE THE EXPERTS AGREE
- The demand is a genuine statutory must-have (forced annual FTC 120-day update + ~13-state renewals, already budgeted/paid to law firms).
- The buyer list and wedge are exceptional (CMO wedge 9; free public-registry pipeline with known renewal dates).
- The attorney sign-off is simultaneously the value, the bottleneck, and the bet-the-business dependency (four of five converge).
- The software is easy; the leverage is unproven (CTO build 7.4; real question is how much FDD assembly compresses with software vs bespoke legal/clerical labor).

## WHERE THE EXPERTS DISAGREE (PM calls)
- Legal (4.8) vs CMO/CFO (7.7/7.4) on whether it's a GO at all. **Call: Legal's frame is load-bearing.** Per doc-07, a fundamental legal/feasibility flag can't be papered over; the compliant structure (attorney-to-franchisor relationship, separate fee billing, attorney performs substantive judgments) converts FranAudit from "productized service that owns the customer" into "law firm's back-office vendor with thin dependent margin" — it changes who the business is.
- CMO competitive air 8 vs its own defensibility 6. **Call: score competition 7** — incumbents beatable, but the defensive counter (a flat-fee renewal package from a firm that already owns the legal work + client) is cheap and obvious once proven.
- COO REFINE (6.0, seasonality/throughput) vs CFO/CTO GO. **Call: COO right that this is structural seasonality** (bites op-tractability to 5), solvable but it compounds the Legal risk because the attorney-panel requirement makes the legal structure harder/costlier.

## RED-TEAM (mandatory)
Challenged five highest sub-scores:
1. CMO Wedge 9 — **HELD** (top-decile path quality; finiteness bites scalability, not wedge).
2. CMO Demand evidence 9 — **HELD** (measures demand for the outcome, statutorily proven).
3. CFO Obtainable market 8→**7** (SAM floor [ASSUMED]; winnable slice squeezed — too-small churn at bottom, lawyer-loyal at top).
4. CTO Time-to-MVP 8→**7** (revenue not legally billable until attorney structure + tri-party contracts exist).
5. CFO Financial risk concentration 8→**7** (revenue diversified but delivery concentrates on one attorney + one Q1 cluster — correlated business-level risk).
- Result: CFO 7.4→**7.3**, CTO 7.4→**7.2**, CMO/COO/Legal unchanged. Mean 6.66→**6.60**. Objectives dim 4 7→6 → total 73.0→**71.5**.

## TOP 5 RISKS (RANKED)
1. UPL / Rule 5.4 — the compliant version kills the profitable version (Legal). Not insurable. Reduce: written task-allocation matrix + structure opinion from CA/NY/IL franchise counsel confirming a UPL-safe structure that still leaves >60% margin + client ownership.
2. Software-leverage/margin thesis unverified (CTO/CFO/COO). Reduce: public-FDD diff (target ≥45% structured data-fill) before build.
3. Dec-31 FYE seasonality cluster + single-attorney throughput (COO) — ~460-hr founder shortfall + ~168 attorney-hr overload at mo-24; a missed March filing is reputation-ending. Reduce: attorney panel, Q4 prep starts, non-Dec-FYE recruitment, ops hires at ~30 clients.
4. Attorney economics compress margin + concentrate dependency (CFO/COO). Reduce: written fixed per-FDD review-only quotes from two attorneys.
5. Trust-transfer "trading my lawyer for a project manager" caps the winnable segment (CMO). Reduce: front-load the named E&O-covered attorney; one 200-franchisor timed-outbound cohort.

## TOP 3 STRENGTHS
- Near-platonic statutory painkiller with a free, named, dated buyer list (objectives dim 1 = 9).
- Capital-light, negative-working-capital, remote, no field ops (CFO 8 capital efficiency, COO 9 logistics).
- Buildable and cheap on tech, squarely in founder skills for the non-legal layers (~9–14 dev-weeks, no critical-path API).

## THE BIGGEST OPEN QUESTION
Is there a structure — confirmed in writing by real franchise counsel across CA/NY/IL — under which a non-attorney-owned company can lawfully sell a fixed-fee, software-leveraged FDD-renewal-and-filing service (founders do assembly/filing/calendar/PM; a supervising attorney does substantive disclosure judgments) WITHOUT committing UPL or improper fee-splitting, AND still retain >60% gross margin and ownership of the customer relationship/pricing to reach ~$300K/founder by month 12? Every other risk is solvable with money and discipline; this one determines whether the business that survives the legal structure is still the attractive business CMO/CFO scored.

## RECOMMENDATION: REFINE
Post-red-team objectives **71.5/100** (above the 70 advance threshold) but **Legal at 4.8 with four sub-scores at 3** is precisely the fundamental-feasibility flag doc-07 says I may not paper over, and three of five experts (COO, Legal, CTO) recommended REFINE. The objectives total clears 70 on absolute merit, but the verdict is gated by the Legal feasibility question, not the weighted average. Not a marginal-score REFINE engineered to dodge a number — the 71.5 reflects honest strength on market pull and capital efficiency; the REFINE is driven by an unresolved structural-legal question that, if it resolves badly, changes what the business is. Refinements (cheap to test): resolve the UPL/Rule 5.4 structure in writing; prove ≥45% software-compressible FDD content; lock attorney economics/capacity; engineer the seasonality smoother; validate ARPU + trust-transfer. Re-review 2026-07-21.

**Verdict vs the run's bar (objectives >75 AND each expert avg ≥7.5): FAIL — decisively.** Objectives 71.5 < 75; and COO 6.0, Legal 4.8, CFO 7.3, CTO 7.2 all below the 7.5 floor. The weakest mean of the run, driven by a genuine UPL structural flaw — the most fundamental single drag any concept this run produced.
