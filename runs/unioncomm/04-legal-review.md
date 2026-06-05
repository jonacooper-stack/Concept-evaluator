LEGAL / REGULATORY REVIEW — Member Engagement & Dues-Collection Overlay for Labor Unions

Not formal legal advice. I am an experienced operator with strong regulatory pattern-recognition, flagging issues the founders must take to retained counsel. Nothing below should be relied on as a legal opinion.

ONE-PARAGRAPH RISK READ

This is a B2B SaaS-plus-payments overlay sold to a non-regulated-as-an-industry buyer (labor unions), which is the good news: there is no licensing regime that gates selling software to unions, and the founders' background does not collide with any credentialing requirement. The bad news is that the revenue model deliberately lives in two of the most regulated corners of American consumer law at once — (1) high-volume A2P SMS messaging into members' personal cell phones, which puts the platform squarely under the TCPA and CTIA/carrier 10DLC rules, and (2) a payment-processing take-rate on dues collected via card and ACH, which makes the company a money-flow intermediary subject to PCI-DSS, NACHA, card-network rules, and potentially money-transmission analysis depending on how funds are structured. Layered on top is the fact that the underlying transaction — union dues authorization — is itself the subject of active, contested, fast-moving post-Janus litigation and state legislation, so the very "renewal/authorization capture" workflow the product sells is a legal artifact that must be defensible, auditable, and revocable. Manageable for founders with prior SOC 2/HIPAA/GDPR experience, but the payments + TCPA exposure is real and must be architected correctly from day one, not bolted on.

REGULATORY MAP

- TCPA (Telephone Consumer Protection Act), 47 U.S.C. 227, enforced by FCC + a massive private plaintiffs' bar via a statutory-damages private right of action ($500–$1,500 per message). Scope: the platform sends SMS, including potential renewal/dues reminders, to members' personal cell phones. This is the single largest litigation-risk surface in the concept. Burden: high and ongoing — prior express consent (and for any marketing content, prior express written consent) must be captured and logged per recipient; honoring opt-outs (STOP) in real time is mandatory. Class actions here routinely settle in the seven-to-eight figures.

- CTIA Messaging Principles + 10DLC registration (The Campaign Registry, run through carriers/aggregators like Twilio/Bandwidth). Scope: any A2P SMS at volume must be brand- and campaign-registered; political/advocacy and "membership" content gets carrier scrutiny, and union/political messaging is a sensitive category that aggregators police. Burden: moderate, mostly operational — registration, throughput limits, content filtering risk.

- CAN-SPAM Act, 15 U.S.C. 7701, enforced by FTC. Scope: the email side (national→local hierarchical email). Burden: low — header accuracy, physical address, functional unsubscribe. Easy to build in.

- PCI-DSS (card-network standard, contractually enforced by acquirers/Visa/Mastercard). Scope: the platform takes a take-rate on card-collected dues. Burden: moderate-to-low IF the founders use a tokenized processor (Stripe/Adyen/Finix) and keep cardholder data out of their environment (SAQ-A scope). High if they ever touch raw PAN data. The founders' SOC 2 experience is directly transferable.

- NACHA Operating Rules (ACH network) + the card network rules. Scope: ACH direct-debit dues collection. Burden: moderate — authorization capture for recurring debits, return/NOC handling, Nacha's WEB-debit account-validation requirement. Recurring ACH "subscription"-style debits carry chargeback/dispute and unauthorized-return exposure.

- State money-transmitter licensing (state banking departments; ~49 states + DC). Scope: THIS IS THE CRITICAL FORK. If the platform merely facilitates payment through a licensed processor and funds settle directly from member to the union's account (processor is merchant of record / union is the merchant), the company is most likely an agent/facilitator and NOT a money transmitter. If the company takes custody/control of dues funds and remits them onward to the union, it risks being deemed a money transmitter, triggering MTL in up to ~49 states (six-figure-plus aggregate cost, bonding, multi-year). The architecture decision determines whether this is a non-issue or a company-killer.

- FTC ROSCA / state automatic-renewal laws (California ARL, NY GBL 527-a, and a growing list). Scope: dues collected as recurring auto-debits from individual members are consumer recurring charges; the member is a natural person being charged on a recurring basis. Burden: moderate — clear disclosure, affirmative consent, and easy cancellation are required and vary by state. Even though the buyer is a union, the charged party is a consumer, so consumer-subscription law is in play.

- State data-privacy laws (CCPA/CPRA in California; plus VA, CO, CT, etc.). Scope: the product's entire value prop is capturing and storing members' personal cell numbers and personal emails — personal information of (often) hundreds of thousands of consumers. Burden: moderate — the company is likely a "service provider"/processor to the union (controller), so a solid DPA pushes most obligations correctly, but breach exposure on a large PII honeypot is real.

- Janus v. AFSCME (2018) and downstream state legislation (e.g., dues-authorization and revocation statutes in CA, NY, WA, NJ, and contrary "paycheck protection" laws in other states). Scope: this is not a regime the company is regulated BY, but the legal validity of the authorizations the product captures depends on state-specific rules about how dues consent must be obtained, worded, witnessed, and revoked. Burden: indirect but important — the product is selling the authorization artifact, so it must be configurable to each state's rules and must produce defensible, timestamped, auditable consent records.

- Labor-law adjacency (NLRA for private-sector unions; state PERA-equivalents for public-sector). Scope: the company is a vendor, not a labor-law actor, so direct exposure is low, but messaging content and dues-handling sit near union-governance rules.

LICENSING SUMMARY

No occupational or industry license is required to sell software to labor unions; unions are not a licensed-counterparty category, and the founders need no credential to serve them. The one licensing question that actually matters is money-transmitter licensing, and whether it applies is entirely an architecture choice, not an inherent property of the business. If the company structures payments so it never takes possession or control of dues funds — i.e., it integrates a licensed processor (Stripe, Adyen, Finix, or a payfac partner) where the union is the merchant of record and funds settle member-to-union, with the company earning a referral/platform share of the processing margin — then no MTL is required and this stays a paperwork-light SaaS. If instead the company aggregates dues into its own account and remits to unions, it likely triggers MTL across ~49 states + DC (each with its own application, surety bond, net-worth and reporting requirements; aggregate cost easily $150K–$500K+ and 18+ months), plus federal FinCEN MSB registration. Strong recommendation: contract with a regulated payments partner and stay off the money-transmission rail entirely. There are no per-state operator exams, no continuing education, and no professional licensure in this concept.

LIABILITY POSTURE

The dominant exposure is TCPA statutory-damages litigation. Because damages are per-message and there is an aggressive plaintiffs' bar, a single mis-scoped SMS campaign — texts sent without provable prior express consent, or failure to honor an opt-out — can generate class exposure that dwarfs revenue. The platform must treat consent capture and STOP-handling as load-bearing infrastructure, and the customer contracts must contractually push responsibility for the legality of recipient lists onto the union (the union supplies/controls the membership list and asserts consent) while the platform supplies the opt-out plumbing and audit trail. The second exposure is data-breach liability on a large consumer-PII honeypot (cell numbers, personal emails, and payment metadata of potentially millions of members across clients); this is insurable via cyber/tech-E&O at moderate premiums for a SOC 2-credible shop, and most statutory obligation is correctly allocated by being the union's service provider/processor under a DPA. The third is payments dispute/chargeback and unauthorized-return exposure, largely transferred to the processor partner if the company is not the merchant of record. Pre-entity, the founders carry personal exposure on all contracts and any consent/messaging misstep, so forming the entity (Delaware C-corp or LLC) and routing all contracts through it before sending a single text or collecting a single dollar is non-negotiable. Insurance stack: tech E&O / cyber, plus general liability; D&O once revenue is meaningful. Net leftover risk after good architecture and contracts: TCPA tail risk (real but manageable with rigorous consent logging) and reputational/political risk of being a vendor in a politically charged, litigated space (some clients and some carriers may balk at union/political messaging).

SCORES (1–10) (higher = lower risk)

1. Industry regulatory burden: 7 — Selling software to unions is not a licensed/regulated industry; the burden comes from the payments and TCPA overlays the company chooses to operate in, not from the union vertical itself (no NLRA/PERA licensure on a vendor).

2. Licensing requirements: 6 — No occupational license needed, but money-transmitter licensing under ~49 state banking codes looms IF the fund-flow is structured wrong; capped at 6 because the founders must affirmatively architect around it rather than ignore it.

3. Data privacy exposure: 6 — Large consumer-PII honeypot (personal cell + email of potentially millions) under CCPA/CPRA and peer state laws; manageable as a union's service provider under a DPA, but breach magnitude keeps this off a high score.

4. Employment & contractor risk: 9 — Remote software team, no field workers, no 1099 misclassification surface, no in-home entry; the only real obligation is standard IP-assignment from any contractors. This is genuinely low under standard W-2/true-1099 norms.

5. Consumer protection complexity: 4 — The charged party is a natural person on recurring auto-debits, squarely invoking FTC ROSCA plus California's ARL (Bus. & Prof. Code 17600) and New York GBL 527-a-style auto-renewal laws, AND high-volume SMS under the TCPA; this stacked consumer-law exposure is the weakest dimension.

6. IP cleanliness: 7 — Original software; main dependencies are an SMS aggregator (Twilio/Bandwidth) and a payments processor (Stripe/Adyen) under standard commercial terms, plus read/write integration into legacy union databases (UnionWare, Union Link) that should be done via supported export/API or customer-authorized access, not scraping; clean if integration is contractually permissioned.

7. Contract simplicity: 5 — Not clickwrap: national/state union deals are negotiated MSAs with DPAs, security addenda, and data-ownership terms, and the union must contractually own the legality of its membership/consent lists; a meaningful but routine B2B contracting motion.

8. Liability exposure: 5 — TCPA per-message statutory damages ($500–$1,500/text, 47 U.S.C. 227) create real class-action tail risk, and a large PII honeypot adds breach exposure; insurable and contractually allocable but not a low-risk profile.

9. Jurisdictional simplicity: 5 — Operates nationally, and several burdens (state auto-renewal laws, state privacy laws, state dues-authorization/revocation statutes post-Janus, potential MTL) multiply state-by-state with genuine cliffs in CA/NY/IL/WA rather than scaling linearly.

10. Regulatory trajectory: 5 — Mixed and active: TCPA rules are tightening (FCC's 2024–2025 consent/revocation and one-to-one consent activity), state privacy and auto-renewal laws are proliferating, and post-Janus dues litigation/legislation is live and politically contested; the environment is moving, not stable.

AVERAGE SCORE: 5.9 / 10

TOP 3 LEGAL/REGULATORY STRENGTHS

- No industry licensure or founder credential gate: selling software to unions requires no occupational license, no exams, and no specialized legal credential, so nothing collides with the founder profile.
- Clean employment/operations posture: a remote software team with no field workers, no in-home entry, and no 1099 misclassification surface earns a genuinely high mark (dimension 4 = 9).
- Money-transmission risk is avoidable by design: routing all funds through a licensed processor with the union as merchant of record keeps the company off the MTL rail entirely, converting a potential 49-state nightmare into a non-issue.

TOP 3 LEGAL/REGULATORY RISKS

- TCPA per-message statutory-damages litigation on high-volume SMS — the single largest dollar exposure, with an aggressive plaintiffs' bar and class-action history.
- Stacked consumer-subscription law (FTC ROSCA + California ARL + NY/other state auto-renewal statutes) on recurring auto-debits charged to individual members, who are consumers regardless of the union being the buyer.
- Architecture-dependent money-transmitter exposure: if dues funds ever flow into the company's control, ~49-state MTL + FinCEN MSB registration becomes a launch-blocking, capital-heavy obligation.

BIGGEST SINGLE RISK

The biggest single risk is TCPA exposure on the SMS channel. The product's core revenue and core value both depend on sending high volumes of text messages to members' personal cell phones, and the TCPA (47 U.S.C. 227) attaches statutory damages of $500 to $1,500 per message with a private right of action and a sophisticated, well-funded plaintiffs' bar that specializes in turning consent gaps into class actions. The danger is structural: the membership lists are supplied by unions whose post-Janus data is admittedly incomplete and messy, consent provenance is exactly what is missing, and a single national rollout could push millions of texts before anyone has verified that each recipient gave prior express consent and that every STOP request is honored in real time. A platform that automates this at scale is the perfect defendant — deep enough to be worth suing, central enough to be named alongside its union clients. This is survivable only if consent capture, consent logging, opt-out propagation, and per-campaign content classification (transactional vs. marketing vs. political/advocacy) are built as first-class, auditable infrastructure from day one, and if the customer contracts squarely allocate list-legality to the union while the platform provides the compliance plumbing. Get this wrong and a single settlement can exceed a year of revenue; get it right and it becomes a defensible moat that sleepy incumbents lack.

QUESTIONS FOR REAL COUNSEL BEFORE LAUNCH

1. Money transmission: Under our intended fund-flow (member → processor → union account, company takes a platform share of processing margin), do we avoid money-transmitter licensing in all 50 states and FinCEN MSB registration? What exact contractual and settlement structure with our processor (Stripe Connect / Adyen / Finix / payfac) keeps us a facilitator and not a transmitter, and where is the line we must never cross?

2. TCPA program design: What is the minimum defensible consent-capture and opt-out architecture for transactional vs. marketing vs. political/advocacy SMS to members? How do we contractually and technically allocate liability between us and the union for the legality of member lists, and what consent records must we store to survive a class action?

3. Consumer auto-renewal law: Do FTC ROSCA, California's ARL (Bus. & Prof. Code 17600 et seq.), and New York GBL 527-a apply to recurring dues auto-debits where a union is our customer but the charged party is an individual member? What disclosure, affirmative-consent, and cancellation flows must we build to comply across the strictest states?

4. Post-Janus dues authorization: How must the digital re-sign/renewal workflow be configured per state so that the dues authorizations we capture are legally valid, properly worded, and revocable, and so our audit trail is admissible if a member later disputes the deduction?

5. Data role and breach: Are we a "service provider"/processor under CCPA/CPRA and peer state laws with the union as controller, and does our standard DPA correctly allocate breach-notification and consumer-rights obligations for a multi-million-record consumer-PII dataset?

6. Integration rights: Is read/write integration into UnionWare and Union Link permissible via supported APIs/exports under our customers' licenses, or does it risk tortious-interference or terms-of-service claims by those incumbents?

RECOMMENDATION: GO (conditional / REFINE on payments architecture)

The legal posture is acceptable and the risks are knowable rather than fatal, but only if two structural decisions are locked before launch. First, the payments architecture must route all dues funds through a licensed processor with the union as merchant of record so the company never takes custody of funds — this single design choice is the difference between a paperwork-light SaaS and a 49-state money-transmitter-licensing trap, and it must be confirmed with counsel and the processor before a dollar moves. Second, the TCPA/consent stack and consumer auto-renewal flows must be built as first-class infrastructure from day one, with per-recipient consent logging, real-time opt-out, and contractual allocation of list-legality to the unions. With those two conditions met, nothing here requires a credential the founders lack, the employment/IP/contract surface is routine, and the founders' SOC 2/HIPAA/GDPR background maps directly onto the PCI-DSS and CCPA obligations. The political/litigated nature of the post-Janus dues environment is a feature for market pull but a reputational and regulatory-trajectory watch-item, not a blocker. Proceed, but treat "facilitator-not-transmitter" and "consent-as-infrastructure" as gating launch requirements, not later cleanup.
