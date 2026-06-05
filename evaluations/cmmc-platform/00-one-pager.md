# Concept One-Pager — "Rampart" (working name)

## One-line
An AI-first compliance platform that gets a small U.S. defense contractor
CMMC-certified in weeks instead of months, then becomes the system of record
that keeps them audit-ready every year after.

## The customer
Small and mid-sized companies in the U.S. Defense Industrial Base (DIB) —
typically 10–500 employees — that handle Controlled Unclassified Information
(CUI) and must reach **CMMC Level 2** (which maps to the 110 controls of NIST
SP 800-171). These are machine shops, electronics manufacturers, engineering
firms, aerospace part suppliers, and IT/professional-services subcontractors
that sell to the DoD or to prime contractors. Most have little or no in-house
security/compliance staff; many lean on an outside IT provider or MSP. A
secondary buyer is the **MSP / MSSP / compliance consultancy** that manages
CMMC for a book of such clients and would use the platform across all of them.

## The pain (why they buy)
CMMC certification is becoming a **contractual gate**: under the DoD's phased
rollout, contracts increasingly require a CMMC status before a company can be
awarded or keep the work. Losing eligibility means losing defense revenue that
is often the core of the business. Reaching Level 2 is heavy and recurring:
- author and maintain ~20+ security policies, a System Security Plan (SSP), and
  a Plan of Action & Milestones (POA&M);
- implement and evidence all 110 NIST 800-171 controls;
- pass a third-party (C3PAO) assessment for certified status;
- then sustain it — annual affirmations and a triennial reassessment.

Today the customer's options are: hire a **consultant** ($50K–$150K+ per
engagement, [ASSUMED] from typical DIB advisory pricing), wrestle a **horizontal
GRC/compliance-automation tool** not tailored to CMMC, or **DIY in spreadsheets**.
The first is expensive and doesn't leave a living system behind; the second
makes the buyer do the CMMC translation themselves; the third rarely survives an
assessment.

## The product
An AI-first platform delivered in two phases.

**Phase 1 — Get compliant (the wedge).**
The customer uploads whatever documentation they already have — existing
policies, network diagrams, asset inventories, prior assessment reports, HR and
IT procedures. The platform's AI ingests it and:
1. auto-drafts the full required CMMC/NIST 800-171 **policy set and SSP**,
   pre-populated with the company's own specifics pulled from the uploads;
2. runs a **guided interview** that asks the user only the questions its
   ingestion could not answer, and asks targeted follow-ups where documentation
   is missing;
3. **flags non-compliance** control-by-control and produces a **gap scorecard**
   mapped to all 110 controls, plus a starter **POA&M**.
The output is the company's actual, ready-to-use compliance documentation set —
not advice, the artifacts themselves — and a clear picture of where they stand.

**Phase 2 — Stay compliant (the hub).**
That scorecard and document set become the anchor for an ongoing compliance
system of record: continuous evidence collection, control status tracking,
renewal/affirmation reminders, task assignment, and **audit-ready exports** the
company hands to its C3PAO assessor and uses for annual affirmations. Think
"Drata/Vanta, but built specifically for CMMC and the DIB."

## Revenue model
Annual SaaS subscription, billed yearly up front.
- [ASSUMED] tiers of **$7,500–$24,000 / year** by company size and control
  scope; midpoint target ACV ≈ **$12K**.
- Optional one-time **onboarding / readiness package** ($5K–$15K) for hands-on
  help reaching first-assessment readiness.
- A **partner/multi-tenant tier** for MSPs and consultancies managing many DIB
  clients (per-client pricing).
Recurring by nature: CMMC compliance is not a one-time event — affirmations are
annual and reassessment is triennial, so the customer needs the system every
year.

## Positioning
"The AI compliance platform that gets your defense business CMMC-certified in
weeks, not months — and keeps you audit-ready year after year." Specialized for
CMMC and the DIB rather than a generic, horizontal compliance tool; priced and
scoped for a small contractor rather than an enterprise security team.

## Why now
- CMMC 2.0 rules are finalized: the 32 CFR program rule took effect in late 2024,
  and the 48 CFR/DFARS rule that puts CMMC into contracts is phasing into
  solicitations through the mid-to-late 2020s. The buying deadline is no longer
  hypothetical — it is appearing in contracts now.
- Tens of thousands of small contractors ([ASSUMED] ~76,000–80,000 organizations
  estimated to need Level 2, per figures in the DoD CMMC rulemaking) face the
  same forced, deadline-driven, budgeted buy at roughly the same time.
- LLMs are now good enough to read a company's messy source documents and draft
  control-mapped policy language and gap analysis from them — the core technical
  bet that was not reliable a few years ago.

## Who's building it
Two versatile generalist founders: top-tier at marketing, positioning, and
founder-led sales; able to build the software themselves; with hands-on
compliance-operator experience running SOC 2 Type II, HIPAA/HITECH, and
GDPR/CCPA programs, plus enterprise sales into regulated industries. Deep
CMMC-/assessor-specific knowledge would be scaffolded through a named
practitioner or advisor (e.g., a CMMC Registered Practitioner or former C3PAO
assessor) rather than held by the founders on day one.
