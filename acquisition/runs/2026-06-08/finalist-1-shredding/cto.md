# CTO REVIEW — Regional Secure Document-Destruction (Shredding) Company

## ONE-PARAGRAPH TECHNICAL READ
This is a route-based field-service business almost certainly running on paper, a
generic accounting package, and a calendar in the owner's head — which is exactly the
profile the founders' edge is built for. The inherited systems are thin and likely
unsupported, but that is GOOD news here: there is little legacy lock-in to fight,
the data that matters (the recurring customer/route schedule) is small and structured
enough to digitize, and a proven, vertical, off-the-shelf SaaS category (route-based
service / shredding-specific platforms like CERO/BHS/Shred-Tech ROM, or generalist
Jobber/Housecall Pro) exists to drop the whole operation onto. The two real technical
risks are (a) the inherited data lives on paper and in one retiring person's memory,
so migration is a manual transcription project, not an export; and (b) the
compliance artifact — the Certificate of Destruction and chain-of-custody — is the
product's legal value, so any new system must reproduce it auditably from day one, not
"later."

## INHERITED-SYSTEMS SKETCH
- **Accounting:** Almost certainly QuickBooks Desktop or QuickBooks Online, possibly an
  outside bookkeeper. [ASSUMED — verify the exact product/version and who administers it;
  Desktop is end-of-life-ward and a migration item.]
- **Scheduling / dispatch / routing:** Likely paper route sheets, a wall calendar, and
  the owner's/dispatcher's memory — NOT routing software. This is the core operational
  debt and the biggest modernization prize.
- **Contracts:** Paper, signed once years ago, auto-renewing, filed in cabinets. No
  e-sign, no central contract repository, terms and renewal dates not queryable.
- **Certificates of Destruction / chain-of-custody:** The compliance product. Today
  likely carbon-copy paper books or a Word/PDF template printed per job. Not searchable,
  not customer-self-serve, a liability if a customer ever needs to produce one for a
  HIPAA/FACTA audit and it's misfiled.
- **Invoicing / billing:** Paper or QuickBooks manual invoices; recurring billing run by
  hand monthly. No card-on-file/ACH autopay, so DSO and collections effort are higher
  than they need to be.
- **Website / lead gen:** Thin or dated brochure site, no SEO, no paid search, no online
  quote/booking. Effectively no digital front door.
- **Data condition:** The "database" is the route schedule + customer list + pricing,
  spread across paper, QuickBooks customer records, and the owner's head. Small in row
  count (hundreds of accounts), exportable in principle, but dirty and incomplete.
- **Lock-in:** LOW. No bespoke custom system mentioned; the risk is paper/tribal
  knowledge, not a proprietary platform you can't escape.

## MODERNIZATION PLAN

### 90-day quick wins (configure + migrate, weeks of effort)
1. **Route/field-service platform** — stand up **Jobber or Housecall Pro** (generalist,
   ~$200–$500/mo) for scheduling, recurring jobs, mobile driver app, and digital service
   confirmation; OR a **shredding-vertical platform (CERO Live / BHS / Shred-Tech ROM)**
   if console/bin tracking and per-container weights matter for billing.
   **Effort:** [ASSUMED 3–6 weeks] to configure recurring routes + migrate the account
   list. Verify by counting active accounts and whether route/frequency data exists in
   any digital form. **Gain:** dispatcher labor cut, fewer missed/duplicated stops,
   driver accountability.
2. **Digital invoicing + autopay** — **QuickBooks Online + Stripe/QBO Payments** with
   card-on-file/ACH on recurring contracts. **Effort:** [ASSUMED 2–3 weeks]. **Gain:**
   DSO from ~45 to ~15–20 days [ASSUMED], lower collections labor; verify current DSO
   from the AR aging in diligence.
3. **Digital Certificate of Destruction + chain-of-custody** — generate the certificate
   automatically from the completed job in the FSM platform, emailed to the customer and
   stored in a searchable customer portal. **Effort:** [ASSUMED 2–4 weeks] (template +
   workflow config). **Gain:** removes the single biggest compliance/liability exposure;
   becomes a sales differentiator vs. paper-filing competitors.
4. **E-sign contracts** — **DocuSign/PandaDoc** for renewals and new accounts; load
   existing contracts into a repository with renewal dates surfaced. **Effort:** [ASSUMED
   1–2 weeks]. **Gain:** queryable renewal pipeline, no re-paper churn at transition.

### Longer program (3–12 months)
5. **Website + local SEO + paid search + online quote** — rebuild the front door
   (WordPress/Webflow + Google Business Profile + Google/Bing Local Service Ads).
   **Effort:** [ASSUMED 4–8 weeks build + ongoing]. **Gain:** a real inbound channel to
   replace the owner's word-of-mouth, capturing the under-marketed small-account segment
   the nationals (Shred-it/Stericycle, Iron Mountain) ignore.
6. **CRM + sales automation** — **HubSpot (free→Starter)** for the pipeline, automated
   review requests (Google reviews), and email nurture to dormant purge-job customers.
   **Effort:** [ASSUMED 3–5 weeks].
7. **Route optimization + density** — once jobs are digital, layer routing optimization
   (built into the vertical platforms, or **Routific/OptimoRoute**) to add stops per
   route-mile. **Gain:** the real margin lever — more revenue per truck-hour without
   adding trucks.
8. **AI layers (thin, on top — not core):** an **AI phone/booking agent** (e.g.,
   voice-AI receptionist) to capture after-hours quote calls; **AI-drafted** marketing/SEO
   content and review responses; AI-assisted route-frequency upsell ("this account's
   volume suggests weekly, not monthly"). Honest limit: AI does NOT touch the physical
   shred operation, chain-of-custody, or weights — it's a front-office/marketing multiplier
   only.

## CRITICAL ASSUMPTIONS
1. **The customer/route schedule can be reconstructed digitally.** If frequencies,
   console counts, and pricing live only on paper and in the owner's memory, migration is
   weeks of manual transcription, not an export. *Verify:* ask for the QuickBooks customer
   export + any route sheets during diligence; sample 20 accounts for completeness.
2. **Drivers will adopt a mobile app.** Route drivers who've run paper for 25 years may
   resist tablets/phones. Adoption, not software, is the stall point. *Verify:* meet the
   crew, check driver tenure/age, gauge openness pre-close.
3. **The Certificate of Destruction has no hidden regulatory format requirement** beyond
   what a configurable template covers (NAID AAA, HIPAA, FACTA). *Verify:* confirm whether
   NAID AAA is held and what its audit demands of the documentation system.
4. **No proprietary scale/weighing or truck telematics is locked to a single vendor**
   whose data you can't extract for billing. *Verify:* inventory the shred trucks'
   onboard systems and how per-job weights are currently captured/billed.
5. **QuickBooks data is clean enough to port to QBO.** Desktop-to-Online migrations
   surface dirty historical data. *Verify:* get a copy of the company file for a test
   migration in diligence.

## INHERITED INFORMATION-SECURITY POSTURE
The irony is sharp: this is a **data-DESTRUCTION** company whose own **data-PROTECTION**
hygiene is almost certainly weak. It holds customer PII-adjacent records (account
contacts, service addresses, billing), employee records (drivers' PII, payroll), and —
critically — **chain-of-custody and Certificate-of-Destruction records that are the
legal proof its customers rely on for their own HIPAA/FACTA compliance.** Likely inherited
neglect: no MFA on email/QuickBooks, shared passwords, certificates stored as loose
paper/files with no backup, an aging office PC as the single point of failure, and
ransomware exposure on that PC. **First-90-day controls:** enable MFA everywhere
(Microsoft 365/Google Workspace, QBO, banking); move to a managed cloud backup of the
QuickBooks file and all certificate records; replace shared logins with named accounts;
basic endpoint protection on office machines; and — highest priority — get
Certificates of Destruction into an immutable, backed-up, searchable store, because losing
that record set is not just an IT problem, it's a breach of the core compliance promise to
customers and a litigation exposure. **At scale:** a written information-security policy,
NAID AAA-aligned controls, vendor/payment PCI scope kept minimal by using
Stripe/QBO-hosted payment (never storing card data), and incident-response basics. None of
this is heavy — it's standard SaaS hygiene, achievable in the first quarter — but it is
non-optional given what the certificates represent.

## SCORES (1–10)
1.  Inherited systems condition:        4  — Likely paper routes + QuickBooks + owner's memory; thin and dated, but not catastrophic one-PC chaos.
2.  Technical & data debt:              5  — Data is dirty and partly on paper/tribal, but small (hundreds of accounts) and structurally simple to clean.
3.  Modernization upside — tech/AI:     9  — Glaring, high-ROI off-the-shelf wins: Jobber/Housecall Pro routing + QBO/Stripe autopay + digital CoD + local-SEO front door, all deployable in <90 days on a business with none of them.
4.  Effort to modernize:                7  — Quick wins are configure-and-migrate, not build: [ASSUMED 3–6 wks] for FSM + [ASSUMED 2–3 wks] for billing; the only real labor is paper-to-digital data entry.
5.  Critical dependency risk:           7  — No proprietary platform lock-in cited; main dependency is tribal knowledge in the retiring owner, which is people-risk more than tech-risk.
6.  Cybersecurity posture inherited:    4  — Almost certainly no MFA, shared passwords, unbacked paper certificates; fixable but a real inherited liability given chain-of-custody stakes.
7.  Data ownership & migration:         6  — Data is owned and QuickBooks-exportable, but route/contract/certificate data on paper makes migration a manual transcription project, not a clean export.
8.  Automation / AI leverage:           7  — Real labor-saving on dispatch/billing/collections and lead-winning via AI booking agent + automated reviews/SEO content; honest limit — AI can't touch the physical shred/custody chain.
9.  Scaling / tech headroom:            8  — A SaaS FSM stack (Jobber/Housecall Pro or shredding-vertical CERO/BHS) scales to more trucks, routes, and bolt-on acquisitions with no re-platform.
10. Ongoing maintenance burden:         8  — Post-modernization it's all managed SaaS (QBO, Stripe, Jobber, HubSpot, DocuSign) — no custom code, no on-call, runnable by two owner-operators.

## AVERAGE SCORE: 6.5 / 10

## TOP 3 TECHNICAL STRENGTHS
- **Greenfield modernization on a real business:** near-zero legacy lock-in means the
  founders deploy a proven off-the-shelf stack (Jobber/Housecall Pro + QBO/Stripe +
  DocuSign + HubSpot) onto a cash-flowing operation in under 90 days, not after a build.
- **Small, simple, ownable dataset:** hundreds of structured recurring accounts —
  migratable and cleanable — not millions of rows in a proprietary trap.
- **Self-running SaaS end state with clear automation ROI:** autopay kills DSO, routing
  software adds stops per route-mile, and an AI booking agent + automated reviews/SEO
  open an inbound channel the nationals ignore — all maintainable by two operators.

## TOP 3 TECHNICAL RISKS
- **Migration is manual transcription, not an export:** route frequencies, console
  counts, pricing, and contract terms likely live on paper and in the owner's head.
- **Compliance artifact must be reproduced auditably from day one:** the Certificate of
  Destruction / chain-of-custody is the legal product; any gap during cutover is a
  customer-compliance and liability exposure, not a cosmetic one.
- **Inherited security neglect on the very thing customers trust:** weak hygiene (no MFA,
  unbacked certificate records) at a company whose value proposition is data protection.

## BIGGEST SINGLE RISK
The biggest systems risk is that **the operating knowledge that makes the routes
profitable — which account is serviced how often, at what price, with how many consoles,
and which renewal is due when — exists nowhere as clean digital data; it lives on paper
route sheets and in the retiring owner's 25-year memory.** Modernization assumes you can
get this into a system; in reality you may be hand-transcribing it during the same window
you're trying to retain drivers and customers through an ownership change. If that
transcription is rushed or incomplete, you get missed stops, mis-billing, lost recurring
revenue, and — worst case — a Certificate of Destruction you can't produce when a customer
faces a HIPAA/FACTA audit. The mitigation is to treat data capture as a pre-close /
first-30-day project with the owner still on hand during a transition consulting period,
NOT as something the founders do after he's gone.

## QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- **Can the customer/route/pricing data be exported from the current system in a usable
  format, and how much of it is paper-only or in the owner's head?** Get the QuickBooks
  export and any route sheets, and sample 20 accounts for completeness before close.
- **How are Certificates of Destruction and chain-of-custody records created and stored
  today, and is NAID AAA certification held with any prescribed documentation format?**
  This dictates how the new system must reproduce the compliance artifact.
- **How are per-job weights and console counts captured and billed — manually, or via
  truck-mounted scales/telematics tied to a specific vendor?** Determines whether billing
  data is portable or vendor-locked.
- **Will the route drivers (tenure/age) adopt a mobile app, and will the owner commit to a
  transition consulting period to transfer route knowledge into the new system?**
- **What does the office PC/network look like — MFA, backups, shared passwords — and where
  do certificate records physically/digitally live today?**

## RECOMMENDATION: GO
Technically this is a clean, attractive modernization target: low legacy lock-in, a small
ownable dataset, a mature off-the-shelf SaaS category to drop onto it, and quick wins
deliverable in under 90 days with a self-running end state — exactly the founders' edge.
The GO is conditioned on two diligence items that, if they fail, flip this to RE-TRADE:
(1) confirm the route/contract/certificate data can actually be captured digitally with
the owner's help during a transition period (not after his exit), and (2) confirm the
Certificate-of-Destruction/chain-of-custody workflow and any NAID AAA documentation
requirements can be reproduced auditably in the new stack from day one. Both are
addressable; neither is a reason to walk — but the founders must price the
data-transcription and security-hardening work into the first-90-day plan rather than
assume "it's all on paper, we'll just digitize it."
