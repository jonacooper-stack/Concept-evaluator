# CTO REVIEW — SOC 1 Readiness Managed Service

ONE-PARAGRAPH TECHNICAL READ
A low-risk, well-trodden build: a compliance-evidence-management SaaS (control register, evidence-request workflow, reminders, audit-package assembly) wrapped around a human-reviewed managed service. None of the hard parts are research problems — the closest analogues (Vanta, Drata, Secureframe, AuditBoard, Hyperproof) prove the architecture is a standard multi-tenant CRUD-plus-workflow app with integrations and document storage. The real technical work is narrow: a structured control/evidence data model, a reliable scheduler/reminder engine, secure document handling, and a thin layer of read-only integrations to pull evidence automatically. The genuine risk is not feasibility but security posture and data sensitivity — this product collects evidence about a service org's controls over its customers' financial reporting, high-trust, sometimes PII/financial data, and the buyer is a CFO/controller who will themselves demand a credible security story. The software is a force-multiplier, not the moat; the moat is the controls expertise and the CPA-firm relationship — a GTM/skill question more than a CTO one.

ARCHITECTURE SKETCH
- Frontend: single multi-tenant web app (Next.js/React on Vercel, or Rails/Django monolith) — dashboards for control-register status, evidence-request queue, readiness scorecard, audit-package export. Two personas: service-org client and internal controls specialist.
- Backend: boring monolith (Postgres as system of record) modeling Organizations, Engagements (per audit window), Control Objectives, Controls, Evidence Requests, Evidence Items (versioned), Reviews, Audit Packages. The core custom wedge — ~60% of the build is this data model + workflow state machine.
- Document/evidence storage: object store (S3 with SSE-KMS) for evidence (screenshots, exports, policy PDFs, ticket extracts), strict per-tenant key/path isolation, immutable audit trail of who uploaded/reviewed what and when.
- Scheduler / reminders: background jobs (Sidekiq/Celery/Temporal or hosted queue) driving recurring evidence-collection cadences, nudge emails, SLA tracking. Reliability of the cadence engine makes the "continuous readiness" promise true.
- Integrations: read-only connectors to pull evidence "where available" — AWS/GCP config, GitHub/GitLab, Okta/Google Workspace, Jira, HRIS. The most variable and underspecified part; ranges from a handful of OAuth reads to an open-ended backlog.
- Auth: off-the-shelf (Auth0/Clerk/WorkOS) with SSO/SAML for enterprise tenants, RBAC separating client from reviewer, MFA mandatory.
- ML/AI: optional, non-load-bearing. An LLM could draft "management's description," map evidence to control objectives, or summarize gaps — useful but not bet on; humans review everything before it reaches a CPA. Keeping AI out of the critical path is correct.
- Hosting: standard PaaS/cloud (Vercel + managed Postgres + S3). No exotic infra. Complexity hides in integration breadth and evidence security/audit-trail rigor, not any algorithm.

BUILD PLAN TO REVENUE-EARNING MVP
~8-12 weeks of one experienced developer to a revenue-earning MVP, because first customers can be served with a thin product plus heavy human work and integrations punted.
1. Core data model + control register + evidence-request workflow (4-5 dev-weeks). The non-negotiable spine.
2. Document upload + secure storage + audit trail (1.5-2 dev-weeks). S3 SSE-KMS, per-tenant isolation, immutable log. In v1 because evidence is the product and security is the trust gate.
3. Scheduler/reminder engine + status dashboard + audit-package export (2-3 dev-weeks). Export can start as templated PDF/zip.
4. Auth + RBAC + MFA via Auth0/Clerk (0.5-1 dev-week). Bought, not built.
5. Automated integrations (PUNT to v2). First 3-10 customers manually upload or have the specialist pull evidence. Build connectors only after you know which systems recur — otherwise you burn weeks on an open-ended backlog before a dollar.
Revenue does NOT wait on the software: onboarding fee + first-year subscription earnable with a Notion/Airtable-grade workflow plus specialist labor while the real app is built in parallel. Time-to-first-dollar is the sales cycle, not the build.

CRITICAL ASSUMPTIONS
1. The "software" is a thin wedge; the moat is human controls expertise. Verify by mapping one real SOC 1 engagement end-to-end and listing every artifact — if 80% of value is specialist judgment, the build is small (good) but the labor model needs scrutiny (a COO/CFO concern).
2. Automated evidence integrations are "nice-to-have where available," not the core promise. If customers expect Vanta-grade auto-collection, the integration backlog balloons. Verify by asking 5 buyers whether they'd pay for managed readiness with mostly manual evidence upload in year one.
3. SOC 1 control sets are bespoke per org's financial-reporting role, not a fixed checklist like SOC 2's Trust Services Criteria. More configurability, less templating than SOC 2 tools. Verify by drafting control objectives for 3 service-org types (payroll admin, loan servicer, claims processor) and checking overlap.
4. The CPA relationship is a partnership/handoff, not a technical integration. Verify the data-exchange format CPAs accept (most want organized PDFs/spreadsheets, not API access) — confirms the export feature is simple.
5. No real-time/high-throughput requirement. Verify evidence cadences are daily/weekly/quarterly, not streaming — keeps the scheduler trivial.

INFORMATION SECURITY POSTURE
The single most important technical dimension here. Data: evidence about a service org's internal controls — access logs, change-management tickets, reconciliation screenshots, policy documents, potentially samples containing PII or financial data from the org's own customers. Lives in multi-tenant Postgres + S3. Threat model: a breach is catastrophic to the brand because buyers are CFOs/controllers buying a compliance product — you cannot sell "pass your audit" while failing your own. Launch controls (not later): TLS, S3 SSE-KMS + encrypted Postgres, strict per-tenant isolation, RBAC separating client/reviewer, mandatory MFA, secrets in a manager (never in env files committed to repo), comprehensive immutable audit logging of every evidence access/upload/review, least-privilege read-only scopes on every integration token, documented backup/restore. PII handling: minimize — instruct clients to redact customer PII from evidence samples, retention/deletion policy for any retained PII. Written IR plan and breach-notification from day one. SOC 2 implications: you'll be asked for your own SOC 2 Type II within the first handful of enterprise-ish deals — design controls in from day one to attain it in 6-9 months; dogfooding your own SOC 2 is both necessary and a marketing asset, and the founders' stated SOC 2 Type II operator background makes this genuinely bridgeable.

SCORES (1–10)
1. Technical feasibility: 9 — Boring proven stack end-to-end (Postgres + S3 + Next.js + Sidekiq-class queue + Auth0); analogues Vanta/Drata/AuditBoard/Hyperproof prove every component is solved, zero research risk.
2. Build vs buy posture: 8 — Auth, hosting, storage, email, queue all off-the-shelf; the only true custom code is the control/evidence data model + cadence engine, ~6-7 dev-weeks of genuinely bespoke work.
3. Architecture cleanliness: 8 — Single multi-tenant monolith with Postgres system of record, one object store, one job queue, read-only integrations — few moving parts, no microservice sprawl, failure surface concentrated in scheduler and integration tokens.
4. Time to revenue-earning MVP: 9 — First dollar doesn't wait on the app; onboarding fee + year-one subscription earnable in weeks via specialist labor + Airtable-grade workflow, real app (8-12 dev-weeks) built in parallel.
5. Technical-assumption risk: 7 — Core assumptions (manual-first evidence acceptable, CPA wants PDFs not APIs, no real-time) are mundane and cheaply verifiable; the one open question is how bespoke per-client control sets are, which affects productization not buildability.
6. Third-party dependency risk: 7 — Dependencies (Auth0, cloud, optional OAuth integrations) replaceable and stable; no single critical API or model on the path, though the CPA-firm relationship is a business dependency rather than technical.
7. Data architecture quality: 7 — Simple, owned, portable relational + object model; accumulated multi-year evidence history is a mild retention asset, but the sensitivity of financial-controls evidence makes it as much a liability as a moat.
8. Information security posture: 8 — Attainable and credible because requirements are standard (SSE-KMS, MFA, RBAC, immutable audit log, secrets manager — ~2 dev-weeks plus policy work) and the founders' stated SOC 2 Type II operator experience means it can be designed in from day one, not bolted on.
9. Scaling headroom: 8 — A multi-tenant Postgres/S3 monolith comfortably serves thousands of low-throughput orgs on weekly/quarterly cadences; the binding constraint is human reviewer capacity, not the database, so no rewrite looms.
10. Maintenance burden: 6 — The core app is self-running, but every added auto-collection integration is a perpetual maintenance liability (vendor API drift), so disciplined integration scope is required to avoid an oncall treadmill.

AVERAGE SCORE: 7.7 / 10

TOP 3 TECHNICAL STRENGTHS
- Zero research risk and a thin custom wedge: the entire stack is proven by named incumbents (Vanta, Drata, AuditBoard, Hyperproof), so the only bespoke code is the control/evidence model + cadence engine (~6-7 dev-weeks).
- Revenue decoupled from build: onboarding and subscription earnable with specialist labor + a lightweight workflow in weeks, so founders are never building 12 months before a dollar.
- Security is bridgeable, not aspirational: every required control is standard and the founders' SOC 2 Type II operator background lets them design it in from day one and dogfood their own SOC 2 as a sales asset.

TOP 3 TECHNICAL RISKS
- Integration scope creep: "automated evidence pull where available" is open-ended; chasing parity with SOC 2 automation tools turns a clean monolith into a perpetual connector-maintenance burden.
- Evidence-data sensitivity: you hold financial-controls evidence (possibly PII) for compliance-buying CFOs — a breach is brand-ending, so the security bar is high from the first customer.
- Productization ceiling from bespoke control sets: SOC 1 control objectives are tailored per the org's financial-reporting role, so the software templates less cleanly than SOC 2 tools, pushing more value (and cost) onto the human specialist.

BIGGEST SINGLE RISK
The human-judgment portion of the work may not productize the way the software implies, leaving a labor-bound service wearing a software costume. SOC 1 control objectives are bespoke to each service org's specific role in its customers' financial reporting — unlike SOC 2's fixed Trust Services Criteria, there is no single checklist, so much of the value is the controls specialist scoping objectives, judging evidence quality, and quarterbacking the CPA. If that judgment cannot be templated into reusable control libraries and review playbooks, the software stays thin, each new client demands meaningful expert hours, and gross margin and scalability are gated by how many qualified controls specialists you can hire and supervise — a people-scaling problem, not a database-scaling problem. The CTO mitigation is to invest early in a structured reusable control-objective library keyed by service-org type and a rules-assisted evidence-review layer, so the marginal client converges toward configuration rather than bespoke consulting; whether that convergence happens determines if this is a scalable product or a boutique practice.

QUESTIONS THE FOUNDERS MUST ANSWER
- How bespoke are SOC 1 control sets across target verticals? Draft control objectives for three distinct service-org types and report the overlap — high overlap means a productizable library; low overlap means a labor-bound consultancy.
- Will buyers pay for managed readiness with mostly manual evidence upload in year one, deferring integrations to v2? If no, the integration backlog (and maintenance) is far larger than implied.
- What format do partner CPA firms actually accept for the audit package — organized PDFs/spreadsheets, or structured/API handoff? Determines whether export is a half-week or a real integration project.
- Plan to attain your own SOC 2 Type II, on what timeline, given compliance-buying CFOs will demand proof your own house is in order?
- How will you scale the controls-specialist function — reusable playbooks and a control library, or linear hiring — and have you costed the gross-margin implications of each?

RECOMMENDATION: GO
From a purely technical standpoint a clean, low-risk, capital-light build: a boring multi-tenant Postgres/S3/Next.js monolith with a cadence engine and read-only integrations, every component proven by named incumbents, an 8-12 dev-week MVP, revenue earnable before the app is finished. The security bar is high but entirely standard and bridgeable given the founders' SOC 2 operator background, so no buildability objection. The one reservation — why founders must answer the bespoke-control-set and labor-scaling questions — is not a technical bomb but a margin/scalability question at the intersection of CTO and COO: keep integration scope ruthlessly narrow, invest early in a reusable control-objective library and rules-assisted review to convert clients from bespoke to configured, and design security in from week one. On the technology axis: GO.
