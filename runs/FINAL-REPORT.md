# Discovery Loop — Final Report (END STATE B)

**Goal:** Find 2+ DISTINCT concepts clearing the SHORTLIST bar — mean of five expert
averages **> 8.0** AND **no sub-score < 7** AND **objectives >= 80** — on honest,
red-teamed scores.

**Outcome: BOUND REACHED — 3 generation rounds completed AND 12 concepts deep-dived,
with ZERO concepts clearing the bar.** Per the goal and CLAUDE.md, an honest
zero-clear run is an acceptable, valid outcome: *"A run that explores the field,
produces full rigorous packets, and finds ZERO qualifiers is a SUCCESS. A run that
manufactures qualifiers at 8.1 is a FAILURE."* No score was tuned toward the bar at
any point; every concept was red-teamed and lowered where evidence demanded.

---

## Cross-round scoreboard (all 12 deep-dived concepts)

| # | Concept | Rd | CFO | CMO | COO | Legal | CTO | Mean (post-RT) | Low sub | Obj | Verdict |
|---|---------|----|-----|-----|-----|-------|-----|----------------|---------|-----|---------|
| 1 | SecureControls Defense Tier-2 (NIST 800-171/SPRS) | 1 | 7.7 | 7.6 | 7.5 | 7.3 | 7.7 | **7.56** | 5 | 79.5 | near-miss |
| 2 | ClearWater Water Ops (EPA LCRI) | 1 | 7.6 | 6.5 | 7.4 | 7.4 | 8.1 | **7.40** | 4 | 69 | FAIL |
| 3 | CosmeticMoCRA Ops (FDA MoCRA) | 1 | 7.5 | 7.0 | 7.2 | 7.5 | 7.8 | **7.40** | 6 | 73.5 | near-miss |
| 4 | DOTDrug Consortium (49 CFR Part 40) | 1 | 7.4 | 6.7 | 7.1 | 6.5 | 7.5 | **7.04** | 4 | 71 | FAIL |
| 5 | InsuranceCarrierAuditOps (WC premium audit) | 2 | 7.5 | 6.7 | 5.9 | 5.6 | 7.3 | **6.60** | 4 | 69 | FAIL |
| 6 | ApprovedVendorEngine (contractor COI/vendor) | 2 | 7.3 | 6.8 | 6.5 | 6.6 | 6.0 | **6.64** | 3 | 66.5 | FAIL |
| 7 | RebateCaptureOps (utility/IRA rebate capture) | 2 | 6.8 | 7.2 | 5.9 | 6.4 | 5.3 | **6.32** | 3 | 66 | FAIL |
| 8 | SuretyComplianceOps (bonding-readiness) | 2 | 7.1 | 7.0 | 6.3 | 6.9 | 7.0 | **6.86** | 4 | 69 | FAIL |
| 9 | DataProofEU (GDPR deal-enablement) | 3 | 7.7 | 7.0 | 7.0 | 5.3 | 7.5 | **6.90** | 3 | 70 | FAIL |
| 10 | SupplyAttest (aerospace AS9100 supplier-qual) | 3 | 7.4 | 6.5 | 6.6 | 5.3 | 6.9 | **6.54** | 3 | 68 | FAIL |
| 11 | FoundationFile (foundation grant-compliance net) | 3 | 7.1 | 6.7 | 7.4 | 7.5 | 7.5 | **7.24** | 5 | 73 | near-miss |
| 12 | TrialKeeper (clinical-site qualification net) | 3 | 7.6 | 5.7 | 7.3 | 7.3 | 7.3 | **7.04** | 4 | 63.5 | FAIL |

Honest means clustered **6.32–7.56**. None approached the >8.0 bar; every concept
carried at least one structurally weak sub-score below 7.

Per-round funnel: 90 + 90 + 80 = **260 theses generated → triaged → 12 deep-dived
with full 5-expert councils + red-teamed PM synthesis** (60 council reviews + 12
synthesis red-teams). FATAL-screened in triage on funded-incumbent encroachment,
PHI/FCRA/securities liability, field-ops, and free substitutes (~35 of 80 in round 3
alone).

---

## Why zero cleared — the structural finding

The SHORTLIST bar requires **every one of 50 sub-scores >= 7 AND a mean > 8.0**, i.e.
a concept with **no weak dimension**. Across 12 honest councils, every concept in this
founder-thesis space (bootstrapped, marketing-led, productized B2B managed service
around a forced/recurring compliance buy for SMBs) carried at least one of three
recurring structural ceilings — and, decisively, **the moves that fix one ceiling
re-import another:**

1. **Differentiation / Defensibility (~5–6 everywhere).** A bootstrapped productized
   service is inherently copyable. The only bootstrap-holdable moats are (a) a
   network/data effect or (b) becoming the operational system-of-record. But:
   - A genuine two-sided network needs the *value-conferring counterparty* (prime,
     sponsor, foundation, buyer) to ratify a reused credential — and that party has a
     legal/audit DUTY to re-verify, so it won't (C10 SupplyAttest, C11 FoundationFile,
     C12 TrialKeeper all died here), OR a funded incumbent already owns the rail
     (NGOsource, Veeva SiteVault, Exostar, ISN/Avetta).
   - An operational system-of-record either depends on writing into a third party's
     controlled portal (C6 ApprovedVendor — "rented ground," CTO 3) or hinges on a
     scarce credentialed expert (C8 Surety) or a rules-maintenance treadmill (C7 Rebate).

2. **Legal liability / licensing (~4–6 wherever the forced-buy is "real").** The hook
   that makes a buy forced and differentiated tends to BE the liability: advising on a
   government attestation (C1 False Claims Act / CUI; C10 ITAR), a take-rate/contingency
   on a regulated outcome (C5 insurance-consultant licensing; C7 False Claims Act on
   federal rebate $; C8 surety-fraud §1001/FCA), standing in as a statutory agent
   (C9 GDPR Art 27 representative), or custodying sensitive regulated data.

3. **Market-pull / income realism dips** on latent demand (C5 "they don't know they're
   overcharged"), free/self-serviceable filings (C3 MoCRA free FDA portal), low-ACV
   slow public buyers (C2 water systems, board-vote), or "found money" that churns.

**The clinching evidence:** FoundationFile (C11) was the FIRST concept to clear the
liability wall (clean Legal 7.6 — the IRC 4945 obligation stays with the foundation,
equivalency has a "qualified tax practitioner" safe harbor). It IMMEDIATELY hit the
defensibility wall (CMO Defensibility 5: network cold-start + NGOsource already owns
the hardest layer). TrialKeeper (C12) repeated it with a worse competitor (Veeva,
$2B+). **In this thesis space a concept can have clean liability OR a defensible moat,
not both — and the bar demands both.** That is the honest reason for zero clears.

---

## The 3 strongest near-misses (ranked) + the single cheapest experiment for each

### 1. SecureControls Defense Tier-2 — managed NIST 800-171 / SPRS for small defense subs
Mean **7.56** (highest of the run), objectives **79.5** (closest to the 80 floor),
lowest sub-score 5. The textbook archetype: federal-mandate-forced, recurring,
budgeted, sleepy hourly-GRC incumbents, dead-center founder fit.
- **What holds it back:** two Legal 5s — False Claims Act spillover (DOJ Civil
  Cyber-Fraud Initiative) + the portal custodying CUI (deemed-export/breach tail);
  and copyable service-differentiation vs Vanta/Drata moving down-market.
- **Single cheapest decisive experiment:** Have counsel confirm an **"artifact-only,
  raw-CUI-never-custodied" architecture** (portal holds policies/POA&M/attestation
  evidence, technically blocks CUI upload) and obtain a written **E&O + cyber quote**
  against that scope (~1–2 weeks, low-$thousands). If counsel confirms the CUI/FCA
  exposure collapses, Legal's privacy+liability 5s plausibly rise to 7, which lifts
  both the mean and the objectives total across the floor. This is the highest-leverage
  single fix in the entire run.

### 2. FoundationFile — shared grantee due-diligence network for private foundations
Mean **7.24**, objectives **73**, lowest sub-score 5 — and the **only concept with a
genuinely clean liability profile** (the structural standout). Statutory liability
stays with the foundation; equivalency safe harbor; public/free data; ~8–12 dev-weeks.
- **What holds it back:** CMO Defensibility 5 — the "vet once, reuse" network is a
  two-sided cold-start AND its hardest layer (foreign equivalency reuse) is already
  NGOsource's productized business; ARPU may compress if each foundation must legally
  own its own determination.
- **Single cheapest decisive experiment:** A **990-PF grantee-overlap study across
  30–50 target foundations** (public data, ~days) PLUS **8–10 nonprofit-counsel
  interviews** on whether a foundation will legally *rely* on another foundation's
  reused diligence. This one near-zero-cost study resolves both halves of the
  Defensibility 5 — does the network compound (overlap %), and will buyers ratify
  reuse (legal reliance). If overlap is high AND counsel says foundations can rely,
  Defensibility moves toward 7+ and the concept is the run's best candidate for a
  structurally-revised, clean-room re-submission. If not, abandon — cheaply.

### 3. CosmeticMoCRA Ops — managed FDA MoCRA compliance for indie cosmetics brands
Mean **7.40**, objectives **73.5**, lowest sub-score **6** — the **closest concept to
the "no sub-score below 7" condition** (only 6s, no 4s or 5s anywhere). Brand-new FDA
mandate with no entrenched player; sharp "stay on shelf" revenue-protection frame;
clean B2B liability.
- **What holds it back:** a cluster of 6s — willingness-to-pay vs the *free* FDA
  registration portal, shallow recurrence (most value is one-time onboarding),
  copyable differentiation (Registrar Corp), and unproven customer truth.
- **Single cheapest decisive experiment:** Attempt to **close 10 paid annual contracts
  (cash, not LOIs)** against a one-pager *after explicitly telling each brand "the FDA
  registration itself is free."* This single pre-sell falsifies the willingness-to-pay,
  shallow-recurrence, and customer-truth risks simultaneously. If 10 brands pre-commit
  real cash knowing the filing is free, the three binding 6s (recurrence, differentiation,
  customer-truth) lift toward 7+; if they won't, the concept is correctly killed before
  any build.

---

## What a future run should change (seed for any continuation)
The bar is likely only clearable in this space by a concept that simultaneously holds
a **structural moat the founders can actually control** (proprietary accumulating data
that improves the product for the *paying* customer directly — not a credential others
must ratify) AND **genuinely clean liability** (operational/internal value, customer
owns all attestation risk, no regulated take-rate, no statutory-agent role, no
sensitive-data custody). No concept generated across 260 theses cleanly held both. The
honest conclusion is that this specific bar (>8.0 mean, every sub-score >=7, obj >=80)
sits above what this founder-thesis space reliably produces — the field tops out
~7.5 on rigorous, red-teamed scoring. The single best path forward is to run the
cheapest experiment on near-miss #1 (SecureControls artifact-only counsel/E&O check)
or #2 (FoundationFile overlap + reliance study) before generating any new field.
