# CFO REVIEW — Carrier Commission Reconciliation & Recovery Service

## ONE-PARAGRAPH FINANCIAL READ
The numbers pencil well, and unusually so for a bootstrap: this is a software-leveraged business sold on found money, where the entry offer pays for itself out of recovered dollars and the durable revenue is a sticky, data-moated subscription on top. The economics rhyme closely with proven adjacent categories — contingency/SaaS revenue-recovery (medical/insurance underpayment recovery, retail freight-audit, telecom expense management, SaaS-spend reconciliation) where vendors routinely take 15–35% of recovered dollars and then convert to recurring monitoring. The two real financial questions are not "do the unit economics work" (they clearly can) but (1) is the leakage rate big and real enough at the small-agency tier to fund attractive contingency checks, and (2) does the recurring subscription hold its price once the historical "windfall" is harvested and the monthly catch shrinks to steady-state. Both are testable cheaply before a line of code is written.

## THE MATH

**Target customer profile and the leakage pool:**
- Target agency: $1M–$50M annual commission revenue. Representative early target at ~$5M annual commission revenue [ASSUMED midpoint; real distribution heavily weighted to $1M–$10M — cheap test: pull state-level counts of licensed agencies and a sample of BGA/IMO public profiles].
- Silent leakage estimate: 2%–8% of commission revenue per cycle [ESTIMATE — to be validated]. I will NOT take the 8% top end. I use a conservative 1.5%–4% recoverable-and-collectible band, because some leakage is real but uncollectible (genuine lapses, contractual ambiguity, statute-barred), and recovery success is never 100%.

**LAYER 1 — The contingency wedge (initial historical audit)**
- Lookback: 12–24 months before records/relationships go cold.
- Recoverable pool on a $5M/yr agency at 2.5% recoverable leakage over an 18-month lookback ≈ $5M × 1.5 yr × 2.5% = ~$187K identified shortfall.
- Realized recovery (carriers contest, some fail): 50%–70% lands ⇒ ~$94K–$131K collected. Call it ~$110K [ASSUMED].
- Contingency take-rate: revenue-recovery norms 15%–35%. Use 25% [ASSUMED, anchored to named comparables] ⇒ ~$27K one-time contingency revenue per onboarded $5M agency.
- Lumpy, one-time "harvest" revenue. NOT the business — it is the customer-acquisition mechanism that funds itself.

**LAYER 2 — The recurring subscription (the durable business)**
- Steady-state ongoing leakage is smaller than the historical backlog but recurs every cycle. On a $5M agency, ongoing catch might be 1%–2.5% of commissions = $50K–$125K/yr identified.
- Subscription pricing by size/volume, anchored to value: protecting $50K–$125K/yr of otherwise-lost income justifies $1.5K–$4K/month = $18K–$48K/yr [ASSUMED — value-based, 15–40% of dollars protected]. Use ~$2.5K/mo = $30K/yr ARPU as the planning midpoint for a $5M agency, scaling to ~$6K–$12K/yr for $1M agencies and ~$60K–$120K/yr for $20M+.

**Gross margin:**
- Cost to serve = software (ingestion/normalization/recompute) + light human review per cycle. Build-once, run-many. Per-customer marginal cost at steady state ~$3K–$8K/yr at ~$30K ARPU ⇒ gross margin ~73%–90%. Model 78%–85% blended [ASSUMED — comparable to ops-heavy vertical SaaS like freight-audit/TEM at 65–80%, not pure 90% SaaS]. Cheap test: time-and-motion a single manual reconciliation on one real agency's statements.

**PATH TO THE FOUNDER-INCOME LADDER (recurring is the spine; contingency is fuel)**
Target: ~$300K/founder by mo12 (~$600K combined), ~$500K+/founder by mo24 (~$1M+ combined).
- Recurring ARPU ~$30K/yr, ~80% GM: ~$600K of gross profit ≈ ~$600K / (30K × 0.80) ≈ **25 recurring agencies**. Plus contingency: 25 onboardings × ~$27K ≈ $675K of additional (lumpy) first-year cash. So in year one the contingency harvest alone can fund or exceed the mo12 rung while you build the recurring base.
- mo24 at ~$1M+ combined GP on recurring alone: ~$1M / (30K × 0.80) ≈ **~42 recurring agencies**, i.e., roughly 40–50 agencies under subscription. A very small absolute customer count for a category with thousands of BGAs/IMOs/FMOs.
- Pessimistic case (~1% recoverable): contingency checks ~halve (~$13K/onboarding) and subscription compresses to ~$12K–$18K/yr → mo24 needs ~70–110 recurring agencies — still small share; CAC efficiency and onboarding throughput become the binding constraint, not demand. The model survives the pessimistic case; it just needs more logos.

**CAC / LTV:**
- CAC: founder-led, list-buildable segment (state DOI licensing data, NAILBA/IMO rosters, LinkedIn). The contingency offer ("we audit your last 18 months free, you pay only from money we recover") collapses sales friction to near zero. Blended CAC $2K–$8K/agency [ASSUMED]. The first audit (~$13K–$27K) typically EXCEEDS CAC → customer acquisition is cash-positive on day one before any subscription. Rare and excellent.
- LTV: $30K ARPU, 80% margin, assumed 85%–92% annual gross retention (sticky — wired into their statements, protects their own revenue) → gross-profit LTV ≈ $200K–$300K per recurring agency [ASSUMED]. LTV/CAC comfortably > 10 even after haircuts; payback immediate (contingency) to <6 months (subscription). The strongest single quantitative fact in the file.

**Bottom line:** at conservative-to-midrange assumptions the recurring business reaches the mo24 rung at ~40–70 agencies, acquisition is self-funding (often cash-positive), and gross margins are vertical-SaaS-grade. The open questions are the size/collectibility of the leakage pool and the durability of recurring price after the backlog is harvested.

## SCORES (1–10)
1.  Startup capital efficiency:        **9** — Software + founder time; no inventory/deposits/licenses/equipment; first revenue can come from a single manually-assisted recovery before the platform is fully built.
2.  Working-capital profile:           **9** — Contingency revenue collected FROM recovered dollars; recurring SaaS billed monthly/annual upfront; customer effectively pays you out of money you just put in their pocket — negative working-capital dynamics.
3.  Cash flow self-funding:            **8** — Each new logo throws off a one-time contingency check (~$13K–$27K) that typically exceeds CAC, so growth funds growth; minor drag: contingency cash is lumpy and timing-dependent on carrier response.
4.  Unit economics quality:            **9** — LTV/CAC > 10 and payback immediate-to-sub-6-months (contingency check ≥ CAC on day one; $200K–$300K LTV vs. $2K–$8K CAC). Even halving every favorable assumption leaves LTV/CAC > 5.
5.  Gross margin:                      **8** — ~78%–85% blended; build-once/run-many software with a thin human-review layer, benchmarked to freight-audit/TEM (65–80%) and pure-SaaS (85–90%). Not a 9 because statement parsing keeps a real human-in-the-loop cost.
6.  Path to founder-income ladder:     **8** — Conservative recurring math reaches the mo24 rung at ~40–70 agencies — a tiny slice of a multi-thousand-firm market — with the contingency harvest covering the mo12 rung in year one. Not a 9 because it leans on an unvalidated leakage rate and subscription-price durability.
7.  Realistic obtainable market:       **8** — Thousands of U.S. BGAs/IMOs/FMOs and benefits GAs; needing only 40–70 recurring logos means two founders barely scratch the SOM; adjacent proof in revenue-recovery/expense-audit categories.
8.  Financial risk concentration:      **7** — Revenue diversifies fast across many small agencies (no single-customer dependence); the remaining concentration is structural — dependence on continued access to/parseability of carrier statements and carriers' willingness to pay claims (a counterparty dependence).
9.  Scaling economics:                 **8** — Margins improve with scale: each newly-mapped carrier format and comp-grid template is reusable across all agencies on that carrier; review team scales sub-linearly. Network-of-templates operating-leverage story.
10. Financeability / exit optionality: **8** — High-retention recurring revenue on a proprietary data asset (encoded comp grids + multi-carrier mapping library) is clean and acquirable by insurtech/agency-management roll-ups; not a 9 only because contingency-heavy early revenue is valued below pure ARR.

**AVERAGE SCORE: 8.2 / 10**

## TOP 3 FINANCIAL STRENGTHS
- Self-funding, cash-positive customer acquisition: the first audit usually pays more than it costs to land the customer — a genuinely rare property that de-risks the bootstrap and compresses payback to ~zero.
- Vertical-SaaS-grade recurring economics with a real data moat: ~78%–85% gross margin, sticky retention, and a per-carrier template library that makes margins IMPROVE with scale — LTV/CAC > 10 after conservative haircuts.
- Tiny logo count to clear the ladder: ~40–70 recurring agencies reach the mo24 rung against a multi-thousand-firm base, so the plan does not depend on large market share.

## TOP 3 FINANCIAL RISKS
- Leakage-pool uncertainty: contingency check size and value-based subscription price hinge on an unvalidated 2%–8% estimate; if true recoverable leakage is ~1% or less, checks halve and pricing power erodes, forcing 2–3x more logos.
- Recurring-price durability after the windfall: once the backlog is harvested, the monthly catch shrinks; if agencies perceive small ongoing value, churn/price compression turns this from sticky ARR into one-time-recovery consulting with a tail.
- Counterparty/channel dependence on carriers: revenue requires carrier statements stay machine-ingestible AND carriers actually pay valid claims; a carrier that stonewalls, reformats, or contractually discourages third-party audits can throttle realized recovery.

## BIGGEST SINGLE RISK
The single financial issue most likely to kill this is that steady-state recoverable leakage at the small-agency tier is materially smaller than the headline 2%–8%, which simultaneously shrinks the contingency check (the acquisition fuel) AND undermines the recurring subscription price (the durable business). The model is beautifully self-reinforcing when leakage is large: the first audit pays for acquisition, proves value, and justifies a value-based recurring price. But that chain runs in reverse if the real recoverable number is ~1% or less: the contingency check no longer reliably exceeds CAC (acquisition stops being free), the demonstrated "found money" is unimpressive (close rates and price anchoring fall), and — most dangerously — after the one-time backlog is cleaned, the ongoing catch may be too small for a $2K–$4K/month subscription to feel justified, collapsing the business into episodic recovery consulting with weak retention. This is a magnitude risk, not an existence risk: that carriers mispay is well-documented; the question is the SIZE of the collectible pool at this tier, which a free historical audit on 3–5 real agencies would answer before any meaningful capital is committed.

## QUESTIONS THE FOUNDERS MUST ANSWER
- What is the actual recoverable-AND-collectible leakage rate at the $1M–$10M tier (dollars carriers actually pay back, not gross discrepancy) — measured on 3–5 real agencies' last 18 months? This one number drives contingency check size, subscription price, and required logo count simultaneously.
- After the backlog is harvested, what is the steady-state monthly catch as a % of commissions, and at what monthly catch does an agency principal still happily pay $2K–$4K/month — where is the floor on recurring price/retention once the windfall is gone?
- How do carrier contracts and carrier behavior treat third-party commission audits — any contractual restriction, any pattern of stonewalling, any format-instability that makes ingestion a moving target and throttles recovery?
- What is the real cost/time to onboard one agency (build the comp grid, map each carrier's format, load history), and how much is one-time-per-carrier reusable vs. one-time-per-agency repeated — this sets true gross margin and the operating-leverage curve.
- What is the empirical close rate and CAC from one real outbound campaign to ~100 agencies offering the free contingency audit?

## RECOMMENDATION: GO
The financial architecture is among the better bootstrap shapes I see: capital-light to launch, customer acquisition that funds itself (often cash-positive on the first audit), vertical-SaaS-grade recurring margins, a compounding per-carrier data moat that improves margins with scale, LTV/CAC comfortably above 10 on conservative assumptions, and a ladder that clears at only ~40–70 recurring logos in a multi-thousand-firm market. The whole thesis rests on one quantitative unknown — the true recoverable-and-collectible leakage rate at the small-agency tier and the durability of recurring price after the backlog is harvested — and that unknown is unusually cheap to resolve: a free historical audit on 3–5 real agencies answers it before committing real capital, and the contingency structure means even the validation step can be revenue-generating. Proceed, with the explicit condition that the first dollar of build follows, not precedes, a measured leakage rate on real statements.
