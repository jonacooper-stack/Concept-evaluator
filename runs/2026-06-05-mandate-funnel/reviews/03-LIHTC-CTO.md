# CTO REVIEW — LIHTC (Section 42) Compliance Managed Service

ONE-PARAGRAPH TECHNICAL READ
A document-and-deadline business with a thin software spine wrapped around expert human review — the shape a two-founder bootstrap can ship, because none of the hard parts are research problems. The genuinely hard engineering is the long tail of integrations: the certification math is deterministic but voluminous (HUD income/rent limits, set-aside, student rules), and the "file the state-agency report" step is fragmented across ~50 state HFAs each using different portals, file formats, and XML/spreadsheet schemas. The defensible path is to start as a managed service where the software is internal tooling (deadline engine, calculation checker, document vault) and a credentialed specialist owns final review — earning revenue in ~8-12 dev-weeks without the full multi-state automation. The trap is over-promising "software files your state report automatically" on day one; that's a per-state grind to punt to v2.

ARCHITECTURE SKETCH
- Frontend: single Next.js app (Vercel) for two audiences — internal specialist console (work queue, deadline calendar, certification review) + light client portal (document upload, status, "you're audit-ready" dashboard).
- Backend: boring Postgres (Supabase/Neon) as system of record for properties, units, households, certifications, deadlines, filings. The normalized schema is the actual moat — get the data model right and the rest is CRUD plus rules.
- Deadline/rules engine: background scheduler (Inngest, Trigger.dev, cron worker) computing re-cert due dates, AOC deadlines, set-aside/rent-limit checks. Deterministic date math + threshold comparison against HUD limit tables — NOT ML.
- Income/rent-limit data: ingest HUD MTSP income/rent limits annually (machine-readable each year), versioned tables keyed by county/year/household-size. The calculation backbone.
- Document intake: S3-compatible storage with per-property folders, optional OCR/extraction (Textract or LLM with structured output) to pre-fill fields from pay stubs/leases/verifications — strictly a draft a human approves.
- State-agency filing: the messy edge. Per-state adapters producing required XML/spreadsheet upload format (ProLink/Emphasys/state portals). Initially a human pasting/uploading; automation is per-state custom work.
- Auth/hosting: Clerk/Auth0 + Postgres RLS for tenant isolation; managed PaaS; Stripe for tiered per-property subscriptions.
- Complexity hides in: (1) breadth of state-by-state filing formats; (2) keeping HUD limit tables and §42 rule changes current/versioned; (3) PII-heavy tenant files (SSNs, income docs) raising the security bar above generic SaaS.

BUILD PLAN TO REVENUE-EARNING MVP
~8-12 dev-weeks of one developer to a revenue-earning managed-service MVP, because the software is internal tooling, not self-serve. The specialist can deliver value with spreadsheets on day one; software just compounds margin.
1. Data model + property/unit/household/certification schema + document vault with strict access control (~3 wks). The spine.
2. HUD income/rent-limit ingestion + certification calculation checker (income eligibility, rent limit, set-aside ratio, student-rule flags) (~2-3 wks). Deterministic, testable.
3. Deadline engine + specialist work queue + client status portal (~2-3 wks).
4. Stripe tiered billing + onboarding flow for ingesting an existing property's files (~1 wk).
5. PUNT TO V2: automated multi-state report generation/filing, OCR auto-extraction, self-serve client product, white-label. Do these per-state as customer density justifies.
The remediation one-time offering needs almost no new software (specialist + vault) — sell from week one to fund the build.

CRITICAL ASSUMPTIONS
1. The certification work is rules-deterministic enough that software does the calculation and a specialist only reviews. If large portions need judgment per state, leverage shrinks and margins approach pure consulting. VERIFY: a credentialed advisor walks 10 real certifications marking mechanical vs judgment. One week.
2. A small number of states cover most early customers, so only a few filing adapters initially. VERIFY: pull geographic distribution of first 20 target accounts; confirm 3-5 states cover the majority.
3. HUD limit data + §42 rule updates available in machine-readable form and change predictably (annually). VERIFY: download last 3 years of HUD MTSP limits, confirm format stability.
4. Owners will hand a third party their tenant files (SSNs, income docs) and trust the system of record. If they insist on keeping it in-house, you become a thin reviewer with weak lock-in. VERIFY: ask 5 target buyers directly.
5. [CREDENTIAL] A credentialed specialist (HCCP/SHCM/NCP) is reachable as hire or partner. Founders are not LIHTC experts; bridgeable per the founder profile but on the critical path. VERIFY: confirm comp + availability before committing.

INFORMATION SECURITY POSTURE
The most security-sensitive concept shape a bootstrap can pick short of healthcare: tenant files contain full PII including SSNs, DOBs, income/wage documentation, household composition — a high-value breach target and clear liability if leaked. Data in Postgres + object storage; threat model is credential theft, broken tenant isolation (one owner seeing another's tenant data), exposed document URLs. Launch controls (not later): encryption at rest/in transit (default on managed PaaS), per-tenant isolation at the DB layer (Postgres RLS, not just app-layer), signed time-limited URLs for every document, SSO/MFA for the specialist console, field-level encryption/tokenization for SSNs, full audit logging of who viewed which tenant file (you're selling audit-readiness — your own audit trail must be impeccable), documented incident-response + breach-notification plan. SOC 2 Type II will be asked for by larger management companies within the first year; founders have run SOC 2 Type II cycles before (per profile), so it's a known schedulable cost (~$15-40K + several eng weeks). No HIPAA BAAs, but data-processing terms with owners required. Do NOT ship OCR-by-LLM that sends raw SSN documents to a third-party model without a DPA and PII-redaction strategy.

SCORES (1–10)
1. Technical feasibility: 8 — All boring proven tech (Postgres + Next.js + Inngest + Stripe); the only "hard" piece is deterministic date/limit math, no research problems, buildable in ~8-12 dev-weeks.
2. Build vs buy posture: 7 — Auth, billing, storage, OCR, scheduling all off-the-shelf; the custom wedge is the §42 data model and rules engine, appropriately thin but irreducibly proprietary.
3. Architecture cleanliness: 7 — Few moving parts for the core (one app, one DB, one scheduler), but the state-filing adapter layer is an open-ended fan-out that grows messier with each state.
4. Time to revenue-earning MVP: 8 — Remediation service sells from week one with just specialist + vault; full managed MVP in ~8-12 dev-weeks of one dev, well under a quarter, because software starts as internal tooling.
5. Technical-assumption risk: 6 — Core calc is verifiable and low-risk, but "rules are mechanical not judgment" and "few states cover most customers" are load-bearing and not yet validated.
6. Third-party dependency risk: 7 — Vercel/Supabase/Stripe/Clerk are replaceable commodities; the real exposure is HUD data format and per-state portals, government-stable but outside your control.
7. Data architecture quality: 6 — Schema is owned/portable and a genuine moat, but it is SSN/PII-heavy and leakage-prone, a liability that drags this despite clean ownership.
8. Information security posture: 7 — Requires real controls at launch (Postgres RLS isolation, SSN field encryption, signed URLs, audit logging, MFA) and founders have run SOC 2 Type II before, so it's schedulable rather than unknown — but PII sensitivity means any slip is catastrophic.
9. Scaling headroom: 8 — Postgres + managed PaaS easily supports 100x the property/unit count (units are thousands, not millions of rows); binding constraint is specialist labor and per-state coverage, not infra.
10. Maintenance burden: 6 — Self-running for core scheduling, but annual HUD-limit refreshes, §42 rule changes, and each new state portal are recurring engineering/compliance upkeep that never fully ends.

AVERAGE SCORE: 7.0 / 10

TOP 3 TECHNICAL STRENGTHS
- The hard problem is deterministic, not AI: date math and threshold comparison against published HUD tables, fully testable, no model-reliability bet — buildable in ~8-12 dev-weeks with Postgres + Inngest + Next.js.
- Revenue precedes the full build: the file-remediation one-time service needs only specialist + document vault, funding the software build instead of waiting on it.
- Scaling is labor-bound, not infra-bound: data volumes (units, households, certifications) are trivially small for Postgres, so the architecture supports 100x growth without a rewrite.

TOP 3 TECHNICAL RISKS
- State-by-state filing fragmentation: ~50 HFA portals/formats turn "the software files your report" into an open-ended per-state integration backlog that never closes.
- PII concentration: holding SSNs and income docs for thousands of tenants makes you a breach target; one isolation bug or leaked document URL is an existential reportable event.
- Maintenance treadmill: annual HUD limit refreshes + §42 rule changes + each new state must be tracked correctly forever — errors here are exactly the recapture events you promise to prevent, so your own bugs carry the customer's catastrophic liability.

BIGGEST SINGLE RISK
Your software's correctness IS the product's liability surface, and the failure mode you're paid to prevent is the same one your own bugs can cause. You're selling "never trigger a recapture," so a miscalculated income limit, a missed re-certification deadline from a scheduler edge case, or a wrong set-aside computation isn't a normal SaaS bug — it can be the exact Form 8823 / credit-recapture event that destroys the customer's deal and exposes you to negligence claims. This forces a higher engineering-quality bar than a typical bootstrap (exhaustive test coverage against real HUD tables, versioned rule sets, human-in-the-loop review on every filing, meticulous audit logging) AND a higher security bar (SSN-grade PII for thousands of tenants). The combination — catastrophic-consequence correctness plus catastrophic-consequence data sensitivity — means the cheap-and-fast bootstrap shortcuts aren't available; cutting corners on either calculation rigor or data isolation converts your value proposition into your largest liability.

QUESTIONS THE FOUNDERS MUST ANSWER
- What fraction of certification work is genuinely mechanical (software-automatable) vs expert judgment that varies by state? Determines whether you're a software-leveraged service at high margin or a labor consultancy with a tool — walk 10 real certifications with a credentialed advisor.
- Will target buyers actually let you become the system of record for their tenant files (SSNs, income docs), or insist on keeping data in-house? Dictates security obligations and lock-in strength.
- Across the first 20-30 target accounts, how concentrated is the state distribution? If 3-5 states cover the majority, the filing-adapter problem is tractable; if accounts span 20 states, the backlog swamps two founders.
- Do you have a committed credentialed LIHTC specialist (HCCP/SHCM/NCP) as hire or partner, and at what cost, since they're on the critical path for delivery and product correctness?
- Concrete plan/budget for SSN-grade PII handling and SOC 2 Type II, and can remediation revenue fund it before a large management-company customer demands the attestation?

RECOMMENDATION: GO (with one scope discipline)
From a pure technical-feasibility/build-effort standpoint a GO: the architecture is boring and proven, the core is deterministic rather than AI-dependent, revenue can precede the full build via the remediation offering, an MVP is reachable in ~8-12 dev-weeks. The founders' prior SOC 2 Type II experience directly de-risks the one elevated requirement (SSN-grade PII security). The single scope discipline: do NOT promise automated multi-state filing on day one. Ship as a managed service where software is internal tooling and a credentialed specialist owns every filing, then add state-filing automation one state at a time as customer density justifies. Treat calculation correctness and tenant-data isolation as launch-grade — because in this domain a bug is not a bug, it is the recapture event you were hired to prevent. Validate the "mechanical vs judgment" ratio and the state-concentration assumption before scaling spend; both are cheap to check and load-bearing.
