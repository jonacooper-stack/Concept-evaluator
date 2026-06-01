CTO REVIEW — Managed Certified-Payroll & Prevailing-Wage Compliance for Public-Works Contractors

ONE-PARAGRAPH TECHNICAL READ
A document-generation, rules-engine, and portal-integration problem wrapped in a managed-service shell — none research-grade, all buildable by a competent full-stack dev, and the right bootstrap move is to keep the managed-service human in the loop for v1 rather than fully automate the long tail of jurisdiction quirks. The two genuine landmines: (a) acquiring and keeping current the wage-determination and fringe-rule data across federal + 30+ state regimes, and (b) the agency-portal filing layer (DOL/SAM, LCPtracker, state systems), the dirtiest, most brittle integration surface, most likely to silently break. Good news for a bootstrap: you can ship revenue-earning value with humans filling automation gaps and a spreadsheet-grade rules engine for one or two states, because the customer buys outcome (a clean WH-347 filed on time), not software. The risk is mistaking "we'll automate filing into LCPtracker" for solved when it's a permanent integration-maintenance tax.

ARCHITECTURE SKETCH
- Frontend: thin Next.js/React on Vercel — project dashboard, deadline tracker, exception queue, document review/sign workflow. CRUD + workflow UI.
- Backend: normal app server (Node/TS or Python/FastAPI) on a managed host, Postgres as system of record (contractors, projects, workers, wage determinations, payroll periods, reports).
- Rules/calc engine (the real wedge): versioned, data-driven engine mapping (project location + classification + date) → prevailing wage + fringe, then validating gross/fringe/hours vs submitted payroll. Deterministic rules + lookup tables, NOT ML. Complexity hides in jurisdiction breadth and the change cadence of determinations.
- Data ingestion: CSV templates first, then connectors to QuickBooks/Foundation/Sage 300 CRE/ADP. CSV-first is bootstrap-correct.
- Document generation: WH-347 PDF + state-format generators (server-side PDF templating). Boring and proven.
- Portal filing layer (the brittle part): DOL, LCPtracker, MyLCM, Elation, state portals — mix of manual upload, file export, occasional API. Treat much as human-assisted RPA for v1.
- Async/background: scheduler (Temporal or cron + queue) for weekly deadline reminders, generation jobs, wage-determination refresh pulls. Deadline-tracking reliability is operationally load-bearing.
- ML/AI: optional/peripheral — LLM-assisted classification mapping + audit-correspondence drafting; NOT on the critical path; do not bet the rules engine on an LLM.
- Auth/hosting: off-the-shelf (Clerk/Auth0/Cognito), RBAC, single managed cloud.

BUILD PLAN TO REVENUE-EARNING MVP
~10–16 weeks of one dev to a revenue-earning MVP serving a handful of contractors in ONE or TWO jurisdictions (federal WH-347 + one heavy state, e.g. CA or NY), with the human covering what software doesn't yet automate.
1. Data model + payroll CSV ingestion + worker/classification mapping (2–3 wks).
2. WH-347 generation + validation rules for federal + one state, seeded with hand-loaded determinations (3–4 wks) — this plus a human reviewer is already sellable.
3. Deadline tracking, exception queue, audit-record store, contractor dashboard (2–3 wks).
4. Filing layer for the first one or two portals — likely manual-assisted (export + human upload) before API automation (1–2 wks).
5. Onboarding/billing (Stripe subscriptions + usage tiers by active project/crew) (1 wk).
Punt to v2: additional state regimes (load incrementally on demand), accounting-system connectors, automated portal RPA, LLM audit-response drafting, apprenticeship-ratio automation. The founders' compliance background + named advisor lets the human carry missing automation without blocking revenue — clears the "no 12-month build before revenue" bar.

CRITICAL ASSUMPTIONS
1. Wage-determination/fringe data sourceable and kept current affordably. Federal WDs published by DOL (SAM.gov) and downloadable; states vary, some publish poorly. Verify: spend two days pulling WDs for federal + two target states; confirm a parseable source + change frequency. Ugly-PDF-only states are manual cost centers.
2. Portal filing programmatic OR cheap by hand at MVP scale. LCPtracker and many state portals lack clean public APIs. Verify: open accounts, file one test report manually, document mechanics. Hand-upload-only → price human filing time per project per week.
3. Contractors will hand over payroll data and let you file under their certification. Reports signed under penalty of perjury by the contractor — verify the legal/workflow split (contractor e-signs). Ask three target contractors in discovery.
4. Rules stable enough to encode deterministically. Classification disputes, conformance, fringe-credit math have judgment calls. Verify with advisor: what fraction of weekly reports are mechanical vs human-judgment? That ratio is the gross-margin ceiling.
5. The 10–16 week estimate assumes ONE-to-TWO jurisdictions, not national. Broad multi-state on day one balloons the build and tips toward manual ops.

INFORMATION SECURITY POSTURE
Data: worker PII (names, addresses, last four SSN on WH-347, hours, pay rates), contractor financials, project data, in Postgres + document store — you are custodian of employee PII for many small employers, a real breach-liability and sales-objection surface. Threat model: account takeover exposing workforce PII, insider/access-control failure, leak of generated PDFs. Controls at launch: TLS + at-rest encryption (managed DB + encrypted object storage for PDFs), real secrets manager (no env-var keys in repo), least-privilege RBAC, full audit logging (needed anyway for the audit-ready record, doubles as security), MFA on all logins, scoped per-contractor isolation. At scale enterprise-ish GCs ask for SOC 2 — attainable here (simple single-cloud architecture; founders have run SOC 2 Type II per profile, a genuine de-risker). Written IR plan + breach-notification process before storing the first real SSN (state breach laws apply to employee PII). PII minimization is the cheapest win — store only required SSN digits, tokenize/mask.

SCORES (1–10)
1. Technical feasibility: 8 — Deterministic rules engine + PDF generation + portal export are proven, boring tech; no research problem; the hard part is data breadth, not capability (federal WDs downloadable from SAM.gov, WH-347 a fixed form).
2. Build vs. buy posture: 7 — Auth/billing/hosting/PDF libs off-the-shelf; the rules engine + jurisdiction data are the genuine custom wedge, appropriately thin for v1.
3. Architecture cleanliness: 7 — Postgres + app server + worker queue + thin UI is clean; filing-layer adapters are the one place sprawl creeps in.
4. Time to revenue-earning MVP: 8 — Federal + one-state managed service with humans in the loop is sellable in ~10–16 dev-weeks because the customer buys the filed outcome, not the software.
5. Technical-assumption risk: 6 — Bet-the-business assumption is per-jurisdiction wage-data availability + portal-filing mechanics; knowable but unverified and state-varying.
6. Third-party dependency risk: 5 — LCPtracker + state portals on the critical path with no clean public APIs and ToS exposure; dependent on systems you can't control that change without notice.
7. Data architecture quality: 7 — Owned Postgres + object store, portable/queryable; the audit-record requirement aligns with good data hygiene, though worker PII raises the liability profile.
8. Information security posture: 7 — Worker PII/SSN custody demands real controls, but the needed set is standard and the founders' SOC 2 Type II experience makes day-one design + later SOC 2 attainable.
9. Scaling headroom: 7 — Compute scales trivially (reports cheap to generate); what scales non-linearly is the human exception/judgment load and per-jurisdiction rule-encoding, not the DB.
10. Maintenance burden: 5 — Wage determinations change continuously and portals drift, so rules data + filing adapters are a permanent upkeep tax — an ongoing engineering-plus-compliance treadmill, not a self-running app.

AVERAGE SCORE: 6.7 / 10

TOP 3 TECHNICAL STRENGTHS
- Output is a fixed, legally-defined artifact (WH-347 + known state forms) — generation/validation are deterministic and testable, not probabilistic; quality is verifiable.
- Bootstrap-correct human-in-the-loop path: ship revenue in ~10–16 dev-weeks for one/two jurisdictions, automate the long tail only as customers pay; no long pre-revenue build.
- Security + audit reinforce each other — the audit-ready record doubles as access-logging/data-trail; founders' SOC 2 background makes the posture credible.

TOP 3 TECHNICAL RISKS
- Portal filing layer (LCPtracker, state e-filing) has no clean APIs, is brittle, can break/change silently — a permanent integration-and-RPA maintenance cost scaling with jurisdiction count.
- Wage-determination/fringe data across 30+ state regimes is fragmented and changes constantly; keeping current is open-ended upkeep, and getting it wrong creates customer liability (withheld payments, perjury exposure).
- The human judgment-call fraction (conformance, classification disputes, fringe credits) sets a hard automation/gross-margin ceiling; if too high, the business drifts toward labor-intensive ops.

BIGGEST SINGLE RISK
The jurisdiction-expansion treadmill colliding with filing-layer brittleness. Revenue depends on serving contractors across many regimes, but each new jurisdiction means encoding new wage-determination sources, fringe rules, and submission mechanics — and the submission side (LCPtracker, MyLCM, dozens of state portals) is exactly the un-API'd, change-without-notice surface that becomes permanent manual filing labor and silent failures. A silent filing failure is not cosmetic: a missed/mis-filed certified payroll withholds the contractor's progress payment — their worst nightmare and your direct accountability. So the system must be conservative, heavily alerting, human-backstopped — fine for a focused one-or-two-state launch, but quietly converts into a sprawling rules-and-RPA maintenance org if growth requires broad multi-state coverage. The founders must consciously choose: a deep one-or-two-state managed service (clean, defensible, software-leveraged) or a national-breadth product (trends toward a manual-ops compliance shop, pressuring tractability and margin).

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- For your first two jurisdictions, what is the actual machine-accessibility of wage determinations and the actual filing mechanism for each portal — API, file upload, or hand-keyed? (Open accounts and file one test report before writing the rules engine.)
- Who signs the certified payroll under penalty of perjury — the contractor or your specialist — and what e-signature/approval workflow keeps liability where it legally belongs while letting you prepare-and-file?
- What fraction of weekly reports require a genuine human judgment call vs mechanical generation, and how does it move as you add jurisdictions — that number is both your margin ceiling and hiring curve?
- Will you commit to a deliberately narrow footprint at launch (federal + 1–2 states), or does the sales motion require broad coverage that explodes the build/ops?
- What payroll/timekeeping systems do your first ten contractors use, and will CSV export carry you to revenue before building connectors?

RECOMMENDATION: GO (with one scope discipline)
Technically sound, buildable, bootstrap-appropriate: deterministic document generation + rules engine + managed-service human layer, shippable to revenue in ~10–16 dev-weeks for a focused footprint, no research risk, a security posture the founders are equipped to meet (SOC 2 background). The non-negotiable scope discipline is to launch narrow — federal Davis-Bacon + one or two heavy states — and treat portal-filing and per-jurisdiction wage-data layers as the permanent maintenance cost they are, expanding only as paying demand pulls. Verify wage-data sources and portal mechanics for the first two jurisdictions before committing engineering time; those two cheap experiments retire most assumption/dependency risk. Average lands 6.7 because the maintenance treadmill (dim 10) and un-API'd portal dependency (dim 6) are real and structural, not because anything is unbuildable.
