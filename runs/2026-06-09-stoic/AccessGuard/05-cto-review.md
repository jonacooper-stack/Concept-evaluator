CTO REVIEW — AccessGuard

ONE-PARAGRAPH TECHNICAL READ
Technically this is a comfortable bootstrap: the hard parts are mostly assembled from mature, boring components — a headless-browser crawler (Playwright) wired to the open-source axe-core accessibility rules engine, a Postgres database, a thin Next.js dashboard, and a scheduler. Nothing here is a research problem. The genuine technical caveat is that automated accessibility scanning only catches roughly 30-40% of WCAG 2.1/2.2 AA success criteria; the remaining defensible value (keyboard traps, screen-reader semantics, focus order, alt-text quality, the documentation trail that actually deflects a demand letter) is human expert work, not code. So the "software product" is really a software-leveraged services business where the crawler is the top-of-funnel and the recurring monitoring artifact, and the remediation/attestation is delivered by people. That is an honest, buildable shape — the risk is not feasibility but that the team mistakes the easy 35% for the whole product and ships a glorified scanner that plaintiffs and their experts can pick apart.

ARCHITECTURE SKETCH
- Frontend: Next.js dashboard on Vercel — client portal showing scan results, remediation queue, downloadable VPAT/accessibility-statement/audit-trail PDFs. Standard CRUD + report rendering. Low complexity.
- Backend: Node/TypeScript (one language across crawler + axe-core, which is JS-native); API on a managed host (Render/Fly/AWS Fargate). Job orchestration via a queue (BullMQ on Redis, or SQS).
- Crawler/scanner: Playwright headless Chromium rendering each page (must render JS — modern sites and third-party widgets are client-side), injecting axe-core to evaluate WCAG rules. The real engineering: crawl-budget control, sitemap + link discovery, auth'd-page scanning (checkout/booking behind login), de-duplication of templated pages, screenshot capture for evidence. Where complexity lives.
- Data store: Postgres for scan results, findings history (the dated audit trail is the product — append-only/immutable findings table matters), client/site config. Object storage (S3) for screenshots and PDFs.
- Async/background: scheduled recurring crawls, queued scan workers, PDF generation. Headless-browser fleet is the cost/ops center of gravity.
- Integrations: GitHub/GitLab API to deliver remediation as PRs; optionally Shopify/WordPress APIs/plugins; Stripe for billing; email/notification. None bet-the-business.
- ML/AI: optional and non-critical — an LLM could draft remediation guidance, summarize findings, or first-pass alt-text, but nothing depends on AI correctness. Do NOT let AI generate legal-attestation language unreviewed.
- Auth/hosting: standard managed PaaS; client portal needs proper multi-tenant auth (Clerk/Auth0/Cognito). Crawler workers need careful secrets handling for client site credentials.

BUILD PLAN TO REVENUE-EARNING MVP
Estimate: ~8-12 dev-weeks of one developer to first paying "active-litigation onboarding" client; the very first revenue can precede the software, because the rapid-response service can be delivered with off-the-shelf tooling and human work while the product is built.
1. (Weeks 0-2) Scanner core: Playwright + axe-core against a list of URLs, store findings + screenshots, dedupe templated pages. Load-bearing. (~2 wk)
2. (Weeks 2-4) Crawl orchestration: sitemap/link discovery, scheduled recurring crawls, authenticated-page scanning, crawl-budget limits. (~2 wk)
3. (Weeks 4-7) Client portal + reporting: Next.js dashboard, findings triage, and the revenue artifact — VPAT-style report, accessibility statement, dated remediation audit trail PDF. (~3 wk)
4. (Weeks 7-9) Billing + multi-tenant auth + GitHub PR delivery. (~2 wk)
5. (Punt to v2) Direct CMS plugins, LLM-assisted remediation drafting, self-serve onboarding, white-glove SOC2 controls.
Critically: the manual expert audit and demand-letter evidence file — the legally defensible parts — are human deliverables on day one regardless of software maturity. Revenue does NOT wait on the full build; a founder can close and service the first just-sued client in week 1-2 with a manual audit + a Google-Docs report, then productize the recurring monitoring behind it.

CRITICAL ASSUMPTIONS
- Automated scanning covers enough to be the recurring "monitoring" hook. [ASSUMED: axe-core detects ~30-40% of WCAG AA issues — well-established, not controversial.] Verify: run axe-core against 5 known-sued sites vs. the actual cited violations in their public complaints.
- The crawler reliably renders/scans modern JS-heavy/widget-laden sites. Verify: point Playwright+axe at 10 real mid-market e-commerce/booking sites; measure render failures, dynamic-content gaps, bot-blocking (Cloudflare/Akamai).
- The "defensible documentation" actually moves the needle with defense counsel. A legal assumption gating the whole value prop. Verify: interview 3-5 ADA defense attorneys on what evidence helped/hurt in real settlements before building report templates.
- Drift is real/frequent enough to justify recurring fees. [ASSUMED plausible.] Verify: re-scan 5 target sites weekly for a month, quantify new violations.
- Remediation can be delivered without owning the client's codebase. The PR-to-dev-team model assumes clients have a dev team; many mid-market Shopify/WordPress clients do not. Verify: ask 10 prospects who would actually implement a fix.

INFORMATION SECURITY POSTURE
Data collected is moderate-sensitivity but the threat model is real. AccessGuard stores: client site URLs and crawl results, screenshots of client pages (checkout/account pages can incidentally capture PII/PCI if the crawler authenticates), client-supplied site/CMS/login credentials for authenticated scanning, and — most sensitively — a documented record of every accessibility defect on a client's site, i.e., a curated list of that client's legal vulnerabilities. That findings database is a juicy target: a breach would hand plaintiff firms a pre-built evidence file against every client at once. That elevates infosec from "nice later" to "designed in from day one."
Controls at launch: encryption at rest (Postgres + S3 KMS) and in transit (TLS); a real secrets manager for crawl credentials (AWS Secrets Manager/Doppler/Vault — never env vars or DB plaintext); strict tenant isolation (row-level scoping, tested); least-privilege founder access; audit logging on who viewed which client's findings (which doubles as product value); avoid storing checkout/account PII — scan representative pages rather than logging into real customer accounts, and scrub/redact screenshots. Incident response: written plan + breach-notification. SOC 2 Type II will be asked for by regulated buyers within year one; the founders' SOC 2 operator background makes ~3-6 month attainment realistic once revenue justifies it.

SCORES (1-10)
1. Technical feasibility: 8 — Playwright + axe-core + Postgres + Next.js is proven end-to-end; the automated-scan core is ~2 dev-weeks and axe-core is the de-facto open-source standard (used by Google Lighthouse and Microsoft Accessibility Insights). No research risk.
2. Build vs. buy posture: 8 — axe-core, Playwright, Stripe, Clerk/Auth0, PDF generation all off-the-shelf; the only true custom wedge is crawl orchestration + the reporting/audit-trail artifact, buildable in ~5 dev-weeks.
3. Architecture cleanliness: 7 — Few moving parts and clean separation (scanner workers / Postgres / portal), but the headless-browser worker fleet plus authenticated-page scanning adds a genuine operational surface.
4. Time to revenue-earning MVP: 8 — First revenue can precede software via manual audit + rapid response, and the productized recurring MVP is ~8-12 dev-weeks; revenue decoupled from build, ideal bootstrap profile.
5. Technical-assumption risk: 6 — Core scanner assumptions are well-established, but the load-bearing assumption (that automated scanning + documentation deflects suits) is legal, not technical, and unverified by the team.
6. Third-party dependency risk: 7 — Dependencies (axe-core, Playwright, GitHub/Shopify/WP APIs, Stripe) are replaceable open standards or commodity services; minor exposure if axe-core's rule coverage shifts, but it's open source and forkable.
7. Data architecture quality: 6 — Simple, owned, portable Postgres+S3, but the data is as much liability as moat (a centralized list of every client's legal vulnerabilities).
8. Information security posture: 6 — Required controls (KMS, Secrets Manager, tenant isolation, audit logging) are standard and the founders have SOC 2 experience, but security must be designed-in because the findings DB is a high-value breach target; not yet evidenced as designed-in.
9. Scaling headroom: 7 — Postgres + queued stateless Playwright workers scale horizontally to thousands of sites with no rewrite; the first strain is headless-browser compute cost, manageable by sampling/scheduling.
10. Maintenance burden: 6 — Crawlers are maintenance-prone (sites change, anti-bot defenses evolve, axe-core updates, JS edge cases), and the manual-audit component is a permanent human load that does not self-run.

AVERAGE SCORE: 6.9 / 10

TOP 3 TECHNICAL STRENGTHS
- The entire stack is boring and proven: axe-core (the open-source industry-standard engine behind Lighthouse) + Playwright + Postgres + Next.js + Stripe; no research risk, ~8-12 dev-weeks to a productized MVP.
- Revenue is decoupled from the build — the human audit and rapid-response can be sold and delivered in week one with off-the-shelf tools, funding the product build from cash flow.
- The recurring monitoring artifact (dated, append-only audit trail) is simultaneously the product, the legal deliverable, and a defensible data asset — clean alignment of tech, value, and retention.

TOP 3 TECHNICAL RISKS
- Automated scanning catches only ~30-40% of WCAG AA criteria; if the team over-trusts the crawler, the deliverable is legally weak and the human-expert audit (a non-scaling cost) is doing the real work.
- The findings database is a single concentrated breach target — a curated list of every client's legal vulnerabilities — that turns a routine breach into a catastrophic, suit-triggering event for the whole book.
- Crawler maintenance is a permanent tax: JS-heavy sites, third-party widgets, anti-bot defenses, and axe-core rule churn silently degrade scan reliability.

BIGGEST SINGLE RISK
The biggest technical-into-business risk is the gap between what the software can prove and what actually defends a client in court. Automated tooling reliably detects only about a third of WCAG AA criteria, and the issues most cited in real ADA web complaints (keyboard navigation, focus management, screen-reader compatibility, meaningful alt text, accessible names) are precisely the ones automation handles poorly. If the founders build a slick scanner and sell its green dashboard as "provably accessible," they create a document that a plaintiff's expert can dismantle — and worse, a paper trail showing the client believed they were compliant while obvious manual-only defects remained. The defensibility rests on the human-audit layer and on what defense attorneys actually find persuasive, neither of which technology guarantees. This is also where cost bites: the part that scales (crawler) is the part that doesn't fully protect the client, and the part that protects the client (expert manual audit + remediation) is the part that doesn't scale. The whole margin and durability story depends on getting that automation-to-human ratio right — an unproven assumption the team must validate before betting the build.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- When you run axe-core against the actual sites cited in 5 recent public Title III complaints, what fraction of the specifically cited violations does the automated scan catch? (Sizes how much value must be human-delivered and your true gross margin.)
- What is the planned automation-to-manual-audit ratio per client per month, and what does the human-hours cost do to gross margin at $2,500/mo ARPU?
- Who actually implements remediations for a Shopify/WordPress mid-market client with no in-house dev team — PRs (assumes a dev team), direct edits (assumes access + liability), or a to-do list (weak)?
- How will you handle the findings database as a breach target from day one — tenant isolation, secrets management, screenshot PII redaction, and whether you ever authenticate into real customer accounts?
- Will the scanner authenticate into checkout/booking/account flows, and if so, how do you avoid capturing PCI/PHI/PII and tripping clients' anti-bot systems?

RECOMMENDATION: GO (with one scoping discipline)
The technology is feasible, cheap, and buildable in ~8-12 dev-weeks on a boring proven stack, with the rare bonus that first revenue precedes the software via human-delivered rapid response, and the founders' SOC 2 operator background directly de-risks the one infosec concern that matters (the concentrated findings database). The single discipline I require: do not position or build this as an automated-scanner SaaS. The crawler is the monitoring hook and top-of-funnel; the defensible product is the human-audited documentation, and the team must validate (a) the automated-vs-cited-violation coverage on real complaints and (b) the gross-margin impact of the manual-audit labor before scaling. Architect the findings store as a high-value breach target from line one. If those validations hold and the manual-audit ratio keeps unit economics intact, this is a clean technical GO.
