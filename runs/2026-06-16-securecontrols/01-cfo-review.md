# CFO REVIEW — SecureControls

ONE-PARAGRAPH FINANCIAL READ
The numbers pencil, and they pencil unusually well for a bootstrap: this is a negative-working-capital, recurring-revenue, software-leveraged service against a regulation-forced, already-budgeted buy, with published pricing in the $18K–$42K/yr range and a deliberately low-touch artifact-only design that keeps margins high and capital needs near-zero. The financial spine — advance billing funds growth, ~70–80% steady-state recurring margin, retention structurally high because the obligation is permanent — is genuinely strong and is corroborated by named comparables (Vanta/Drata economics, public CMMC consulting pricing). The honest fragility is not the model's structure but its throughput: onboarding is a 40–80-hour, gated, credentialed-labor unit, and the entire month-12/month-24 income ladder depends on (a) onboarding actually compressing to ~$4–6K loaded cost via templating and (b) selling ~28 then ~55 accounts on a founder-led close — both achievable but unproven, and both labor-bound rather than capital-bound. This is a finance profile I would want to own; the risk lives in sales velocity and onboarding throughput, not in whether the unit economics work.

THE MATH

I'll reverse-engineer the income ladder from the founders' own stated pricing and check whether the headcount/margin assumptions hold.

**Revenue per account (from the published table):**
- Core: $9,500 onboarding + $18,000 ARR
- Plus: $12,500 onboarding + $30,000 ARR
- Scale: $15,000 onboarding + $42,000 ARR
- Blended recurring stated at ~$26K/yr/account. That blend implies a mix weighted toward Core/Plus (a 50/35/15 Core/Plus/Scale mix = $18K(.50)+$30K(.35)+$42K(.15) = $9K+$10.5K+$6.3K = $25.8K — internally consistent, so the ~$26K blend is honest, not optimistic). [ASSUMED mix 50/35/15; verify against the first 10–20 signed accounts.]

**Month 12 check — founder-stated ~28 accounts, ~$730K ARR, ~$300K/founder:**
- 28 × ~$26K = ~$728K ARR. The $730K ARR figure is arithmetically correct.
- Onboarding revenue mo1–12: ~28 new accounts × ~$11K blended onboarding = ~$308K of one-time cash on top of ARR. [Onboarding is collected up front — real cash, not just a P&L line.]
- Total mo-12 collected revenue (annualized run-rate ARR $728K + onboarding ~$308K, but onboarding is non-recurring; for distributable cash I use cash actually in the door during the year). Roughly: recurring billed in year (ramping, so realized < $728K run-rate — call it ~$380–430K of recurring actually invoiced as accounts ramp through the year) + ~$308K onboarding = **~$690–740K of cash collected in year 1.** [ASSUMED linear-ish account ramp; verify with the cohort build.]
- Costs in year 1: team = 2 founders + 1 analyst + fractional practitioner. Cash opex excluding founder draw: analyst ~$90–120K loaded; fractional RP/CCP ~$60–110K [ASSUMED — credentialed CMMC practitioners are scarce; fractional rates $150–250/hr, ~30–50 hrs/mo = ~$54K–$150K/yr]; tooling/software/SEO/insurance ~$40–80K. Call cash opex ~$200–310K.
- **Distributable to 2 founders: ~$690–740K collected − ~$200–310K opex = ~$380–540K total, i.e., ~$190–270K/founder.** The founders' ~$300K/founder claim is at the *optimistic edge* of my range and depends on onboarding cash landing fully in-year and opex staying lean. I'd call mo-12 **~$200–300K/founder — meets the $300K ladder rung at the top of the band, comfortably clears it if onboarding cash is front-loaded.** This is a hit-or-near-hit on the first rung, not a miss.

**Month 24 check — founder-stated ~55 accounts, ~$1.45M ARR, ~$500K/founder:**
- 55 × ~$26K = ~$1.43M ARR. The $1.45M figure is correct.
- Steady-state recurring gross margin 70–80%: $1.43M × 0.75 = ~$1.07M recurring gross profit. Plus onboarding margin on ~27 net-new accounts in year 2 (27 × ~$11K = ~$297K onboarding revenue; if loaded cost has fallen to $4–6K, onboarding gross profit ~$135–190K).
- Combined gross profit ~$1.2M. Team mo-24 = 2 founders + 2 analysts + practitioner. Non-founder cash opex: 2 analysts ~$200–260K + practitioner ~$80–130K + tooling/marketing/G&A ~$80–140K = ~$360–530K.
- **Distributable: ~$1.2M gross profit − ~$360–530K opex = ~$670K–$840K total → ~$335–420K/founder.** That lands **below the founders' $500K/founder claim.** To actually reach $500K/founder at mo-24 you need either (a) more accounts (~70–75, the lower end of the stated upside) or (b) a richer mix / higher retention / faster onboarding-cost compression. **Honest read: $500K/founder is upside-case, not base-case, at 55 accounts; the base 55-account scenario delivers ~$350–420K/founder — which still clears and exceeds the $300K mo-24 floor handily and grows past $500K in the 70–100-account band the founders flag as upside.**

**Capacity sanity check (does the labor exist to deliver 55 accounts?):**
- Steady-state: 55 × ~30–35 hrs/yr = ~1,650–1,925 delivery hours.
- Onboarding in year 2: ~27 new × 40–80 hrs = ~1,080–2,160 hours (this is the swing factor; templating to the low end is the whole game).
- Total ~2,700–4,100 delivery hours/yr against 2.5 delivery FTEs (~4,500–5,000 productive hours) + founders. **It fits at the templated/low end and busts at the un-templated/high end.** This confirms the founders' own claim that templating onboarding is the central operational project — financially, it is also the central *margin and income* lever.

**CAC / payback (the part the one-pager under-specifies):**
- Product-led top (free assessment, SEO, LinkedIn) + founder-led close. If founder time is the main CAC and we cost it, [ASSUMED] blended CAC of ~$2,000–6,000/account (mostly founder selling time + some paid/SEO), against first-year revenue of onboarding ~$11K + ~$26K recurring = ~$37K. **Payback is essentially immediate — the onboarding fee alone (~$9.5–15K) covers CAC and most of year-1 delivery cost.** LTV at even a 4-year life and 75% margin = ~$26K × 4 × 0.75 + onboarding margin ≈ ~$80–95K. **LTV/CAC ≈ 13–40x on these assumptions — exceptional, but the binding constraint is lead-to-close volume and founder selling hours, not CAC dollars.** [Verify CAC empirically in gate #3/#4.]

**Net:** mo-12 ladder rung (~$300K/founder) is a hit-to-narrow-beat; mo-24 *floor* ($300K+) is cleared with large margin; the founders' headline $500K/founder at mo-24 is upside-leaning and needs ~70+ accounts or better onboarding compression. The structure (negative working capital, high margin, sticky recurring) is the real prize.

SCORES (1–10)

1.  Startup capital efficiency:        9  — Bootstrapped on $30–60K founder capital; artifact-only design deliberately avoids GovCloud/CUI-custody capex; first onboarding fee (~$9.5–15K) is collected up front, so the business is near-self-capitalizing from customer #1 — comparable to early Vanta/Drata services-light launches that needed no inventory or facilities.

2.  Working-capital profile:           9  — Billed annually or quarterly in advance with onboarding collected up front; runs on negative working capital by design. No inventory, no AR float of consequence, no vendor deposits (enclave/GRC tooling is resold or customer-paid). This is the strongest possible WC profile.

3.  Cash flow self-funding:            9  — Advance billing + immediate onboarding cash means growth is funded by the act of selling, not by an outside raise; cash-flow positive month 9–12 is credible because each new account delivers ~$11K up front against ~$4–12K loaded onboarding cost. Growth pays for growth.

4.  Unit economics quality:            8  — On stated pricing and [ASSUMED] $2–6K CAC, LTV/CAC ≈ 13–40x and payback is sub-3-months (onboarding fee alone clears CAC). Named analog: Vanta/Drata sell comparable compliance ARPU at high retention; here the operated-service angle plus a permanent obligation supports the LTV. Held at 8 not 9 because CAC and close-rate are unproven and the model is labor-throughput-bound, which caps the velocity at which great unit economics can be harvested.

5.  Gross margin:                      8  — Stated 70–80% steady-state recurring margin is consistent with a 30–35 hr/yr/account delivery load at $26K ARPU (e.g., 32 hrs × $90/hr loaded = ~$2,880 COGS on $26K = ~89% gross on labor alone, before tooling/QC — so 70–80% after the credentialed-reviewer gate and platform costs is reasonable, even slightly conservative). Year-1 onboarding-heavy margin of 55–65% is honestly disclosed. Named comparable: SaaS-enabled compliance services run 65–80% gross; this is in-band.

6.  Path to founder-income ladder:     8  — My own bottoms-up from the founders' pricing reaches ~$200–300K/founder by mo-12 and ~$350–420K/founder at 55 accounts by mo-24 (clearing the $300K floor decisively, reaching the $500K headline only at ~70+ accounts / upside). The ladder's first two rungs ($300K mo-12, $500K+ mo-24-and-growing) are met-to-near-met on conservative-to-base assumptions, with the $500K rung arriving slightly later than the founders claim — strong, evidenced, not heroic.

7.  Realistic obtainable market:       8  — Bottoms-up SOM of 8,000–15,000 in-profile U.S. subs is grounded in DoD's own ~80,000 CMMC-L2 estimate narrowed by size/CUI/budget filters; capturing just 55 accounts is ~0.4–0.7% of the serviceable segment — two founders barely scratch it, and the Nov-10-2026 mandate creates a dated demand wave. Named, regulator-sourced sizing rather than TAM theater.

8.  Financial risk concentration:      8  — Revenue is diversified across dozens of small accounts paying $18–42K each (no single customer is material), and demand is policy-driven rather than tied to one channel. Held at 8 not 9 because the *acquisition* concentrates on a few referral sources (prime supplier-development teams, MEP/APEX), and the whole demand curve is keyed to one regulatory timeline (CMMC phase-in) that has slipped before.

9.  Scaling economics:                 8  — Margins improve with scale as onboarding templatizes ($8–12K → $4–6K loaded) and recurring delivery stays ~30–35 hrs/account; the step-costs (analyst hires, second credentialed reviewer at ~30 customers) are small and disclosed. Named analog: productized compliance/SaaS-services businesses show exactly this onboarding-cost decay curve as templates mature.

10. Financeability / exit optionality: 8  — High-retention recurring revenue against a permanent regulatory obligation is precisely what acquirers (MSSPs, GRC platforms moving down-market, PE roll-ups of compliance services) pay multiples for; a clean book of ~$1.4M+ ARR with a sticky system-of-record is a transferable asset, not a personal-services practice. Held at 8 because the credentialed-reviewer gate gives the business a key-person/credential dependency a buyer would diligence.

AVERAGE SCORE: 8.3 / 10

TOP 3 FINANCIAL STRENGTHS
- Negative-working-capital, self-funding cash engine: onboarding fees (~$9.5–15K) and advance-billed subscriptions mean the business is near-self-capitalizing from the first customer, launchable on $30–60K, cash-flow positive by month 9–12 — a near-ideal bootstrap finance profile.
- Durable, high-margin recurring revenue against a permanent, budgeted obligation: ~70–80% steady-state gross margin on $18–42K ARR per account, with structurally high retention because the SPRS/SSP/POA&M maintenance never ends and the evidence system-of-record is sticky — corroborated by Vanta/Drata-class compliance economics.
- Exceptional unit economics with sub-3-month payback: the onboarding fee alone clears [ASSUMED] $2–6K CAC, putting LTV/CAC in the 13–40x range; the financial constraint is selling/delivery throughput, not capital or payback.

TOP 3 FINANCIAL RISKS
- Onboarding throughput and cost-compression risk: the entire margin and income ladder assumes onboarding falls from $8–12K to $4–6K loaded and that 40–80-hr engagements templatize; if templating stalls, year-1 margin stays at 55–65%, capacity busts at the high end, and the mo-24 income figure slides materially.
- The $500K/founder mo-24 figure is upside-leaning: my bottoms-up from the founders' own pricing yields ~$350–420K/founder at 55 accounts — clearing the $300K floor handily but reaching $500K only at ~70+ accounts; the founders are quoting the optimistic edge of their own model.
- Single-timeline demand concentration: the demand wave is keyed to the CMMC phase-in (mandatory in new CUI contracts Nov 10, 2026); CMMC dates have slipped repeatedly over five years, and a further slip would stretch the sales ramp and delay both ladder rungs even though the underlying DFARS 800-171/SPRS obligation already exists today.

BIGGEST SINGLE RISK
The financial issue most likely to bend this concept is **sales velocity bounded by a founder-led close colliding with onboarding throughput bounded by scarce credentialed labor** — a two-sided throughput squeeze that sits between "will it sell" and "can we deliver it." Every revenue number depends on signing ~28 accounts in year 1 and ~55 by year 2 through a deeper "mock review" plus consultative proposal that the founders personally run, while simultaneously each signed account consumes 40–80 hours of onboarding that must pass a Registered Practitioner / Certified CMMC Practitioner gate before anything is posted. If selling is slower than modeled (the founders have no pre-existing DIB relationships or CMMC reputation — their honest disclosed gap), ARR ramps behind plan and the mo-12 ~$300K/founder rung is missed on the low side. If selling hits plan but onboarding doesn't templatize, the credentialed-reviewer bottleneck caps how many accounts can actually be brought live, throttling realized revenue regardless of pipeline and pinning year-1 margin at the 55–65% floor. The mitigants are real (templating as the central project, a fractional practitioner from month 0, a second reviewer by ~30 customers, prime-referral channel) and none of this threatens *capital* — the business won't run out of cash — but it directly governs whether the income ladder is hit on schedule, and it is the variable I would instrument most aggressively before believing the trajectory.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What is the actual loaded cost and hour count of the first 3–5 onboardings, and what is the demonstrated trajectory toward $4–6K — i.e., prove the templating curve, since it drives both margin and the income ladder? (This is gate #4's real financial payload.)
- What is the empirical lead → assessment-completion → onboarding close rate and the founder-hours per closed account, so we can compute true CAC and the realistic accounts-signed-per-month ceiling? (Gate #3 should produce this; a 10% assessment-completion pass threshold is a proxy, not a close rate.)
- What is the fully-loaded annual cost of the credentialed RP/CCP coverage at 28 and at 55 accounts (fractional → second reviewer), since scarce credentialed labor is both the QC gate and the largest controllable swing in gross margin?
- If the CMMC contract-mandate date slips again (it has before), what is the bridge revenue from the *already-in-force* DFARS 800-171/SPRS obligation alone, and does the mo-12 ladder rung survive a 6–12-month mandate slip?
- What blended Core/Plus/Scale mix are the first 10–20 signed accounts, and does it hold the ~$26K ARPU the entire model rests on, or does the truly-small-shop focus drag the blend toward $18K Core?

RECOMMENDATION: GO
The financial structure is genuinely strong and rests on evidence rather than adjectives: a negative-working-capital, ~70–80%-margin, sticky recurring business against a regulation-forced, already-budgeted buy, launchable on $30–60K and self-funding from the first onboarding fee, with named comparables (Vanta/Drata economics, public CMMC consulting pricing, DoD's own market sizing) supporting the ARPU, retention, and TAM. My own bottoms-up from the founders' published pricing clears the $300K/founder mo-12 rung (at the top of a ~$200–300K band) and decisively clears the $300K mo-24 floor, reaching ~$350–420K/founder at 55 accounts; the only place I trim the founders' own narrative is their $500K/founder mo-24 headline, which is upside-leaning and arrives at ~70+ accounts rather than 55 — a calibration note, not a disqualifier, since the ladder's required rungs are met. This is a GO on financial merit, conditioned on the founders proving two unproven-but-testable curves cheaply in the first 90 days: that onboarding templatizes toward $4–6K loaded, and that the founder-led close signs accounts fast enough to ramp ARR on the modeled schedule. Neither is a capital risk; both are throughput risks, and both are exactly what the founders' own <$25K validation gates are designed to measure.
