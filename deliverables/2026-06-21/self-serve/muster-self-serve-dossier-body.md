# Muster Self-Serve — Concept Dossier
**Tier: C (Pass / Reposition)  |  Objectives Score: 62.6 / 100  |  June 21, 2026**

*Plain-English write-up for a smart non-expert. The full council packet and the documented red-team are in the Appendix.*

## 1. IN ONE PARAGRAPH
We'd sell a do-it-yourself software subscription to small defense manufacturers — think a 35-person machine shop that makes parts for bigger defense contractors. The U.S. government requires any shop that handles sensitive (but unclassified) defense information to keep a current cybersecurity self-score on file, maintain two specific security documents, and answer their customers' security questionnaires. Starting November 10, 2026, a tougher version ("CMMC Level 2") begins phasing into new contracts. Our software would walk the owner through it themselves — no consultant, no sales call: upload your existing policies, get an automated gap analysis, an estimated government score, auto-drafted documents, a plain-English to-do list, and reminders to keep it current. We'd charge roughly $200-$600/month. **The honest headline: the demand is excellent, but the specific product we picked — cheap, self-serve, do-it-yourself CMMC software — is the single most crowded corner of this market, with a cheaper, better-funded competitor already underneath us and three giant, well-funded companies pushing down from above. That combination is a deal-breaker as drawn, and the right move is to keep the customer but change the product.**

## 2. WHO PAYS — AND WHY THEY CAN'T SAY NO
The buyer: the owner of a small defense subcontractor (roughly 15-200 employees) that handles "Controlled Unclassified Information" on defense purchase orders. They usually have one outside IT provider and no security staff, and the owner personally carries the compliance worry.
The forcing function (two of the five types at once):
- **Type 1 — a government mandate.** Defense rules (DFARS) already require these shops to keep a current self-assessment score in a government system. A blank or stale score can make them ineligible for new work right now. The tougher CMMC Level 2 check starts phasing into new contracts Nov 10, 2026.
- **Type 2 — a customer/contract requirement.** Their bigger customers (the "primes") flow the requirement down and send security questionnaires they must answer to keep the contract.
What breaks, and how fast: if they don't keep this current, they lose eligibility for new purchase orders — fast, concrete, tied to revenue. A real painkiller. Nobody has to be convinced they have the problem. **This part of the idea is genuinely strong — the strongest part.**

## 3. THE MONEY IN PLAIN TERMS
This is a low-price, high-volume model, and that's the catch. At ~$350/month average ($4,200/year):

| Milestone | Income goal (both founders) | Revenue needed (incl. lean costs) | Customers at ~$350/mo |
|-----------|------------------------------|-------------------------------------|------------------------|
| Month 12 | ~$600K | ~$770K/yr | ~185 (range 110-320) |
| Month 24 | ~$1.05M | ~$1.35M/yr | ~320 (range 190-560) |

The good news: ~320 customers is only about 0.8% of a conservative pool of ~40,000 affected shops — the ceiling isn't the problem. The hard part is the "PLG volume" problem (product-led growth = people find it, try it, and buy with a credit card, no salesperson). To get ~185 paying shops in 12 months with no sales team, a lot of non-technical owners have to find us online, run the free tool, and actually finish a genuinely hard compliance task alone and put a card down. That last step is the entire business, and it's unproven — and we'd be charging $200-$600/month when a competitor charges $99 and several tools give the free part away for $0. The math works on paper; the path to those customers is uncertain and the price is under pressure from below.

## 4. WHY WE WIN (AND HOW THIN THAT REALLY IS)
Our honest edge is marketing, positioning, and the ability to build software ourselves — a sharper message and a simpler product than the sleepy players. The wedge: a free gap analysis as the hook, content/SEO on present-tense pain, and warm referrals from DoD-run small-business help centers (APEX Accelerators, MEP centers). **The uncomfortable truth:** that edge differentiates the marketing, not the product. Our "fastest, simplest, cheapest, CMMC-only, no-consultant" pitch is already claimed by competitors who have it or can copy it in a single marketing cycle. And our one truly different design choice — deliberately not storing the customer's sensitive data — cuts against us competitively: it keeps us safe and cheap, but it also means we can't do the expensive, "sticky" work (setting up and monitoring a secure environment) that buyers increasingly want and that the strong competitors now sell. A happy customer is "one export away" from leaving. There's no real lock-in.

## 5. THE COMPETITION (FROM THE ANALYST — PLAIN ENGLISH)
This is where the idea breaks. Our chosen corner is squeezed from both sides.
**Cheaper than us, already here (the floor):**
- **FutureFeed** — does almost exactly our product (CMMC-only, guided assessment that auto-fills the documents), but cheaper ($99/month vs. our $200 floor), with 1,400+ customers, a 300+ partner channel, six years in, $9.3M raised. The single biggest problem: it is our concept, already built and funded.
- **ComplyUp** — "the industry's lowest price," free trial, generates the score and exports the documents.
- **6+ free tools** (Ardalyst, Peerless, others) already give away the free score-and-gap-analysis hook. So our "free hook" is table stakes and willingness to pay for "score + documents" is already pushed toward zero.
**Bigger and pushing down (the ceiling):**
- **Vanta** — $4.15B valuation, ~$300M annual revenue, 16,000 customers; already shipped a dedicated CMMC product in a government-authorized cloud. When a niche brand gets hot, they out-spend it on content or buy it.
- **Drata** — $328M raised; shipped a CMMC product; easy "you already use us, just add CMMC" cross-sell.
- **Secureframe Defense** (launched March 2026) — the most dangerous: same "fast, no consultant" promise plus it sets up the secure environment we deliberately don't — so it does strictly more of the buyer's real job.
**And the default path:** most owners' instinct is "ask my IT guy." The MSP is the trusted, already-paid relationship, and MSPs bundle this work into what they already sell.
**Plain verdict:** this isn't a sleepy market we can out-hustle. It's a funded, fast-moving one — "the right weapon to the wrong fight."

## 6. THE BIGGEST RISKS (TOP 3, PLAIN)
1. **We're boxed in by funded competitors on both sides.** Cheaper specialist below (FutureFeed at $99), giant well-funded platforms above (Vanta/Drata/Secureframe). Exactly the opponent our whole strategy says to avoid — the reason this gets a "pass."
2. **The core bet — non-technical owners do this hard task themselves and pay — may be wrong.** The whole industry says these owners reach for a human. If they stall at the scary part, our free tool just becomes a lead magnet for a consulting service we don't want to staff.
3. **We can't easily prove our answers are right, and the customer is personally on the hook to the government.** The tool produces an estimated score and documents the owner posts to a federal system and legally affirms. With no credentialed expert in the loop and content kept current by one informal advisor, a wrong answer is both a legal exposure and reputationally fatal in a tight, gossipy defense community.

## 7. WHAT WE'D TEST NEXT (CHEAP EXPERIMENTS)
Fast, cheap ways to learn before building — and they apply to a repositioned version too:
1. **Talk to 15-20 shop owners and 5-8 MSPs/APEX counselors** (~$0): which job hurts most and is least served? "Score + documents" is taken; the messier "answer all my different primes' questionnaires" job may be wide open.
2. **Free-tool smoke test** (~$1-2K): a landing page offering the free gap analysis, a little traffic plus a few warm referrals; measure how many non-technical owners finish it alone and say they'd pay. This one number makes or breaks the self-serve bet.
3. **Keyword reality check** (~$100-200): pull difficulty on the top 30 search terms to confirm we could rank before a $4B competitor points its content machine at the same words.
4. **One channel pilot:** get a single APEX/MEP center or MSP to agree to refer, on real terms, before assuming "no sales team" works.

## 8. THE SCORECARD (PLAIN)
- **Must-have / forcing function — 9.** Excellent. Government-mandated, recurring, budgeted, hard 2026 deadline. The best part of the idea.
- **Competition — 3.** The deal-breaker. Crowded with cheaper specialists and richer giants who've already shipped competing products.
- **Path to founder income — 6.** Needs only ~0.8% of the market, but the path (winning low-priced self-serve customers against cheaper, funded rivals) is genuinely uncertain.
- **Recurring revenue — 7.** Real monthly subscription with habit-forming reminders, but weak lock-in and real "we passed, cancel" churn risk.
- **Probability of success — 6.** Demand is near-certain; this configuration succeeding is not.
- **Capital efficiency — 8.** Genuinely cheap to build and run; cash arrives at signup.
- **Operational tractability — 8.** No field work; software does the delivery; only seams are support load and keeping content current.
- **Skill / founder fit — 6.** Marketing and software fit is great, but the missing CMMC credential matters here because competitors sell on exactly that authority.
- **Scalability — 8.** Build-once-sell-many; scales cleanly; a sellable asset.
- **Legal risk-gate: SERIOUS BUT MANAGEABLE** (not fatal). No license needed to sell the software; the real exposure is the "wrong-score-you-attested-to" tail, handled with conservative labeling, a tight contract, a liability cap, and insurance. A checklist, not a wall — and it does NOT lower the tier.

**Honest tier: C (Pass / Reposition).** The lowest single score anywhere was a 2 (the analyst on how aggressively the giants are already pushing into this niche). The reason for the C is not the demand — it's that the chosen product walks straight into the one opponent type our strategy says to avoid (hard-constraint #5).
**What would move it up — honestly, this needs a reposition, not a tweak.** Keep the customer and the forcing function; change the product. The three most promising directions: (1) build the stickier software the giants ignore — helping subs answer all their different primes' security questionnaires (messier, harder to copy than "score + documents"); (2) deliver a software-leveraged but service-fronted readiness offer through the IT-provider relationship the buyer already trusts (where the beatable competitors are the sleepy local consultants); or (3) arm the IT providers instead of competing with them. Each moves us off the crowded square and onto the "sleepy-incumbent" ground where our marketing actually wins. Next step: 15-20 conversations to pick which one, then re-test it fresh.
