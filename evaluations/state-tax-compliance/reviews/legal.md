LEGAL / REGULATORY REVIEW — Multi-State Compliance Dashboard
(Not formal legal advice — operator pattern-recognition flagging issues for real counsel.)

ONE-PARAGRAPH RISK READ
One of the cleaner regulatory postures a B2B SaaS can have: informational/workflow software telling companies about their OWN obligations — it does not become a licensed tax preparer, registered agent, or law firm so long as it stays on the right side of the unauthorized-practice-of-law (UPL) line and frames output as software-generated information, not legal/tax advice. Two material exposures: (1) UPL and accountant/tax-advice liability if "guided workflows and plain-language explanations" drift into advising on tax positions; (2) accuracy/reliance liability — a wrong "green" the customer relied on. Both are contractually/structurally manageable (disclaimers + E&O + "we surface, you/your accountant decide"); the done-for-you filing add-on is the one piece that meaningfully raises licensing and liability stakes and should be ring-fenced or partnered out.

REGULATORY MAP
- UPL — state bars / UPL statutes (all 50; e.g., Cal. Bus. & Prof. Code §6125-6126, Tex. Gov't Code §81.101). Advising legal positions ("you have nexus here," "you must foreign-qualify") can be construed as practicing law. Janson v. LegalZoom (W.D. Mo. 2011, settled) established self-help software tools are largely permissible if they don't exercise legal judgment for the user. Central design constraint, not a blocker.
- Unauthorized practice of accountancy / tax-advice — state boards + IRS Circular 230. Computing/preparing/filing returns implicates state CPA regulation and federal preparer rules (PTIN, Circular 230). Low if surfacing only; rises sharply if done-for-you files returns.
- Registered-agent regulation — Secretaries of State; Model Registered Agents Act (~14 states). Low-to-moderate; handled by partnering rather than becoming a CRA.
- Data privacy — CCPA/CPRA + ~19 other state laws. Ingests employee location PII, entity data, revenue-by-state. Standard B2B SaaS: DPA, reasonable security, deletion/access. No special category. Low if built in from day one.
- FTC ROSCA + state auto-renewal laws (e.g., Cal. B&P §17600; FTC click-to-cancel). Annual auto-renewing SaaS; low burden.
- GLBA — generally NOT triggered (not a financial institution). Check counsel if tax-payment money ever flows through the platform (avoid in v1).
- CAN-SPAM / TCPA — standard for B2B outbound; low.

LICENSING SUMMARY
Core product (dashboard, inventory, status lights, calendar, alerts, explanations): effectively NO license required — informational SaaS, only a home-state business license. Can launch with zero professional licensing.
Done-for-you add-on depends on WHAT is filed: annual reports, franchise reports, foreign-qualification, RA renewals are ministerial/clerical, routinely done by non-lawyers (CT Corporation, CSC, Harbor Compliance) — low licensing risk. Sales-tax returns and payroll registrations edge toward tax-preparer territory (PTIN/Circular 230; some state preparer rules) — clean path is to partner/white-label a licensed provider (CPA firm or Avalara/TaxJar). Do not become a commercial registered agent — resell/partner.

LIABILITY POSTURE
Dominant liability is accuracy-and-reliance: the whole value prop is "trust our red/yellow/green." A misclassification (no nexus when there is; green on a missed Delaware filing) → penalties, back taxes, lost good standing, and the customer argues the product caused it. Real and recurring but insurable/contractable: (a) Tech E&O / professional liability ($1-3M limits, low-five-figure premium early-stage); (b) customer agreement with "informational, not legal/tax advice; verify with your professional; as-is" disclaimer, limitation-of-liability capped at fees paid, indemnity — standard SaaS risk allocation (terms don't override statute but largely effective). "We surface, your accountant confirms" keeps the human professional decision-of-record. Pre-entity personal exposure solved by forming/capitalizing a C-corp/LLC. Done-for-you raises the stakes — pressing "submit" makes E&O concrete; needs tighter SLAs, its own rider, ideally a licensed filing partner sharing risk. Data liability modest: employee-state and revenue data are PII/confidential but not special-category.

SCORES (1–10) (higher = lower risk)
1. Industry regulatory burden: 7 — Lightly regulated informational SaaS; only real overlay is the UPL/tax-practice line, navigable via the Janson v. LegalZoom self-help precedent.
2. Licensing requirements: 8 — Core needs no professional license (only home-state business license); mirrors how Harbor Compliance/CSC do ministerial filings unlicensed. Licensing appears only in the tax-return add-on.
3. Data privacy exposure: 7 — CCPA/CPRA + ~20 state laws apply to employee-state/revenue data, but no HIPAA/biometric/children's; standard DPA + security suffices.
4. Employment & contractor risk: 8 — Founders' own posture is simple small team; product discusses customers' obligations but doesn't employ on their behalf, so misclassification risk sits with the customer.
5. Consumer protection complexity: 8 — Pure B2B; ROSCA + state auto-renewal apply but low-burden vs 50-state consumer subscriptions.
6. IP cleanliness: 7 — Original software + proprietary rules DB; some dependency on government data/resellers but no restricted-API chokepoint.
7. Contract simplicity: 7 — Clickwrap/standard MSA for SMB; mid-market five-figure deals want negotiated MSAs + DPAs + caps.
8. Liability exposure: 6 — Accuracy-and-reliance is genuine and recurring; insurable via Tech E&O and capped by LoL, but not eliminable, and done-for-you worsens it.
9. Jurisdictional simplicity: 6 — Vendor operates from one state, but product correctness depends on tracking 50 states' rules — the regulatory analog of operating in 50 states.
10. Regulatory trajectory: 8 — Favorable: post-South Dakota v. Wayfair (2018) economic-nexus expansion + state revenue-hunting steadily increase obligations, growing demand.

AVERAGE SCORE: 7.2 / 10

TOP 3 STRENGTHS
- Core is unlicensed informational SaaS with no founder credential requirement (confirmed by CSC/Harbor Compliance doing ministerial filings unlicensed).
- Regulatory trajectory is a tailwind (Wayfair nexus expansion keeps multiplying obligations).
- Pure B2B, no special-category data — lowest, most well-trodden burden tier.

TOP 3 RISKS
- UPL / unauthorized tax practice if explanations slide from information into advice (Cal. B&P §6125; Circular 230).
- Accuracy-and-reliance liability: a wrong green leading to a penalty is the natural lawsuit; insurable but inherent.
- The done-for-you add-on edges into tax-preparer regulation and concretizes E&O.

BIGGEST SINGLE RISK
Accuracy-and-reliance liability fused with the UPL/tax-advice line, because they compound. The promise is that a customer can trust a status light instead of a tax department — so the more useful and authoritative the product, the more it invites reliance, and the more a missed obligation looks like the product's fault. If founders try to be more helpful by telling customers what their obligation IS ("you have nexus in Texas, register now"), they drift toward UPL/unauthorized tax practice, where a bar/board complaint or a plaintiff's lawyer can argue the software exercised unlicensed professional judgment. The needle-threading solution exists (surface as information, human professional decision-of-record, disclaim, insure, cap) and Janson v. LegalZoom shows self-help tools survive when designed correctly — but it is a continuous design discipline as the product gets "smarter."

QUESTIONS FOR REAL COUNSEL
- Where exactly is the UPL/tax-practice line for our specific outputs — can we say "obligation X applies to you based on your data" as information, or is that advice in any state, and how should explanations be worded?
- For done-for-you, which filings are ministerial vs which cross into tax-preparer regulation, and where do we need a PTIN/Circular 230/licensed partner of record?
- Standard customer agreement contents (LoL cap at fees, as-is/no-warranty, informational-not-advice, indemnity) and enforceability given terms can't override statute?
- Tech E&O limits/riders for (a) software and (b) filing add-on, and what the carrier requires us to disclaim?
- Do we ever touch customer money (paying tax/fee on their behalf)? If so, money-transmitter/escrow/GLBA considerations to avoid in v1?
- For registered-agent functionality, must we register under any state's Model Registered Agents Act, or cleanly resell/partner?

RECOMMENDATION: GO — structurally clean B2B SaaS regulatory profile with a regulatory tailwind. Fold in one refinement-within-GO: ship the core as pure information ("we surface; your accountant confirms and files") and ring-fence the done-for-you add-on behind a licensed CPA/sales-tax partner. With that boundary + standard E&O/LoL/disclaimer contracting, the legal posture is comfortably acceptable for launch.
