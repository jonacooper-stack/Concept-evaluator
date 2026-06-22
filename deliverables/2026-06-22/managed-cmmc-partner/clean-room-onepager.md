# Clean-Room One-Pager (council input)

> Neutral standalone restatement handed to each of the six council subagents. No brand
> name, no prior scores, no tier, no round count, no lineage disclosed
> (Fresh-Evaluation Protocol). Score on absolute merit.

THE CUSTOMER. Small U.S. defense contractors and subcontractors — precision machine shops,
specialty manufacturers, electronics and engineering-services firms, roughly **15–100
employees** (a ~40-person shop is typical) — that handle Controlled Unclassified
Information (CUI) on defense work and therefore fall under **CMMC Level 2**, and whose
contracts require a **third-party certification** (not self-attestation). They have **no
in-house security or compliance staff** (at most one outsourced IT provider), the **owner or
a single ops/quality lead personally carries the obligation**, they are **non-technical**,
and they are facing their **first** certification with a hard deadline tied to live
contracts. These owners do not want to learn cybersecurity; they want the contract kept and
the problem taken off their desk.

THE FORCING FUNCTION. To win or keep CUI-bearing DoD contracts, these firms must hold a
current **CMMC Level 2 certification issued by an accredited third-party assessment
organization (a "C3PAO")** — an audit against **110 security controls (NIST SP 800-171)**.
The certification is **mandated, phasing into contracts from November 10, 2026**, and is
**not one-and-done**: renewed **every three years**, with an **annual affirmation** of
continued compliance in between. A missing, failed, or lapsed certification makes the firm
**ineligible to bid or to keep the contract** — a fast, concrete, revenue-threatening
consequence. Two things make merely buying a tool insufficient for this buyer: (1) actually
**implementing 110 technical security controls** is far beyond a non-technical owner with
one outside IT contractor; and (2) the firm typically **does not even know where its CUI
lives** — it sits in CAD drawings, PDFs, scanned documents, email and file shares — and
getting **scope wrong is the most expensive mistake** in the process.

THE PRODUCT / SERVICE. A **managed service — "done with you," not do-it-yourself** — that
takes ownership of getting a small contractor certified and keeping it certified, delivered
by a **lean expert team whose work is heavily automated by AI**. The outcome sold is **"you
will pass, and you will stay compliant,"** not "here is software to help you try." Five
connected components:

- **Automated CUI discovery & scoping (the entry point).** Software scans the customer's
  environment and identifies where CUI actually lives — including in **CAD files, PDFs,
  images and scanned drawings that generic tools miss** — then defines the **smallest correct
  compliance boundary**. This de-risks the engagement and **lowers the customer's total cost
  by shrinking scope**.
- **AI-generated readiness, policies & security plan.** AI produces the gap analysis against
  all 110 controls, drafts the written policies, and writes the **System Security Plan (SSP)
  and Plan of Action & Milestones (POA&M)** tailored to the customer's **actual environment**
  (not blank templates) — work that traditionally consumes the bulk of a consultant's
  billable hours.
- **Remediation done, not just described (the core human + AI layer).** The service
  **implements or orchestrates the actual technical fixes** — multifactor authentication, a
  compliant cloud enclave, encryption, logging/monitoring, endpoint protection,
  incident-response capability — via AI-generated step-by-step runbooks, automated
  configuration, and a network of **implementation partners**. A non-technical owner is
  carried to a genuinely **audit-ready** state.
- **Assessment ownership.** The service prepares the evidence package, runs a **mock
  assessment**, hands the prepared client to an **independent accredited assessor** from a
  vetted partner network, and supports the client through the real assessment. The provider
  **performs no assessment and issues no certification** — it deliberately stays on the
  **preparation** side of the industry's independence rule.
- **Managed continuity (the recurring engine).** After certification the service
  continuously monitors for new CUI and control **"drift,"** manages the **annual
  affirmation**, auto-answers primes' flow-down security questionnaires from stored evidence,
  and proactively runs **re-certification prep** before the three-year renewal.

The provider stores **compliance documentation and evidence-of-control**, plus the
**metadata/locations** of CUI from the discovery scan — but is designed **not to take
custody of the customer's actual CUI** itself. The defining characteristic versus ordinary
compliance software is that **a human team is accountable for the outcome**, with AI doing
the analytical and documentation labor that would otherwise make expert delivery
unaffordable for a small shop.

REVENUE MODEL. Two layers. (1) An **upfront get-certified engagement fee** for the
first-time readiness-to-certification project — on the order of **$15,000–$40,000
[ASSUMED]**, priced as a fraction of the traditional consultant-plus-implementation path
(which commonly runs from the tens of thousands into six figures for larger
small-businesses). (2) A **recurring managed-compliance retainer** for continuity — on the
order of **$1,500–$5,000 per month (~$18,000–$60,000/yr) [ASSUMED]**, tiered by size/scope —
covering monitoring, the annual affirmation, drift remediation, and re-cert prep. A possible
**third stream**: referral/qualified-handoff fees from partner accredited assessors who
receive pre-prepared clients. The economics depend on **AI leverage**: how many clients one
expert delivery person can carry to a passing outcome and keep compliant. (All figures are
[ASSUMED] working hypotheses to be validated by cheap experiments.)

POSITIONING / GO-TO-MARKET. The pitch: *"You run your shop; we run your compliance. We find
your sensitive data, build your security program, fix what's broken, get you through the
assessment, and keep you compliant year after year — an expert team, powered by AI, for a
fraction of what a traditional consultant costs."* Sold against: **low-cost self-serve
compliance/documentation tools** (hand a non-technical owner a 110-item to-do list and stop
at the paperwork — the customer still has to implement everything and survive the audit
alone); **premium managed-compliance and secure-enclave firms** (deliver a similar managed
outcome but are priced for and oriented toward large contractors, often well into six
figures); **hourly consultants and Registered Provider Organizations** (project-based,
labor-priced, leave at the finish line, nothing recurring); and the customer's **existing
IT/MSP** (generalists who do not know CMMC). The wedge is being the **only affordable,
AI-leveraged, fully-managed path for the small shop** — owning the outcome and the recurring
relationship — with **automated CUI discovery as a credibility-establishing entry point**
most competitors cannot match. Acquisition is **partner-led and marketing-led**:
co-marketing with accredited assessors (who need a pipeline of prepared clients), referral
relationships with MEP/APEX manufacturing-extension and procurement centers, partnerships
with IT/MSPs that want a CMMC answer for their clients, and content/SEO on present-tense
CMMC pain. No founder-led enterprise sales close is required to transact.

THE TEAM & DELIVERY MODEL. Two founders strong at **marketing/positioning** who can **build
software**, with hands-on **compliance-operator experience running SOC 2 Type II,
HIPAA/HITECH, and GDPR/CCPA** programs. They do **not** hold a CMMC assessor accreditation
and do not intend to become a C3PAO. The plan is to **register as a Registered Provider
Organization (RPO)**, add a **CMMC-credentialed delivery lead** and a small number of
compliance **"success managers"** whose capacity is multiplied by the AI tooling, and rely
on **partners** for specialized implementation (e.g., government-cloud enclaves),
CUI-discovery technology, and the independent assessor network. A senior **DoD/DIB advisor**
informs methodology and content. The intent is a **lean, high-leverage delivery team** — not
a large billable-hours consultancy — with software and AI absorbing the work that would
otherwise require headcount.
