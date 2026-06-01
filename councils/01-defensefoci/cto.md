CTO REVIEW — Managed FOCI Mitigation & NISPOM Compliance for Small Cleared Defense Contractors

ONE-PARAGRAPH TECHNICAL READ
Technically a document-and-workflow SaaS wrapped around a managed compliance service — the software is a boring, very buildable CRUD + document-management + scheduler app, not a research problem. The hard part is that the customer's data is classified-adjacent: NISPOM/32 CFR Part 117 artifacts (TCP, ECP, visitor/IT-access controls, self-inspection findings) describe how a cleared facility protects classified information, and FOCI documents describe foreign-ownership structures. That data is mostly not classified itself, but it is Controlled Unclassified Information (CUI) and acutely sensitive, so the security posture and hosting decision (FedRAMP/IL-equivalent, possibly NIST 800-171/CMMC on your own house) is the load-bearing requirement, not the feature set. For a two-founder bootstrap the build is small (8–12 dev-weeks for a real MVP); the security/self-compliance burden is what can quietly become a permanent tax and a sales blocker.

ARCHITECTURE SKETCH
- Frontend: standard Next.js/React workspace on a managed host — dashboards for compliance calendar, self-inspection checklists, findings/remediation tracker, training records, evidence library. No exotic UI.
- Backend: single Postgres-backed app (Node/TS or Python/Django) — tenants (per cleared facility), users/roles (FSO, GSC member, advisor, founder), document versioning, deadline scheduling. Bulk of the build, conventional.
- Document/evidence store: object storage (S3-class) with versioning, immutability/object-lock for the "tamper-evident evidence library," per-tenant encryption keys. Where real security design lives.
- Scheduler/async: background worker (cron + queue) driving recurring-obligation calendar, reminders, annual self-inspection kickoffs. Low complexity.
- AI/document generation: LLM behind a server-side prompt layer for drafting policies, TCP/ECP boilerplate, GSC minutes, intake summarization. Assistive, human-in-the-loop, NOT autonomous — the biggest data-handling decision, because you cannot send CUI to a consumer LLM endpoint.
- Auth: SSO/MFA (Auth0/WorkOS/Okta), strong MFA, RBAC, full audit logging from day one — non-negotiable for this buyer.
- Hosting: the real complexity. Defense procurement/security will ask whether the platform meets NIST SP 800-171 / handles CUI appropriately and is FedRAMP-aware; architecture must be deployable into a US-region, access-controlled, audit-logged, ideally CUI-capable enclave (AWS GovCloud / Microsoft GCC High). Complexity hides in the hosting/compliance envelope and the LLM data path, not the code.

BUILD PLAN TO REVENUE-EARNING MVP
8–12 weeks of one dev's effort; first dollars earnable via the managed service (setup engagement) BEFORE the software is fully built.
1. Tenant + auth + RBAC + audit logging (2–3 wks) — must be right first time; not punt-able.
2. Compliance calendar + scheduler + reminders (1–2 wks) — retention engine; ship early.
3. Document/evidence library with versioning, object-lock immutability, per-tenant encryption (2–3 wks) — the "tamper-evident" promise.
4. Self-inspection checklist + findings/remediation + DCSA review-prep export (2 wks) — core deliverable.
5. AI-assisted document generation with compliant LLM path + human review gates (1–2 wks) — PUNT to v2; early customers served with templates + advisor labor.
The setup/readiness engagement ($10K–$30K [ASSUMED; verify 3–5 calls]) is deliverable services-led in week 1 while software is built — the right bootstrap shape.

CRITICAL ASSUMPTIONS
1. Compliance artifacts are CUI, not classified, and can lawfully live on a properly secured commercial cloud. If any customer needs to store actual classified material, the architecture is wrong. Verify against 32 CFR Part 117 + advisor in week 1.
2. An LLM can lawfully/reliably draft NISPOM/FOCI boilerplate without exposing CUI out-of-boundary. Verify a CUI-eligible LLM path (Azure OpenAI GCC High, Bedrock GovCloud, or self-hosted) and prototype 5 real drafts for advisor accuracy review.
3. Customers will accept a SaaS vendor holding their security-program evidence. Cleared FSOs are professionally paranoid; willingness unproven. Verify with 8–10 discovery calls.
4. The buyer's procurement security review of YOUR platform is passable by a bootstrap. Ask 3 targets what primes/DCSA expect of subcontractor SaaS vendors handling CUI (800-171 self-attestation? CMMC? FedRAMP?). Determines whether self-compliance overhead is months or years.
5. The named cleared practitioner is reliably available and legally-required roles can be filled by partners. Business/legal assumption gating the offering. Verify with signed advisor LOI before build.

INFORMATION SECURITY POSTURE
The dimension that defines the business. Data: per-facility compliance documents, TCP, ECP, IT/visitor access controls, FOCI structure details, self-inspection findings (a roadmap of where the facility is vulnerable), training records, GSC minutes. Some of the most sensitive non-classified data a defense supplier holds; an aggregated cross-contractor database is a counterintelligence target of real value. Threat model must include nation-state-grade adversaries and insider risk. Controls at LAUNCH (not later): US-only hosting with no foreign-national admin access (pointed, given customers are FOCI firms — your own supply chain must be clean), encryption at rest with per-tenant keys + in transit (TLS 1.2+), enforced phishing-resistant MFA, least-privilege RBAC, immutable audit logging, object-lock on the evidence library, secrets in a managed vault with rotation, documented incident response. At SCALE: align your own platform to NIST SP 800-171 (plausibly CMMC) because you're a CUI-handling vendor — a real ongoing program on yourselves. SOC 2 Type II is table stakes and likely insufficient alone; FedRAMP or GovCloud/GCC High residency may be demanded. The LLM data path is the sharpest hazard: any CUI to a non-CUI-boundary model is a reportable spillage. PII is minor relative to CUI exposure. A breach here is national-security-adjacent — could end the company and trigger DCSA/FBI involvement.

SCORES (1–10)
1. Technical feasibility:             8  — Document-management + scheduler + RBAC on Postgres/Next.js/S3-object-lock is proven, boring tech; LLM use assistive/human-gated, not load-bearing.
2. Build vs. buy posture:             8  — Auth, object storage with object-lock, scheduler, LLM API all bought; thin custom wedge is the compliance-workflow layer (~8–12 dev-weeks).
3. Architecture cleanliness:          7  — Few moving parts, clean, but GovCloud/CUI-enclave hosting adds non-trivial complexity around a simple core.
4. Time to revenue-earning MVP:       8  — Setup engagement bills week 1 services-led; software MVP 8–12 one-dev-weeks; revenue doesn't wait on full product.
5. Technical-assumption risk:         5  — Hinges on CUI-not-classified and a CUI-eligible LLM path; verifiable cheaply but unconfirmed, and a wrong data-classification call is fatal.
6. Third-party dependency risk:       6  — Replaceable vendors, but a mandatory CUI-boundary host (GovCloud/GCC High) locks you to a narrow, costlier set.
7. Data architecture quality:         7  — Per-tenant isolation, versioned immutable evidence store, owned/portable; clean, but aggregated sensitivity is as much liability as moat.
8. Information security posture:      6  — Serious designable posture, but nation-state threat model + likely 800-171/CMMC-on-yourself means launch security heavier than normal SaaS — caps a bootstrap's realistic readiness.
9. Scaling headroom:                  8  — Per-facility tenant model on Postgres + object storage scales to thousands without rewrite; binding constraint is human advisor throughput, not architecture.
10. Maintenance burden:               6  — App low-maintenance, but ongoing security/compliance of your own CUI-handling platform (audits, 800-171 evidence, IR drills, LLM-boundary vigilance) is a permanent non-trivial tax for two founders.

AVERAGE SCORE: 6.9 / 10

TOP 3 TECHNICAL STRENGTHS
- Small, boring, proven software wedge: document management, scheduler, RBAC, immutable evidence store — 8–12 dev-weeks with off-the-shelf components.
- Revenue doesn't wait on the build: setup/readiness engagement bills week 1 services-led; cash-flow-positive potential before product finished.
- Clean, scalable per-facility tenant data model; software layer supports 100x launch volume without rewrite.

TOP 3 TECHNICAL RISKS
- The CUI/classification call: if any in-scope artifact is classified (or a customer expects you to hold classified material), commercial-cloud SaaS is categorically wrong and the business can't be built as described.
- Your own platform's compliance burden: handling defense-contractor CUI likely forces NIST 800-171 (plausibly CMMC) and possibly GovCloud/GCC High on yourselves — a permanent, expensive program and a hard procurement gate to first enterprise close.
- The LLM data path: routing CUI through a non-CUI-boundary model is a reportable spillage with national-security consequences; the AI scale lever must be fenced into a CUI-eligible boundary or kept off CUI, constraining the automation that gives margin.

BIGGEST SINGLE RISK
The product centralizes, across many cleared suppliers, exactly the data a foreign intelligence service most wants: a structured, queryable library of each contractor's security-control plans, foreign-ownership structures, and self-inspection findings (an enumerated list of where each facility is weak). That aggregation turns a modest SaaS into a nation-state-grade target, and the bar to hold it responsibly is a defense-grade posture: US-only infra with provably no foreign-national admin access (doubly pointed since customers are FOCI-flagged), per-tenant encryption, immutable audit, mature incident response, and almost certainly a NIST 800-171/CMMC-aligned program on your own house, possibly in GovCloud/GCC High. Not impossible, but it converts the lean two-founder bootstrap into one carrying a continuous costly compliance/security obligation on itself, and a single spillage/breach is plausibly a company-ending, DCSA/FBI-involving incident. The founders' SOC 2/HIPAA/GDPR background is relevant scaffolding, but defense CUI/800-171 is a meaningfully higher bar; underestimating it is how this build silently goes wrong.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- Are all in-scope artifacts (TCP, ECP, self-inspection records, GSC minutes, FOCI docs) legally CUI/business-sensitive and NOT classified — confirmed by the advisor and against 32 CFR Part 117 — and will you contractually refuse to hold classified material?
- What exactly will customers' primes and DCSA require of a SaaS vendor storing their CUI: SOC 2 only, 800-171 self-attestation, CMMC, or FedRAMP/GovCloud residency? (Swings security cost/time from weeks to years.)
- What is the CUI-eligible path for AI document-generation (Azure OpenAI GCC High, Bedrock GovCloud, self-hosted) or do you keep CUI out of the LLM entirely? Have you prototyped + advisor-checked 5 real generated documents?
- Can you guarantee no foreign-national administrative/developer access to the platform/infra, and is your own supply chain clean enough to pass scrutiny from FOCI-mitigated customers?

RECOMMENDATION: REFINE
The software is genuinely easy and the revenue-before-product shape excellent, so technology is not the obstacle — the security/compliance envelope is, and it must be designed in from day one. Refine before committing: (1) week 1, get the advisor to confirm in writing the CUI-not-classified classification and contractually exclude classified material, killing the fatal-architecture scenario; (2) run 3–5 procurement-security interviews to pin down whether 800-171/CMMC/GovCloud is required of your platform, and price that program explicitly; (3) decide the LLM-on-CUI boundary deliberately — default to keeping CUI out of the model and using AI only on non-sensitive boilerplate at launch, treating the CUI-eligible LLM path as a v2 decision. Make those calls and this is a clean, buildable, defensible technical plan.
