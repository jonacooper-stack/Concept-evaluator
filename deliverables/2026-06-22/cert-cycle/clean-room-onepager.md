# Clean-Room One-Pager (council input)

> Neutral standalone restatement handed to each of the six council subagents. No brand
> name, no prior scores, no tier, no round count, no lineage disclosed
> (Fresh-Evaluation Protocol). Score on absolute merit.

THE CUSTOMER. Small U.S. defense contractors and subcontractors — precision machine shops,
specialty manufacturers, electronics and engineering-services firms, roughly **15–100
employees** (a ~40-person shop is typical) — that handle Controlled Unclassified
Information (CUI) on defense work and therefore fall under **CMMC Level 2**. Critically,
these are firms whose contracts require a **third-party certification** (not
self-attestation): they must pass a formal assessment by an accredited independent
assessor. They have **no in-house compliance or security staff** (at most one outsourced IT
provider), the **owner or a single ops/quality lead personally carries the obligation**,
and they are facing their **first** certification with a hard deadline attached to live
contracts.

THE FORCING FUNCTION. To win or keep CUI-bearing DoD contracts, these firms must hold a
current **CMMC Level 2 certification issued by an accredited third-party assessment
organization (a "C3PAO")** — an audit against 110 security controls. The certification is
**mandated, phasing into contracts from November 10, 2026**, and is **not one-and-done**:
it must be **renewed every three years**, with an **annual affirmation** of continued
compliance in between. A missing, failed, or lapsed certification makes the firm
**ineligible to bid or to keep the contract** — a fast, concrete, revenue-threatening
consequence. This is a recurring, scheduled, high-stakes **event** (the assessment), not a
static document obligation. Compounding it: accredited-assessor capacity is scarce (on the
order of ~100 accredited assessors for tens of thousands of firms needing certification),
so getting *through* the assessment — finding an available assessor and walking in
genuinely ready to pass — is itself a painful bottleneck.

THE PRODUCT. A software platform that carries a small contractor through the **entire
certification lifecycle — from "where do I stand" all the way to "certified, and still
certified three years later."** Four connected stages:

- **Readiness & gap analysis.** Assess current state against all 110 controls, generate the
  System Security Plan (SSP) and Plan of Action & Milestones (POA&M), and produce a
  prioritized remediation roadmap in plain English.
- **Guided path to *audit-ready* (the core).** For each control, the platform walks a
  non-technical owner through closing the gap AND collecting the **specific evidence an
  assessor will demand** — organized into an **assessment-ready evidence package** mapped
  control-by-control to what the auditor checks. The deliverable is not just a score; it is
  a firm that can **pass**.
- **Assessor matching & handoff.** The platform maintains a network of **partner accredited
  assessors (C3PAOs)**, matches the now-ready contractor to one with available capacity,
  and hands over the organized evidence package so the assessment runs **faster and
  cheaper**. The platform itself performs **no assessment and issues no certification** —
  and deliberately stays on the *preparation* side of the industry's independence rule (the
  firm that prepares you may not be the firm that certifies you), referring to
  **independent** partner assessors.
- **Stay-certified (the recurring engine).** Between assessments the platform manages the
  **annual affirmation**, monitors for control "drift," auto-answers primes' flow-down
  security questionnaires from the evidence it already stores, and **proactively runs the
  re-certification prep when the three-year renewal approaches** — bringing the customer
  back through the cycle.

By design the platform stores **compliance documentation and evidence-of-control**
(policies, control status, audit artifacts, questionnaire answers) — not the customer's
actual CUI — so the most sensitive operational data does not enter the tool. All readiness
scores and generated documents are clearly labeled estimates/drafts; the product is not an
accredited assessor and issues no certification.

REVENUE MODEL. A **recurring annual SaaS subscription that spans the whole cycle** (not a
one-time readiness fee), tiered by company size/scope — on the order of **$400–$1,200 per
month (~$5,000–$15,000 per year)**. The price is anchored to the *ongoing* obligation
(annual affirmation + monitoring + 3-year re-cert prep), which is what sustains the
subscription past the first certification. Positioned as **a fraction of the all-in cost of
getting certified the traditional way** (consultant-led readiness plus assessment commonly
runs into the tens of thousands of dollars, recurring each cycle). A **second revenue
stream** comes from the **assessor-partner network**: because the platform delivers
assessors pre-qualified, evidence-organized clients that cut assessment labor, partner
assessors pay a **referral / qualified-handoff fee** (or revenue share) for those
introductions. (Pricing figures are [ASSUMED] working hypotheses to be validated by cheap
experiments.)

POSITIONING / GO-TO-MARKET. The pitch: *"We get you certified — and keep you certified.
From your first gap analysis to a passing assessment with a vetted assessor, to staying
ready for your renewal three years out, it's one system that owns the whole certification
cycle for you."* Sold against: **expensive hourly consultants and Registered Provider
Organizations** (project-based, leave you at the finish line, nothing recurring);
**managed-service / secure-enclave providers** (heavy and costly, a different scope);
**broad GRC automation platforms** (cover many frameworks, complex, stop at readiness, and
have no assessor relationship); and **low-cost CMMC documentation tools** (stop at the score
and the paperwork — you still have to find an assessor and survive the audit alone). The
wedge is **owning the assessment event and the recurring cycle around it** — being the
connective tissue between a small contractor and the scarce accredited assessor, and the
system that is still there at renewal. Acquisition is **partner-led and marketing-led**:
co-marketing with accredited assessors (who have more ready-to-certify demand than they can
serve and need a pipeline of *prepared* clients), referral relationships with MEP/APEX
manufacturing-extension and procurement-assistance centers, and content/SEO on the
present-tense pain of getting through a CMMC assessment. No founder-led enterprise sales
close is required to transact.

THE TEAM. Two founders who are strong at marketing/positioning and can build software, with
hands-on compliance-operator experience running SOC 2 Type II, HIPAA/HITECH, and GDPR/CCPA
programs. They do **not** hold a CMMC assessor accreditation and do not intend to become a
C3PAO; their role is to build the software and the **assessor-partner network**,
coordinating with accredited assessors rather than competing with them. A senior DoD/DIB
advisor informs the methodology and content. The goal is meaningful **recurring** software
revenue without building a large services team.
