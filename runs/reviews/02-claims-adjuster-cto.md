CTO REVIEW — Independent Claims Adjuster Workspace

ONE-PARAGRAPH TECHNICAL READ
This is a mobile-first photo-and-file capture app with a structured-data backbone and document generation — fundamentally a well-trodden field-data-collection SaaS pattern (a vertical-specific cousin of CompanyCam, ServiceTitan field apps, or Procore's photo module), not a research problem. The hard parts are not the core capture loop, which is boring and buildable; the real complexity hides in two places: (1) the offline-first sync architecture demanded by adjusters working catastrophe zones with no connectivity, and (2) the "carrier-ready format" claim, which is a long-tail integration and template-maintenance treadmill rather than one clean spec. The "automatic labeling/tagging by area and damage type" is the one line that quietly imports ML/computer-vision risk the founders cannot operate themselves, and it must be scoped down to manual-tagging-plus-templates for the MVP. For a two-founder bootstrap with one prototype-grade coder, this is feasible but will need a real engineer earlier than most concepts because offline sync and conflict resolution is genuinely hard.

ARCHITECTURE SKETCH
- Frontend: cross-platform mobile app (React Native or Flutter) for on-site capture; React/Next.js web app for file assembly, claim pipeline, firm admin. Mobile is the load-bearing surface.
- Offline-first local store on device (SQLite/WatermelonDB or Realm) with a sync engine to the backend — the single most complex subsystem; photos and notes must be captured with zero connectivity and reconcile later.
- Backend: standard API (Node/Postgres or Django/Postgres) on a managed host (Render/Fly/AWS). Postgres holds claims, photo metadata, scope notes, checklist state, deadlines.
- Object storage for photos (S3 or Cloudflare R2) — high volume: hundreds of photos per claim × thousands of claims is the cost/bandwidth center of gravity. Thumbnail + compression pipeline needed.
- Document generation: server-side PDF assembly (Puppeteer-to-PDF, or DocRaptor/Carbone) producing the photo report + narrative + checklist in carrier templates. Templates are config/data, not code, or maintenance explodes.
- Async/background: image processing, thumbnailing, PDF rendering, sync conflict resolution want a job queue (managed queue + workers, or Inngest/Trigger.dev).
- Auth: email/password + SSO-light via managed provider (Auth0, Clerk, Supabase Auth); multi-tenant with firm-level roles.
- ML/AI (danger zone): "automatic labeling by area and damage type" implies vision classification. Punt to v2. MVP uses structured manual tagging with smart defaults + voice-to-text via OS/native APIs or Whisper.
- Integrations: exports to estimating tools (Xactimate/Symbility) and carrier portals — almost certainly file-export and manual-upload at first, not live API, because those systems are closed.

BUILD PLAN TO REVENUE-EARNING MVP
Estimate: ~18–28 dev-weeks of one capable developer to a revenue-earning MVP — notably longer than generic CRUD SaaS because of offline sync. With prototype-grade founder coding (Jon ~3–4/10 today, 5–6 with effort), this realistically means hiring one real mobile/sync engineer for ~3–4 months, affordable inside the $100k–$250k ceiling but a meaningful slice of it.
1. Core capture + claim model (4–6 dev-weeks): mobile photo capture, per-claim organization, manual area/damage tagging, voice-to-text scope notes, measurement/moisture fields.
2. Offline-first sync engine (5–8 dev-weeks): local store, background sync, conflict resolution, large-photo upload resumption. The chunk that blows estimates; cannot be punted (CAT-zone-no-connectivity is the wedge).
3. File assembly / PDF generation (3–5 dev-weeks): templated carrier-ready package, checklist with missing-item flagging. Start with 2–3 most common carrier formats, not "all carriers."
4. Pipeline + web admin + billing (3–4 dev-weeks): claim status board, deadlines, Stripe subscription billing, seat management, firm roles.
5. Auth, multi-tenancy, hosting hardening (2–3 dev-weeks): managed auth, tenant isolation, encryption, backups.
Punt to v2: CV auto-classification; live API integrations to carrier portals and Xactimate; usage-metering refinements; catastrophe-deployment team features.

CRITICAL ASSUMPTIONS
1. "Automatic labeling/tagging by area and damage type" deliverable without a real CV model. Verify: interview 10 adjusters, confirm structured manual tagging with templates is acceptable (almost certainly yes).
2. "Carrier-ready format" is a small, stable set, not a sprawling per-carrier matrix. Verify: collect actual required-photo-report specs from the 3–5 largest carrier IA programs and measure variance.
3. Adjusters accept manual upload/export to carrier portals rather than live integration (portals are closed and won't grant a small vendor API access early). Verify: ask 10 adjusters whether "generate the package, I upload it" is good enough.
4. Offline sync at the photo volumes described (hundreds/claim, dozens of claims in a CAT deployment, intermittent rural connectivity) is reliable enough that adjusters trust it with pay-determining files. Verify: build sync first, stress-test airplane mode with a 300-photo claim.
5. The founders can hire a mobile/offline-sync engineer inside budget (specialized skill; engineering is the team's gap). Verify: get a fixed-bid or 3-month contractor quote for the sync subsystem before committing.

INFORMATION SECURITY POSTURE
Data is moderately sensitive but not the worst class: property addresses, photos of damaged homes/interiors (incidentally occupants, documents, license plates), insured names, claim numbers, adjuster identity. PII bordering on sensitive; not HIPAA or card data, but a breach of "photos of thousands of people's homes tied to insurance claims" is a real reputational/contractual event. Where it lives: photos in object storage, metadata in Postgres, copies cached on adjuster devices (a meaningful exposure — lost/stolen trucks and phones). Controls at launch: TLS 1.2+ in transit; encryption at rest on object storage and DB (S3/R2 SSE + Postgres encryption); managed auth with strong passwords and optional MFA; strict tenant isolation; device-level encryption requirement and remote-wipe/token-revocation for lost devices; signed expiring URLs for photo access; audit logging of file access and exports; encrypted tested backups with retention policy. At scale, when an IA firm or carrier asks: SOC 2 Type II will come up because carriers impose vendor-security requirements on their IA networks — architecture should be SOC2-attainable (centralized logging, access reviews, least-privilege); a managed stack (Auth0/Clerk + AWS/GCP + Vanta) makes that a ~6-month lift, not a rebuild. The non-obvious threat is the offline device cache — the most likely breach vector is a stolen phone in a CAT zone, not the server, so device encryption + revocation must be designed in from day one.

SCORES (1–10)
1. Technical feasibility: 7 — Boring proven stack end-to-end (React Native + Postgres + S3 + server-side PDF); the only non-trivial subsystem is offline sync, hard-but-solved with WatermelonDB/Realm-class tools, not research.
2. Build vs. buy posture: 7 — Most assembled (managed auth via Clerk, Stripe billing, R2 storage, Inngest queues, DocRaptor/Carbone PDFs); the genuine custom wedge is the sync engine and capture/assembly UX.
3. Architecture cleanliness: 6 — Reasonable shape but multiple interacting systems (mobile local store, sync engine, object storage, PDF pipeline, web admin) and an inherent offline/online dual-state that adds real moving parts.
4. Time to revenue-earning MVP: 5 — ~18–28 dev-weeks with offline sync on the critical path; honestly mediocre because it is well past the <8-week ideal and likely needs a hired engineer.
5. Technical-assumption risk: 6 — Most assumptions cheaply verifiable with adjuster interviews, but "auto-labeling by damage type" and "carrier-format universality" carry scope-creep risk if taken literally.
6. Third-party dependency risk: 7 — Few brittle critical dependencies if integrations stay file-export (no reliance on closed Xactimate/carrier-portal APIs); swappable vendors for auth, storage, PDF.
7. Data architecture quality: 7 — Owned, portable data in Postgres + own object storage; clean multi-tenant model, no vendor lock on the data; main wrinkle is high-volume image storage cost.
8. Information security posture: 6 — Standard controls well understood, but the offline device cache of homeowner photos is a real exposure that must be designed for (device encryption + remote revocation), and SOC2 will be demanded by carrier networks before it's built.
9. Scaling headroom: 7 — Postgres + object storage + stateless API + job queue scales to many thousands of adjusters without rewrite; first strain is storage/bandwidth cost and PDF-render throughput, both solvable with caching and async workers.
10. Maintenance burden: 5 — Honestly mediocre: the carrier-template treadmill plus mobile-OS upgrade churn plus sync-edge-case bugs make this a continuous engineering commitment, not a self-running app, for a two-person team.

AVERAGE SCORE: 6.3 / 10

TOP 3 TECHNICAL STRENGTHS
- The core stack is boring and proven; nothing requires invention, and a bootstrap can buy auth, billing, storage, queues, and PDF generation off the shelf, building only the capture UX and sync wedge.
- The data is owned and portable (Postgres + own object storage), no value-path dependency on a closed third-party API as long as carrier/estimator integration stays file-export.
- Scaling profile is benign: a stateless API over Postgres and object storage with async workers scales to thousands of seats before any re-architecture; cost growth (image storage) is predictable.

TOP 3 TECHNICAL RISKS
- Offline-first sync of large photo volumes in zero-connectivity CAT zones is the genuinely hard subsystem; get it wrong and adjusters lose pay-determining files — fatal to trust — and it sits on the critical path and inflates the build estimate.
- The "carrier-ready format" promise is a long-tail, ever-changing template-maintenance treadmill that quietly becomes a permanent operational engineering load for a two-founder team.
- The "automatic labeling by damage type" line imports computer-vision/ML risk the founders cannot operate; if taken literally for MVP it becomes a research project disguised as a feature.

BIGGEST SINGLE RISK
The offline-first sync engine is the technical issue most likely to break this business. Adjusters work the exact conditions where connectivity is worst — rural storm zones, blue-tarp neighborhoods after a hurricane, the inside of a flooded house with no signal — and they capture the documentation that literally determines whether and how much they get paid. The product's whole promise ("every claim file before you leave the site") depends on capturing hundreds of large photos plus structured notes entirely offline and reliably reconciling them later without losing, duplicating, or corrupting a single file. Offline sync with conflict resolution and resumable large-binary upload is one of the genuinely hard problems in mobile engineering; it is solvable with mature tools (WatermelonDB, Realm, resumable upload protocols), but it is precisely the kind of subsystem where a prototype-grade builder ships something that demos perfectly on office wifi and then silently drops a photo on adjuster number forty's truck in week three — which permanently destroys the trust the product runs on. This is why I'd insist the sync engine be built and abused first, before any other feature, and why it argues for hiring a real mobile engineer early rather than vibe-coding it.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- Is reliable offline capture-and-sync in zero-connectivity CAT zones a hard requirement for v1, and have you scoped who builds the sync engine — the single subsystem most likely to require a real mobile engineer and to blow the timeline and budget?
- When you say "automatic labeling/tagging by damage type," do you mean computer-vision classification or structured manual tagging with templates? If the former, who builds and operates the model, and have you confirmed manual tagging isn't already good enough for MVP?
- How many distinct carrier "required package" formats actually exist among your early customers' carriers, how often do they change, and who owns keeping templates current — a 5-template config job or a permanent integration treadmill?
- For homeowner-photo data cached on adjuster devices, what is your plan for device encryption, lost-device token revocation/remote wipe, and breach notification — and will carrier IA networks require SOC 2 before letting their adjusters use the tool?
- Will carrier portals and estimating tools (Xactimate/Symbility) be file-export only at launch, and have you validated that adjusters accept "generate the package, I upload it" rather than expecting live integration you cannot get API access to?

RECOMMENDATION: REFINE
