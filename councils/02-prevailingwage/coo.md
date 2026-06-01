COO REVIEW — Managed Certified-Payroll & Prevailing-Wage Compliance for Public-Works Contractors

ONE-PARAGRAPH OPERATIONS READ
A remote, software-leveraged managed compliance service — structurally the same shape as the CMMC archetype: a regulation forces a weekly, penalty-backed, budgeted buy, and the work product is documents (WH-347 / state-equivalent certified payrolls) plus portal filings and audit correspondence, all deliverable from a laptop. Two founders + a software engine + one named prevailing-wage specialist can plausibly run it, and the unit of work (a weekly per-project payroll certification) is high-frequency, standardized, and machine-generatable. The real tension is not field ops — there is none — but ingestion friction (every contractor's payroll/timekeeping data is a different mess), the weekly cadence (a recurring deadline every Monday–Tuesday, not a quarterly sprint), and jurisdiction-specific wage-determination/fringe expertise depth gating how many states you can serve before hiring beyond one specialist. The labor model is "exception review per project per week," which scales with active projects, so the staffing math matters.

THE TUESDAY-IN-MARCH WALKTHROUGH
Month 12: ~25 contractor customers averaging ~4 active covered projects each → ~100 active projects. Certified payroll is due weekly; agencies expect prior week's payroll within 7 days of pay date, so work clusters Mon–Wed after a Friday pay period.
Tuesday 7am: ingestion jobs pull prior-week payroll/timekeeping — some via clean API into the contractor's payroll system (Foundation, Sage 300 CRE, QuickBooks, ADP, Paychex), many via emailed CSVs, a few via a hand-filled spreadsheet. Software maps each worker to a classification, applies the active wage determination for that county/trade, computes prevailing base + fringe, checks fringe-credit offsets (cash vs bona-fide plan), validates apprentice-to-journeyman ratios, generates WH-347 or state form (CA DIR eCPR, NY, WA L&I). ~85 of 100 reconcile and queue for filing.
~15 throw exceptions: a worker in a classification the determination lacks (needs a conformance request — multi-day to multi-week), an apprentice-ratio breach, an ambiguous fringe annualization, a paycheck under the prevailing rate that must be flagged for a restitution check before truthful "penalty of perjury" certification. Founder A / specialist works the queue: "Worker #4417 coded laborer but ran conduit — that's electrician rate; confirm and we re-rate, else back wages owed." Three contractors don't reply; filings slip, deadlines tracked. Two portal uploads reject on format (a known LCPtracker/eCPR annoyance) and get re-keyed. One contractor got a DOL audit letter; the specialist spends 90 min assembling the audit-ready record (12 weeks of certified payrolls, conformance approvals, fringe docs) and drafting the response. Founder B runs two onboarding calls + a content/sales push. By 6pm ~95 filed, 5 in exception/waiting status with deadlines tracked, audit response drafted. Nobody got in a truck; friction was data quality, jurisdiction edge cases, and the perjury-grade standard meaning you cannot file machine output blindly.

CAPACITY MATH
Ladder: ~$300K/founder mo12 = ~$600K income. Lean managed-service: revenue ≈ income + specialist cost + thin overhead; target ARR ~$750K–$850K [ASSUMED GM 70–80%]. Pricing blended ~$2.5K/contractor/mo = $30K/yr. Customers for ~$800K: ~27 contractors at ~4 projects = ~108 active projects.
Weekly load: 108 projects × ~4.3 wk/mo = ~465 report-cycles/mo, ~108/week. Software generates/validates all; human cost is exceptions:
- ~15% exception rate [ASSUMED 10–20%; verify by sampling first 10 contractors' first month] → ~16 exception-cycles/wk × ~25 min = ~6.7 hrs/wk.
- Routine QC on ~92 clean cycles × ~3 min = ~4.6 hrs/wk.
- Portal rejections ~8/wk × 15 min = ~2 hrs/wk.
- Audit responses ~1/mo × 4 hrs = ~1 hr/wk amortized.
- Correspondence/conformance follow-ups ~3 hrs/wk.
Total ≈ ~17.3 hrs/wk specialist work for ~27 contractors / 108 projects — well within ONE FTE, advisor on call for hard conformance/fringe. Onboarding ~27 contractors × 3–5 hrs = ~110–135 hrs/yr ≈ ~2.5 hrs/wk by a founder.
Bottleneck: exception queue scales linearly with active projects, gated on a SCARCE skill. At 108 projects one specialist suffices. To 3x revenue (~$2.4M ARR, ~80 contractors, ~320 projects) → ~3 specialists / ~52 exception-hrs/wk — one new specialist per ~$700K–$800K ARR. A real recurring hiring dependency in a thin pool, but a known, linear, affordable curve — not a field-ops wall. Capacity holds for mo12 and mo24.

SCORES (1–10)
1. Delivery clarity & repeatability: 8 — Standardized weekly WH-347/state-form certification; software ~85% clean, human handles a defined exception queue (~16/wk at 108 projects); documentable/trainable, shown by per-cycle decomposition.
2. Supply chain resilience: 7 — Inputs are data: contractor payroll exports (multi-format), DOL wage-determination data (SAM.gov/WDOL, free/public), cloud/AI APIs; only soft single-source risk is agency portals you must integrate with.
3. Logistics tractability: 9 — Fully remote, zero routing/installs/trucks; delivery is doc generation + portal filing + email; the walkthrough has zero field events.
4. Customer-ops scalability: 6 — Onboarding moderate-touch (~3–5 hrs each, map format + load determinations); ongoing support is a weekly per-project exception queue, not self-serve SaaS.
5. Vendor/partner dependency risk: 6 — Cloud/LLM/state portals/payroll systems mostly replaceable; real exposure is portal/export format changes breaking ingestion, but none bet-the-business.
6. Hiring feasibility: 6 — First/recurring hire is a prevailing-wage/Davis-Bacon specialist, a scarce skill (agency/labor-compliance/construction-CPA backgrounds); one suffices to ~$800K ARR, each +$700K–$800K needs another in a thin pool.
7. Throughput capacity at target: 8 — Shown: ~108 projects / ~27 contractors mo12 = ~17.3 hrs/wk, inside one FTE plus founders; hits the ladder without heroic headcount.
8. Quality control simplicity: 6 — Software standardizes generation, but every report is signed under penalty of perjury, so errors carry legal/withheld-payment consequences and a human must own exceptions; high-stakes failure mode demands tight QC.
9. Geographic / seasonality risk: 7 — National base, year-round weekly obligation (no weather/holiday peak); mild jurisdiction-concentration since each new state's regime is its own learning cost — expansion gated by expertise, not demand.
10. Tooling maturity available: 5 — The compliance engine (wage-determination matching, fringe-credit logic, state-form generation, portal submission) must largely be BUILT; off-the-shelf covers periphery (CRM, billing, cloud, LLM) only.

AVERAGE SCORE: 6.8 / 10

TOP 3 OPERATIONAL STRENGTHS
- Fully remote, zero field ops — the walkthrough contains no truck/install/site visit; exactly the founders' preferred shape.
- Favorable throughput math: ~27 contractors / ~108 projects to the mo12 ladder needs only ~17.3 hrs/wk specialist labor — one FTE plus founders clears it.
- Weekly cadence makes work standardized and software-leverageable; ~85% of cycles machine-generated clean, concentrating effort on a bounded exception queue.

TOP 3 OPERATIONAL RISKS
- Data-ingestion friction: every contractor's export differs (Foundation, Sage 300 CRE, QuickBooks, ADP, manual spreadsheets); dirty input (mis-coded classifications, ambiguous fringe plans) is the largest recurring labor sink.
- Scarce-specialist hiring dependency: throughput scales linearly with projects, gated on Davis-Bacon expertise; each ~$700K–$800K ARR needs another specialist that may be slow to fill.
- High-stakes QC under perjury-grade certification: a wrong rate or missed weekly deadline can trigger withheld payments/back-wage findings; severe failure mode demands review discipline that limits pure automation.

BIGGEST SINGLE RISK
Collision between data-ingestion chaos and the perjury-grade weekly certification standard. The promise is "software ingests payroll/timekeeping and generates validated certified payroll," but the data is only as good as a harried clerk's coding, and the certification is signed under penalty of perjury — you cannot file machine output, you must catch and resolve every mis-classification, fringe ambiguity, ratio breach, and underpayment before certifying. If real exception rates run toward 20–30% (vs assumed ~15%), the queue balloons and the elegant ~17-hrs/wk model becomes a 35–40-hr grind per ~100 projects, doubling specialist headcount and compressing margin. Worse, a wrong filed report that withholds a contractor's payment or yields a back-wage/debarment finding has a severe reputational/liability blast radius in a tight community. The thesis rests on the exception rate being bounded and ingestion cleanable at scale — the number the founders cannot yet prove.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What is the actual exception rate? Sample the first 10 contractors' first month — what fraction of weekly per-project cycles need human resolution, and how many minutes each? The whole model hinges on this 10–20% assumption.
- How many distinct payroll/timekeeping source systems/formats must you ingest for the first 25 customers, and engineering cost per mapping? Clean API for the top 3, or perpetual CSV-cleaning?
- For each state, who supplies jurisdiction-specific wage-determination, fringe-credit, and e-filing-portal expertise, and how fast can the specialist + advisor cover a new state? Cadence of adding states without a new hire?
- Where does liability land when a report you generated/filed is wrong and payment is withheld? E&O + contractual cap; how does that shape the QC step?
- Realistic specialist-hire lead time/cost, and plan when you need a second/third faster than the pool supplies?

RECOMMENDATION: GO (with exception-rate validation as a gating pre-build experiment)
One of the cleaner concepts of its type: fully remote zero field ops (dim 3 = 9), throughput math closes at the mo12 ladder with one specialist + founders (~17.3 hrs/wk for ~108 projects), work is a standardized software-leverageable weekly deliverable. Not higher because the core engine must be built not bought (dim 10 = 5), onboarding + weekly exception queue are moderate-touch (dim 4 = 6), QC is high-stakes under perjury-grade certification (dim 8 = 6), scaling is gated on a scarce specialist (dim 6 = 6) — ordinary friction of a productized compliance service, not a field-ops wall. Before build dollars: ingest 10 real contractors' last month and measure true exception rate + per-exception minutes. At/below ~15–20%, margins hold and this is a strong operate-able business; much higher → re-price per-project or narrow jurisdiction scope before scaling.
