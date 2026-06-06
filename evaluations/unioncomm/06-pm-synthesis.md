SYNTHESIS — Member Engagement & Dues-Collection Overlay for Labor Unions
Date: 2026-06-06
Council members reviewed: CFO, CMO, COO, Legal/Regulatory, CTO

ONE-PARAGRAPH PM READ
This is a genuinely strong wedge wrapped around a genuinely hard go-to-market and a legal posture that is binary on a single architecture choice. The must-have is real and rare: when a state flips right-to-work / paycheck-protection (or post-Janus for all public-sector locals), affected unions face an existential, deadline-driven collapse of their dues pipeline — that is a painkiller already budgeted, not a vitamin. The product is buildable from boring primitives by these founders, capital-light, and remote-first, which fits the founder profile cleanly. But three things stand between the thesis and the income ladder, and they are not independent: (1) buyer access and trust into an insular, politically suspicious institution that two tech founders with no labor pedigree get screened out of; (2) a legal surface (TCPA mass-texting + payments/money-transmission) where one wrong architecture choice or one defective-consent text blast is a multi-million-dollar event; and (3) two unverified economic numbers — retained take-rate spread and digital-adoption depth — whose product governs whether each signing is worth $120K/yr or ~$24K/yr. The honest call is REFINE, not GO: the legal and customer-truth gaps are de-riskable but currently unevidenced, and no founder has yet talked to a secretary-treasurer.

SCORE SUMMARY
- Objectives scorecard weighted total (orchestrator, see 07-objectives-scorecard.md): 69 / 100
- CFO average:    7.1 / 10
- CMO average:    6.9 / 10
- COO average:    6.8 / 10
- Legal average:  5.1 / 10
- CTO average:    6.8 / 10
- MEAN OF THE FIVE: 6.54 / 10 (pre-red-team) → 6.48 / 10 (post-red-team)
- SINGLE LOWEST SUB-SCORE ANYWHERE: 3 — Legal: Consumer protection complexity (3) and Jurisdictional simplicity (3), tied at the floor of the packet.

RED-TEAM (mandatory)
Took the four highest sub-scores in the packet and argued each is one point too high. Three of four challenges land; one survives.
1. COO Logistics tractability = 9 → 8. A 9 ignores the money-movement operational drag (45 ACH returns/business-day, KYC, chargebacks, reconciliation) the same reviewer flags two paragraphs later. LANDS. COO recomputed average 6.7.
2. Legal Employment & contractor risk = 9 → 8. Defensible only on the narrow reading "the founders' OWN structure is clean"; as a read of labor/employment risk in a product that touches NLRA dues-authorization mechanics, 9 is too high. LANDS. Legal recomputed average 5.0.
3. CFO Startup capital efficiency = 9 → held. Dollar-cost genuinely is low; the high cost is time-to-revenue, which CFO already books elsewhere (Cash flow 7, Path 6). Double-penalizing would be unfair. SURVIVES.
4. CMO Competitive air = 8 → 7. The seam is real today but the moat is thin: incumbent MMS vendors hold the DB of record and trust relationship and can bolt on payments; Action Network can add dues. No structural lock-in beyond first-mover. LANDS. CMO recomputed average 6.8.
Post-red-team: CFO 7.1, CMO 6.8, COO 6.7, Legal 5.0, CTO 6.8. MEAN 6.48.

WHERE THE EXPERTS AGREE
- The wedge is a real must-have, not a vitamin (CFO, CMO, structure of the trigger event).
- The build is tractable and founder-fit (CTO 8 feasibility / ~12-18 dev-weeks, COO no field ops, CFO capital-light).
- Two hotspots named identically by COO and CTO: heterogeneous legacy-DB integration and the burden of being a money-and-PII custodian.
- Everything dangerous is structurally avoidable (Legal/CTO): facilitator no-funds-held architecture + day-one TCPA consent.

WHERE THE EXPERTS DISAGREE
- Legal (5.1) vs CFO/CMO upside: same feature (take-rate on member-paid dues via mass-texted payment links) is both the revenue engine and the catastrophic tail. Legal's frame GATES CFO's frame — the upside is only real if the architecture/consent conditions are met first.
- CMO Customer truth = 5 vs the GO-leaning packet: zero evidence any founder has spoken to a secretary-treasurer; the other four reviews implicitly assume the door opens. CMO's frame is load-bearing for whether this gets a first customer at all.
- COO Logistics 9 vs COO's own payment-ops narrative (resolved in red-team). Integration-variance is the swing between "lean overlay" and "high-touch grind"; unresolved until 2-3 real integrations are attempted.

TOP 5 RISKS (RANKED)
1. Buyer access and trust (CMO; COO secondary) — gates revenue entirely. Reduce with a labor-side advisor on the cap table, one marquee international design partner, and 10 real buyer interviews first.
2. TCPA mass-texting liability (Legal) — $500-$1,500/message, class-action; catastrophic severity, controllable probability. Reduce with documented express written consent at capture, A2P 10DLC, counsel sign-off before first blast.
3. Retained take-rate × adoption depth (CFO) — if low/low, per-body revenue is ~1/5 of the example and the ladder needs 25-30 signings. Reduce by modeling PayFac/Interchange-Plus and pressure-testing take-rate vs flat per-member fee.
4. Money-transmitter architecture binary (Legal; CTO) — facilitator = viable, settle-funds = fatal. Reduce by committing to Stripe Connect settle-to-union day one + a fintech-counsel memo.
5. Integration variance becoming a services grind (COO; CTO) — erodes margin/scalability. Reduce by proving one templatized importer against 2-3 real union DB exports.

TOP 3 STRENGTHS
- Rare, genuine must-have with a discrete forcing event (RTW/paycheck-protection flip, Janus exposure).
- Sticky, recurring, take-rate revenue on a mission-critical money flow with near-zero working capital.
- Clean founder/operations fit: capital-light, remote-first, no field ops, ~12-18 dev-weeks, compliance background directly relevant.

THE BIGGEST OPEN QUESTION
Will union leadership — specifically a state/international secretary-treasurer — actually buy a member-paid digital dues rail from two outsider tech founders, at a take-rate, and mandate it down to locals? Every favorable number in the packet assumes yes; no reviewer has evidence. This collapses two sub-questions: (a) does the door open at all to founders with no labor pedigree, and (b) if it opens, does a percentage-of-dues take-rate survive an institution culturally primed to see "a fintech skimming our members' dues" as a betrayal — or must it become a flat per-member SaaS fee, which rewrites the CFO economics? Answer with 10 real interviews and one signed design partner.

RECOMMENDATION: REFINE (NEAR-MISS against the bar)
- Objectives weighted total 69/100 — below the 70 advance line, in the 55-69 "refine and rescore" band.
- Post-red-team mean of the five is 6.48 — good on build and wedge, dragged by Legal (5.0) and customer-truth (5).
- Lowest sub-score in the packet is 3 (Legal: consumer protection, jurisdictional). Against the active finalist/winner bar (mean > 8.0, no sub-score < 7, objectives >= 80) this is a clear FAIL — and an honest one. It misses on de-riskable items, not a fatal structural flaw, which is exactly what REFINE is for. Not softened to GO: there is no buyer evidence and an unresolved catastrophic-tail legal surface.

THE 3-5 CHANGES THAT WOULD MOVE IT TO GO
1. Prove buyer access and price model (CMO): 10 real secretary-treasurer interviews; pressure-test take-rate vs flat per-member fee; recruit a named labor-side advisor. Verify: >=2 credible "I would pilot this" + clear pricing read.
2. Lock the legal architecture in writing (Legal): commit to Stripe Connect facilitator/no-funds-held; fintech-counsel memo confirming no money-transmitter trigger.
3. Build TCPA-grade consent before any send capability (Legal): per-number express written consent + A2P 10DLC as a non-negotiable gate; counsel sign-off.
4. De-risk the two governing economic numbers (CFO): model PayFac/Interchange-Plus retained spread; capture real adoption-depth estimate from interviews.
5. Prove integration templatizes (COO/CTO): one importer, three real union DB sources, no custom code per source.
Target re-review date: 2026-08-08.

NEXT STEPS
- Run 10 leadership interviews; pressure-test pricing. Due 2026-07-18.
- Recruit one labor-side advisor onto the cap table. Due 2026-07-25.
- Obtain written no-money-transmission memo (Stripe Connect facilitator). Due 2026-07-25.
- Design TCPA consent + A2P 10DLC flow; counsel sign-off. Due 2026-08-01.
- Secure 2-3 sample union DB exports; build/test one templatized importer. Due 2026-08-01.
- Re-convene council on the refined concept. 2026-08-08.

VERDICT IN ONE LINE: NEAR-MISS — REFINE. Post-red-team mean 6.48/10, objectives total 69/100, lowest sub-score 3 (Legal). Misses the bar on de-riskable items (buyer evidence, legal architecture, two economic unknowns), not on a fatal structural flaw.
