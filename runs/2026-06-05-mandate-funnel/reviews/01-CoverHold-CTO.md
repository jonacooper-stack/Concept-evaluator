# CTO REVIEW — CoverHold (Insurer-Attestation Management for Property Owners)

ONE-PARAGRAPH TECHNICAL READ
A boring, very buildable concept for a two-founder bootstrap: a deadline-tracking register, a guided document/evidence intake portal, a packaging/assembly step, and a human compliance reviewer in the loop. No hard technical problem — no real-time system, no ML that must work, no proprietary data pipeline. Complexity hides only in document ingestion (carrier loss-control letters are unstructured PDFs/emails that must be parsed into discrete dated requirements) and the fact that the service handles others' property/financial/insurance records, raising the security bar above a generic SaaS toy. Real risk is not "can they build it" but "how much of the per-account work stays manual" — the carrier-ready response assembly/review is human labor software only assists. Software-leveraged service, not pure software.

ARCHITECTURE SKETCH
- Frontend: single multi-tenant web app (Next.js/React on Vercel) — owner/manager portal (upload evidence, see open requirements) + internal operator console (review, assemble packages). ~3 dev-weeks on shadcn/ui + Tailwind.
- Backend: thin API + Postgres (Supabase/Neon) as system of record. Core entities: Property, Policy, Requirement (deadline, status, carrier, evidence-needed), EvidenceItem, ResponsePackage. The "deadline engine" is a scheduled job computing upcoming/overdue requirements and firing reminders. ~2 dev-weeks.
- Document store: S3/Supabase Storage for evidence files, per-tenant prefixing, server-side encryption; Postgres holds metadata/pointers, not blobs.
- Document ingestion/parsing: v1 operator-assisted (human keys requirements, optional LLM draft-extraction assist). LLM as "convenience a human always verifies"; autonomous parsing is where the bomb is. ~1–2 dev-weeks.
- Notifications: transactional email + SMS (Resend/Postmark + Twilio) tied to the deadline engine. ~0.5 dev-week.
- Response assembly: carrier-ready PDF/bundle (react-pdf or HTML-to-PDF), human-curated in v1. ~1 dev-week.
- Auth + billing: Clerk/Auth0/Supabase Auth; Stripe Billing for recurring per-property/portfolio subs + one-time onboarding fee. ~1 dev-week.
- Real complexity is NOT the stack (all off-the-shelf); it is (a) turning messy unstructured correspondence into a clean structured register reliably, and (b) the human-review labor per response that doesn't scale with software alone.

BUILD PLAN TO REVENUE-EARNING MVP
~7–10 dev-weeks of one developer; "revenue-earning" = a paying owner uploads evidence, we track deadlines, a human assembles a response.
1. Data model + Postgres + Stripe recurring billing + auth. ~2.5 wks. Core.
2. Owner portal (upload, view requirements/deadlines, status). ~2 wks. Core.
3. Deadline engine + reminders (cron + email/SMS). ~1.5 wks. Core — the actual promise.
4. Operator console (review queue, assemble package, mark submitted/closed). ~1.5 wks. Core but can launch crude.
5. LLM-assisted requirement extraction. ~1.5 wks. PUNT to v2 — v1 operators key manually; de-risks accuracy.
Scrappy MVP (manual register, no LLM, email reminders, Stripe, portal upload) ~6 weeks and can take real money. The deadline engine is the only part you cannot fake.

CRITICAL ASSUMPTIONS
1. Carrier loss-control letters reduce reliably to a structured dated requirement list. [ASSUMED 70–90% clean enough to key in <15 min.] Verify: collect 15–20 real letters from 3–4 carriers, time extraction, check variance.
2. Carriers accept third-party-assembled evidence packages without a special portal/credential/producer-of-record relationship. [ASSUMED most accept by email/broker channel; some have proprietary portals.] Verify: ask 3 owners how they submit today and to whom (reveals whether broker is the gatekeeper).
3. Durable software-leveraged service, not a hidden manual treadmill — one operator manages many properties because most periods have few open requirements. Verify: ask managers how many open requirements a 50-property portfolio carries/year (likely lumpy).
4. Founders not pulled into regulated insurance advice (what remediation satisfies the carrier). If package quality depends on interpreting coverage terms, that's an expertise/liability dependency, not tech. Verify with a loss-control consultant.
5. LLM extraction, when added, is a verified-draft assist, never an unattended parser of legally consequential deadlines. A hallucinated date becomes a lost-coverage event. Mitigation is design discipline.

INFORMATION SECURITY POSTURE
Data: property addresses/portfolios, policy details, carrier correspondence, vendor invoices, remediation photos, owner contact/financial-adjacent records — sensitive commercial + modest PII (not health/SSN), documents whose loss is reputationally/contractually serious. Lives in Postgres (metadata) + S3 (documents), single multi-tenant cloud account. Threat model: portal account takeover, tenant-isolation failure (Owner A sees Owner B), exposed buckets, operator-console over-privilege. Launch controls (not later): TLS everywhere; server-side encryption at rest; strict per-tenant authz on every row/object (RLS or enforced tenant_id); SSO/MFA on operator console; secrets in a manager; immutable audit logging of who-submitted-what-when (also product value — evidence provenance); tested backups of DB + document store. At scale SOC 2 Type II becomes a sales requirement — and the founders' stated SOC 2 Type II program experience makes it bridgeable and a sales weapon. Documented breach-response/notification plan. No exotic security R&D; disciplined standard-SaaS hygiene with audit logging first-class.

SCORES (1–10)
1. Technical feasibility: 9 — Entirely proven tech (Next.js + Postgres + S3 + Stripe + cron); the only "AI" (letter extraction) is a punted human-verified assist, nothing bet-the-business depends on a model working.
2. Build vs buy posture: 9 — Almost everything off-the-shelf (Supabase/Neon, Stripe Billing, Clerk/Auth0, Resend/Twilio, Vercel); only custom code is the requirement/deadline register + operator console (~4–5 dev-weeks bespoke).
3. Architecture cleanliness: 8 — Five core entities, one DB, one object store, one cron worker, one billing/notify integration set; no real-time/distributed-state complexity, small inspectable failure surface.
4. Time to revenue-earning MVP: 8 — Billable MVP (portal upload + deadline engine + Stripe + crude operator console) ~6 weeks of one dev, under the 8-week bar; billing doesn't depend on LLM/extraction.
5. Technical-assumption risk: 6 — Build is low-risk, but two assumptions carry weight: messy letters reduce cleanly to structured requirements, and carriers/brokers accept third-party packages — operational/market unknowns, cheaply verifiable but currently unverified.
6. Third-party dependency risk: 8 — Dependencies (Stripe, Supabase, Vercel, Resend, Twilio, an LLM API) all commodity/replaceable; LLM is the only accuracy-touching one and is optional and swappable.
7. Data architecture quality: 7 — Simple, owned, portable (Postgres + S3, exportable per tenant); accumulated evidence file is a genuine retention moat; held below 8 because tenant-isolation/provenance must be exact or the data becomes a liability.
8. Information security posture: 7 — Needed controls standard, founders have real SOC 2 Type II experience making audit-readiness a sales weapon; held at 7 because it handles loss-sensitive insurance evidence so launch-day isolation/audit-logging/backups are mandatory.
9. Scaling headroom: 8 — Postgres + object storage + stateless web tier scales to thousands of properties without rearchitecture (low-write, document-centric); binding constraint is human reviewer capacity, not infra.
10. Maintenance burden: 7 — Software largely runs itself (managed cron/billing/storage), but the operator-review step is permanent human-ops load and extraction logic needs ongoing tuning as carrier formats vary.

AVERAGE SCORE: 7.7 / 10

TOP 3 TECHNICAL STRENGTHS
- Entire stack commodity and assemblable; bespoke wedge is a ~4–5 dev-week register → short time-to-first-dollar (~6 weeks), capital-light.
- No bet-the-business technical risk: no ML that must work, no real-time, no scraping; the one AI feature is optional, human-verified, punted to v2.
- The accumulated continuously-maintained evidence file is a real data-retention moat raising switching costs — and SOC 2 Type II experience makes the security posture a sales asset.

TOP 3 TECHNICAL RISKS
- Document ingestion variance: heterogeneous unstructured letters, accuracy is legally consequential (a wrong date is a lost-coverage event); must stay human-verified, permanent tuning load.
- Hidden manual-ops treadmill: response assembly/review is human labor software only assists; lumpy/high open-requirement volume makes operator capacity (not infra) the ceiling and erodes the software-leveraged thesis.
- Tenant isolation and evidence integrity: holds loss-sensitive records; a cross-tenant leak or lost evidence file destroys the exact promise being sold.

BIGGEST SINGLE RISK
The deadline/requirement register depends on reliably extracting legally consequential dates and obligations from unstructured carrier-specific correspondence, and the cost of a single error is asymmetric and catastrophic to the customer. The positioning is "never lose your coverage." A misread deadline, a requirement buried in a multi-page letter, or an LLM-hallucinated date taken as truth → the customer loses coverage → their lender triggers → existential for them → a software defect becomes a serious liability and reputation event. Mitigation is real but disciplined: human-in-the-loop verification of every requirement/deadline at launch, LLM only as a verified draft assist, immutable audit logging, explicit operator double-check on anything within N days of a deadline. None hard to build; the risk is organizational discipline around accuracy under volume.

QUESTIONS THE FOUNDERS MUST ANSWER
- Show 15–20 real loss-control letters across 3–4 carriers — how long to reduce each to a structured dated list, and how much format variance? (Sizes extraction risk + per-account labor.)
- How do owners submit loss-control evidence today — directly, via proprietary carrier portal, or via broker? If broker is gatekeeper, does the service insert cleanly or need a producer/broker relationship?
- How lumpy is open-requirement volume across a policy year for a 50-property portfolio, and how many properties can one reviewer manage at peak — where does human capacity cap the model and what does it do to gross margin?

RECOMMENDATION: GO
From a pure technical/build standpoint a clean GO: stack entirely off-the-shelf, custom wedge small (~4–5 dev-weeks), billable MVP ~6 weeks, no bet-the-business model dependency, scales on managed infra. The two things keeping it from a 9-average are not code — accuracy/liability discipline around legally consequential deadlines, and how much per-account work stays manual (operator capacity is the binding constraint). Don't cut scope; gate the build on three cheap de-risking experiments: (1) time manual extraction on a real letter sample (<15 min/letter, bounded variance), (2) confirm with 3–5 owners who the submission gatekeeper is, (3) instrument human-verified extraction with audit logging from day one, LLM strictly a draft assist. Pass those and the technical case is strong; residual risk lives in operations and liability discipline, not feasibility.
