CFO REVIEW — Member Engagement & Dues-Collection Overlay for Labor Unions

ONE-PARAGRAPH FINANCIAL READ
The financial spine of this concept is unusually strong because the monetization is a payment take-rate on a recurring, mission-critical money flow (union dues) plus an SMS markup — both scale with usage, require no inventory or AR float, and become structurally sticky once they are the dues rail. The pain is genuinely budget-threatening (a union that cannot collect dues is going out of business), which is the rarest and most valuable thing a CFO can underwrite. The two real financial questions are (a) whether a freemium-to-take-rate model produces enough dollars per union to clear the $300K/$500K-per-founder ladder without an implausibly large logo count, and (b) chargeback/dispute and payment-ops risk on the dues rail, where the founders sit in the money flow and inherit liability. The numbers can pencil to the income ladder on a few hundred mid-sized locals, but the take-rate-on-payments model means revenue is throttled by both adoption depth (what fraction of members actually pay digitally) and the founders' ability to keep most of the processing spread rather than handing it to Stripe/an acquirer.

THE MATH
Target (relabeled per objectives ladder, NOT the $2M figure in the CFO doc): ~$300K/founder by month 12 = ~$600K combined ARR; ~$500K/founder by month 24 = ~$1.0M+ combined ARR; $2M/founder is upside only.

Revenue is two streams. Stream A is the payment take-rate on dues collected digitally. Stream B is SMS markup.

Assumptions:
- US union membership: ~14.3M members [SOURCE: BLS Union Members Summary, Jan 2024, ~14.4M wage/salary union members, ~10.0% rate]. Serviceable focus is members in right-to-work / paycheck-protection states where payroll deduction is impaired — [ASSUMED] 3–6M members in affected segments; verify by mapping the 27 right-to-work states' public-sector and affected private-sector membership against BLS state tables (cheap: one analyst-day).
- Average annual dues per member: [ASSUMED] $400–$900/year (often ~1–2% of wages or a flat $30–$70/month). Verify by pulling 10–20 union LM-2 filings from the DOL OLMS public database (free, ~half a day) — LM-2s disclose total dues receipts and membership.
- Digital-collection adoption: of members in a union that signs, the fraction who actually pay via the new card/ACH rail rather than other means — [ASSUMED] 25–60% in year 1, ramping. Verify via a pilot with one local.
- Net take-rate the company KEEPS after the underlying processor (Stripe/acquirer) is paid: card interchange+processor ~2.9%+$0.30; ACH ~0.5–0.8%. The company's RETAINED spread is [ASSUMED] 0.5–1.5% on card and 0.3–0.6% on ACH. Verify by quoting an Interchange-Plus or PayFac arrangement (free quotes from Stripe Connect, Finix, or a sponsor bank).

Worked example, Stream A:
- Take a mid-sized state body with 50,000 members. At $600/yr average dues and 40% digital adoption → dues flowing through the rail = 50,000 × $600 × 0.40 = $12.0M/yr.
- At a retained net take of 1.0% blended (mix of card and ACH) → $120,000/yr revenue from ONE such body.
- To reach ~$600K combined ARR (month-12 rung): ~5 such bodies, OR ~25 locals of 10,000 members at the same economics.
- To reach ~$1.0M combined ARR (month-24 rung): ~8–9 such state-level bodies, or the equivalent in locals.

Stream B (SMS markup): at, say, 50,000 members × 24 texts/yr × $0.005 retained markup = $6,000/yr per 50k body — small, call it 5–10% of revenue. It is a rounding error next to the payment rail; the rail is the business.

Reading: the income ladder is reachable on single-digit-to-low-double-digit state/national signings, which is plausible given a top-down mandate motion (one executive director can push adoption down to many locals). The fragility is entirely in two numbers I had to assume: the retained take-rate spread (if Stripe eats most of it, 1.0% becomes 0.3% and you need 3x the logos) and digital adoption depth (if only 20% of members ever switch to the digital rail, revenue per body falls proportionally). Both are cheaply testable before committing.

SCORES (1–10)
1.  Startup capital efficiency:        9  — Pure software overlay + integrations; no inventory, no field ops; launchable for low five figures plus founder dev time, with payment-rail compliance (PCI/PayFac) the only real cost, which founders' prior SOC 2/HIPAA experience de-risks.
2.  Working-capital profile:           8  — Take-rate is netted at settlement so the company is paid as money moves (no AR cycle, no deposits out); minor float/reserve held against chargebacks is the only working-capital tie-up, typically [ASSUMED] 5–10% rolling reserve per processor norms.
3.  Cash flow self-funding:            7  — Usage/take-rate revenue arrives continuously with no upfront CAC inventory, so growth largely self-funds; the drag is freemium (free tier consumes SMS/infra before any payment volume converts), making early dollars lumpy until the dues rail turns on.
4.  Unit economics quality:            7  — One signed state body throwing ~$120K/yr against a low-touch software cost base implies strong gross contribution and likely LTV/CAC >5 given multi-year stickiness, but CAC is founder-led enterprise sales with long union procurement cycles [ASSUMED 6–12 mo], pushing payback toward the longer end.
5.  Gross margin:                      6  — The headline take-rate is gross of the underlying processor; the company's RETAINED margin after Stripe/acquirer fees is the real number and is unproven — if it can secure PayFac/Interchange-Plus economics margins are 70%+, if it resells Stripe at standard rates the spread is thin, so I cap this until the spread is verified.
6.  Path to $2M in 24mo:               6  — Relabeling to the objectives LADDER (~$300K/founder mo-12, ~$500K/founder mo-24): the ladder is reachable on ~5–9 mid-sized signings per the math above; literal $2M/founder is upside and would need ~30+ such bodies, which I do not credit in 24 months given union sales cycles.
7.  Realistic obtainable market:       7  — BLS reports ~14.4M US union members; even the affected right-to-work/paycheck-protection subset [ASSUMED 3–6M members] at $400–$900 dues each is a multi-billion-dollar dues flow, far more than two founders can scratch in 24 months.
8.  Financial risk concentration:      5  — A top-down mandate model means a handful of national/state signings can dominate revenue early (one body = a large revenue share), plus single-channel dependence on the payment processor relationship; diversification only arrives after many bodies sign.
9.  Scaling economics:                 8  — Margins improve with scale because incremental member volume rides fixed software and the company can negotiate better processor pricing as dues volume grows (volume-tiered interchange/PayFac economics are documented in Stripe Connect and Finix pricing), with no step-function ops hiring tied to member count.
10. Financeability / exit optionality: 8  — Recurring take-rate on a sticky payment rail is a clean, transferable asset; vertical payments/embedded-fintech assets trade at high revenue multiples (e.g., named comparable: Toast and Mindbody monetize vertical SaaS via payment take-rate), and the horizontal extension to associations/non-profits widens the buyer pool.

AVERAGE SCORE: 7.1 / 10

TOP 3 FINANCIAL STRENGTHS
- Monetization is a take-rate on a recurring, existential money flow (dues), so revenue is both recurring and structurally sticky once it becomes the rail — the strongest possible CFO position.
- Near-zero working capital: paid at settlement, no inventory, no AR cycle, no field ops; launch cost is low five figures plus founder dev time.
- Scaling economics improve rather than degrade — incremental members ride fixed software, and dues volume earns better processor pricing over time.

TOP 3 FINANCIAL RISKS
- The RETAINED take-rate spread is unknown; if the underlying processor captures most of the fee, the headline 1% collapses to a fraction and the logo count needed to hit the ladder multiplies.
- Adoption DEPTH risk: signing a union body does not equal members switching to the digital rail — if only 20–30% ever pay digitally, per-body revenue falls proportionally and the freemium free tier still burns cost.
- Chargeback/dispute and payment-ops liability: sitting in the dues money flow means the company inherits refund/chargeback exposure, reserve requirements, and potential KYC/sponsor-bank obligations on tens of thousands of individual payers.

BIGGEST SINGLE RISK
The single financial issue most likely to kill this is the collision of two unverified numbers: the retained payment spread and the digital-adoption depth. The entire model rests on the company keeping a meaningful slice of a recurring dues flow, but the headline "take-rate" is gross — the underlying processor (Stripe, an acquirer, or a sponsor bank) is paid first, and what the company keeps could be anywhere from a healthy 1%+ (if it can stand up PayFac/Interchange-Plus economics) down to a thin few-tenths-of-a-percent (if it merely resells Stripe at list). Compound that with adoption depth: even a mandated rollout only earns on dues that actually flow through the new rail, and members are notoriously slow to switch payment habits, so a 40% assumption could realistically be 20%. If both land on the unfavorable side simultaneously — 0.4% retained on 20% adoption — per-body revenue is roughly one-fifth of my worked example, turning a 5-signing ladder into a 25-signing slog against 6–12 month union procurement cycles, which would push the month-12 income rung out of reach. Becoming a registered PayFac/MSP to capture the spread also drags in money-transmission, KYC, and reserve obligations that raise both cost and regulatory exposure — manageable given the founders' compliance background, but not free.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What net spread do you actually retain per transaction after the underlying processor is paid, under a realistic card/ACH mix, and does capturing it require you to register as a PayFac/money-services business (with the reserve, KYC, and sponsor-bank costs that implies)?
- In a real pilot, what fraction of a local's members actually move their dues onto your digital rail within 6 and 12 months, and how fast does that ramp — i.e., what is true adoption depth, not just logos signed?
- What is the average annual dues-per-member and total dues receipts in your target bodies (verifiable today from DOL OLMS LM-2 filings), and how many members sit in the impaired-payroll-deduction segment you can realistically reach?
- What is your expected chargeback/dispute rate on individual dues payments, and what rolling reserve and liability does your processor/sponsor bank impose on it?
- What is the realistic union sales cycle from first contact to a mandated rollout, and how many bodies can two founder-led sellers close in the first 12 and 24 months?

RECOMMENDATION: GO
Financially this is one of the better-shaped concepts a CFO can underwrite: a take-rate on a recurring, existential money flow, near-zero working capital, improving scale economics, and a clean transferable asset, all reachable to the income ladder on single-digit-to-low-double-digit signings. The GO is conditional on resolving the two numbers that govern the whole model — the retained payment spread and the digital-adoption depth — both of which are cheap to test (free processor quotes plus a single-local pilot, and free LM-2 data for dues sizing). If the verified retained spread comes in below ~0.5% AND pilot adoption depth below ~25%, this should drop to REFINE and the team should renegotiate processor economics (move toward PayFac/Interchange-Plus) or add a flat per-member SaaS floor to the freemium model so revenue is not wholly hostage to adoption depth, before committing.
