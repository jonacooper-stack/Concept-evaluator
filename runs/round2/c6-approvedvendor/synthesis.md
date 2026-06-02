# Concept 6 — ApprovedVendorEngine — PM Synthesis

**Verdict: FAIL against SHORTLIST bar (all three). Recommendation: NO-GO as structured.**

- Mean (post red-team): **6.64** (CFO 7.3, CMO 6.8, COO 6.5, Legal 6.6, CTO 6.0) — needs > 8.0. FAIL.
- Lowest sub-score: **3** (CTO Third-party dependency) — needs none < 7. FAIL hard.
- Objectives total: **66.5 / 100** — needs >= 80. FAIL.

## Red-team reductions
CFO Startup 9→8, CFO Cash-flow 8→7, COO Logistics 9→8 (inconsistent with vendor-dependency 4). CFO working-cap 9 + CMO wedge/GTM 8 held.

## Dimensions holding it back (exact)
1. **CTO third-party dependency (3) + assumption risk (4)**: buyer-controlled portals (ISN/Avetta/Veriforce/Browz) have NO contractor-side write API → keystone is manual labor on rented ground; delegated-credential ToS risk + storing contractors' portal passwords; incumbents are simultaneously competitors AND acquirers AND executioners.
2. **Defensibility (CMO 5) + retention (CFO "invisible once compliant")**: category collapse to "$99/mo paperwork" + free insurance-agent substitute caps ACV.
3. **Liability (Legal 5)**: accountable for invoice release through pipes it doesn't control; performance fee strengthens assumed-duty/E&O.

## Failure-mode signal (NEW)
The "operational system-of-record" moat REQUIRED integrating with others' portals = heavy platform dependency on rented ground (the exact anti-pattern). LESSON: an operational system-of-record is only a clean moat if the customer OWNS the data/workflow surface — NOT if delivering value requires writing into a third party's controlled portal. ContractorPrequalOps (#62) shares this fault → DROPPED as near-duplicate.
