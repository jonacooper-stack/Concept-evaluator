CTO REVIEW — Multi-State Tax & Filing Compliance Dashboard

ONE-PARAGRAPH TECHNICAL READ
The visible product — dashboard with red/yellow/green statuses, deadline calendar, alerts — is a boring, very buildable CRUD-plus-scheduler app a single dev can stand up in weeks (Next.js + Postgres + cron). Viability is NOT in the UI; it is entirely in the rules engine and its data: an authoritative, continuously-maintained map of every state's franchise tax, annual-report, foreign-qualification, payroll/UI registration, and economic-nexus rules, keyed to a company's employees, revenue-by-state, and entity structure. That content is the real "build," and it is not software — it is a recurring research/legal-maintenance liability across 50+ jurisdictions that decay every legislative session. The app is trivial; the trustworthy data is hard.

ARCHITECTURE SKETCH
- Frontend: Next.js/React on Vercel; standard dashboard (status tiles, calendar, obligation detail, checklists). ~1 dev-week custom UI once data model settles.
- Backend: Node/TS or Python API on managed host; Postgres system of record (entities, employees, state-presence facts, obligations, due dates, statuses, evidence/filing records).
- Rules engine: a VERSIONED ruleset (data, not code) mapping (jurisdiction × trigger) → obligation + cadence + form + payment + penalty. Declarative rule rows + a small evaluator so non-engineers maintain it. A content/CMS problem disguised as software.
- Integrations (hard, load-bearing): payroll/HRIS (Gusto, Rippling, Justworks, Deel) to auto-detect employee state presence; billing (Stripe)/accounting (QuickBooks) to estimate revenue-by-state for nexus; entity data mostly manual. Each = OAuth app + token store + sync worker.
- Async: scheduler/cron recomputes status nightly, rolls due dates, fires alerts (email/Slack), re-evaluates on new facts. BullMQ/SQS + worker.
- ML/AI: NONE required, correctly. LLMs at most draft plain-language explanations — never on the critical "are you compliant" path (hallucinated tax guidance is liability).
- Auth/security: multi-tenant with strict per-company isolation; holds EIN, payroll-derived employee location, revenue — sensitive financial PII; SOC2 a near-certain enterprise ask.
- Hosting: fully managed, serverless-leaning, remote-first.

BUILD PLAN TO REVENUE-EARNING MVP
~8-12 dev-weeks of one developer IF v1 is sold as "manually-onboarded, controller verifies inputs," not a fully-automated oracle. Long pole is rules content.
1. Data model + manual obligation engine (2-3 wks): entities, hand-entered state-presence facts, obligation table, due-date rollforward, status logic, calendar. Demoable alone.
2. Seed ruleset, narrow scope (2-4 wks research + entry, ongoing forever): DE franchise + annual reports + foreign-qual + payroll/UI for ~10 concentration states (CA, NY, TX, WA, MA, CO, IL, FL, GA + DE). Do NOT attempt all 50 + sales-tax nexus day one.
3. Alerts + scheduler (1 wk): nightly recompute, email/Slack, due-soon digests.
4. One payroll integration (1-2 wks): Gusto or Rippling OAuth to auto-pull work states — highest-credibility trigger. Punt billing/accounting revenue-nexus to v2.
5. Billing + tiering (0.5 wk): Stripe subscriptions, entity/state/employee tiers.
Punt to v2: full 50-state, automated sales-tax nexus, done-for-you filing execution, accounting sync, multi-user roles/approvals.

CRITICAL ASSUMPTIONS
1. "We can build and KEEP CURRENT an authoritative cross-jurisdiction ruleset." Bet-the-business. Rules change every session; a stale rule that says compliant when not is the core failure. Verify: spend one week encoding just 5 states' rules from primary sources, log ambiguous edge cases (subsidiaries, short years, mergers, thresholds) you can't resolve without a CPA. If 5 states take a painful week, 50 maintained forever is a staffing line item.
2. "Payroll/billing APIs give reliable trigger signal." Gusto/Rippling/Deel expose work location, but coverage is partial; many ICP customers use providers without good APIs or run contractors off-platform. Verify: pull top-3 payroll API docs, confirm work-state + hire-date fields populated. Revenue-by-state from Stripe/QuickBooks is harder — ship address ≠ tax situs, SaaS sourcing is messy.
3. "Customers accept a tool that informs rather than guarantees." If positioned as "tells you whether you're compliant," you assumed a CPA-grade liability/accuracy bar. Verify with first 5 design-partner contracts: do they read the disclaimer and still pay?
4. "Entity/structure data captured cheaply." Corporate structure mostly NOT API-available; entered manually. Verify: time a controller entering a 3-entity, 8-state company correctly.

INFORMATION SECURITY POSTURE
Collects EINs, entity details, state registration IDs, employee names + work locations + counts (payroll PII), revenue by jurisdiction, uploaded filings/credentials — sensitive financial + employee PII a finance buyer will diligence. Multi-tenant isolation is the primary threat model: a cross-tenant leak is catastrophic and most likely — row-level tenancy + tested authorization on every query are launch-day controls. Required at launch: SSO/strong auth (Auth0/Clerk/WorkOS), encryption in transit + at rest, real secrets manager, least-privilege OAuth scopes with encrypted token storage + rotation, audit logging. At scale: SOC 2 Type II near-certain — favorably, founders have real SOC 2 Type II program experience, so bridgeable, but a 3-6 month, ~$15-40K/yr effort (Vanta/Drata + auditor). Clear deletion/retention policy + incident-response runbook from day one. Nothing exotic; the discipline is SOC2 muscle, which founders have.

SCORES (1–10)
1. Technical feasibility: 8 — Boring proven CRUD + cron + OAuth; buildable on Next.js/Postgres/BullMQ. Not higher because the rules-content layer is the genuine difficulty, verified-buildable only at narrow scope.
2. Build vs. buy posture: 6 — Infra off-the-shelf, but the core wedge (multi-jurisdiction ruleset) can't be bought cheaply and must be hand-built/maintained.
3. Architecture cleanliness: 7 — Dashboard + scheduler + declarative rule evaluator + a few sync workers; no distributed-systems complexity if rules stay data.
4. Time to revenue-earning MVP: 8 — Narrow-scope MVP (10 states, one payroll integration, Stripe) ~8-12 dev-weeks of one dev; revenue before 50-state coverage exists.
5. Technical-assumption risk: 5 — Ruleset accuracy/freshness is bet-the-business with a real failure mode; not fully de-riskable by code.
6. Third-party dependency risk: 6 — Payroll/accounting APIs are the value-add triggers, each replaceable, app degrades to manual entry; coverage gaps blunt the automation pitch.
7. Data architecture quality: 7 — Simple owned portable relational model; accumulated obligation history is a mild switching-cost moat if isolation is right.
8. Information security posture: 8 — Sensitive PII needs real controls, but all are standard (per-tenant isolation, WorkOS/Clerk SSO, encrypted token vault, Vanta/Drata SOC 2 Type II) and founders have demonstrated SOC 2 Type II experience, making it attainable.
9. Scaling headroom: 8 — Tiny per-tenant load (nightly recompute of a few dozen obligations); Postgres + queue to thousands of customers, no rewrite, cost-per-tenant near zero.
10. Maintenance burden: 4 — Code maintenance light, but the PRODUCT needs perpetual human research across 50 jurisdictions every cycle — a structural never-ending content-ops cost for a two-person team; weakest part.

AVERAGE SCORE: 6.7 / 10

TOP 3 STRENGTHS
- Software is low-risk and fast: boring proven stack, no ML on the critical path, narrow MVP in ~8-12 dev-weeks of one dev.
- Low-throughput cheap-to-scale architecture: per-tenant compute trivial, infra near-zero, Postgres + queue to thousands, no rewrite.
- Security posture attainable not aspirational — all controls standard; founders' real SOC 2 Type II experience de-risks finance-buyer diligence.

TOP 3 RISKS
- The ruleset is the actual product and it decays: perpetual research across 50+ jurisdictions; stale rules = direct accuracy/legal exposure.
- Trigger-detection depends on partial payroll/billing API coverage; many ICP customers degrade the "we automatically know your obligations" pitch back to manual entry.
- Accuracy/liability budget mismatch: "you ARE compliant" pushes the correctness bar toward a CPA's, which a two-founder content op can't guarantee.

BIGGEST SINGLE RISK
Not the code — the perpetual correctness and freshness of cross-jurisdiction rules content combined with the implicit accuracy expectation the positioning creates. "See whether you're compliant" trains customers to trust the green light. Every state changes franchise math, report cadences, thresholds, and nexus rules on its own schedule; a single stale rule showing "compliant" while a customer is delinquent produces exactly the surprise penalty the product was sold to prevent — now the product's fault. For two founders with no tax department, keeping 50+ jurisdictions accurate forever is an unbounded human-research liability that scales with breadth, not revenue, adjacent to professional-liability territory. Technical mitigation (declarative versioned rules, "informational, verify with advisor" framing, narrow high-confidence scope first, audit trails) reduces but doesn't eliminate it — a content-ops and liability problem wearing a software costume.

QUESTIONS THE FOUNDERS MUST ANSWER
- Rules-maintenance operating model: who researches/updates 50 jurisdictions every cycle, at what cost, and how do you detect a rule change before a customer is harmed?
- Decision-support or compliance guarantee? The two imply radically different accuracy budgets/liability/investment — which are you selling, and have design partners accepted the disclaimer and still paid?
- What fraction of your real ICP uses payroll/accounting providers with APIs good enough to auto-detect work-states and revenue-by-state? If low, the differentiating automation collapses to manual entry.
- How do you handle day-one edge cases (subsidiaries, short years, mid-year foreign quals, mergers, SaaS sales-tax sourcing) without a CPA, and what does a wrong answer cost?
- Will you cap v1 to ~10 high-concentration states + entity/payroll obligations and exclude automated sales-tax nexus until later, or commit to 50-state + nexus at launch (a build-killing over-scope)?

RECOMMENDATION: REFINE — technology is sound and fast to ship, but the real product is the rules-content engine and its perpetual accuracy, which the one-pager treats as a feature rather than the central operating liability. De-risk before commitment: (1) run the one-week five-state encoding experiment; (2) re-position v1 as decision-support with verify-with-advisor framing; (3) hard-cap launch scope to ~10 states + entity/payroll + ONE payroll integration; (4) confirm payroll/billing API coverage across the real ICP. If those land, the technical case for GO is strong; the open question is content sustainability, not software feasibility.
