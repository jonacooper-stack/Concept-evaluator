CTO REVIEW — FranAudit

ONE-PARAGRAPH TECHNICAL READ
This is a thin-software-layer-over-a-services-business, and that framing is the key to the technical verdict. The genuinely automatable parts — a deadline/compliance calendar, a structured FDD document-assembly engine with data reuse across the 23 items and across the ~13 registration states, a per-state filing-status tracker, and an attorney sign-off workflow — are all boring, proven CRUD-plus-document-generation work that one capable developer can build with off-the-shelf tooling in roughly 9–14 dev-weeks. The danger is that the highest-value-sounding piece — "multi-state filing" — is, by the concept's own honest note, NOT API-driven for most states: it is a manual paper/portal grind that software can organize but not eliminate. So the real product is a workflow/document system plus a human filing-operations team, and the technical risk is low precisely because the software ambition is modest; the business risk lives in the manual-ops and attorney-dependency layers, not in the code.

ARCHITECTURE SKETCH
- Frontend: standard multi-tenant web app — Next.js/React on Vercel, one portal for internal ops + a lighter client-facing view (document status, deadlines, e-signature requests).
- Backend: conventional app server (Node/TS or Python/Django), Postgres as system of record; nothing exotic.
- Data store: Postgres holding the structured franchisor profile (canonical data feeding the 23 FDD items — entity info, officers, litigation, outlet counts, fee schedules, FPRs) + a per-state filing ledger (status, fee paid, comment letters, deadlines). S3-equivalent object storage for generated PDFs/DOCX and uploaded audited financials.
- Document assembly: the real custom wedge. A templating engine (docxtemplater, or structured-content → PDF) mapping canonical data into the 23-item structure + state-specific cover pages/addenda. Where data-reuse value concentrates.
- Async/background: a scheduler/cron driving the deadline-calendar engine (120-days-after-FYE alerts, per-state renewal reminders, comment-letter SLAs). Low-volume, low-complexity.
- E-signature/sign-off: DocuSign/Dropbox Sign for attorney sign-off + franchisor approval — buy, not build.
- Integrations: CPA financials arrive as files/email (not API); state filings largely manual portal/paper. Essentially NO meaningful third-party API on the critical path — good for dependency risk, bad for the automation thesis.
- ML/AI: optional and non-load-bearing. An LLM could draft redline suggestions or summarize comment letters, but must NOT be on the critical path — every output attorney-reviewed.
- Hosting/auth: Vercel + managed Postgres (Supabase/Neon/RDS); auth via Clerk/Auth0/WorkOS. Standard.
The real complexity is correctly modeling the FDD's 23-item data schema and per-state filing rules so data genuinely reuses across items and states — a domain-modeling problem, laborious but not engineering-hard.

BUILD PLAN TO REVENUE-EARNING MVP
~9–14 dev-weeks of one developer, because the MVP can lean on human ops while the software matures.
1. Core multi-tenant CRUD + auth + franchisor data model (2–3 wks). Bought auth, Postgres, basic portal. The 23-item schema is the load-bearing design task.
2. Deadline/compliance calendar engine (1.5–2 wks). Cron + rules for FYE+120 days, per-state renewal windows, amendment triggers, comment-letter SLAs. Valuable, cheap.
3. Per-state filing ledger + status tracker + comment-letter log (1.5–2 wks). Spreadsheet-killer; high perceived value, low build cost.
4. FDD document-assembly engine (3–4 wks, the wedge). Template the 23 items + state addenda from canonical data; generate filing-ready DOCX/PDF. Start with one or two states, expand manually.
5. Attorney sign-off + franchisor approval workflow via DocuSign (1–1.5 wks). Bought integration + state machine.
Punt to v2: AI-assisted redlining/comment-letter summarization; SOC 2 formalization; any state-portal submission automation (likely never fully automatable). You do NOT need the document engine fully built to earn the first dollar — sign and service early clients with calendar + ledger + manual document work, then back-fill automation. Time-to-first-revenue is gated by acquisition, not code.

CRITICAL ASSUMPTIONS
1. FDD assembly genuinely compresses with software via data reuse. [ASSUMED 40–70% of per-renewal effort is reusable structured data; verify: take 3–5 real FDDs from public registries (CA DFPI, MN, WI publish them), diff a base FDD against its state addenda + prior-year version to measure boilerplate-with-variable-fill vs bespoke drafting.] If mostly bespoke, the software is a thin calendar and the margin thesis weakens.
2. State filing cannot be meaningfully API-automated. The concept concedes this. Verify by enumerating the ~13 states' submission mechanisms from regulator sites — a 2-day desk task. Plan must assume manual submission as steady-state.
3. A partnered attorney's sign-off can be a fast, scoped, repeatable step rather than a custom hourly engagement per client. If every FDD needs deep bespoke attorney hours, the "fixed fee, not hourly" positioning collapses on margin and the automation premise. Verify: one franchise attorney quotes a per-renewal flat review-only fee.
4. Non-attorneys can lawfully perform assembly/filing/PM without it being UPL in the relevant states. Legal, not technical — flag for the legal reviewer; cheap verification is a single consult.
5. State formats are stable enough that templates don't need constant rework. [ASSUMED infrequent; verify via 2–3 years of regulator bulletins.]

INFORMATION SECURITY POSTURE
Data: franchisor corporate financials (audited statements, FPRs), litigation history, officer PII, franchise-sale records — confidential business/financial data + modest PII; a confidentiality-and-integrity problem, not a regulated-PII (HIPAA/PCI) problem. Controls at launch (standard, within the founders' SOC 2 Type II background): TLS + at-rest encryption (managed-DB + S3), bought IdP with SSO/MFA, RBAC separating internal ops from client views, secrets in a managed vault, audit logging of who-touched-which-document, encrypted backups with tested restore, tight access to the attorney sign-off chain. Integrity matters acutely: a filing-ready legal document silently corrupted or tied to the wrong client is a liability event, so document versioning, immutability of filed versions, and an audit trail are first-class. SOC 2 attainable/worth pursuing early (buyers are compliance-minded; CPAs/attorneys will ask); founders' real SOC 2 experience makes it a 4–8 week formalization. Worst realistic incident: a missed-deadline-due-to-system-failure causing a registration to lapse — argues for redundant deadline alerting (system + human calendar).

SCORES (1-10)
1. Technical feasibility: 8 — Boring proven tech (Next.js + Postgres + DOCX templating + DocuSign); no ML on the critical path, no research problems; ~9–14 dev-weeks.
2. Build vs. buy posture: 8 — Auth, e-sign, hosting, DB all bought; the only genuine custom build is the FDD document-assembly engine (~3–4 wks), a thin defensible wedge.
3. Architecture cleanliness: 8 — Single Postgres system-of-record, one app server, one scheduler, one document pipeline; few interacting systems, no distributed-state complexity.
4. Time to revenue-earning MVP: 8 — First dollar gated by sales, not code; calendar + ledger + manual document service bills clients within weeks while the engine is back-filled (full MVP 9–14 wks).
5. Technical-assumption risk: 6 — The whole margin thesis rests on how much FDD assembly truly compresses with software vs remaining bespoke legal/clerical work — unverified; load-bearing assumption is domain, not code.
6. Third-party dependency risk: 8 — No critical-path API; only replaceable commodity vendors (auth, e-sign, hosting) with trivial swap cost — the absence of state e-filing APIs is bad for automation but good for dependency risk.
7. Data architecture quality: 7 — Simple, owned, portable Postgres + object storage; canonical franchisor profile clean to model, though document versioning/immutability must be designed in deliberately.
8. Information security posture: 7 — Standard confidentiality controls fully within the founders' proven SOC 2 Type II experience; sensitive financials/PII but no exotic regulated-data burden; needs deliberate document-integrity + redundant-deadline design.
9. Scaling headroom: 8 — Architecture trivially supports 100x clients (low write volume, document-centric); the binding scaling constraint is human filing/review labor, not the stack — the code never needs a rewrite.
10. Maintenance burden: 6 — Code is low-maintenance, but state-format/template upkeep and the per-renewal manual filing + attorney-review cycle are a permanent operational load on humans, not self-running.

AVERAGE SCORE: 7.4 / 10

TOP 3 TECHNICAL STRENGTHS
- No research risk and no critical-path third-party API: the entire system is commodity web tooling, and the lack of state e-filing APIs paradoxically removes integration brittleness.
- Genuinely small custom surface area: only the FDD document-assembly engine is bespoke (~3–4 wks); everything else is bought, so a single developer can ship and maintain it.
- Revenue is not blocked by build completion — the calendar + filing ledger alone are billable, letting the founders earn while automation matures.

TOP 3 TECHNICAL RISKS
- The automation/margin thesis is unverified: if FDD updating is mostly bespoke legal drafting rather than structured data-fill, the "software-leveraged fixed fee" story degrades into a relabeled services firm with thin tech leverage.
- Manual state-filing labor and attorney-review cycles are the true scaling ceiling; the software does not relieve the per-client human-hours that define unit economics.
- Data/document integrity and deadline reliability are liability-critical: a corrupted filing or a missed registration deadline caused by a system fault is real client-harm, demanding immutability, versioning, audit trails, and redundant alerting from day one.

BIGGEST SINGLE RISK
Not technical-build risk — the build is easy — it is that the central premise ("how much of FDD assembly + multi-state filing genuinely compresses with software") is unproven and may be largely false. If the bulk of an annual FDD renewal is bespoke legal judgment (litigation disclosures, FPRs, material-change analysis) and per-state submission is irreducibly manual portal/paper work, then the software is a glorified compliance calendar and document repository, the partnered attorney's hours dominate the cost structure, and the "fixed annual fee, not a law-firm hourly bill" positioning becomes a margin trap rather than a software-leverage advantage. In that world the company scales linearly with human labor and attorney availability, not with code — undermining both the gross-margin story and the founders' explicit aversion to a labor-heavy model. Cheaply testable before any code: diff a handful of real public FDDs across years/states to measure the boilerplate-vs-bespoke ratio, and get one franchise attorney to quote a flat per-renewal review fee.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What fraction of a typical annual FDD renewal is structured-data-fill/boilerplate (software-compressible) vs bespoke legal drafting? Show the diff of 3–5 real public FDDs across years/states.
- What is the actual submission mechanism for each of the ~13 registration states — portal, email, or paper — and how many person-hours does one full multi-state filing cycle take with vs without the tooling? Determines the human-labor ceiling and whether the model violates the no-field-ops/no-labor-heavy preference.
- Can the partnered attorney commit to a fixed, scoped, repeatable per-renewal review fee (review-only, not drafting), and does non-attorney assembly/filing avoid UPL in CA, NY, IL, and the other registration states?

RECOMMENDATION: REFINE
The technology is sound, cheap, and low-risk to build — on pure CTO criteria a clean 7.4. REFINE rather than GO because the build's ease masks an unvalidated business premise that determines whether the product has real software leverage at all. Before the ~9–14 dev-weeks, run two near-free desk experiments: (1) the public-FDD diff to quantify boilerplate-vs-bespoke (target: confirm ≥40–50% is data-fill before believing the automation thesis), and (2) a flat per-renewal attorney-review quote + a UPL check across the top registration states. If favorable, build calendar and filing-ledger first (billable immediately), document-assembly engine second; keep AI off the critical path as an attorney-reviewed drafting aid; design document immutability, versioning, and redundant deadline alerting in from day one. If the diff shows the work is mostly bespoke legal drafting, the software wedge is too thin to justify the positioning and the concept should be reshaped toward the calendar/tracking layer or abandoned.
