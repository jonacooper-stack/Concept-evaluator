# SecureControls

## Business Plan
### Managed NIST SP 800-171 & SPRS Compliance Operations for Small Defense Subcontractors

**Version 1.0  |  June 2026**
*Confidential — for founders and prospective advisors*

---

### What this is (and how it differs from an enclave provider)

SecureControls is the **compliance-operations layer** for a small defense
subcontractor — the recurring service that gets the supplier's NIST SP 800-171
program built, gets its SPRS score correct, and keeps the whole evidence-and-
attestation machine current, quarter after quarter, so the supplier stays
prime-ready and audit-ready. It is **not** a cloud or secure-environment provider:
we do not stand up GovCloud enclaves, we do not host email, and — by deliberate
design — **we never take custody of the customer's Controlled Unclassified
Information (CUI).** We sit one layer up from the environment, as the team that
runs the program, maintains the documentation, manages the recurring SPRS and
questionnaire obligations, and stands next to the owner when a prime or a C3PAO
asks questions. We can layer on top of whatever environment the customer already
has — GCC High, a GovCloud enclave, or a small PreVeil-style footprint.

---

## Executive Summary

**The opportunity.** The Department of Defense's CMMC program is in active,
phased rollout: the program rule (32 CFR Part 170) has been in force since
December 2024, the acquisition rule (DFARS 252.204-7021) took effect November 10,
2025, and mandatory third-party Level 2 certification begins appearing in new
CUI contracts on November 10, 2026. Underneath the headline certification event
sits a quieter, permanent obligation that exists *today* and never ends: under
DFARS 252.204-7012/7019/7020, every subcontractor handling CUI must implement
the 110 NIST SP 800-171 controls, **post and maintain a current SPRS score**, keep
a System Security Plan (SSP) and Plan of Action & Milestones (POA&M) current, and
answer a stream of prime supplier-security questionnaires. A stale, missing, or
low SPRS score gets a supplier frozen out of purchase orders. This is a forced,
recurring, budgeted buy — not a one-time project.

**The business.** SecureControls is a productized, fixed-price recurring managed
service. A supplier reaches us through a **free, AI-assisted SPRS & 800-171
readiness assessment**; qualified prospects convert to a one-time onboarding
engagement (assessment, remediation plan, SSP/POA&M build, initial SPRS scoring)
followed by a tier-priced **monthly managed-compliance subscription**: quarterly
control reviews, evidence refresh, SPRS recalculation and re-posting, turnkey
responses to prime questionnaires, and C3PAO-assessment preparation support. The
software does the high-volume, repeatable work — control tracking, evidence
reminders, questionnaire auto-fill, reporting; a credentialed practitioner does
the judgment; the founder runs the close. We are not a C3PAO and we do not
guarantee certification.

**Why this works.** Demand is forced and time-boxed by a federal mandate. The
incumbents serving the smallest suppliers are sleepy — hourly GRC consultants who
do a one-time project and disappear, and generalist MSPs who treat security
paperwork as a side task and miss the defense-specific requirements. The
defining architectural choice — **artifact-only, never-custody-CUI** — bounds our
own regulatory and breach exposure, which is exactly the liability landmine a
small firm in this adjacency has to step around. The free assessment generates
qualified pipeline and proves competence before any commitment; the founders'
compliance-operator and regulated-enterprise-sales background runs the
consultative close this buyer requires.

**The founders.** Two operators with multiple SOC 2 Type II audit cycles, HIPAA
and HITECH program experience, GDPR and CCPA compliance work, multi-million-dollar
enterprise sales into regulated industries (insurance), and a long working
partnership — a compliance-operator instinct paired with regulated-enterprise
deal-closing muscle. The honest gap is no direct defense-industrial-base
experience and no pre-existing CMMC ecosystem relationships, closed through
deliberate advisor recruitment, a named Registered Practitioner (RP) /
CMMC-certified practitioner reviewing work product, paid design partners, and
credibility earned through demonstrated output.

**Financial trajectory.** Bootstrapped, with **$30K–$60K of founder capital** —
lighter than an infrastructure play because there is no enclave to stand up.
Per-customer economics: **$9,500–$15,000 onboarding** plus **$1,500–$3,500/month
recurring** ($18K–$42K/year), at 70–80% steady-state gross margin once delivery
is templated. **Base case (committed): the founder income ladder** — roughly
**$300K of distributable income per founder by month 12** (~28 active accounts)
and **~$500K per founder by month 24** (~55 accounts plus a small analyst team).
**$2M combined is treated as upside**, reachable only once delivery is fully
templatized — we do not commit to it.

**Funding ask.** None. Bootstrap funded by founder capital and customer cash
flow. No outside equity is sought.

---

## 1. Company Description

### What SecureControls Is

SecureControls is a U.S.-based managed-compliance firm providing three integrated
services to small defense subcontractors:

1. **A free, AI-assisted SPRS & 800-171 readiness assessment** that produces a
   personalized gap analysis against the 110 Level 2 control objectives and an
   honest current/target SPRS score estimate.
2. **A fixed-scope onboarding engagement (4–8 weeks):** a documented gap
   assessment, a non-expert-readable remediation plan, a baseline SSP and POA&M,
   the initial SPRS-score calculation and posting package, and setup of the
   compliance system-of-record.
3. **Ongoing managed-compliance operations** on a monthly recurring basis:
   quarterly control reviews, evidence refresh, SPRS recalculation and
   re-posting, turnkey prime-questionnaire responses, POA&M tracking, and
   C3PAO-assessment-preparation support within defined limits.

### The Defining Architectural Choice: Artifact-Only, Never CUI

The single most important design decision is that **SecureControls' system-of-
record holds compliance artifacts and attestation evidence — policies, control
status, POA&M items, SSP sections, questionnaire answers, screenshots, and
configuration evidence — and never the customer's raw CUI.** Raw CUI (controlled
drawings, technical data, covered defense information) is blocked from the
platform by design and by contract; it stays in the customer's own environment.
This one decision keeps SecureControls out of CUI-custody obligations, out of
GovCloud/CMMC-hosting requirements on its own infrastructure, and dramatically
shrinks its breach blast radius — letting a small firm operate credibly in a
heavily regulated adjacency.

### What SecureControls Is Not

- **Not a C3PAO.** We do not perform certification assessments and we do not
  guarantee any customer achieves certification — that rests with an independent
  C3PAO.
- **Not a cloud or enclave provider.** We do not host CUI, run GovCloud, or
  operate the customer's secure environment. Where a customer needs a compliant
  environment, we coordinate with or refer to an enclave/GCC High partner.
- **Not a general MSP.** We do not run help desk, manage endpoints, or do general
  IT. The offering is narrowly scoped to 800-171/SPRS compliance operations.
- **Not a law firm.** We do not give legal advice or interpret contract terms;
  customers retain their own counsel.

### Operating Principles

- **The customer's real problem is "stay on the Approved Supplier List."** We sell
  a maintained SPRS score and audit-readiness, not software.
- **One delivery spine.** A single, productized compliance-operations workflow for
  every customer; published, fixed pricing.
- **Artifact-only.** Compliance evidence lives with us; CUI never does.
- **The customer attests; we prepare.** The supplier signs and owns every
  representation to the government. We build and maintain the evidence behind it.
- **No certification promises.** Readiness is what we deliver. Certification is
  what the C3PAO decides.
- **Disciplined exclusions.** Out-of-scope work is referred or priced as a change
  order.

### Legal Structure

A Delaware entity (C-corp or LLC, finalized with tax counsel), foreign-qualified
where employees are based. The firm will pursue voluntary **CyberAB Registered
Provider Organization (RPO)** designation in year one as a credibility signal,
and a **named RP / CMMC-certified practitioner** (employed or fractional) reviews
all SPRS-affecting work product.

---

## 2. Market Analysis

### Market Size and Shape

The Defense Industrial Base comprises well over 100,000 companies; DoD analyses
estimate on the order of **80,000 will require CMMC Level 2.** The rollout is
phased and the obligation is already live:

| CMMC phase | What it means for the target customer |
|---|---|
| **Program rule — Dec 2024** | 32 CFR Part 170 in effect; SPRS scores and 800-171 self-assessment already contractually required under DFARS 7019/7020. |
| **Acquisition rule — Nov 10, 2025** | DFARS 252.204-7021 effective; phased inclusion of CMMC requirements in solicitations begins. |
| **Phase 2 — Nov 10, 2026** | Mandatory Level 2 C3PAO certification begins appearing in new CUI contracts. Typical readiness prep takes 6–12 months, so the decision window is now. |
| **Phases 3–4 — 2027–2028** | Level 3 and full implementation; requirement extends to options and renewals — the obligation becomes permanent and recurring. |

The recurring nature matters more than the certification event: even after a
supplier certifies, the SPRS score, SSP, POA&M, evidence, and questionnaire
obligations must be **maintained continuously**, every quarter, forever. That is
the subscription.

### Serviceable Obtainable Market

In-scope subcontractors that are (a) too small for full-service consultancies,
(b) sophisticated enough to know they need help, (c) handling CUI through
documents, email, drawings, and file exchange, and (d) able to invest $25K–$60K
in year-one compliance operations. We estimate **8,000–15,000 U.S. companies**
fit. Reaching 55 customers is well under 0.5% penetration — the market is not the
constraint; execution is.

### Ideal Customer Profile

- **Size:** 15–200 employees, $3M–$60M annual revenue, with a defined handful of
  people and systems that touch CUI.
- **DoD dependence:** Meaningful revenue under DFARS 252.204-7012/7019/7020
  flow-downs.
- **Posture:** One internal IT resource or an outsourced MSP; no dedicated
  security or compliance staff; the owner/office manager currently "owns" SPRS.
- **Trigger:** Active or imminent prime flow-down, a stale or missing SPRS score,
  or an inbound supplier-security questionnaire creating urgency in the next
  6–18 months.

### Competitive Landscape

- **Hourly GRC consultants and CMMC boutiques / RPOs.** The main incumbent for
  the smallest subs. They do a one-time readiness project, bill by the hour, then
  disappear — leaving the supplier to maintain the SPRS score and answer
  questionnaires alone. Sleepy, reactive, not packaged as ongoing operations.
  This is the segment we out-position with productization and modern marketing.
- **Generalist MSPs.** Handle the customer's general IT and may "do some of the
  security," but miss defense-specific requirements (SPRS methodology, CUI
  scoping, prime questionnaire nuance) and treat it as a side task.
- **GRC platforms — Vanta, Drata.** Well-funded, modern software companies adding
  800-171/CMMC frameworks. They sell a **self-serve dashboard the customer runs
  itself.** The structural risk: they move down-market toward our segment. The
  structural reason they don't win it: the 30-person machine shop will never
  operate a GRC dashboard or interpret a control objective — it wants the work
  *done for it* with a human who answers the prime's call. We are the operated
  layer above the tool; for the smallest shops we can even run on top of a
  customer's Vanta/Drata instance.
- **Enclave / GCC High providers (Summit 7, ProArch) and CUI tools (PreVeil,
  Virtru), and enclave-managed-service entrants.** These solve the
  *environment* problem. They are **partners, not competitors** — they make CUI
  handling compliant; we run the compliance *program* around it. A supplier
  needs both, and few providers do both well.
- **C3PAOs and assessors.** A different, regulated business — they grade. We
  prepare. We refer and coordinate; we never assess our own clients (a
  conflict-of-interest line we will not cross).

**Where the air is.** Operated, productized **compliance operations** for the
truly small sub — fixed-price, human prime-facing reassurance, a maintained SPRS
score and audit-ready evidence, environment-agnostic. The consultants do
one-time projects; the platforms sell self-serve tools; the enclave providers run
the environment. **No brand owns "we keep your SPRS score correct and your
evidence audit-ready, every quarter, for a fixed price"** for the 30-person shop.
That lane is real but filling, which is why the channel and credibility work
below is gating.

---

## 3. Service Offering

### The Delivery Spine

One productized compliance-operations workflow, run on a software system-of-record
plus expert review:

1. **Compliance system-of-record (artifact-only).** A multi-tenant portal holding
   each customer's control-implementation status against the 110 requirements,
   SSP, POA&M items, evidence artifacts, SPRS-score worksheet, and a reusable
   prime-questionnaire answer library. Raw CUI is technically and contractually
   excluded.
2. **The recurring cadence engine.** A scheduler that drives the quarterly review
   tasks, evidence-refresh reminders, reassessment due dates, SPRS re-posting
   windows, and renewal alerts. This is the retention engine.
3. **The questionnaire-response engine.** Inbound prime supplier-security
   questionnaires are answered fast from the customer's maintained evidence and a
   growing library of how recurring prime questions map to control objectives.
4. **Expert review.** A credentialed RP/CCP signs off on every SPRS-affecting
   judgment and on the SSP/POA&M before anything is posted or sent.

### The Three-Stage Customer Journey

**Stage 1 — Free SPRS & 800-171 readiness assessment.** Every prospect's first
interaction is a free assessment on the SecureControls website: a structured
survey enriched by AI follow-up questions, producing a personalized 15–25 page
report mapping current posture to the 110 Level 2 control objectives, an honest
current/target SPRS estimate, and prioritized remediation. The report states
plainly it is preparatory and not a C3PAO assessment. **Quality bar:** a
credentialed RP reviewing it would agree it caught what they would have caught.

**Stage 2 — Mock review and qualification.** Prospects whose assessment shows real
obligation and ICP fit get a founder-led conversation: a deeper review of CUI
scope, control gaps, and the realistic path to a defensible SPRS score. Qualified
prospects receive a written proposal at published pricing. This is the trust sale.

**Stage 3 — Onboarding, then managed operations.** Onboarding (4–8 weeks): gap
assessment, remediation plan, baseline SSP and POA&M, initial SPRS calculation and
posting package, system-of-record setup, and a readiness review. Then monthly
managed operations: quarterly control reviews, evidence refresh, SPRS
recalculation and re-posting, turnkey questionnaire responses, POA&M tracking, and
C3PAO-assessment-prep support within defined limits.

### Pricing

Published, fixed, tier-based on company size and CUI/questionnaire scope — not
negotiated. This discipline protects margin and forces honest qualification.

| Tier | Profile | Onboarding (one-time) | Monthly | Annual recurring |
|---|---|---|---|---|
| **Core** | <50 emp, single prime, light CUI scope | $9,500 | $1,500 | $18,000 |
| **Plus** | 50–120 emp, multi-prime, moderate scope | $12,500 | $2,500 | $30,000 |
| **Scale** | 120–200 emp, many primes/POs, heavy questionnaire load | $15,000 | $3,500 | $42,000 |

Customers pay separately for any GRC-platform license, secure-email/enclave
vendor, C3PAO assessment, external legal review, and MSP/general IT. **Design
partners** (first two or three customers) receive a setup discount
($5,000–$7,500) in exchange for structured feedback and testimonial rights on a
successful outcome.

### Explicitly Out of Scope

- General IT help desk, endpoint, or device management.
- Hosting, operating, or building the secure environment / enclave (referred to a
  partner).
- Taking custody of, processing, or storing raw CUI.
- Legal advice or contract-term interpretation.
- Certification guarantees of any kind.
- Signing or submitting any government attestation on the customer's behalf — the
  **customer always attests.**
- Heavy ITAR/EAR-controlled workflows requiring separate legal review (screened
  out at intake).

---

## 4. Go-to-Market Strategy

### The Motion: Product Sources and Qualifies; the Founder Closes

A deliberately split funnel. A **product-led** motion does the high-volume work at
the top, where trust is not yet required: the free SPRS assessment sources
prospects, qualifies them on data, and advances them toward sales-readiness. A
**founder-led** sale does the work at the bottom, where the money and trust live:
a $9.5K–$15K + $1.5K–$3.5K/month engagement with business-ending compliance
stakes, sold into a reference-driven culture, is closed by a person.

| Stage | Owner | Mechanism | Output |
|---|---|---|---|
| Source | Product | Free AI SPRS assessment; SEO on "SPRS score / DFARS 7012 / supplier questionnaire" pain, LinkedIn to defense-sub owners, APEX Accelerator and MEP events | Qualified, self-identified prospects |
| Qualify | Product | Assessment scores obligation, CUI scope, and ICP fit automatically | A ranked, sales-ready list with a named gap |
| Close | Founder | Mock review + consultative proposal at published price | Signed onboarding + subscription |
| Expand | Founder/CS | Add primes, questionnaires, and POA&M scope over time | Higher tier, stickier account |

### Channels

- **Prime supplier-development teams.** Primes *want* their suppliers compliant
  and would rather refer a trusted operator than chase each sub. This is the
  highest-leverage channel and a partial moat (channel lock-in vs. self-serve
  platforms).
- **MEP centers and APEX Accelerators.** Government-funded programs that help
  small manufacturers; natural referral partners with the exact ICP.
- **Defense-manufacturing associations and supplier-day events.**
- **Enclave/GCC High partners** (referral both directions): they run the
  environment, we run the program.

---

## 5. Operations & Delivery

### The Tuesday-in-March Walkthrough (at ~40 customers)

On a normal day, the team is: triaging inbound prime questionnaires (answered from
the evidence library, RP-reviewed, returned in days); running the quarter's
scheduled control reviews and evidence refreshes for the cohort due that month;
recalculating and re-posting one or two SPRS scores after a remediation closes a
POA&M item; and prepping one customer for an upcoming C3PAO assessment. No
fieldwork; everything is remote and document-based.

### Capacity Math

Steady-state delivery runs **~30–35 expert/analyst hours per subscriber per
year** (quarterly reviews, evidence, questionnaires, SPRS upkeep). Onboarding is
the heavy, front-loaded unit of work (~40–80 hours per new customer) and is the
true throughput constraint — which is why onboarding is priced toward its loaded
cost and why **templatizing onboarding is the central operational project.** At
~55 active subscribers (the month-24 base case) steady-state delivery is roughly
1,800–1,900 hours/year — about **2.5 delivery FTEs** — covered by the two founders
plus two compliance analysts plus the fractional RP advisor.

### Quality Control (non-negotiable)

Because a wrong SPRS score or a failed prime audit is the exact thing the customer
bought us to prevent, **the RP/CCP signs off on every SPRS-affecting judgment and
every SSP/POA&M before posting or sending.** A second qualified reviewer is added
before ~30 customers to remove the single-point-of-judgment risk and the
bus-factor exposure.

### Hiring Plan

| When | Hire | Why |
|---|---|---|
| Month 0 | Fractional RP/CCP advisor | Judgment + credibility + QC sign-off |
| Month 4–6 | Compliance analyst #1 | Onboarding + evidence throughput |
| Month 10–14 | Compliance analyst #2 / second RP | Remove judgment bottleneck before scale |
| Month 18+ | Customer-success lead | Retention + expansion as count grows |

---

## 6. Management & Founders

Two operators with a multi-year working partnership. Combined background: multiple
**SOC 2 Type II** audit cycles run end-to-end, **HIPAA/HITECH** program
experience, **GDPR/CCPA** compliance work, and **multi-million-dollar enterprise
sales into regulated industries (insurance).** This is precisely the
compliance-operator-plus-regulated-closer pairing the business requires: one
founder owns delivery, program design, and the system-of-record; the other owns
marketing, the consultative close, and channel relationships.

**The honest gap** — no direct defense-industrial-base experience and no
pre-existing CMMC ecosystem relationships — is closed deliberately: a named RP/CCP
reviewing all work product, a senior DoD/security advisor recruited before launch,
voluntary RPO designation, paid design partners, and credibility earned through
demonstrated assessment quality rather than borrowed reputation. The founders'
own SOC 2 Type II operating experience also lets them stand up SecureControls'
*own* security posture (which buyers will ask about) without buying expensive
help.

---

## 7. Financial Plan

### Unit Economics (steady state, per account)

- **Onboarding:** $9,500–$15,000 one-time; loaded delivery cost trends from
  ~$8–12K early to ~$4–6K once templated (the key margin lever).
- **Recurring:** $18K–$42K/year; blended target ~**$26K**.
- **Steady-state recurring gross margin:** 70–80% once delivery is templated
  (lower, ~55–65%, in the first year while onboarding labor and advisor cost are
  heavy).
- **Retention:** structurally high — the obligation never ends, switching
  mid-cycle risks the SPRS posture, and the evidence system-of-record is sticky.

### The Path to the Income Ladder

| Milestone | Active accounts | ~Recurring run-rate | Team | Distributable / founder |
|---|---|---|---|---|
| **Month 12 (base case)** | ~28 | ~$730K ARR + onboarding fees | 2 founders + 1 analyst + fractional RP | **~$300K** |
| **Month 24 (base case)** | ~55 | ~$1.45M ARR | 2 founders + 2 analysts + RP | **~$500K** |
| **Upside (not committed)** | 80–100+ | ~$2.1–2.6M ARR | + CS lead + 2nd RP | toward **$1M combined**; $2M combined only with full templatization |

Honest note, carried from the financial review: the **$500K-per-founder rung is
labor-gated.** Reaching it depends on driving onboarding's loaded cost down
through templatization and on the analyst hires landing on time; if onboarding
stays expensive and bespoke, the curve flattens into a boutique-consultancy shape.
We commit to the ladder, not to the $2M-combined upside.

### Cash Flow and Capital

Subscriptions are billed annually or quarterly **in advance**, and onboarding is
collected up front, so the business is **negative-working-capital** and funds its
own growth. Startup capital of **$30K–$60K** covers the system-of-record build
(~8–12 developer-weeks; revenue can begin on document-delivered onboarding before
the portal is finished), E&O/cyber insurance, legal/contract setup, the
fractional advisor, and initial marketing. **Cash-flow positive by month 9–12.**

---

## 8. Risk Register

Ten risks ranked by potential business impact, drawn directly from the expert
review that informed this plan, with mitigations.

1. **Attestation / False Claims Act spillover.** Because we maintain the program
   behind a government representation (the SPRS score), a later dispute over a
   customer's score could pull the firm in as a witness or contribution target
   (DOJ's Civil Cyber-Fraud Initiative is active in this area). *Mitigation:*
   the customer always attests and signs — we advise and maintain; a clear
   scope-of-work and "not a guarantee" posture; an MSA capping liability at 12
   months of fees; **E&O + cyber insurance bound before customer one**; documented
   evidence trails for every SPRS judgment.
2. **CUI boundary creep.** The product's gravity pulls customers to "just upload
   the file." If raw CUI enters the platform, we inherit 800-171/CMMC and
   GovCloud-grade hosting obligations and a catastrophic breach surface.
   *Mitigation:* artifact-only by design **and** by ToS; a technical control that
   blocks raw-CUI upload; intake screening; staff training.
3. **GRC-platform encroachment / copyable differentiation.** Vanta/Drata move
   down-market; the service itself is copyable. *Mitigation:* lock the
   prime-referral and MEP/APEX channels early; differentiate on operated depth and
   prime-facing reassurance a self-serve tool can't provide; run *on top of* the
   platforms for the smallest shops rather than against them.
4. **Labor-gated onboarding / margin and throughput.** Onboarding is heavy and
   front-loaded; each marginal account can need a hire before its revenue.
   *Mitigation:* price onboarding toward loaded cost; make templatizing onboarding
   the #1 operational project; measure loaded hours per onboarding and drive it
   down cohort over cohort.
5. **Single-practitioner judgment bottleneck / bus factor.** Deep SPRS/control
   judgment rests on one RP. *Mitigation:* a hard QC gate (RP sign-off on every
   SPRS post), a second RP/reviewer before ~30 customers, and templated control
   interpretations.
6. **Content drift (NIST 800-171 Rev 3 → CMMC).** The control set and SPRS
   methodology evolve; stale content silently degrades correctness. *Mitigation:*
   advisor-maintained content with a recurring update line; version-stamped
   control logic; change alerts to affected customers.
7. **Funnel / demand validation.** The free assessment may not convert at the pace
   the plan needs. *Mitigation:* a 60–90 day validation window with explicit
   gates; outreach to 100+ ICP-fit subs; rework the motion below a 3% engagement
   floor.
8. **Assessment quality bar.** A generic-feeling AI assessment damages the brand in
   a small, gossipy ecosystem. *Mitigation:* pre-launch RP validation against the
   work product they'd produce; ongoing re-validation; two iteration cycles then a
   kill decision.
9. **Buyers demand our own security posture.** Security-conscious customers will
   ask for our SOC 2. *Mitigation:* the founders' SOC 2 Type II background lets us
   stand up the control framework ourselves; SOC 2 Type II within ~9–12 months of
   revenue, used as a sales asset.
10. **Indemnification pressure / concentration.** Customers push prime-inherited
    indemnification language; early revenue may concentrate in one prime
    ecosystem. *Mitigation:* MSA caps indemnification at 12 months of fees, no deal
    without the cap or a counsel-reviewed exception; deliberate diversification
    across prime ecosystems.

---

## 9. Milestones and Validation Gates

### Pre-Launch Validation (Days 0–90, under $25,000)

- **Gate 1 — Liability architecture confirmed.** Counsel confirms the
  artifact-only / never-custody-CUI design and the "customer-attests" contracting
  posture bound our exposure; **obtain a written E&O + cyber quote against that
  scope.** *Pass:* counsel sign-off and an affordable, bound-able quote. *(This is
  the single highest-leverage de-risking step — it is what turns the program from
  a liability magnet into a clean managed service.)*
- **Gate 2 — Assessment quality.** Build the SPRS-assessment prototype; retain an
  RP for 5–10 paid hours. *Pass:* the RP agrees the output meets the bar of work
  they'd produce themselves.
- **Gate 3 — Funnel engagement.** Outreach to 100 named ICP-fit subs; measure
  assessment-completion rate. *Pass* above 10%; *fail* below 3%; in between,
  iterate the motion.
- **Gate 4 — Willingness to pay.** Convert 2–3 paid design partners at (discounted)
  published pricing. *Pass:* signed onboarding + subscription, cash in advance.

### Build & Launch (Months 1–6)

System-of-record MVP (8–12 dev-weeks; onboarding delivered document-first in
parallel); first 5–10 paying customers; first analyst hire; SOC 2 Type II program
started.

### Scale (Months 7–24)

Templatize onboarding (drive loaded hours down); second RP/reviewer before ~30
customers; lock 1–2 prime-referral channels; reach the month-12 (~28 accounts) and
month-24 (~55 accounts) ladder milestones; SOC 2 Type II report in hand as a sales
asset.

---

*Prepared as a founder-and-advisor planning document. SecureControls is the
compliance-operations layer for the small defense supplier; it deliberately does
not host, build, or operate the secure environment, and it never takes custody of
CUI — the two decisions that keep a small firm credible, lean, and insurable in a
regulated adjacency.*
