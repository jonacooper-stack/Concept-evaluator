CTO REVIEW — ProxyDocket

ONE-PARAGRAPH TECHNICAL READ
ProxyDocket is technically tractable for a two-founder bootstrap, but its software is mostly a rules-and-deadlines engine plus a document/mailing pipeline — boring, proven tech — wrapped around a delivery model whose true value is the named specialist's judgment, not the code. The honest technical risk is not "can they build it" (they can) but "does software meaningfully compress the work given that NAUPA report generation is a solved, commoditized capability (UPExchange, Sovos) and the genuinely hard parts — messy client AP/AR/payroll/GL ingestion and exemption judgment — resist automation." The first revenue-earning MVP is almost entirely a services engagement with a thin internal tooling layer; the defensible custom build (a maintained 50-state deadline/exemption rules engine + clean multi-source ingestion) is real but is a perpetual maintenance treadmill rather than a one-time build, and that treadmill is the central technical liability.

ARCHITECTURE SKETCH
- Frontend: a thin internal-ops + client-portal app (Next.js on Vercel, or Retool for the internal side to save weeks) — dashboards for property-by-state status, mailing tracking, deadline calendar, document repository. Most "product" value is operator-facing at MVP.
- Backend: standard API (Node/TS or Python/FastAPI) on a managed host (Render/Fly/Fargate). The core custom asset is a 50-state rules engine: dormancy periods by property type, due-diligence windows/thresholds, B2B and de-minimis exemptions, deadline/format per state. Config-as-data (rules tables), not ML.
- Data store: Postgres (managed) holding client property records, owner PII, dormancy state, report history, audit trail. System of record + the audit-defense file.
- Ingestion: the real complexity. Client AP/AR/payroll/GL exports arrive as CSV/Excel/ERP extracts (NetSuite, SAP, Oracle, Workday, QuickBooks) in inconsistent schemas. MVP = templated CSV/Excel mapping with human-in-the-loop reconciliation; no magic auto-parsing.
- Report generation: emit NAUPA II (and the NAUPA-format variants states accept) flat files — a known documented spec, but already commoditized by UPExchange/Sovos, so building from scratch is arguably wasted effort vs licensing/integrating.
- Due-diligence mailings: integrate a print-and-mail API (Lob) for the required owner letters; track returns/responses. Simple async queue (SQS/BullMQ/cron) for mailing windows + deadline reminders.
- Async/scheduled: a deadline/calendar scheduler driving alerts + remittance prep across staggered 50-state dates. Cron-grade complexity.
- ML/AI: none required; the founders should resist pretending otherwise. LLMs could assist exemption-rule drafting or document triage internally, but nothing customer-facing should bet on model reliability for legal determinations.
- Auth/hosting: standard managed IdP (Auth0/Clerk/Cognito), RBAC, single cloud region.
Complexity hides in two places: keeping the 50-state rules engine correct/current, and ingesting/reconciling each client's messy financial data into clean reportable-property records.

BUILD PLAN TO REVENUE-EARNING MVP
Total: ~10-16 dev-weeks of one developer to a chargeable state, because first clients are sold as a service and the software backs the operator. You do NOT need the full 50-state engine to earn the first dollar — you need the handful of states a design-partner client reports into.
1. Auth + client/entity data model + property-records schema + document repository (2-3 wks). Off-the-shelf auth; schema is the load-bearing design work.
2. Ingestion v1 — templated CSV/Excel upload with mapping UI + human reconciliation workflow (3-4 wks). The gnarliest chunk; do NOT auto-detect schemas at MVP.
3. NAUPA report generation — for the 5-10 states first clients need, not all 50 (2-3 wks IF built; ~1 wk if you license UPExchange/Sovos output and wrap it). Strongly consider buy-over-build.
4. Due-diligence mailing workflow via Lob + response tracking + deadline scheduler (2-3 wks).
5. Audit-defense file / report history / export (1-2 wks).
Punt to v2: full 50-state coverage (expand state-by-state as clients demand), auto-schema-detection ingestion, direct ERP API connectors, client self-serve portal, VDA workflow tooling. First 2-3 clients delivered with a partly-manual operator process behind a thin tool — appropriate, but it means early revenue is service-shaped, not product-shaped.

CRITICAL ASSUMPTIONS
1. NAUPA report generation is not the wedge (the one-pager flags UPExchange/Sovos already produce NAUPA files). If the founders believe rebuilding this is their moat, the build is misdirected. Verify: spend one week with UPExchange and a sample dataset; confirm report-gen is commodity and pivot budget to ingestion + service layer.
2. Messy multi-source ingestion is automatable enough to scale margins. [ASSUMED 30-60% lands clean on first pass.] If lower, every client is a heavy manual reconciliation project and leverage evaporates. Verify: get 3 real anonymized AP/AR/payroll extracts and time manual mapping.
3. The named escheatment specialist is hireable/retainable affordably; the entire credibility + audit-defense value rests on this judgment. Verify: one outbound test to fractional UP specialists / ex-Big-4 practitioners for a day-rate before building.
4. A maintained 50-state rules engine can be kept current by a two-person team; staleness causes client penalties. Verify: check whether a maintained ruleset can be licensed (Sovos/Eagle content) rather than hand-maintained.
5. Clients will hand GL/payroll PII to a young vendor. Verify: in the first 5 sales calls, ask what security attestation they require before sharing data.

INFORMATION SECURITY POSTURE
Genuinely sensitive data: owner PII (names, last-known addresses, SSNs in securities/dividend property), client financial records (AP/AR/payroll/GL), and the audit-defense file that is, by design, what a state auditor will scrutinize. Threat model: (a) breach of owner PII triggering state breach-notification, (b) data-integrity failure producing a wrong report + client penalty (as damaging as a breach here), (c) insider/access mistakes given operator-heavy workflows. Controls at launch (not later): encryption at rest (managed Postgres KMS) + in transit (TLS), managed IdP with RBAC + MFA, comprehensive audit logging (doubles as the audit-defense trail product feature), secrets in a manager (not env files), least-privilege access, documented retention/deletion. SOC 2 Type II is table stakes the moment a mid-market+ customer's vendor-security review hits — exactly this customer profile; founders' real SOC 2 Type II experience makes it bridgeable and a sales asset (budget ~$15-40K, a few months). Written IR + breach-notification playbook mandatory given multi-state PII. Not security-novel, but "fix it later" would directly undermine the product's premise (clean, defensible files).

SCORES (1-10)
1. Technical feasibility: 8 — Boring proven stack end-to-end (Postgres + Node/Python + Lob + Auth0); zero research-grade problems; NAUPA II is a documented flat-file spec and rules are config-as-data, not ML.
2. Build vs. buy posture: 5 — Mixed; auth/mailing/hosting off-the-shelf, but the team risks rebuilding NAUPA report-gen that UPExchange/Sovos commoditize, and the rules-content + ingestion are real custom work.
3. Architecture cleanliness: 6 — Conceptually simple (CRUD + scheduler + mailing pipeline), but the 50-state rules engine plus multi-schema ingestion add meaningful surface area beyond a clean single-purpose app.
4. Time to revenue-earning MVP: 7 — ~10-16 dev-weeks to a chargeable service backed by thin tooling for a handful of states, since first clients are sold as a managed service, not full-coverage product.
5. Technical-assumption risk: 5 — The margin-critical bet (messy AP/AR/payroll/GL ingestion automates well enough to scale) is unverified, and the wedge-vs-commodity question on report-gen is unresolved.
6. Third-party dependency risk: 7 — Dependencies few and replaceable (Lob, managed Postgres, an IdP); no single brittle API on the critical path, though licensing UP rules-content would add a content vendor.
7. Data architecture quality: 6 — Owned, portable Postgres system-of-record with a natural audit trail, but it holds high-sensitivity PII + client financials, making it as much liability as asset.
8. Information security posture: 7 — Standard controls fully achievable and founders have real SOC 2 Type II experience, making attestation a bridgeable sales asset — but the PII/financial sensitivity makes it mandatory from day one, capping the upside.
9. Scaling headroom: 6 — Software scales fine technically; the bottleneck is human specialist review + manual ingestion reconciliation per client, operational not architectural, but it caps margin leverage.
10. Maintenance burden: 4 — The 50-state rules engine is a perpetual treadmill (statutes/dormancy/formats change across jurisdictions) where staleness directly causes client penalties; a permanent, accuracy-critical engineering obligation for two people.

AVERAGE SCORE: 6.1 / 10

TOP 3 TECHNICAL STRENGTHS
- No research risk and no ML dependency: every component (rules-as-data engine, NAUPA flat-file output, Lob mailings, scheduler, Postgres) is proven and within a single developer's reach.
- Founders' real SOC 2 Type II experience makes the otherwise-mandatory security/attestation burden a bridgeable strength and even a sales differentiator for the mid-market+ buyer.
- First revenue doesn't require the full build — a ~10-16 dev-week thin-tool-plus-service MVP covering a client's actual filing states can earn money before the 50-state engine exists.

TOP 3 TECHNICAL RISKS
- Perpetual 50-state rules-maintenance treadmill where staleness causes client penalties — an accuracy-critical, never-finished engineering obligation that fits a lean two-person team poorly unless content is licensed.
- Messy, heterogeneous client AP/AR/payroll/GL ingestion may resist automation, turning every client into a manual reconciliation project and collapsing the software-leverage margin story.
- Risk of building the wrong thing — sinking dev-weeks into NAUPA report generation UPExchange/Sovos already commoditize, instead of the genuine wedge (ingestion + service + maintained content).

BIGGEST SINGLE RISK
The maintenance treadmill of a correct, current 50-state rules-and-format engine combined with the unverified automatability of client data ingestion. Unlike typical SaaS where code stabilizes after launch, escheatment statutes, dormancy periods, exemption thresholds, and formats change across 50 independent jurisdictions every year, and a stale rule does not merely annoy a user — it produces a wrong filing that exposes the client to interest, penalties, and a Kelmar-style audit, the exact harm the product promises to prevent. That makes the rules engine a permanent, high-stakes engineering liability for two people, not a buildable asset that recedes. Layered on, if source-data ingestion requires heavy per-client manual reconciliation (the likely reality with SAP/Oracle/Workday/NetSuite/QuickBooks exports), the business behaves like a labor-bound consulting practice wearing a software costume — the software does not compress the work, margins stay services-grade, and the team carries both the reconciliation load AND the rules-maintenance load. The mitigation that resolves both is the same: license maintained UP rules-content (Sovos/Eagle) rather than hand-maintaining it, and validate ingestion effort on real client data before committing the build — but until verified, the defensible-software premise is unproven.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- Are you building NAUPA report generation, or licensing/wrapping UPExchange/Sovos? If rebuilding, what is the justification given it is openly described as commoditized — and where is your custom wedge if not there?
- On 3 real anonymized client extracts (AP/AR/payroll/GL), how many dev-hours to map and reconcile into clean reportable-property records, and what fraction lands clean on first pass? (Determines whether the margin story holds.)
- How will the 50-state rules-and-format engine be kept current — hand-maintained, licensed content, or specialist review — and what is your liability exposure if a stale rule causes a client penalty?
- Given owner SSNs + client financials in the system of record, what security attestation do your first 5 targets require before sharing data, and what is your timeline/budget to SOC 2 Type II?
- What is the specialist's day-rate/equity arrangement, and how many client-hours of expert review per engagement — does human review scale sublinearly with revenue, or linearly?

RECOMMENDATION: REFINE
The technology is feasible and buildable; not a no-go on technical grounds. But as scoped, the build risks targeting the commodity (report generation) while leaving the two hard, margin-determining problems — messy ingestion and a perpetually-maintained 50-state rules engine — unresolved. Before committing build-weeks: (1) run the ingestion timing experiment on 3 real client extracts to confirm software actually compresses the work; (2) decide explicitly to license maintained NAUPA rules-content (Sovos/Eagle) rather than hand-build/maintain, redirecting dev effort to the ingestion + service wedge; (3) lock the named specialist's economics to confirm expert review scales sublinearly with revenue. If ingestion proves automatable and content is licensed, this moves toward GO with a clean ~10-16 dev-week MVP; if ingestion is heavy and content must be hand-maintained, it is a labor-bound consulting practice in software clothing and the maintenance-burden score (4) becomes the whole story.
