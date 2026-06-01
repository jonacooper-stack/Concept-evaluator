COO REVIEW — Water Utility Revenue-Recovery Program

ONE-PARAGRAPH OPERATIONS READ
This is a hybrid data-plus-field-service business aimed at a fragmented universe of ~50,000 community water systems, and operationally it is more tractable than most field-service concepts because the bulk of the recurring value (the ongoing data re-screen and dashboard) is software-light analytics the founders can build and run remotely, while the physical work (meter testing, field verification) is intermittent and front-loaded into the audit phase rather than a daily delivery treadmill. The hard operational truths are (a) the diagnostic audit is partly bespoke per utility because every small utility's billing data is dirty, non-standard, and exported differently, which makes "ingest the data" a recurring custom-ETL grind rather than a clean pipeline; and (b) the sales/onboarding motion into government buyers with boards, procurement rules, and budget cycles is slow and high-touch, which is the real throughput bottleneck — not the field work and not the analytics. Two founders plus a couple of trained field techs can plausibly run this at the scale required, but only because the target customer count to hit $2M is small (roughly 40-55 contracts), and the binding constraint is how many of these slow, relationship-driven government deals two people can close and onboard per year.

THE TUESDAY-IN-MARCH WALKTHROUGH
Assume the 12-month mark, ~12-15 utility contracts signed (a realistic year-one number for a government-buyer motion started cold; [ASSUMED 10-18]). On this Tuesday in March:
- Founder A (data) starts on a customer's billing extract from last week. The utility runs an older billing system; the export came as four CSVs with inconsistent account keys, a meter-read history with gaps, and pumping/production logs as monthly PDFs. He spends ~3 hours cleaning and reconciling before a single anomaly check runs — partly different for every utility because there is no standard format across 50,000 systems. He runs the anomaly library (stopped meters, zero-consumption-but-active, declining-registration, rate-code mismatch, mass-balance apparent loss) and flags 60 suspect meters + 140 billing/rate exceptions worth ~$190k/year for that district.
- Founder B (field/sales) is on the road, driving two hours to field-verify the top 30 suspect meters from a prior audit, plus meet the district manager and board treasurer to present recovered-revenue documentation for a contract up for annual board approval. Meter testing runs ~6-10 verifications/day/tech given travel between dispersed rural connections; a two-day field trip. He's also closing the next three deals — his calendar is the company's chokepoint.
- Meanwhile three existing monitoring customers got their monthly re-screen auto-run over the weekend; two clean, one threw a new anomaly (a meter that flatlined) needing a 20-minute email + dashboard note. Steady-state support is light (~1-3 hrs/customer/month), but onboarding a NEW customer is 40-80 hours of concentrated work.
Where it breaks: Founder B can't be in three places — selling, field-verifying, AND presenting to boards — and Founder A's custom-ETL time per audit doesn't compress because the data is non-standard. The first hire (field/data tech) is needed earlier than the one-pager implies.

CAPACITY MATH (show the work)
Target: ~$2M+ distributable founder income annually within 24 months. ACV midpoint $50k (range $25k-$75k). To clear ~$2M revenue ≈ 40 contracts; to cover overhead/techs and leave ~$2M to founders likely needs ~$2.5-3M revenue ≈ 50-60 contracts. Target band 45-60 active contracts.
Onboarding throughput (binding constraint):
- New-customer onboarding labor: ~40-80 hours each (ingest + first audit + first field campaign + board deliverable). Midpoint 60h. [ASSUMED; verify by timing first 3 audits.]
- Sales cycle for a government buyer with board/procurement: ~4-9 months. [ASSUMED; verify against 5 real intros.]
- Two founders, one primarily selling. To reach 50 contracts by month 24, add ~25 net-new/year. At a 4-9 month cycle with one closer, ~25 closes/year is aggressive but not impossible IF association intros warm the pipeline — the number to stress-test.
Steady-state delivery (NOT the bottleneck):
- Monitoring re-screen: largely automated; ~1-3 hrs/customer/month. 50 × 2 = ~100 hrs/month = ~0.6 FTE.
- Annual re-audit + field verification: ~25 analyst hrs + 2 field-days/year per customer. 50 × 25 = 1,250 analyst hrs/year (~0.7 FTE). Field: 50 × 2 = 100 field-days + ~75 new-customer first-campaign days = ~175 field-days/year ≈ ~1 field FTE, lumpy/travel-heavy → 2 part-time regional techs.
Staffing: Founder B (sales + board presentations, chokepoint); Founder A (data pipeline + audits); Hire 1 (~month 6-9) field-verification tech ~$55-75k; Hire 2 (~month 12-18) data/ops analyst ~$70-90k; Hire 3 (~month 18-24) second regional field tech.
Verdict: two founders + 2-3 hires can deliver 45-60 contracts because steady-state delivery is light (~2-3 combined FTE). The fragile assumption is closing 25 government deals/year through one founder-led sales motion — the throughput wall, in sales/onboarding, not field ops or analytics.

SCORES (1-10)
1. Delivery clarity & repeatability: 5 — Recurring monitoring is repeatable, but the initial diagnostic audit is partly bespoke per utility (no standard data format across 50,000 systems); "ingest the data" is recurring custom-ETL, capping repeatability until a normalization layer is proven.
2. Supply chain resilience: 7 — Minimal physical supply chain; inputs are the customer's own data + field test equipment (off-the-shelf, multi-vendor, no MOQs), so essentially no single-source/deposit exposure.
3. Logistics tractability: 4 — Field verification requires travel to geographically dispersed rural connections at ~6-10/day/tech with significant inter-site drive time, spread across states — a real national field-ops drag, not a metro-clustered route.
4. Customer-ops scalability: 6 — Steady-state support is light (~1-3 hrs/customer/month, ~0.6 FTE across 50), but onboarding is heavy (~60 hrs/customer) and board-facing reporting high-touch, so it scales only moderately.
5. Vendor/partner dependency risk: 8 — No bet-the-business platform dependency: commodity cloud + the utility's own data + the founders' anomaly library; the only channel dependency is state rural-water associations/AWWA, which are many and parallel (50 state associations), not one gatekeeper.
6. Hiring feasibility: 7 — First hire is a field-verification tech doing a learnable, non-licensed task for ~$55-75k, from a wide blue-collar/technician pool; no specialized credential.
7. Throughput capacity at target: 5 — Delivery throughput is fine (~2-3 FTE for 45-60 contracts), but hitting target requires closing ~25 government deals/year on a 4-9 month [ASSUMED] cycle through a single founder-closer — genuinely strained.
8. Quality control simplicity: 5 — Anomaly detection on dirty data risks false positives (flagging a legitimately low-use account), and the failure mode is reputational with a board — an over-stated/wrong recovery number presented to elected officials is a credibility hit that loses the renewal.
9. Geographic / seasonality risk: 7 — Demand is year-round (NRW recurs every cycle) and the buyer universe national/dispersed; field campaigns mildly weather-exposed (winter meter testing), budget cycles add fiscal-year seasonality to closes.
10. Tooling maturity available: 5 — Analytics/dashboard/CRM are off-the-shelf, but the core differentiator — a normalization/ingestion layer absorbing dozens of non-standard billing exports + a validated anomaly library — must be custom-built and matured; no buyable platform does this for small water utilities.

AVERAGE SCORE: 5.9 / 10

TOP 3 OPERATIONAL STRENGTHS
- Light steady-state delivery: once onboarded, ongoing monitoring is mostly automated re-screening at ~1-3 hrs/customer/month (~0.6 FTE across 50), so the recurring revenue is not labor-bound like most field-service recurring revenue.
- Small target customer count: ~45-60 contracts at a $50k midpoint clears the target, so two founders plus 2-3 hires is genuinely sufficient — no army required.
- Low and replaceable dependency surface: commodity cloud + customer-owned data + off-the-shelf field gear + many parallel state-association channels — almost nothing single-sourced or platform-captured.

TOP 3 OPERATIONAL RISKS
- Per-utility custom-ETL: dirty, non-standard billing/meter/production data makes each diagnostic audit partly bespoke, eroding the "standard data work" claim and consuming founder analyst time that doesn't compress until a normalization layer is built.
- Government sales/onboarding throughput: ~25 closes/year on a 4-9 month [ASSUMED] cycle through one founder-closer is the real capacity wall; the field and data work are not the bottleneck.
- Quality/credibility failure mode: a wrong or over-stated recovery number presented to a board is a public reputational hit that kills the renewal — the QC bar is high because the customer answers to elected officials.

BIGGEST SINGLE RISK
The operational issue most likely to kill this is not the field work or the analytics — it is the collision between a slow, board-and-procurement government sales cycle and the per-utility custom-ETL onboarding burden, both landing on the same two founders. To reach ~$2M founder income in 24 months you need ~45-60 active contracts, i.e., closing ~25 government deals/year while each new deal also demands ~40-80 hours of bespoke data ingestion and a first field campaign before it produces a board-renewable dashboard. One founder cannot simultaneously carry a 4-9 month pipeline of dozens of municipal prospects, present recovered-revenue results to boards (the closing-credibility moment, and per the profile neither founder is a natural hard-closer), AND supervise field campaigns; the other cannot both engineer the anomaly library and hand-clean every utility's non-standard export. The business does not break because two people can't test enough meters — steady-state delivery is light. It breaks if the founder-led, long-cycle government deal motion simply doesn't produce 25 signed, onboarded, board-renewing contracts a year, in which case revenue lands at maybe 20-30 contracts ($1-1.5M) — a fine lifestyle business but short of target and reached more slowly than 24 months.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What is the real onboarding cost? Time your first 3 actual utility audits end-to-end. If onboarding is 80+ hours and largely non-reusable, the model needs a normalization layer before scaling.
- What is the true government sales cycle and conversion rate? Get 5 real association intros and measure first-contact-to-signed-contract time and approval steps. Is 25 closes/year through one founder realistic, or do you need a dedicated salesperson by month 9?
- How standard is the billing data across your first 10 targets? Survey which billing systems they run. If the top 3-4 vendors cover most, reusable connectors raise repeatability; if a long tail of spreadsheets/Access, custom-ETL is permanent.
- How do you guarantee the recovery number shown to a board is defensible? What's the false-positive rate, and what verification gate sits between "flagged" and "presented to council"?
- When does the recovered baseline stop recurring? If a utility fixes meters/rate codes in year one, what keeps them paying $50k/year in years 2-5 — does churn spike at first renewal once the big findings are exhausted?

RECOMMENDATION: REFINE
