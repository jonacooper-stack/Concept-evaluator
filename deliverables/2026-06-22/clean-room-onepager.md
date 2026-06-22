# Clean-Room One-Pager (council input)

> Neutral standalone restatement handed to each of the six council subagents. No brand
> name, no prior scores, no tier, no round count, no lineage disclosed
> (Fresh-Evaluation Protocol). Score on absolute merit.

THE CUSTOMER. Small U.S. defense subcontractors — machine shops, welders, fabricators,
and small manufacturers, roughly 15–200 employees (a ~35-person precision machine shop is
typical) — that handle Controlled Unclassified Information (CUI) on defense purchase
orders. They usually serve **one or a small number of prime contractors**, have **no
in-house IT-security or compliance staff** (at most one outsourced IT provider), and the
**owner personally carries the compliance obligation**. They are cost-sensitive,
non-technical, and are working through CMMC for the first time.

THE FORCING FUNCTION. U.S. defense rules (DFARS 252.204-7012 / 7019 / 7020) already
require any subcontractor that touches CUI to keep a current cybersecurity
self-assessment score in the government's SPRS system, maintain a live System Security
Plan (SSP) and Plan of Action & Milestones (POA&M), and answer their prime's flow-down
security questionnaires; a blank or stale SPRS score can make a sub ineligible for new
purchase orders today. CMMC Level 2 — a formal assessment against the 110 NIST 800-171
controls — begins phasing into new CUI contracts on November 10, 2026. The obligation is
recurring (maintained indefinitely), already budgeted, and bought to avoid a fast,
concrete consequence: losing work with their prime.

THE PRODUCT. A self-serve software product that lets a small subcontractor **become and
stay CMMC / NIST 800-171 compliant themselves — without hiring an expensive consultant.**
The center of the product is an **AI guidance layer** that does the job a compliance
consultant would do, delivered as software:

- **Free assessment (the front door).** The owner uploads their existing security
  policies; the software automatically grades them against all 110 NIST 800-171 control
  objectives, returns an estimated SPRS score (current standing and target), and shows
  every gap in plain English. Free and self-serve — no sales call, no credit card.
- **Paid step-by-step remediation guidance (the core).** For each gap, the software walks
  a non-technical owner through fixing it themselves: plain-English explanation of what
  the control means, ready-to-adopt policy templates and worked examples, the concrete
  steps to close the gap, and progress tracking to "done." This is the part that replaces
  the consultant.
- **Document storage and upkeep.** The platform stores and maintains the customer's
  compliance documents (policies, control status, SSP/POA&M text).
- **Prime questionnaire auto-fill (a downstream benefit of the stored data).** Because the
  platform already holds the customer's answers and policies, when a prime sends a
  security questionnaire the software auto-answers most of it from what it already knows,
  asks the owner simple questions for anything missing, and produces a finished draft to
  export.
- **Recurring re-assessment.** Periodic re-scoring and reminders keep the customer current
  as their posture and the rules change.

Everything is powered by a **single private knowledge base per customer** that grows with
every answer the owner gives — which simultaneously improves their compliance posture and
makes future questionnaire auto-fills faster and more complete. By design the system holds
only **compliance documentation** (policies, control status, questionnaire answers) — NOT
the customer's CUI or operational security data (configs, logs, scans) — so neither
party's most sensitive data enters the tool. The customer does the work and self-attests;
all scores and generated documents are clearly labeled estimates/drafts (the product is
not an accredited assessor and issues no certification).

REVENUE MODEL. **Freemium.** The assessment (gap analysis + estimated SPRS score) is free,
to pull users in. The "doing" — step-by-step remediation guidance, document storage,
questionnaire auto-fill, and recurring re-assessment — sits behind a low-cost, published,
self-serve recurring subscription (credit-card signup, no onboarding fee), roughly
**$200–$600 per month** (~$2,400–$7,200 per year), tiered by company size/scope.
Positioned as **a small fraction of the cost of a consultant or managed service**, which
run tens of thousands of dollars per year. Optional higher-touch help may be layered on
later, but the core business is the self-serve subscription.

POSITIONING / GO-TO-MARKET. The pitch: *"Become CMMC compliant yourself — fast, and
without paying for an expensive consultant. See exactly where you stand for free, get
walked through fixing it step by step, and let the software fill out your prime's security
forms for you."* Sold against: expensive hourly CMMC consultants and Registered Provider
Organizations; managed-service / enclave providers; broad GRC automation platforms (e.g.,
Vanta, Drata) that cover many frameworks but are complex and leave the work to the
customer; and CMMC-specialized tools (e.g., FutureFeed, Totem). The wedge is **the
fastest, simplest, lowest-cost do-it-yourself path to compliance for a non-technical
owner** — a free score to pull them in, AI guidance to replace the consultant, and
ongoing form-filling to keep them. Acquisition is product-led and marketing-led: the free
assessment as a top-of-funnel magnet, SEO/content on present-tense SPRS/CMMC pain, and
channel partners (e.g., APEX Accelerators, Manufacturing Extension Partnership centers).
No founder-led sales close is required to transact.

THE TEAM. Two founders who are strong at marketing/positioning and can build software,
with hands-on compliance-operator experience running SOC 2 Type II, HIPAA/HITECH, and
GDPR/CCPA programs. They do NOT hold a CMMC credential (e.g., Registered Practitioner /
Certified CMMC Professional) and plan to launch the self-serve product WITHOUT hiring
credentialed staff — the goal is meaningful recurring revenue from software without adding
headcount, bringing in specialized experts only later as the business grows. A senior
DoD/DIB advisor informs the methodology and content.
