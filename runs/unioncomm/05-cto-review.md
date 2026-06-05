CTO REVIEW — Member Engagement & Dues-Collection Overlay for Labor Unions

ONE-PARAGRAPH TECHNICAL READ

Technically this is a well-trodden build: a multi-tenant web app over Postgres, with email/SMS messaging via Twilio/SendGrid, Stripe (or Stripe + an ACH rail) for direct dues collection, hierarchical role-based access control, and a set of connectors into legacy union systems-of-record. None of the core capabilities are research problems — every piece is boring, off-the-shelf, and assemblable by a competent full-stack dev. The two genuine technical hazards are (1) the "integrates with the union's existing legacy membership database" promise, which is where a clean SaaS quietly turns into a per-customer integration-services business, and (2) becoming a money-movement and PII custodian for politically sensitive membership rosters, which raises the security and compliance bar well above a typical CRUD app. For a two-founder bootstrap with prior SOC 2/HIPAA/GDPR operating experience, this is feasible and the revenue-earning MVP is reachable in roughly 8–12 dev-weeks if the legacy-integration scope is deferred to manual import rather than live sync.

ARCHITECTURE SKETCH

- Frontend: Next.js (React) on Vercel for the staff/officer console; member-facing renewal and payment pages as lightweight server-rendered pages (mobile-first, since members open these from an SMS link on a phone). One thin codebase, no native mobile app needed at MVP.
- Backend: Node/TypeScript (or Python/FastAPI) API on a managed host (Render/Fly/AWS ECS). Multi-tenant with a tenant_id discriminator and row-level security in Postgres; strict tenant isolation is the load-bearing security decision.
- Data store: Postgres (managed — Supabase/RDS/Neon) for members, hierarchy nodes, roles, renewal records, dues transactions, message logs. The org hierarchy (national → state → district → local) is a tree with permissioned scoping — the trickiest data-model piece, but standard adjacency-list/closure-table work.
- Payments: Stripe for cards; Stripe ACH (or Dwolla/Plaid+ACH) for direct debit. Stripe Connect or a platform take-rate model so the founders skim a processing margin. This is the revenue spine and the highest-stakes integration.
- Messaging: Twilio (SMS, with 10DLC/A2P registration per tenant) + SendGrid/Postmark (email). SMS markup is the second revenue stream. Async delivery via a job queue (BullMQ/SQS) with webhook handling for delivery/opt-out status.
- Integrations: connectors to UnionWare / Union Link / homegrown DBs. At MVP this should be CSV import/export, NOT live bidirectional sync — live sync against undocumented legacy schemas is where weeks disappear.
- Auth: managed identity (Auth0/Clerk/Cognito) with RBAC mapped to the org tree; SSO deferred to when a national body demands it.
- Async/background: scheduled renewal-link campaigns, dunning/retry on failed ACH, message fan-out, webhook ingestion. Real complexity hides in (a) the permission tree and (b) reconciling money + dues records across tiers.

BUILD PLAN TO REVENUE-EARNING MVP

Estimate: ~8–12 weeks of one focused developer to a version a small union local will actually pay through, ~16–20 weeks with two paying tiers and polish. Chunks in order:

1. Tenant + hierarchy + RBAC + member data model, with CSV import (2–3 weeks). This is the spine; get tenant isolation and the org tree right first.
2. Digital renewal/onboarding workflow — tokenized renewal links, contact-capture forms, e-signature/affirmative-consent record with audit trail (2 weeks). This is the actual wedge and where conversion is won or lost.
3. Dues collection — Stripe card + ACH, take-rate logic, failed-payment dunning, receipts, reconciliation ledger (2–3 weeks). Money movement; do not rush this.
4. Messaging — Twilio SMS + email, opt-out/consent handling, 10DLC registration flow, markup metering (1.5–2 weeks).
5. Officer console + reporting + role-scoped dashboards (1.5–2 weeks).

Punt to v2: live bidirectional legacy-DB sync (keep CSV at launch), native mobile apps, advanced segmentation/automation, multi-language, SSO. The single biggest scope-control discipline is refusing to build live UnionWare/Union Link connectors for the first few customers.

CRITICAL ASSUMPTIONS

- "Overlay integrates with the legacy system of record." [ASSUMED] If customers demand live sync on day one, MVP slips from ~10 weeks to a quarter-plus of bespoke integration work per vendor. Verify cheaply: ask 5 target unions whether a nightly CSV import/export is acceptable for v1 — most legacy admins already export CSVs.
- A2P/10DLC SMS deliverability for political/union messaging is reliable and not throttled. [ASSUMED] Carriers scrutinize political and "membership/advocacy" SMS; campaign registration can be slow or rejected. Verify: register one 10DLC campaign now and send test political-adjacent traffic; confirm throughput and rejection rates before promising SMS as a revenue line.
- A payment processor will underwrite dues collection for unions at scale and not freeze funds. [ASSUMED — moderate risk] Stripe can be skittish about platforms moving member money for political organizations; an account freeze would be existential for the customer. Verify: confirm acceptable-use with Stripe/Dwolla underwriting in writing before signing the first union, and design for processor portability.
- The "free tier mandated top-down, then monetize transactions" GTM produces enough dues/SMS throughput to hit revenue. [ASSUMED] This is more a business than a technical assumption, but it drives architecture: the system must meter usage and take-rate precisely from day one (billing/metering is not a v2 nicety here). Verify: model take-rate revenue against real dues-per-member figures from 2–3 unions.
- ACH return/chargeback risk on recurring dues is manageable. [ASSUMED] Recurring ACH from individuals carries return rates and dispute handling that must be built in, not bolted on.

INFORMATION SECURITY POSTURE

This system holds a uniquely sensitive dataset: rosters of union members with personal cell numbers and emails, plus financial/payment data and records of who affirmatively (re-)signed. Union membership is politically charged; a breach is not just a PII incident, it is a list of identified union members exposed to employers or hostile parties — a meaningfully higher reputational and even physical-safety threat model than ordinary B2B SaaS. Controls required at launch (not later): encryption in transit (TLS) and at rest (managed-DB encryption), secrets in a manager (AWS Secrets Manager/Doppler) never in code, strict multi-tenant row-level isolation with automated tests proving cross-tenant queries fail, RBAC mapped to the org tree (a local officer must not read another local's roster or another tier's data), full audit logging of access to PII and money movement, MFA for all staff/officer accounts, and PCI scope minimization by keeping card data inside Stripe (tokenization, never touch PANs). Member-facing PII should be reduced to what conversion requires. Incident response: a written plan and breach-notification process are needed before the first roster is loaded, given state data-breach laws and the political stakes. The founders' stated SOC 2 Type II / HIPAA / GDPR operating experience is a genuine asset here — SOC 2 will be table-stakes the moment a national union body evaluates them, and they can design toward it from day one rather than retrofit. ACH/payments push them into needing clear PCI-DSS SAQ posture and money-transmission analysis (likely handled by riding Stripe/Dwolla as the regulated party, but must be confirmed).

SCORES (1–10)

1. Technical feasibility: 8 — Every component is proven, boring tech (Postgres + Stripe + Twilio + Next.js); no research problems, buildable by one strong full-stack dev in ~10 dev-weeks with CSV-import scope.
2. Build vs. buy posture: 8 — Payments (Stripe/Dwolla), SMS/email (Twilio/SendGrid), auth (Clerk/Auth0) are all bought; the only true custom code is the hierarchy/RBAC + renewal-conversion wedge, which is the right thin-wedge posture for a bootstrap.
3. Architecture cleanliness: 6 — Mostly clean, but the national→state→district→local permission tree plus per-tier money reconciliation and metering give it real moving parts beyond a simple CRUD app.
4. Time to revenue-earning MVP: 7 — ~8–12 dev-weeks to a payable MVP IF live legacy sync is deferred to CSV; the integration promise is the only thing that could push it to quarters.
5. Technical-assumption risk: 5 — Three external dependencies carry real, unverified risk: A2P/10DLC throttling of political SMS, processor underwriting/freeze risk on union money, and the legacy-integration scope creep — none are bet-the-company unsolvable, but all are unverified.
6. Third-party dependency risk: 5 — Stripe and Twilio sit squarely on both revenue rails, and both have acceptable-use sensitivity to political/membership organizations; an account action would directly break the business, mitigated only by designing for processor/carrier portability.
7. Data architecture quality: 6 — Data is owned and portable in Postgres and is genuinely a retention moat (the contact/renewal records the union lacks), but multi-tenant isolation of politically sensitive rosters is a leakage-prone failure surface that must be engineered carefully.
8. Information security posture: 7 — Founders' real SOC 2 Type II / HIPAA / GDPR operating experience plus a clear control set (tenant RLS, Stripe tokenization for PCI scope minimization, audit logging, MFA, secrets manager) make a defensible day-one posture realistic; the elevated political-list threat model keeps this from scoring higher.
9. Scaling headroom: 7 — Postgres + managed queue + Stripe/Twilio scale to millions of members and messages without rearchitecture; the metering/reconciliation ledger is the first thing to need attention at high transaction volume, not a rewrite.
10. Maintenance burden: 5 — Money movement (ACH returns, dunning, reconciliation), SMS deliverability/opt-out compliance, and (if ever built) legacy connectors are permanent operational surfaces that demand ongoing oncall attention from two founders.

AVERAGE SCORE: 6.4 / 10

TOP 3 TECHNICAL STRENGTHS

- Thin-wedge architecture: the hard, valuable parts (payments, SMS, auth) are all bought off-the-shelf, leaving only the renewal-conversion workflow and hierarchy RBAC as genuine custom code — ideal bootstrap shape, ~10 dev-weeks to revenue.
- The dataset it captures (members' personal contact info + affirmative renewal records) is exactly what unions are missing post-Janus, making the data itself a durable, owned, portable retention asset rather than a commodity.
- Founders' demonstrated SOC 2 Type II / HIPAA / GDPR operating experience directly de-risks the highest-stakes non-feature work (security and enterprise-audit readiness), which is usually the part bootstrap teams botch.

TOP 3 TECHNICAL RISKS

- Legacy-integration scope creep: "overlay that integrates with the existing system of record" can silently convert a clean SaaS into a bespoke per-union integration-services business unless v1 is disciplined to CSV import/export.
- Payment/SMS platform dependency on politically sensitive organizations: Stripe or Twilio acceptable-use action (freeze, throttle, campaign rejection) would directly sever a revenue rail and harm the customer; both revenue streams ride single, sensitive third parties.
- Multi-tenant isolation failure on politically charged membership rosters: a cross-tenant or cross-tier data leak here is not an ordinary PII bug but an exposure of identified union members, with outsized reputational/legal/safety consequences.

BIGGEST SINGLE RISK

The biggest single risk is not building the app — it is becoming the money-and-roster custodian for politically sensitive organizations atop third parties that can unilaterally cut you off. Both revenue streams (a take-rate on dues moved through Stripe/Dwolla and a markup on SMS sent through Twilio) sit on platforms with explicit, enforced acceptable-use sensitivity to political and membership organizations: A2P/10DLC carrier registration routinely throttles or rejects political/advocacy SMS, and payment processors are known to freeze or offboard platforms moving member money for politically charged groups, especially after a complaint or a media event. A freeze would not merely dent the founders' revenue — it would strand a union's dues collection mid-cycle, which post-Janus is the union's existential cash flow. Compounding this, the data at stake (a list of identified, dues-paying union members with personal contact info) makes any breach or processor dispute a high-visibility political event, not a routine SaaS incident. The technical mitigation is real but must be designed in from day one: confirm acceptable-use in writing with processors and carriers before the first customer, architect for processor and carrier portability (abstract the payment and SMS rails behind internal interfaces), and over-invest in tenant isolation, audit logging, and incident response from the first roster loaded.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE

- For v1, will customers accept nightly CSV import/export against their legacy system of record, or will they demand live bidirectional sync into UnionWare/Union Link on day one? (This single answer swings MVP timeline from ~10 weeks to a quarter-plus and determines whether this is a SaaS or an integration-services business.)
- Have you obtained written acceptable-use confirmation from a payment processor (Stripe/Dwolla) and an SMS provider (Twilio) that they will underwrite and not throttle a platform moving dues and sending messages for labor unions at scale — and what is the contingency if one offboards you?
- What is the precise legal/regulatory posture on money movement — are you strictly a platform riding Stripe/Dwolla as the regulated party (avoiding money-transmitter licensing), and what is your PCI-DSS SAQ scope, ACH-return handling, and chargeback model?
- How will you prove and continuously test multi-tenant and multi-tier isolation so a local officer can never access another local's or another tier's roster, given the elevated stakes of exposing identified union members?
- Is precise usage metering and take-rate billing being built into v1 (not v2), since revenue is entirely transaction- and volume-based and cannot be reconstructed retroactively if not metered from the first transaction?

RECOMMENDATION: GO

Technically this is a sound, well-scoped bootstrap build with a thin custom wedge over bought infrastructure, reachable to revenue in roughly 8–12 dev-weeks, and the founders' compliance-operator background covers the part most teams get wrong. The two things that keep it from a higher score are not feasibility but exposure: the legacy-integration promise must be ruthlessly scoped down to CSV for v1, and the business runs on two third-party rails (payments and SMS) that are unusually sensitive to political/membership customers, with a politically charged dataset that raises the breach blast radius. From a pure technology and security standpoint I recommend GO, conditioned on three de-risking steps before the first paying union: (1) verify CSV-import acceptability with 5 target unions, (2) get written processor and carrier acceptable-use confirmation plus a portability design, and (3) design tenant/tier isolation and audit logging in from day one. If the founders cannot secure processor acceptable-use, this tilts toward REFINE, because the entire revenue model rides on that rail.
