# Clean-Room One-Pager (council input) — Defense-Sub Security-Questionnaire Answer Engine

> Neutral standalone restatement handed to each of the six council subagents for the
> THIRD concept (a self-serve "answer engine" whose core is auto-answering primes'
> security questionnaires, with a learning loop). No brand name, no prior scores, no
> tier, no lineage disclosed (Fresh-Evaluation Protocol).

THE CUSTOMER. Small U.S. defense subcontractors — manufacturers/suppliers with ~15–200
employees (e.g., a ~35-person machine shop) that handle sensitive defense information
(Controlled Unclassified Information, "CUI") on purchase orders from larger defense
companies ("primes"). They have one outside IT provider (an MSP), no in-house security or
compliance staff, and the owner personally carries the compliance burden. Cost-sensitive,
not technical.

THE FORCING FUNCTION. To keep winning work, these subs must continually satisfy their
primes' security demands. Two recurring, non-optional triggers: (1) Government rules
(DFARS 252.204-7012/7019/7020) require any sub touching CUI to keep a current
cybersecurity self-assessment score in a federal system (SPRS), maintain security
documentation, and — the recurring grind — answer each prime's flow-down security
questionnaire to stay an approved supplier. (2) From Nov 10, 2026, a tougher third-party
check (CMMC Level 2, against the 110 NIST 800-171 controls) begins phasing into new CUI
contracts. Primes send these security questionnaires repeatedly (new contracts, renewals,
annual updates), and a sub that can't answer — or answers slowly — risks losing the
order. The work never ends: every few weeks another form, indefinitely.

THE PRODUCT. A self-serve software subscription that does the never-ending
security-questionnaire work for a small sub and keeps them continuously ready. How it
works: (1) Seed — the sub uploads whatever it already has (policies, prior questionnaire
responses, any audit reports). (2) Auto-fill — when a prime sends a security
questionnaire, the sub drops it in and the software automatically answers ~80% of it from
the sub's saved knowledge base. (3) Interview-to-fill-the-gaps — for the remaining
questions, the software asks the owner plain-language questions (and flags which to route
to their IT provider) and writes the answers into the form. (4) Learn — the completed
form is fed back in, so the knowledge base grows and the next form auto-fills more. Over
time the tool answers more and asks less, and each sub's accumulated answer history lives
in the product. As a free on-ramp, the sub can first run an automated gap analysis and
get an estimated SPRS score to see where they stand. The product is specialized only for
the defense/CMMC world (not a general multi-framework tool), built around speed, low cost,
and ease of use for a non-technical owner. By design it holds compliance documentation
and questionnaire answers — not the customer's CUI or live system data — so sensitive
operational data doesn't enter the tool. The software produces drafts/estimates clearly
labeled as such; the customer reviews, decides what to submit, and is responsible for what
they send their primes and attest to the government.

REVENUE MODEL. Low-cost, published, self-serve recurring subscription (credit-card
signup), tiered by size/volume — roughly $200–$600/month (~$2,400–$7,200/year). Priced
far below a consultant or managed service, and bundled (answering + staying-ready
together) rather than sold as separate add-ons. Product-led: a free gap analysis as the
hook; no salesperson required to buy.

POSITIONING / GO-TO-MARKET. Sold against: broad compliance-automation platforms (e.g.,
Vanta, Drata) that treat security-questionnaire answering as a separate paid add-on and
focus on one-time setup; CMMC-specialist tools (e.g., Totem, FutureFeed) focused on the
assessment/score; standalone questionnaire-automation tools (e.g., Conveyor, Loopio,
SafeBase) aimed at large tech vendors, not small manufacturers; and hourly
consultants/MSPs. The wedge: "the one simple, affordable tool that actually answers your
customers' security forms for you and keeps you ready — built for a small shop, not a tech
company, with the form-answering built in, not sold separately." Acquisition is
marketing- and product-led: free gap-analysis hook, plain-English content on the
present-tense pain of SPRS/flow-down questionnaires, and warm referrals from
government-funded small-manufacturer help centers (APEX Accelerators, MEP centers).

THE TEAM. Two founders strong at marketing/positioning who can build software, with
hands-on compliance-operator experience (running SOC 2 Type II, HIPAA, GDPR programs). At
a previous company they built and ran in production a software "answer engine" of exactly
this kind (seed a knowledge base from policies/audit reports, auto-fill inbound security
questionnaires, interview to fill gaps, re-feed completed forms to keep learning); that
prior code is NOT available to reuse here, so they would rebuild the approach, but they
have done it before and seen it work. They do NOT hold a CMMC credential and plan to
launch without hiring credentialed staff, aiming to earn meaningful recurring revenue from
software without adding headcount; a senior DoD/DIB advisor informs the methodology and
content. Note: unlike the founders' prior company, the target customer has no in-house
technical staff (no CTO) to answer the harder gap questions — only an outside IT provider.
