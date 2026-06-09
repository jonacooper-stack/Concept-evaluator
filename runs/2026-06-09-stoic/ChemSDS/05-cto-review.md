CTO REVIEW — ChemSDS

ONE-PARAGRAPH TECHNICAL READ
The buildable core is a well-understood document-management problem: a structured data model for chemical compositions, a rules engine that maps that data to GHS hazard classifications, a deterministic template renderer that emits 16-section SDS documents (PDF/HTML) and GHS labels, version control, and a hosted access portal — none of which is research-grade. The genuine technical risk is not the CRUD/portal layer (boring, off-the-shelf) but the GHS classification engine: GHS classification is criteria-codified (published cut-off concentrations, additivity formulas for mixtures, bridging principles, hazard-category tables), so a deterministic rules engine can do a large share — but the inputs (toxicological data per ingredient, mixture-specific test data, professional judgment on data gaps) are messy, and an automated misclassification is a legally-consequential, liability-bearing error, which is exactly why the model wisely keeps a chemist/toxicologist in the sign-off loop. For a two-founder bootstrap this is achievable: ~14-20 dev-weeks to a revenue-earning MVP if v1 leans on a curated hazard-data source plus chemist sign-off rather than fully automating mixture classification on day one. The deepest non-technical-but-CTO-relevant bomb is the authoritative hazard-data feed — building the engine is easy; sourcing trustworthy, licensable, current input data is the part that can quietly become the whole business cost.

ARCHITECTURE SKETCH
- Frontend: Next.js/React on Vercel for the internal authoring console + the branded customer SDS portal (thin multi-tenant read app: search, filter, current-version download, version history). Boring.
- Backend: Node/TypeScript or Python (FastAPI) on a managed host; Postgres (Supabase/RDS) as system of record for substances, formulations, classifications, document versions, tenant config.
- Classification engine: a deterministic rules service encoding GHS Rev 7 criteria — cut-off/concentration-limit tables, mixture additivity (ATE), bridging principles. Pure code + data tables, not ML. The wedge and where the careful work lives.
- Document/label rendering: templating + PDF pipeline (React-PDF, WeasyPrint, or headless-Chrome HTML-to-PDF) producing the 16-section SDS + GHS labels (pictogram SVGs standardized, free to embed). Deterministic, testable.
- Data store / ingredient hazard library: the critical dependency — a per-CAS hazard-property dataset (classifications, H/P-statements, physical/tox data). Licensed from a data vendor, curated in-house from public sources (ECHA C&L inventory, GESTIS, PubChem, NIOSH), or hybrid. The real moat and the real liability.
- Auth: off-the-shelf (Auth0/Clerk/Cognito) with multi-tenant RBAC; portal needs authenticated employee access and often public/link-based downstream-customer access.
- Async/background: version-diffing, bulk re-classification when a rule or ingredient datum changes (the 2026/2027 wave), label re-generation, notifications. Simple queue (BullMQ/SQS); nothing exotic.
- ML/AI: optional and non-load-bearing — an LLM could draft narrative sections (handling, storage, first-aid) for chemist review, but classification MUST stay deterministic.

BUILD PLAN TO REVENUE-EARNING MVP
Total ~14-20 dev-weeks of one developer (spread dominated by how much hazard data must be curated vs licensed).
1. Data model + ingredient hazard library bootstrap (~4-6 wks): schema for substances/CAS, formulations, classifications, documents, versions, tenants; load an initial hazard-property dataset. Data-quality-bound, could balloon if licensing falls through.
2. Classification rules engine for common cases (~3-4 wks): encode GHS Rev 7 health/physical/environmental criteria, mixture additivity (ATE), high-frequency hazard classes for target verticals (cleaners, coatings, lubricants). Punt the long tail to chemist-manual override in v1.
3. SDS + label rendering (~2-3 wks): 16-section template engine + GHS label generator. Deterministic, snapshot-testable.
4. Hosted portal + auth + versioning (~3-4 wks): multi-tenant branded library, search, current-version download, version history, employee + downstream-customer access. Largely off-the-shelf.
5. Chemist review workflow (~2 wks): sign-off queue, audit trail of who-approved-what, locked published versions. Essential for liability; NOT punt-able.
Punt to v2: full automation of rare hazard classes, EPCRA Tier II/SARA 312 module (manual/spreadsheet at first), distributor-system integrations, LLM-drafted narrative sections.

CRITICAL ASSUMPTIONS
1. A licensable or curatable per-substance hazard dataset exists at acceptable cost and currency. If founders must hand-curate tox data for thousands of CAS numbers with no feed, build cost explodes and currency becomes an ongoing burden. Verify: quotes from a hazard-data vendor + scope ECHA C&L + PubChem coverage for 50 real target-customer ingredients (how many resolve to a usable classification automatically).
2. Deterministic GHS rules cover "enough" of real formulations that chemist time per SDS is minutes, not hours. Verify: take 10 real SDS, run their compositions through a paper version of the rules, measure how often the engine's classification matches the published one.
3. Customers accept a vendor-hosted portal as their official right-to-know access point. Verify: ask 5 prospects.
4. The chemist sign-off scales without becoming the bottleneck. Verify: interview 2-3 GHS-qualified chemists on realistic review time per machine-drafted SDS.
5. Misclassification liability is insurable/contractually bounded. Verify with broker + counsel; ensure every published doc carries an immutable record of inputs, engine version, and approver.

INFORMATION SECURITY POSTURE
Data collected: customer chemical formulations (their core trade secret — composition + concentrations), product catalogs, ingredient/CAS data, generated SDS/labels, basic user PII. The crown jewel is the formulation data — more sensitive than typical SaaS PII; a breach there is a trust-ending event. Threat model: multi-tenant isolation failure, portal access-control errors, credential theft. Controls at launch: encryption at rest (managed Postgres TDE) + in transit (TLS); strict tenant isolation with row-level security + tested authorization; secrets in a manager; audit logging of every classification/edit/sign-off/publish (also serves compliance/liability); least-privilege RBAC separating authoring from portal-read. Incident response plan + tested backups + breach-notification contacts. SOC 2 attainable within months when asked (founders have real SOC 2 Type II program experience, materially de-risking this), likely not required to land SMB at launch. Formulation-confidentiality should be a sales asset, designed in from day one.

SCORES (1-10)
1. Technical feasibility: 7 — Boring proven stack (Next.js + Postgres + PDF templating); the only hard part, GHS classification, is criteria-codified rules not unsolved research, tractable with chemist backstop.
2. Build vs. buy posture: 7 — Portal/auth/PDF/payments off-the-shelf; the genuine custom wedge is the classification engine + hazard-data library, a defensibly thin but real build.
3. Architecture cleanliness: 7 — Few moving parts (one DB, one rules service, one renderer, one portal); complexity concentrates cleanly in the classification engine.
4. Time to revenue-earning MVP: 6 — ~14-20 dev-weeks [ASSUMED, range driven by data-licensing]; above the 8-week ideal because the data library + chemist-workflow chunks are unavoidable, not a quarters-long research slog.
5. Technical-assumption risk: 5 — Hinges on a licensable/curatable hazard dataset and on the rules engine covering enough of real mixtures to keep chemist time low; both verifiable but currently unproven, so honestly mediocre until tested.
6. Third-party dependency risk: 6 — No single brittle API for the app itself, but the hazard-data feed is a potential single critical dependency with real licensing/price exposure if not curated in-house.
7. Data architecture quality: 7 — Owned, portable Postgres system-of-record with clean versioning + immutable audit trail (per-document provenance of inputs + engine version + approver); formulation data is sensitive but well-contained by design.
8. Information security posture: 7 — Founders have real SOC 2 Type II experience; needed controls (TDE, RLS isolation, secrets manager, audit logging) are standard and designed-in; formulation confidentiality is the explicit threat to engineer against from day one.
9. Scaling headroom: 8 — Document-management + read-heavy portal scales trivially on managed Postgres + CDN-fronted static SDS PDFs; the human chemist-review step, not the architecture, is the throughput ceiling, and bulk re-classification is a simple queued batch job — supports 100x customers without rewrite.
10. Maintenance burden: 6 — Software runs itself, but the business carries permanent content-maintenance load (keeping the hazard library + rule tables current as GHS revisions and tox data change), ongoing engineering-adjacent work.

AVERAGE SCORE: 6.6 / 10

TOP 3 TECHNICAL STRENGTHS
- The hard part is codified, not research: GHS classification follows published criteria/cut-off tables/additivity formulas, so a deterministic rules engine (not ML) does the heavy lifting and is fully testable.
- Clean, scalable architecture: read-heavy portal + document store on managed Postgres + CDN scales 100x with no rewrite; bulk re-classification for the 2026/2027 wave is a simple queued batch job.
- Security/compliance maturity is in the founders' wheelhouse: real SOC 2 Type II experience + a naturally audit-logged domain means infosec and immutable provenance are designed-in.

TOP 3 TECHNICAL RISKS
- Hazard-data sourcing: the per-substance/per-mixture classification data feeding the engine is the true cost and currency dependency; if it can't be licensed affordably or curated reliably, the build's economics break.
- Classification coverage gap: if the deterministic engine handles too little of real mixtures, chemist review time per SDS stays high and the human becomes the cost/throughput bottleneck, undermining the productized-software thesis.
- Misclassification liability: an automated wrong classification is a legally consequential error; the architecture must guarantee chemist sign-off provenance + immutable audit trails — a shortcut here is a business-ending bug.

BIGGEST SINGLE RISK
The single biggest risk is the interaction between hazard-data quality and misclassification liability. The software is genuinely easy to build, but it is only as good as the toxicological/hazard input data feeding the classification engine, and that data is incomplete, scattered across public databases of varying authority, and sometimes only obtainable through expensive licensed feeds. If the engine classifies a mixture wrong because an ingredient's hazard datum was stale, missing, or mis-keyed, the resulting SDS and label are legally non-compliant documents the customer relied on for OSHA HazCom and downstream right-to-know — and ChemSDS authored and (via chemist) signed them. That is not a refundable SaaS bug; it is a potential liability event tied to worker safety. The architecture must be built around a defensible human-in-the-loop sign-off with immutable provenance, and the business must keep the hazard library current forever. Survivable, and the model anticipates it with chemist sign-off, but it means the founders cannot lean on "AI does the classification" to cut cost — the chemist is load-bearing, constraining both margin and throughput more than the one-pager's ARPU math implies.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- Where does the per-substance hazard/classification data come from, what does it cost, and how do you keep it current? Run the 50-ingredient coverage test against ECHA C&L + PubChem and get one vendor licensing quote before committing.
- On 10 real target-vertical formulations, what fraction of the GHS classification does a deterministic rules engine get right unaided, and how many minutes of chemist review does each remaining SDS need? This single experiment validates or kills the margin model.
- What is the chemist sign-off workflow and capacity model — one credentialed partner reviewing machine drafts (scalable) or an author-per-SDS consultancy in disguise (capped) — and what is the per-SDS human cost at your assumed ARPU?
- How do you bound misclassification liability — immutable provenance/audit trail, E&O insurance, contractual limitation — and have you priced it?
- Does the multi-tenant portal need true tenant isolation with row-level security from day one, and how will you prove formulation-confidentiality to a prospect (their trade secret, not just PII)?

RECOMMENDATION: REFINE
The technology is feasible and the architecture clean, scalable, and within a two-founder bootstrap's reach (~14-20 dev-weeks). REFINE not GO because two load-bearing assumptions are unverified and govern both build cost and unit economics: (1) the existence of an affordable, current hazard-data source, and (2) the deterministic engine covering enough of real mixtures that chemist review is minutes, not hours. Both are cheap to test before writing significant code — run the 50-ingredient coverage test and the 10-formulation classification-accuracy test, and get one data-licensing quote. If those land well, this becomes a GO with a thin, defensible custom wedge (rules engine + curated hazard library) wrapped in off-the-shelf infrastructure; if the engine covers little and the chemist must author each SDS by hand, it collapses into a manual consultancy with a portal bolted on, and the software-leverage thesis fails.
