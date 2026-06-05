CFO REVIEW — Member Engagement & Dues-Collection Overlay for Labor Unions

ONE-PARAGRAPH FINANCIAL READ

The financial logic here is unusually clean: this is a take-rate business on a money flow (union dues) that, post-Janus, the customer is legally compelled to re-route through some non-payroll channel — meaning the founders are not creating demand, they are intercepting an existing, mandatory cash flow. Payment-processing economics and SMS markup are both high-gross-margin, no-inventory, customer-pays-as-they-transact models with effectively zero working-capital drag, and the "free entry tier mandated top-down" GTM is a genuinely smart way to collapse procurement friction in a slow, hierarchical buyer. The two real financial fragilities are (a) the take-rate is thin relative to a sticker SaaS line, so the whole model lives or dies on dues *throughput volume* and on the union not negotiating the rate to the floor once it sees the dollar amounts, and (b) the obtainable-market is narrow and concentrated — there are only so many U.S. unions, the buying cycle is political, and a handful of large affiliate wins would be most of the revenue. The numbers pencil to the income ladder, but only if the platform captures dues *processing* (not just messaging) on tens of millions of dues dollars.

THE MATH

Target (per the income ladder in 01-objectives.md, which supersedes the "$2M in 24 months" language in my own doc — relabeling accordingly): ~$300K/founder by month 12 (~$600K combined), ~$500K+/founder by month 24 (~$1M+ combined), growing thereafter. I will pencil to ~$1M combined gross profit run-rate by month 24 as the bar, with $600K by month 12 as the early rung.

Two revenue lines:

Line A — Dues-processing take-rate. U.S. union dues run roughly $300–$1,000/member/year [ASSUMED range; verifiable from published AFSCME/SEIU/NEA dues schedules and DOL LM-2 filings, which disclose total dues receipts per union — a free, cheap check]. Call it $500/member/year midpoint. On card/ACH, the platform's *net* take above interchange/processor cost is the real margin. Stripe-style all-in card cost is ~2.9% + $0.30; ACH is ~$0.25–0.80 flat. If the platform charges members/union a blended ~3.0% and keeps ~0.5–1.0% net after processor pass-through [ASSUMED; verify by pricing an actual Stripe Connect / ACH stack], then:

- Per member: $500 dues × ~0.75% net spread = ~$3.75/member/year of net revenue. That is *thin*. To hit $1M combined gross profit on this line alone would need ~$1M ÷ $3.75 ≈ **265,000 members fully processing dues digitally through the platform.** That is a very large number of *active dues-paying* members captured.
- BUT the gross-margin framing matters: if instead the platform marks up on top of cost and keeps ~1.5–2.0% all-in net (plausible if it positions as a bundled service, not a raw processor), per-member net rises to ~$7.50–$10/year, dropping the member count to **100,000–135,000 members** to reach $1M GP. Still large, but a single large state affiliate (SEIU/AFSCME state councils routinely have 50K–200K members) gets you most of the way.

Line B — SMS markup. SMS wholesale (Twilio-class A2P) is ~$0.0079/segment [Twilio published pricing, named source]; a platform markup to ~$0.02–0.03 nets ~$0.012–$0.022/message. A union doing ~24 outreach texts/member/year × 100,000 members = 2.4M messages × ~$0.015 net = ~$36K/year. Material but secondary — SMS is a sweetener, not the engine. [Message volume ASSUMED; verify in first pilot.]

Reverse-engineered customer count. The economic buyer is a union *body*; the revenue unit is the *member*. To reach ~$1M combined GP by month 24 at the optimistic ~$8/member/year net (processing + SMS blended), the platform needs ~**125,000 members actually transacting dues through it.** Realistically that means landing ~2–5 mid/large affiliates (state councils, large locals) OR one national rollout. Month-12 rung of ~$600K GP needs ~75,000 transacting members — i.e., one or two solid affiliate wins with high digital-dues adoption. This is plausible but hinges entirely on *conversion of members onto digital dues*, not just signing the union.

ARPU note: ARPU is best thought of per-member, ~$5–$10/year net, with the union as the contracting entity. The model only works at member scale, and only if dues *collection* (Line A) — not just communication (free tier) — actually flows through the platform.

SCORES (1–10)

1. Startup capital efficiency: 8 — Pure software overlay + payment rails (Stripe Connect / ACH via Dwolla-class provider); no inventory, no field ops; buildable for low five figures plus two founders' dev time. SOC 2 (founders have prior SOC 2 experience) is the main real cost, ~$15–40K [ASSUMED; verifiable from Vanta/Drata quotes].

2. Working-capital profile: 9 — Take-rate is deducted at the moment dues move; SMS billed on usage; the platform never floats inventory or carries AR — money is collected and the spread is skimmed in the same transaction, so the customer effectively pays before the platform incurs cost.

3. Cash flow self-funding: 8 — Transaction/usage revenue with near-zero COGS drag means each new transacting member is immediately gross-margin-positive; growth does not consume cash beyond CAC (founder-led sales), so growth largely pays for growth.

4. Unit economics quality: 6 — Per-member net is thin ($5–$10/year), so LTV/CAC depends wholly on the *number of members per signed union* — a single union win amortizes a long political sales cycle across tens of thousands of members, but if adoption per union is low, payback on the sales effort stretches; not yet demonstrable, hence capped.

5. Gross margin: 8 — After passing through interchange/SMS wholesale, the retained spread is ~70–90% gross margin software-style revenue (Twilio wholesale $0.0079 vs $0.02+ resale; processor cost passed through), with no labor in the unit cost.

6. Path to $2M in 24mo (scored vs. the income LADDER, relabeled): 6 — ~$1M combined GP by month 24 requires ~125K transacting members at optimistic net spread; reachable via a few large-affiliate wins but contingent on high digital-dues *adoption per member*, not just signing unions — credible, not conservative.

7. Realistic obtainable market: 5 — There are roughly 14M union members in the U.S. across ~a few thousand union bodies [BLS/DOL OLMS, named source], but the *addressable buyers* are a finite, concentrated set of national/state bodies; this is a narrow, list-able market, not one where two founders "barely scratch it."

8. Financial risk concentration: 4 — Revenue concentrates in a few large affiliates; losing or failing to renew one national/state contract could swing a large share of revenue, and the rate itself is exposed to a sophisticated buyer negotiating the take-rate down once they see total dollars processed.

9. Scaling economics: 8 — Marginal cost per additional transacting member is near zero (same software, pass-through rails), so margins hold or improve with scale; step-costs are support/compliance, not infrastructure or headcount per customer.

10. Financeability / exit optionality: 7 — A platform skimming a take-rate on a captive, recurring, regulation-driven dues flow with embedded payments is an attractive, transferable asset (payments-attach businesses trade at premium multiples), though the concentrated/politically-sensitive customer base would give an acquirer pause.

AVERAGE SCORE: 6.9 / 10

TOP 3 FINANCIAL STRENGTHS
- Near-perfect working-capital and cash-flow profile: the platform skims its spread inside the same transaction that moves the dues, so it never floats AR or inventory and growth self-funds (scores 9 and 8).
- High gross margin on retained spread: SMS resale (Twilio $0.0079 wholesale → $0.02+ resale) and payment markup over passed-through interchange yield ~70–90% GM with no labor in the unit cost.
- Demand is regulation-forced, not manufactured: post-Janus (2018) and state legislation, public unions *must* re-collect dues outside payroll — the founders intercept an existing mandatory cash flow rather than convince anyone they have a problem.

TOP 3 FINANCIAL RISKS
- Thin per-unit economics: ~$5–$10 net per member/year means the model only works at large member counts (~125K transacting members for $1M GP), so a "signed union" with low digital-dues adoption produces little revenue.
- Revenue concentration: a finite buyer universe where a few large affiliates would be most of the revenue, creating contract-loss and renewal swing risk (scored 4).
- Take-rate compression by a sophisticated buyer: once a national union sees that 0.75–2.0% of, say, $50M in dues is a seven-figure check to the platform, leadership has every incentive — and the negotiating leverage of a large account — to push the rate toward processor cost.

BIGGEST SINGLE RISK

The single most likely killer is a *throughput gap* between signing a union and actually processing its dues. The GTM thesis — give away the free communication tier so leadership mandates the tool down to every chapter — is excellent for *distribution* but it deliberately decouples adoption from the revenue event. A union can enthusiastically roll out the free email/SMS layer to 100,000 members and still collect the bulk of its dues through its existing bank/payroll-remnant/lockbox arrangements, leaving the platform with a large logo, real SMS pennies, and almost none of the dues-processing take-rate that is the actual engine (Line A is ~10x Line B). Because per-member net is thin, the business needs not just signed unions but *high digital-dues conversion per member*, and that conversion is gated by member behavior (re-signing payment authorizations, ACH mandates, card-on-file) that the union — not the platform — controls. If digital-dues adoption lands at, say, 20% of members rather than 70%, the month-24 GP is roughly a third of plan and the income ladder is missed despite impressive-looking distribution metrics.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What is the actual *net* spread you keep per dues dollar after interchange/ACH cost and any pass-through — 0.5%, 1%, 2%? Price a real Stripe Connect / Dwolla / ACH stack and show the retained basis points, because the entire model's scale requirement swings 3x on this number.
- In a pilot, what fraction of a union's members actually move their dues onto your rails within 6–12 months (vs. just using the free comms tier)? This adoption rate, not the number of signed unions, is the revenue driver — name the pilot affiliate and the target conversion.
- How defensible is the take-rate against a large affiliate negotiating it down once dues volume is large — is there a contractual floor, a bundled-value story, or switching cost that prevents the rate compressing to cost on your biggest accounts?
- How many addressable union bodies of sufficient member size realistically exist, and what is your concentration — if the top 3 accounts are >50% of revenue at month 24, what's the diversification plan?

RECOMMENDATION: REFINE

The financial architecture is genuinely good — regulation-forced demand, zero working capital, high-margin pass-through revenue, capital-light build squarely in the founders' wheelhouse (software + payments + prior SOC 2 experience). What holds it back from a clean GO is that the revenue engine (the dues take-rate) is thin per member and *behaviorally gated* by member-level adoption the platform doesn't fully control, against a concentrated, politically-slow buyer base that can compress the rate. To move this to GO: (1) validate the retained net spread per dues dollar with a real payments stack and confirm it is ≥1.5% net, (2) run one paid pilot with a mid-large affiliate and demonstrate ≥50% digital-dues conversion of members within 9 months, and (3) structure contracts so the take-rate has a floor and the union is bought into driving member conversion (e.g., tie the free comms tier to a minimum dues-processing commitment). Land those three and the income ladder ($300K/founder by mo 12, $500K+ by mo 24) is reachable on a handful of large-affiliate wins.
