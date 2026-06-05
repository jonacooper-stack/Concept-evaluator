# COO REVIEW — CoverHold (Insurer-Attestation Management for Property Owners)

ONE-PARAGRAPH OPERATIONS READ
Operationally one of the cleaner managed-service shapes: the unit of work is remote document-and-evidence handling — ingest a carrier loss-control letter, build a deadline register, chase the owner for invoices/photos/vendor certs, assemble a carrier-ready package, specialist reviews before submission. Explicitly no trucks, no on-site inspections, no repairs. That removes the entire field-ops failure surface that kills most "property" businesses. The real question is latency/variability in two steps: (a) chasing evidence out of distracted multi-property owners who are the bottleneck, and (b) the specialist-review step, judgment-heavy, where throughput and quality live or die. Operable by two founders + one or two compliance specialists IF the workflow is genuinely productized; a labor sink if every letter is bespoke.

THE TUESDAY-IN-MARCH WALKTHROUGH
Tuesday in March, month 12. ~110 paying accounts, ~1,400 properties under management, active register of ~350–500 live requirements. Overnight the orchestrator sent reminders for everything inside 30/14/7/3 days and flagged 9 inside the 7-day window still missing evidence. Founder A opens the dashboard at 8:30am: 18 requirements need human action — 6 evidence packages ready for specialist QC, 9 owners who haven't uploaded despite three nudges, 3 new carrier letters from yesterday needing parsing. The 3 letters go through intake (software OCRs/pre-extracts, human confirms each — a misread requirement that fails the carrier is the catastrophic outcome), ~20 min/letter. The compliance specialist spends the morning on the 6 QC packages (~30–40 min each, verifying a contractor invoice actually satisfies a "licensed electrician sign-off"); two bounce back to the owner, four go out. The 9 stalled owners are the grind: templated-but-personal email, and for the 3 inside 7 days an actual phone call — ~15 min/account, ~2.25 hrs; one needs the service to contact the owner's sprinkler vendor directly (authorization on file). Afternoon: Founder B onboards two new accounts (ingest backlog, build registers) — a messy portfolio with a 6-month backlog is 3–5 hrs. Breaks on a bad Tuesday: a carrier with a non-standard portal, an owner who goes dark on a deadline that lapses (reputation/liability), a genuinely ambiguous requirement the specialist guesses wrong. None are field-ops disasters — knowledge-work latency and judgment risks, survivable but real.

CAPACITY MATH
Income target (ladder): ~$600K combined ARR mo12; ~$1.0M+ mo24.
Pricing [ASSUMED]: anchor on account economics — blended ~$1,200–1,800/account/month ($14K–$22K ARR/account) reflecting existential coverage risk on financed real estate. Verify by quoting 15 owners.
Mo-12 (~$600K ARR): at ~$16K ARR/account → ~38 accounts; at thinner ~$6K → ~100 accounts. Reachable at ~40–110 accounts. Mo-24 (~$1.0M): ~60–170 accounts.
Delivery-labor constraint: [ASSUMED] ~1.5–3 active requirements/account/month (spiky around renewal). ~70 min skilled time/requirement (intake ~20 + QC ~30–40 + owner-chase ~15 on the ~30% that stall). At 100 accounts × 2 req/mo = 200 req/mo × 70 min = ~233 hrs/mo = ~54 hrs/wk. One specialist delivers ~30–32 productive hrs/wk → ~100 accounts needs ~1.7 FTE + founder oversight → round to 2 specialists. Onboarding ~4 hrs/account front-weighted. Mo-24 (~150 accounts) → ~3 specialists. At ~$1.0M ARR carrying ~3 specialists (~$220K loaded) + tooling, ample founder income. Bottleneck lands on QC/specialist labor — the right, hireable place.

SCORES (1–10)
1. Delivery clarity & repeatability: 7 — Documented requirement→evidence→QC→submit loop templatizes well; capped below 8 because carrier acceptability is judgment-laden and varies, so a maturing playbook is needed.
2. Supply chain resilience: 8 — Inputs are documents from the owner + cloud/OCR/LLM APIs; no MOQs/deposits/single-source vendor; only hard dependency is carrier portals (email-submittable in most cases).
3. Logistics tractability: 9 — Zero physical logistics: explicitly remote, no inspections/repairs/routing/install windows; 100% desk work against a national base — the structural opposite of field-ops.
4. Customer-ops scalability: 6 — Software handles deadlines/reminders/intake, but owner-chase and the white-glove "got it across the line" moment are inherently medium-touch; the promise forces a human safety-net per deadline.
5. Vendor/partner dependency risk: 7 — Main dependencies (AWS/OCR/LLM, carrier channels) diversified and substitutable; carrier process changes are an annoyance not a kill-switch (submission is email/portal document delivery).
6. Hiring feasibility: 8 — First hire is a remote compliance/document-coordination specialist at ~$60K–$85K loaded; deep pool (insurance-ops, paralegal, compliance-coordinator), far easier than licensed trades/field techs.
7. Throughput capacity at target: 8 — ~$1.0M ARR (~150 accounts, ~300 req/mo) needs ~3 specialists + 2 founders, ~80 specialist hrs/wk vs ~30 productive/FTE — comfortably lean, bottleneck is hireable QC labor.
8. Quality control simplicity: 6 — Failure mode (missed deadline / rejected package) is high-consequence and acceptability judgment is non-trivial, so QC needs a real human gate + growing knowledge base; standardizable over time, not low-variance day one.
9. Geographic / seasonality risk: 7 — National, remote, weather-neutral; mild seasonality around renewal cycles; hard-market urgency is broad, concentration risk low though tied to the insurance cycle.
10. Tooling maturity available: 6 — Deadline engine/intake/reminders/assembly buildable on off-the-shelf primitives, but no turnkey product covers this loop — founders build the orchestration layer (within ability, not buy-and-go).

AVERAGE SCORE: 7.2 / 10

TOP 3 OPERATIONAL STRENGTHS
- Genuinely no field operations: remote document/evidence work, no inspections/repairs, eliminating routing/trucks/install windows/density problems (9 on logistics).
- Lean hireable team: ~$1.0M ARR carried by 2 founders + ~3 remote specialists at ~$60–85K each, a deep affordable pool (8 on throughput/hiring).
- Software does the unglamorous heavy lifting, concentrating scarce human time on the two high-value steps (QC review, owner escalation) where price is justified.

TOP 3 OPERATIONAL RISKS
- The owner is the bottleneck: the service can't manufacture evidence the owner won't supply; a non-responsive customer who then misses a deadline creates a "you failed me" event though the failure was theirs.
- QC variability and acceptability judgment: deciding whether evidence satisfies a specific carrier's ask is non-trivial and high-consequence until a knowledge base matures.
- Carrier/channel heterogeneity: every carrier formats letters and accepts submissions differently; non-standard portals resist automation and raise per-requirement time.

BIGGEST SINGLE RISK
The gap between the promise and the dependency: the offer is "never lose your coverage to a missed insurer requirement," but the most common reason requirements lapse is that the owner doesn't produce the evidence in time — the exact input the service does not control. The business is a managed loop wrapped around a customer who is distracted, scattered, and disorganized about this work. The service inherits responsibility for an outcome whose critical input lives with the least reliable party. The human-escalation step is load-bearing and scales with the messy tail, not with revenue. If underestimated, per-account labor blows past the model, two specialists become four, margins compress, and a few "they still let my policy lapse" failures poison the word-of-mouth a marketing-led GTM depends on. Survivable with clear contractual scoping ("we manage and chase; final responsibility to supply evidence is yours"), aggressive nudging, and authorized vendor-direct retrieval — but must be designed for from day one.

QUESTIONS THE FOUNDERS MUST ANSWER
- Real average frequency and variance of carrier loss-control requirements per managed property per year? Verify by pulling 12 months of letters from 3–5 carriers or 10 owners.
- How standardizable is the QC/acceptability judgment — checklist-driven knowledge base a $70K specialist runs, or senior insurance/loss-control expertise at $120K+?
- How will you contractually/operationally handle the owner failing to supply evidence and a deadline lapsing — SLA, liability scope, escalation ladder?
- What fraction of target carriers accept document submission by portal/email vs require a controlled integration, and how much time does the non-standard tail add?

RECOMMENDATION: GO
Operationally clears the bar. The rare "property" concept with no field operations, no physical supply chain, no routing, and a loop two founders + a small affordable remote team can run — capacity math reaches ~$1.0M ARR with ~3 specialists, bottleneck on hireable QC labor not founders. Execution risks are ordinary knowledge-work risks (owner non-responsiveness, QC variability, carrier heterogeneity), all manageable. One non-negotiable design requirement before launch: harden the owner-dependency boundary (SLA, liability scope, authorized vendor-direct evidence retrieval) so "never lose coverage" is achievable rather than an open-ended commitment. With that designed in, two people can operate this.
