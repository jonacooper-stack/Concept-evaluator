# Clean-Room One-Pager (council input) — "Muster" concept

> This is the neutral standalone restatement handed to each of the six council
> subagents. No brand name, no prior scores, no tier, no round count, no lineage
> were disclosed to the reviewers (Fresh-Evaluation Protocol, CLAUDE.md).

THE CUSTOMER. Small U.S. defense subcontractors — manufacturers and suppliers with
roughly 15–200 employees (archetype: a ~35-person precision machine shop, ~$8M
revenue, 1–3 prime customers such as Lockheed or RTX). They handle Controlled
Unclassified Information (CUI) on defense purchase orders. They typically have one
outsourced IT provider (MSP), no in-house security or compliance staff, and the
owner personally "owns" the compliance obligation.

THE FORCING FUNCTION (why the buy is not optional). U.S. defense-contracting rules
(DFARS 252.204-7012/7019/7020) already require any subcontractor that touches CUI to
(a) maintain a current cybersecurity self-assessment score in the government's SPRS
system, (b) keep a live System Security Plan (SSP) and Plan of Action & Milestones
(POA&M), and (c) answer prime contractors' flow-down security questionnaires. A blank
or stale SPRS score can make a sub ineligible for new purchase orders now. Separately,
CMMC Level 2 — a third-party assessment against the 110 NIST 800-171 controls — begins
phasing into new CUI contracts on Nov 10, 2026. The obligation is recurring
(maintained every quarter, indefinitely), already budgeted in owners' minds, and
bought to avoid a fast, concrete consequence: losing the ability to win/keep work with
their primes.

THE PRODUCT. A productized, fixed-scope, fixed-price managed compliance service that
keeps the sub's NIST 800-171 evidence audit-ready and SPRS score correct every quarter
— explicitly WITHOUT taking custody of the customer's CUI or hosting their environment
("artifact-only": the provider's system of record holds only the compliance proof —
policies, control status, SSP/POA&M sections, evidence pointers, questionnaire
answers). Delivery combines software and a thin expert layer: (1) a self-serve guided
online assessment maps answers to the 110 control objectives and produces an estimated
current/target SPRS score plus a prioritized remediation report (this doubles as the
lead magnet/intake); (2) software does the repeatable high-volume work — scoring,
control mapping, SSP/POA&M document generation, evidence-refresh reminders, and a
reusable library to auto-answer prime questionnaires; (3) a credentialed practitioner
(Registered Practitioner / CMMC professional) reviews every deliverable that affects
the official score before it is finalized; the customer (not the provider) posts the
score and signs all government attestations. The provider is NOT an accredited assessor
(C3PAO) and offers no certification guarantee — it prepares; the customer attests.
Onboarding is a one-time ~4–8 week engagement that builds the baseline SSP/POA&M/SPRS
package; thereafter a quarterly cadence maintains it.

REVENUE MODEL. Recurring subscription plus a one-time onboarding fee, published and
fixed (not custom-bid). Three size-based tiers: ~$9,500 onboarding + $1,500/mo
(smallest, <50 emp), $12,500 + $2,500/mo (mid, 50–120 emp), $15,000 + $3,500/mo
(largest, 120–200 emp) — about $18K–$42K per customer per year plus onboarding.
Positioned at ~3–5× the price of do-it-yourself compliance software, on the basis that
the provider operates the program rather than handing over a tool. Customers separately
pay their own vendors for any GRC software license, secure email/enclave, the
third-party assessment itself, legal review, and general IT.

POSITIONING / GO-TO-MARKET. Sold against three alternatives: self-serve GRC software
(e.g., Vanta, Drata) that leaves the work to a customer who can't operate it;
enclave/managed-environment bundlers (e.g., OSIbeyond, Summit 7) that take over the
customer's environment and CUI (heavier, pricier); and hourly consultants/RPOs who
leave after a one-time project. The wedge is "operated for you, artifact-only, one
fixed price — you keep your data and environment." Acquisition is
marketing/positioning-led (SEO + targeted ads on present-tense SPRS/PO-freeze pain,
warm intros, channel partners such as APEX Accelerators and manufacturing-extension
centers) with a founder-led consultative close on the free-assessment funnel.

THE TEAM. Two founders: one a compliance operator who has run SOC 2 Type II,
HIPAA/HITECH and GDPR/CCPA programs end-to-end (owns delivery, methodology, and the
software system of record); one a go-to-market closer who has sold multi-million-dollar
engagements into heavily regulated industries (owns positioning and the consultative
close). One can build software. They have a senior DoD/DIB advisor but do not yet hold
the RP/CCP credential themselves (plan to retain one fractionally).
