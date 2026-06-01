CTO REVIEW — Compressed Air Optimization Service

ONE-PARAGRAPH TECHNICAL READ
This is a field-services business wearing a light software jacket, and from a pure technology standpoint that is a gift: the "build" is a survey-data capture workflow plus a customer-facing reporting dashboard, both of which are boring CRUD over a small relational dataset and assemblable from off-the-shelf SaaS in well under 8 dev-weeks. The hard parts of this business are physical and operational (acoustic survey skill, technician routing, leak-quantification accuracy), not technical — there is no ML research problem, no high-scale data pipeline, and no real-time system on the critical path. The single genuine technical/quasi-technical risk is the integrity of the CFM-to-dollars savings calculation, because that number is the entire sales pitch and the entire renewal justification, and it is currently a manual estimate, not an instrument-grade measurement. For a two-founder bootstrap where one founder vibe-codes, this is one of the most technically de-risked concepts you can pick.

ARCHITECTURE SKETCH
- Frontend: a thin web app (Next.js on Vercel) for the customer dashboard; a mobile-friendly survey-entry form (PWA or a no-code tool like Fillout/Jotform initially) the technician uses on-site to log each leak: location, photo, acoustic-imager reading, estimated CFM, estimated $/yr.
- Backend: managed Postgres (Supabase or Neon) holding the core entities — Plant, Survey, Leak, Repair, SavingsLedger. Business logic is a small set of deterministic calculators (CFM-loss estimate from orifice size + pressure; $/yr from kWh price + compressor efficiency + run-hours). No microservices; one app.
- Integrations: Stripe for recurring billing; an email/PDF service (Resend + a PDF lib like react-pdf or a service like DocRaptor) to generate the written report; cloud object storage (S3/Supabase Storage) for leak photos and acoustic-imager exports.
- Async/background: trivial — scheduled re-survey reminders and a nightly savings-rollup job (a cron on Vercel/Supabase Edge Function). No queue infrastructure needed at this scale.
- ML/AI: none required on the critical path. The acoustic imaging is done by the purchased hardware (e.g., Fluke ii900-class acoustic cameras, SDT/UE Systems ultrasonic detectors), not by software they build. Optional: an LLM to draft the narrative report prose from structured findings — a nice-to-have, not load-bearing.
- Auth: off-the-shelf (Supabase Auth/Clerk) with simple per-customer tenant isolation.
- Hosting: Vercel + Supabase; effectively serverless, near-zero ops.
- Where complexity actually lives: NOT in the stack. It lives in (a) the correctness/defensibility of the savings math and (b) the operational data discipline of getting consistent, comparable readings across technicians and across re-surveys so the trend line is credible.

BUILD PLAN TO REVENUE-EARNING MVP
Total estimate: roughly 4-7 dev-weeks of one developer's time to a version customers will pay for; you can earn revenue on week 1 with zero software because the first surveys can be sold and delivered with a spreadsheet + a Google Doc report.
- Chunk 0 (week 0, no code): sell and deliver the first 2-3 surveys using a spreadsheet calculator and a templated Word/Google Doc report. This is the actual revenue-earning MVP. The software is a margin/retention enhancer, not a prerequisite. [build estimate: 0 dev-weeks]
- Chunk 1 (1.5-2 weeks): the savings calculator + data model in Postgres — Plant/Survey/Leak/SavingsLedger schema and the deterministic CFM/$ formulas, version-controlled so the methodology is auditable. This is the only piece that deserves real care.
- Chunk 2 (1.5-2 weeks): technician survey-entry form with photo upload and the auto-calc, plus PDF report generation. Can start as a no-code form (Jotform/Fillout) to defer custom build.
- Chunk 3 (1-1.5 weeks): customer dashboard (leaks found/fixed, CFM recovered, cumulative $ and kWh) + Stripe recurring billing.
- Chunk 4 (1 week, punt to v2): utility-rebate paperwork export and shared-savings metering reconciliation. Genuinely punt-able until a customer asks.
- Punt to v2 also: native mobile app, role-based multi-tenant admin, any LLM report drafting.

CRITICAL ASSUMPTIONS
1. The savings number is defensible enough to survive a skeptical plant manager and a renewal. ASSUMED the CFM-loss and $/yr estimates land within roughly ±25-40% of reality [ASSUMED range; verify cheaply by, on the first 3 paid sites, fixing tagged leaks and reading actual compressor amp-draw/run-hours before and after to compare predicted vs. measured savings]. If the math is systematically optimistic, churn at renewal is the business killer — this is a technical-credibility risk, not a CRUD risk.
2. Acoustic imaging hardware reliably surfaces the bulk of leaks in a noisy plant. ASSUMED a modern acoustic camera finds the leaks that matter [verify by renting a Fluke ii900-class unit for one week and surveying a friendly plant before buying].
3. Survey readings are reproducible across technicians and across quarters so the trend line is trustworthy. ASSUMED with a standardized capture form and reading protocol [verify by having two people independently survey the same site and comparing total CFM within a tolerance].
4. No customer-side data integration is needed at launch — readings are manually entered, not pulled from compressor SCADA/IoT. ASSUMED true [verify in first sales calls; if customers expect live compressor telemetry, scope expands materially and a real engineer is needed].
5. The dashboard/report is "good enough to be the differentiator" without enterprise features. ASSUMED true for SMB plants [verify by showing the templated PDF to 3 target buyers and asking what would make them sign].

INFORMATION SECURITY POSTURE
Data collected is low-sensitivity by enterprise standards: plant layouts, leak locations, energy consumption figures, photos of equipment, and customer billing contact info. There is no consumer PII at scale, no payment card data (Stripe holds that), no PHI, and no regulated data — which dramatically lowers the threat model. The real sensitivity is competitive/operational: a plant's energy waste and facility photos are information a customer would not want leaked publicly. Controls needed at launch: TLS in transit (default on Vercel/Supabase), encryption at rest (default on managed Postgres/object storage), per-tenant row-level isolation so Customer A cannot see Customer B's plant data (Supabase RLS policies — a concrete, enforceable control), SSO/strong auth via Clerk or Supabase Auth with MFA for staff, secrets in a manager (Vercel/Doppler env vars, never in code), and audit logging on data access. At scale, if you land a large manufacturer, expect a security questionnaire and possibly a SOC 2 Type I request; the stack chosen (Vercel + Supabase + Stripe, all carrying their own SOC 2 reports) makes that attainable without re-architecture — budget ~$15-30k and a few months when the first enterprise asks. The biggest infosec footgun is photos: facility imagery uploaded by technicians via phones must go to access-controlled storage, not a public bucket — design that on day one.

SCORES (1-10)
1. Technical feasibility: 9 — Entirely boring, proven tech (Next.js + Postgres + Stripe + S3); the only "hard" component is hardware they buy, not software they build; deliverable as a spreadsheet on day one. [stack named; build ~4-7 dev-weeks]
2. Build vs. buy posture: 9 — Almost everything is bought (Supabase, Vercel, Stripe, Jotform, acoustic cameras); the only custom code is the savings calculator and dashboard — a genuinely thin wedge. [named off-the-shelf components]
3. Architecture cleanliness: 9 — One app, one managed database, ~5 entities, one cron job; no queues, no microservices, no real-time, no ML on the critical path. [concrete: single Postgres instance, deterministic calculators]
4. Time to revenue-earning MVP: 9 — Revenue possible week 1 with spreadsheet + Google Doc; software MVP in ~4-7 dev-weeks of one dev, far inside the <8-week bar. [build estimate inline]
5. Technical-assumption risk: 6 — Low build risk, but the savings-math accuracy assumption is load-bearing for renewals and currently unverified; capped at 6 until predicted-vs-measured is checked on real sites.
6. Third-party dependency risk: 8 — Dependencies (Vercel, Supabase, Stripe) are all individually replaceable commodity infra with no single brittle API on the critical path; hardware has multiple vendors (Fluke, SDT, UE Systems). [named, replaceable]
7. Data architecture quality: 8 — Small, owned, portable relational dataset in standard Postgres with no vendor lock-in beyond commodity managed hosting; trivially exportable, and the accumulating multi-survey trend data is a genuine retention moat. [concrete: portable Postgres, ~5 entities]
8. Information security posture: 8 — Low-sensitivity data, no PII/PHI/PCI at scale, and SOC 2 attainable on a SOC-2-backed stack; concrete launch control is Supabase row-level security for tenant isolation plus access-controlled photo storage. [named control: RLS + private object storage]
9. Scaling headroom: 8 — Architecture supports 100x customers trivially because load is tiny (a few surveys per plant per quarter, not high-throughput); the real scaling constraint is human technicians/trucks, not infra. [concrete: data volume is per-quarter, not per-second]
10. Maintenance burden: 8 — Serverless managed stack runs itself with near-zero oncall; the ongoing engineering is occasional feature work, not firefighting. [concrete: Vercel + managed Postgres, no self-hosted infra]

AVERAGE SCORE: 8.2 / 10

TOP 3 TECHNICAL STRENGTHS
- The technology is almost entirely off-the-shelf and the custom wedge is tiny — a savings calculator and a reporting dashboard, buildable in 4-7 dev-weeks, with revenue earnable on a spreadsheet before any code ships.
- The architecture is genuinely simple and self-running: one managed Postgres, one Next.js app, Stripe billing, no ML, no queues, no real-time, so two founders can own it without an oncall burden.
- The threat model is mild — no consumer PII, no PHI, no card data on their servers — and the stack (Vercel/Supabase/Stripe) is SOC-2-attainable when an enterprise customer eventually asks, with no re-architecture required.

TOP 3 TECHNICAL RISKS
- The savings/ROI number is a manual estimate, not an instrument-grade measurement, and it is the whole pitch; if it is systematically optimistic, renewals collapse and the "recurring" model breaks.
- Survey-data reproducibility across technicians and quarters is a data-discipline problem, not a software problem; inconsistent readings make the trend line (the retention asset) untrustworthy.
- Scope creep toward live compressor IoT/SCADA telemetry — if customers expect real-time monitoring, the project jumps from a CRUD app to a real engineering effort the founders cannot staff alone (engineering is their stated 3-4/10 gap).

BIGGEST SINGLE RISK
The biggest technical-adjacent risk is the credibility and durability of the savings calculation, because it is simultaneously the sales pitch, the renewal justification, and the basis for any shared-savings billing — and it is currently a modeled estimate, not a measured fact. A leak's CFM loss is inferred from orifice size and line pressure, and the dollar figure layers on assumed compressor efficiency, kWh price, and run-hours; small optimistic errors compound, and a plant manager who fixes the tagged leaks but does not see his electric bill move will not renew, and may dispute a shared-savings invoice. This is not a build problem the founders can vibe-code their way around; it is a methodology-integrity problem that must be calibrated against real before/after compressor measurements on the first handful of sites. If the predicted savings reliably track measured savings within a defensible tolerance, the recurring model is durable and the dashboard becomes a powerful retention moat; if they do not, no amount of clean software saves a business whose core claim does not hold up.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- On your first 3 paid sites, how will you measure ACTUAL energy reduction (compressor amp-draw / run-hours / kWh before and after) to validate that your predicted CFM-to-dollar savings are accurate, and what tolerance counts as "credible"?
- Do target customers expect, now or soon, live compressor telemetry / IoT monitoring rather than periodic manual surveys — and if so, who builds and maintains that, given engineering is the team's weakest capability?
- How do you standardize the survey-capture protocol so two different technicians surveying the same plant produce comparable total-CFM numbers, so your quarter-over-quarter trend line is trustworthy?
- Will you offer the shared-savings billing option, and if so, whose meter and whose methodology is the contractual source of truth when the customer disputes the measured savings?
- Where do technician-uploaded facility photos live, and is that storage private-by-default with per-tenant access control from day one?

RECOMMENDATION: GO
