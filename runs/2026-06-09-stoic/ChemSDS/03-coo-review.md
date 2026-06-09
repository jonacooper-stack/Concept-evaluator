COO REVIEW — ChemSDS

ONE-PARAGRAPH OPERATIONS READ
This is operationally one of the cleaner models I evaluate: a remote-first, software-leveraged recurring service with a single thin human-in-the-loop step (chemist/toxicologist sign-off on classifications) sitting on top of an authoring/portal engine the founders build. There are no trucks, no installs, no field visits, no physical inventory, and no geographic concentration — SDS authoring and portal hosting are pure knowledge-work delivered over the web nationally. The one real operational question is the throughput and availability of qualified chemist review capacity, because the founders explicitly are not chemists; that single dependency is the hinge on which the whole operations story turns. Subject to solving the chemist-capacity bottleneck, two founders plus a fractional/contract chemist and eventually a couple of authoring staff can plausibly run this.

THE TUESDAY-IN-MARCH WALKTHROUGH
It is a Tuesday in March at ~12 months. [ASSUMED] ~90 paying customers at blended ARPU ~$1,800/mo (verify against the signed-customer list). The founders are not authoring documents keystroke by keystroke — the software does the heavy lifting.
Founder A (GTM) spends the morning on pipeline: three discovery calls with small formulators who found the "OSHA HazCom 2024 / GHS Rev 7" content, plus a partner check-in with a chemical distributor pushing its 40 small suppliers to "get a current SDS or we delist you." New customers sign, then enter onboarding: they upload existing SDS + formulation/ingredient data (or a spreadsheet of SKUs + component CAS numbers). The software ingests, maps components to hazard data, and produces draft GHS classifications + draft 16-section SDS + labels for review.
Founder B (product/ops) triages the authoring queue: 14 brand-new SDS for a new line, 9 re-authored SDS for a customer who reformulated three cleaners, 6 portal/version updates. The software pre-classified all. The human bottleneck is chemist review: the contract toxicologist ([ASSUMED] $120–180/hr, verify via one rate check) logs in remotely, reviews proposed classifications, corrects edge cases (a mixture near a corrosivity cut-off, an ambiguous aspiration-hazard call), and signs off. Founder B handles everything not needing a chemist signature: formatting QC, label layout, portal publishing, comms, version control.
Support is low and predictable. Billing is automated subscription. Churn is near-zero because an unmaintained SDS is a live OSHA liability + delisting risk with the customer's own buyers. Where it breaks on a bad Tuesday: the chemist is the single point of failure — if the queue spikes (deadline-driven onboarding) with one chemist, sign-off backs up and onboarding SLAs slip.

CAPACITY MATH
Target: ~$300K/founder by mo 12 = ~$600K combined; ~$500K/founder by mo 24 = ~$1M combined (scored vs the ladder).
At [ASSUMED] $1,800/mo = $21.6K/yr/customer:
- ~$800K ARR / $21.6K ≈ ~37 customers to clear ~$300K/founder by mo 12 if costs stay lean; comfortable target ~50–60.
- ~$1.3–1.5M ARR ≈ ~60–70 customers for ~$1M by mo 24.
Binding constraint is chemist-review hours:
- New SDS: [ASSUMED] chemist review 0.5–1.0 hr per NEW SDS once software drafts (verify by timing first 20 — the single most important number). Non-chemist formatting/label/publish ~0.5 hr.
- Maintenance: [ASSUMED] avg 1–3 chemist-review-hr per customer per month (verify after 90 days of queue data).
At 70 customers (mo 24): maintenance 70 × 2 hr = 140 chemist-hr/mo ≈ 35 hr/wk; onboarding [ASSUMED] 3 new/mo × ~30 SDS × 0.75 hr = ~67 chemist-hr/mo ≈ 17 hr/wk. Total ≈ ~52 chemist-hr/wk → ~1.3 chemist-FTE (one full-time + one fractional, or a flexing partner firm). At mo 12 / ~50 customers, ~25–35 chemist-hr/wk — comfortably ONE contract chemist. Non-chemist authoring/formatting/portal labor at 70 customers ≈ ~40–50 hr/wk → one ops hire ([ASSUMED] $55–75K) + partial Founder B time.
Org at mo 24 ≈ 2 founders + 1 ops hire + ~1.3 chemist-FTE → ~$1.3–1.5M ARR. Works IF per-SDS chemist-review-hour holds; if review is 2–3 hr/SDS instead of 0.5–1.0, the chemist requirement roughly triples and the model gets ops-heavy fast.

SCORES (1–10)
1. Delivery clarity & repeatability: 8 — The unit of work is highly standardized: GHS criteria are codified rules (29 CFR 1910.1200 App A–C aligned to GHS Rev 7), the 16-section SDS format is fixed by regulation, and the software produces a consistent draft every time; only chemist sign-off varies. Regulation-defined output is genuine repeatability.
2. Supply chain resilience: 8 — "Supply chain" is cloud hosting (replaceable) + a licensed hazard-data feed (2+ vendors: Verisk 3E, ChemADVISOR/SciVera-type) + chemist labor; no MOQs/deposits/FX/physical inputs.
3. Logistics tractability: 9 — Zero physical logistics: no routing/trucks/install windows/regional density; 100% remote knowledge work delivered over the web to any US state — best-case logistics.
4. Path to founder income (ladder): 7 — Reaches ~$300K/founder by mo 12 at ~37–50 customers and ~$500K/founder by mo 24 at ~60–70 at [ASSUMED] $21.6K ARPU; credible, not heroic, but gated on the chemist-hour assumption and closing ~5–6 net logos/month.
5. Probability of success: 7 — Demand is regulation-forced; the 2026/2027 wave is a real dated catalyst; named incumbents prove buyers pay; the small-formulator gap is real — moderate execution risk concentrated in the chemist dependency, not demand.
6. Capital efficiency: 8 — Launchable for low five figures: founders build the software, only pre-revenue cash is a hazard-data license + a fractional chemist per-review ([ASSUMED] a few thousand/mo); recurring revenue from customer one, cash-flow positive fast, no inventory/field assets.
7. Operational tractability: 8 — Lean, remote-first, low-touch; subscription billing, on-demand portal, predictable support, no field ops; the only non-trivial human step is concentrated, schedulable expert review rather than dispersed labor — exactly the founders' profile.
8. Quality control simplicity: 7 — Consistency anchored by codified GHS rules + fixed 16-section template, errors catchable in review; but the failure mode has teeth — a wrong classification is a regulatory/liability event, not a refundable cosmetic miss, so QC must be rigorous and chemist sign-off is load-bearing.
9. Geographic / seasonality risk: 9 — National, year-round, weather-neutral, no seasonality; the only time-concentration is the one-off deadline wave (a tailwind, not seasonality), and maintenance revenue is perpetual.
10. Tooling maturity available: 6 — CRM/billing/ticketing/portal-hosting are off-the-shelf, but the core classification + 16-section authoring + label-generation + versioning engine must be BUILT (it is the product) and kept current with rule changes — buildable by these founders but not buy-able.

AVERAGE SCORE: 7.7 / 10

TOP 3 OPERATIONAL STRENGTHS
- Pure remote knowledge-work with zero physical logistics, no field ops, no inventory, national reach, year-round (dims 3, 7, 9 all 8–9).
- The deliverable is regulation-defined and standardized: fixed 16-section format, codified GHS criteria, software-generated drafts — high repeatability and trainability, one variable human step.
- Recurring by physics, not hope: a stale SDS is a live OSHA citation + delisting risk, so churn is naturally low and the maintenance queue is a perpetual revenue engine.

TOP 3 OPERATIONAL RISKS
- Chemist-review capacity is a single point of failure and the throughput bottleneck — at mo 24 the model needs ~1.3 chemist-FTE, and if per-SDS review runs 2–3 hr instead of 0.5–1.0, the requirement roughly triples and the business tilts toward an expert-labor shop.
- The core authoring/classification engine must be built and continuously maintained against rule changes — not buy-able, so a permanent software-build/maintenance burden sits on the founders.
- Quality failure is non-refundable: a misclassification is a regulatory/liability event, so review can never be "good enough fast" — QC rigor caps how aggressively review hours compress.

BIGGEST SINGLE RISK
The chemist/toxicologist sign-off is the one thing that makes me ask whether two non-chemist founders can actually run this at scale. Every authored/re-authored SDS legally and reputationally depends on a correct hazard classification, and the founders cannot personally provide that judgment — they must rent or hire it. If per-SDS review actually takes 2–3 hours rather than the assumed 0.5–1.0 (edge cases, mixture rules, and liability caution make chemists slow and careful), then at 70 customers the business needs three-plus chemist-FTEs instead of ~1.3, COGS swells, and the model degrades from "software with a thin expert layer" into "an expert-staffing shop with a software front end" — exactly the labor-heavy shape the founders are trying to avoid, and which concentrates bet-the-business risk in a scarce specialist's availability and retention. The entire operational case stands or falls on the real measured chemist-hours-per-SDS, so that number must be empirically established before scaling acquisition.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What is the REAL measured chemist-review time per new SDS and per maintenance edit once the software produces the draft? Time the first 20–30 real documents and publish the distribution.
- What is the chemist sourcing and redundancy plan — one named hire, a fractional 1099, or a partner firm — and what happens to onboarding SLAs and liability sign-off if that person is unavailable for two weeks during the 2026/2027 crunch? Name the backup.
- Who legally and professionally stands behind the classification — does the chemist's sign-off carry their professional liability, do the founders, and what is the E&O/indemnification structure when a misclassified SDS leads to a customer's OSHA citation or a downstream incident?
- How much of the 16-section authoring can the software genuinely automate end-to-end vs needing human authoring per document — what fraction is "software output, chemist just signs" vs "human still writes section X"? This drives the non-chemist authoring headcount.

RECOMMENDATION: GO
Operationally this is among the most tractable concepts I see: remote, capital-light, recurring-by-regulation, nationally serviceable, no field ops, and a standardized regulation-defined deliverable — dims 3, 7, 9 genuinely strong. The 7.7 average reflects a real and bounded operational risk, not a structural flaw. The single thing between this and a clean GO at scale is the chemist-review-hours-per-SDS assumption. GO with a hard gate: before scaling acquisition past ~15–20 customers, empirically measure chemist hours per document on real work, lock in primary-plus-backup chemist capacity (employed anchor + fractional flex, or a partner firm), and confirm the authoring engine automates enough of the 16 sections that the human role is "review and sign," not "write from scratch." If those three hold, two founders + one ops hire + ~1.3 chemist-FTE run this to the income ladder.
