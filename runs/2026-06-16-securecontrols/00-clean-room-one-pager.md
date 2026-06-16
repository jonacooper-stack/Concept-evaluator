# Concept One-Pager — SecureControls

A standalone brief for independent expert review. Score it on its own merits.

## The customer
Small U.S. defense subcontractors — firms in the Defense Industrial Base (DIB) that
sell to the Department of Defense (DoD), directly or as a sub to a prime contractor.
Target profile: **15–200 employees, $3M–$60M revenue**, with a defined handful of
people and systems that touch **Controlled Unclassified Information (CUI)** —
typically documents, email, and engineering drawings. They usually have one internal
IT person or an outsourced general-IT provider (MSP), **no dedicated security or
compliance staff**, and the owner currently "owns" compliance personally.

Market shape: the DIB exceeds 100,000 companies; DoD analyses estimate ~80,000 will
require CMMC Level 2. The narrower serviceable segment — subs too small for
full-service consultancies, sophisticated enough to know they need help, handling CUI
via documents/email/drawings, and able to spend $25K–$60K on year-one compliance — is
estimated at **8,000–15,000 U.S. companies**.

## The forcing function (why the buy is not optional)
Federal contract regulation plus prime-contractor flow-down. Under **DFARS
252.204-7012 / 7019 / 7020**, any subcontractor handling CUI must implement the **110
NIST SP 800-171 security controls**, calculate and maintain a current **SPRS score**
(the score DoD and primes look up to judge a supplier's security posture), keep a
**System Security Plan (SSP)** and **Plan of Action & Milestones (POA&M)** current, and
answer prime supplier-security questionnaires. The **CMMC** program adds third-party
certification on top: program rule effective Dec 2024; the DFARS 252.204-7021
acquisition rule effective Nov 10, 2025; **mandatory CMMC Level 2 certification begins
appearing in new CUI contracts on Nov 10, 2026**, phasing into options and renewals
through 2027–2028.

Consequence of not solving it: a **stale or missing SPRS score gets a supplier frozen
out of purchase orders**, and missing certification will block award of new CUI
contracts. The obligation is **recurring and effectively permanent** — even after a
sub certifies, the SPRS score, SSP, POA&M, evidence, and questionnaire responses must
be maintained every quarter, indefinitely. The buy is forced (regulation + prime
requirement), recurring, deadline-driven, and already a budgeted line for firms with
meaningful DoD revenue.

## The product
A **productized, fixed-price, recurring managed-compliance service**. Three integrated
parts:
1. **Free, AI-assisted SPRS & 800-171 readiness assessment** — a structured survey
   enriched by AI follow-ups that produces a 15–25 page report mapping the customer's
   posture to the 110 control objectives, an honest current/target SPRS estimate, and
   a prioritized remediation list. Doubles as the lead magnet.
2. **Fixed-scope onboarding engagement (4–8 weeks)** — documented gap assessment, a
   plain-language remediation plan, a baseline SSP and POA&M, the initial SPRS
   calculation and posting package, and setup in the system-of-record.
3. **Ongoing managed-compliance operations (the subscription)** — quarterly control
   reviews, evidence refresh, SPRS recalculation and re-posting, turnkey responses to
   prime questionnaires, POA&M tracking, and C3PAO-assessment-prep support within
   defined limits.

**Defining architectural choice — artifact-only, never CUI.** The system-of-record
holds compliance *artifacts* and attestation evidence (policies, control status,
POA&M items, SSP sections, questionnaire answers, configuration evidence) and **never
the customer's raw CUI**, which is blocked from the platform by design and by contract
and stays in the customer's own environment. This is meant to keep the firm out of
CUI-custody obligations, out of GovCloud/CMMC-hosting requirements on its own
infrastructure, and to shrink breach exposure so a small firm stays insurable.

**What it is not:** not a C3PAO (it prepares; it does not assess or guarantee
certification); not a cloud/enclave provider in this phase (it refers the secure
environment to a partner); not a general MSP (no help desk, endpoints, or general IT);
not a law firm. The customer always attests and signs every government representation;
the firm prepares the evidence behind it.

## The revenue model
Free assessment → one-time onboarding fee → tier-priced **monthly recurring
subscription**. Published, fixed, tier-based pricing (not negotiated):

| Tier | Profile | Onboarding | Monthly | Annual recurring |
|---|---|---|---|---|
| Core | <50 emp, single prime, light scope | $9,500 | $1,500 | $18,000 |
| Plus | 50–120 emp, multi-prime, moderate | $12,500 | $2,500 | $30,000 |
| Scale | 120–200 emp, many primes, heavy questionnaire load | $15,000 | $3,500 | $42,000 |

Blended recurring target ~$26K/year/account. Onboarding loaded delivery cost trends
from ~$8–12K early to ~$4–6K once templated (the key margin lever). Steady-state
recurring gross margin ~70–80% once templated (~55–65% in year one). Customers pay
separately for any GRC-platform license, secure-email/enclave vendor, C3PAO
assessment, legal review, and general IT. Retention is expected to be structurally
high because the obligation never ends and the evidence system-of-record is sticky.

**Financial trajectory (founder-stated base case, to be validated):** bootstrapped on
$30K–$60K of founder capital; billed annually or quarterly in advance with onboarding
collected up front, so the business runs on negative working capital and funds its own
growth; cash-flow positive by month 9–12.
- **Month 12:** ~28 active accounts, ~$730K ARR plus onboarding, team of 2 founders +
  1 analyst + fractional credentialed practitioner; ~$300K distributable per founder.
- **Month 24:** ~55 active accounts, ~$1.45M ARR, team of 2 founders + 2 analysts +
  practitioner; ~$500K per founder.
- **Upside (not committed):** 80–100+ accounts, ~$2.1–2.6M ARR.

## Positioning and where the open lane is
Intended position: *"We keep your SPRS score correct and your evidence audit-ready,
every quarter, for a fixed price"* — operated, productized compliance operations for
the truly small sub, environment-agnostic, with human prime-facing reassurance. The
claim is that no existing brand owns this lane for the ~30-person shop, though the lane
is described as "real but filling."

## The competitive landscape (named players, for independent verification)
- **Hourly GRC consultants / CMMC boutiques (Registered Provider Organizations).**
  One-time projects, billed hourly, then gone — leaving the sub to maintain SPRS
  alone. Characterized as sleepy and reactive; the segment to out-position with
  productization and modern marketing.
- **Generalist MSPs.** Run general IT, often miss defense-specific requirements, treat
  security as a side task.
- **GRC platforms — Vanta, Drata.** Well-funded; sell a self-serve dashboard the
  customer operates itself. Risk: a down-market move. Thesis for why they don't win
  the 30-person shop: that shop will never operate a GRC dashboard — it wants the work
  done for it — so the service is "the operated layer above the tool" and can run on
  top of a customer's Vanta/Drata.
- **Enclave / GCC High providers (e.g., Summit 7, ProArch) and CUI-handling tools
  (e.g., PreVeil, Virtru).** Solve the secure environment; framed as partners, not
  competitors.
- **C3PAOs / assessors.** A different, regulated business — they grade; this firm
  prepares, and never assesses its own clients.

## Go-to-market
A **split funnel**: a product-led top (free AI SPRS assessment; SEO on SPRS/DFARS
pain; LinkedIn outreach to sub owners; APEX Accelerator and Manufacturing Extension
Partnership events) sources and qualifies prospects on data, and a **founder-led
close** (a deeper "mock review" of CUI scope plus a consultative written proposal at
published pricing) signs the onboarding + subscription. Highest-leverage channel:
**prime-contractor supplier-development teams**, who want their subs compliant and
prefer to refer a trusted operator (a partial moat versus self-serve platforms). Other
channels: MEP centers, APEX Accelerators, defense-manufacturing associations and
supplier-day events, and enclave/GCC High partners (two-way referral).

## Operations
Steady-state delivery runs ~30–35 expert/analyst hours per subscriber per year.
**Onboarding is the heavy, front-loaded unit (~40–80 hours per new customer)** and the
true throughput constraint — which is why onboarding is priced toward loaded cost and
why **templatizing onboarding is the central operational project**. At ~55 active
subscribers, steady-state delivery is ~1,800–1,900 hours/year (~2.5 delivery FTEs),
covered by two founders plus two compliance analysts plus a fractional credentialed
practitioner. **Quality control is a hard gate:** a credentialed Registered
Practitioner / Certified CMMC Practitioner signs off on every SPRS-affecting judgment
and the SSP/POA&M before anything is posted or sent, with a second qualified reviewer
added before ~30 customers to remove single-point-of-judgment risk. Hiring: fractional
practitioner at month 0; compliance analyst #1 at month 4–6; analyst #2 / second
practitioner at month 10–14; customer-success lead at month 18+. The model is
remote-first and software-leveraged; it is **not** a field-service / on-site model.

## The founders
Two operators with a multi-year working partnership. Combined background: multiple
**SOC 2 Type II** audit cycles run end-to-end, **HIPAA/HITECH** program experience,
**GDPR/CCPA** work, and **multi-million-dollar enterprise sales into regulated
industries (insurance)** — a compliance-operator-plus-regulated-closer pairing. One
founder owns delivery, program design, and the system-of-record; the other owns
marketing, the consultative close, and channel relationships. The honest gap — **no
direct DIB experience and no pre-existing CMMC relationships** — is to be closed with a
named RP/CCP reviewing all work product, a senior DoD/security advisor recruited before
launch, voluntary CyberAB Registered Provider Organization (RPO) designation, and paid
design partners. The founders' own SOC 2 Type II operating experience is intended to
let them stand up the firm's own security posture without buying expensive help.

## Risk / liability posture (facts for independent assessment)
- Artifact-only design (never takes custody of CUI) intended to bound exposure and
  keep the firm out of GovCloud-hosting and CUI-custody obligations.
- The customer always attests and signs every government representation; the firm
  prepares the evidence behind it and makes no certification guarantee.
- Master Service Agreement caps liability at 12 months of fees; E&O + cyber insurance
  to be bound before the first customer.
- The DOJ Civil Cyber-Fraud Initiative (using the False Claims Act against false cyber
  attestations) is active; a later dispute over a customer's SPRS score could pull the
  firm in as a witness or contribution target.
- Voluntary CyberAB RPO designation pursued in year one; a named RP/CCP reviews all
  SPRS-affecting work product. Heavy ITAR/EAR-controlled workflows are screened out at
  intake. Not a C3PAO; not a law firm.

## Pre-launch validation gates (founder-stated, days 0–90, under $25K)
1. Counsel confirms the artifact-only / never-custody-CUI and "customer-attests"
   posture bounds exposure; obtain a written E&O + cyber quote against that scope.
2. Build the assessment prototype; retain an RP for 5–10 paid hours to confirm the
   output meets a credentialed practitioner's bar.
3. Outreach to 100 named in-profile subs; measure assessment-completion rate (pass
   above 10%, fail below 3%).
4. Convert 2–3 paid design partners at published pricing (signed onboarding +
   subscription, cash in advance).

## Optional future expansion (gated, explicitly not part of the committed launch)
Once an installed base, brand, references, and cash flow exist, the same customers
reveal a second, larger need: a compliant place for their CUI-handling employees to
work. The optional Phase 2 ("BeaconEnclave") would isolate just the CUI-handling
population (typically 3–25 people) into a single hardened AWS GovCloud enclave deployed
into the customer's own tenant, stream familiar Office apps inside it, and operate the
security, identity, monitoring, and evidence around it — with CUI living in the
customer-owned, FedRAMP-authorized tenant and the firm operating via just-in-time,
fully audited access. Pricing ~$25K setup + $8,500–$13,500/month, roughly 3–5× the ACV
of the core subscription. This is a heavier managed-infrastructure / MSSP-style
business that re-introduces the liability the core service was designed to avoid, so it
is treated as a **gated option**, not a commitment: it would be bridged first by
reselling/white-labeling a partner's enclave to the existing base to validate demand,
and pursued only if in-base demand is proven, cash flow can fund the heavier build and
insurance and a senior security-engineer hire, and the founders affirmatively choose to
take on 24/7-leaning security operations. The core service is designed to stand fully
on its own without it.
