# LEGAL / REGULATORY REVIEW — CoverHold (Insurer-Attestation Management for Property Owners)

Not formal legal advice. Operator pattern-recognition flagging issues for retained counsel.

ONE-PARAGRAPH RISK READ
At its legal core a B2B document-aggregation and administrative-correspondence service — relatively benign by insurance-industry standards. Dominant question: whether assembling and submitting "carrier-ready" loss-control evidence on an insured's behalf, for a fee, crosses into activities reserved to licensed insurance adjusters, producers, or consultants in some states; the one-pager wisely carves out certification of underlying repairs (the single most dangerous line). Remaining exposure is ordinary: contract-based liability if a deadline is missed and the owner loses coverage (high-consequence, tied to the core promise), modest commercial-PII handling, consumer-protection mechanics on the recurring subscription. Not fatal, but the adjuster/consultant-licensing question and the missed-deadline liability tail are real and must be resolved with state-specific counsel.

REGULATORY MAP
- State insurance adjuster / public-adjuster licensing (NAIC Model Public Adjuster Licensing Act, ~40+ states; CA Ins. Code §15006; FL §626.854; NY Ins. Law §2101(g)). The one to watch. Public adjusters negotiate/effect settlement of a CLAIM for an insured. This service manages loss-control/underwriting corrective requirements and renewal attestations, NOT first-party claims — on its face outside the definition. But the line is state-specific; some states define "adjusting" broadly. Burden: moderate per-state diligence, likely clearable if scope stays on loss-control and off claims.
- State insurance producer/consultant licensing (e.g., NY Ins. Law §2107). A handful of states license "insurance consultants" who for a fee advise insureds on coverage/policy terms/compliance. If the service drifts from "organize and submit your evidence" to "advise on what the carrier really requires," it brushes this. Burden: low-to-moderate, scope-dependent.
- Unauthorized practice of law (all 50 states). Interpreting policy conditions, advising on legal consequences of non-compliance, or drafting responses that take legal positions can be UPL. Must present as administrative/document management. Burden: low if disciplined.
- FTC Act §5 / state UDAP + auto-renewal laws (CA ARL §17600; NY GBL §527-a; FTC negative-option rule). Recurring auto-renewing subscription: clear disclosure, affirmative consent, easy cancel. B2B softens but some state ARLs reach business subscriptions. Burden: low if built in.
- State data-privacy / commercial PII (CCPA/CPRA where applicable). Overwhelmingly commercial/property documents, incidental PII; no HIPAA/biometric/children's data. Burden: low.
- GLBA — attaches to financial institutions handling consumers' NPI; this is commercial-property insurance data so likely no attachment, but carrier/broker partners may push obligations down by contract. Burden: low, contract-driven.
- E&O / professional-services liability (insurable). The liability spine; addressed below.

LICENSING SUMMARY
Base case — a remote service that organizes, collects, packages, and transmits the owner's own factual evidence to satisfy carrier loss-control requirements, without negotiating claims, advising on coverage adequacy, or certifying repair truth — no insurance license is clearly required; only ordinary business registration / foreign-qualification per state. Plausible here because the one-pager drew the two protective lines. The risk is at the edges: if counsel reads "submits a carrier-ready response package on the insured's behalf, for compensation" as adjusting or consulting, that state's public-adjuster or insurance-consultant license could be required (exam, bond, CE, $25–$1,000+ fees per state, renewals). The founders hold no such credential, and a 50-state public-adjuster footprint would collide with the "no specialized credentials" profile. Mitigation is structural: keep scope provably on loss-control administration (not claims), get a clean opinion in top target states before selling, and partner with/employ a licensed individual where a state insists. The dimension to resolve before scale.

LIABILITY POSTURE
Exposure concentrated in one place: the service exists to prevent a catastrophic outcome (coverage loss), so a failure is causally adjacent to that catastrophe. Missed deadline / rejected package / inadequate evidence → non-renewal or cancellation → replacement coverage at far higher premium, lender technical default for failure to maintain required insurance, even forced sale. Plaintiff argues the service's whole reason for being was to stop exactly this. Manageable but deliberate:
- Contract: negotiated-but-templated MSA with a clear scope statement (administrative management of evidence/deadlines; owner remains responsible for repairs and truth of evidence), explicit no-guarantee-of-carrier-acceptance disclaimer, liability cap (fees paid), carve-out that the carrier's renewal decision is outside the service's control, indemnity for owner misrepresentations. The "does not certify truth of underlying repairs" sentence is the right posture — must be papered.
- Insurance: Professional liability / tech-and-services E&O is load-bearing (low five figures annually); GL and cyber standard adds. No on-site work → no field workers'-comp, no premises-injury, no auto — meaningful de-risking vs inspection incumbents.
- Founder personal exposure: ordinary — LLC/C-corp before first contract, keep formalities, carry E&O.
- Marketing-claim liability: "never lose your coverage" is a results promise; defensible if the contract disclaims guaranteed outcomes, but UDAP risk rises with the gap. Soften to a process promise ("never miss an insurer requirement").

SCORES (1–10; higher = lower risk)
1. Industry regulatory burden: 6 — Touches heavily regulated insurance, but the activity is administrative document management adjacent to (not inside) the regulated claims/coverage core; real but bounded, scope-dependent.
2. Licensing requirements: 6 — Base case needs only business registration, but a credible state-specific risk that public-adjuster (FL §626.854, CA §15006, NY §2101) or consultant (NY §2107) licensing attaches at the edges keeps this out of 8 until cleared.
3. Data privacy exposure: 8 — Predominantly commercial property/vendor documents, only incidental PII; no HIPAA, no BIPA, no COPPA, so the heaviest regimes don't attach and standard CCPA-track hygiene suffices.
4. Employment & contractor risk: 9 — Remote W-2 specialists, no field workers, no homes entered, no background-check/workers'-comp-for-crews; classic 1099-misclassification/multi-state field-labor risk structurally absent.
5. Consumer protection complexity: 7 — B2B annual subscription, not a 50-state consumer auto-renewal product, so CA ARL/FTC negative-option apply in lighter B2B form; clean if disclosure/cancel built in.
6. IP cleanliness: 8 — Original workflow software, no dependence on a restricted third-party API/licensed content/platform terms; only inbound IP is the customer's own documents under contract — no platform-revocation risk.
7. Contract simplicity: 6 — Heavier than clickwrap: the missed-deadline tail demands a real MSA with scope limits/disclaimers/cap per customer; not catastrophic but not frictionless.
8. Liability exposure: 5 — Core promise sits one causal step from a catastrophic insured outcome (coverage loss, lender default); a single bad miss can generate outsized damages; insurable via E&O and cappable by contract, but genuinely mediocre given stakes.
9. Jurisdictional simplicity: 6 — Operates across many states; privacy/consumer rules roughly additive, but the insurance-licensing question can hit state cliffs (a state reading the activity as adjusting forces a per-state licensed individual).
10. Regulatory trajectory: 7 — Hard-market loss-control rigor is intensifying (more documentation demanded), growing demand; insurance-services regulation stable-to-slowly-tightening with no specific pending bill targeting evidence-administration services.

AVERAGE SCORE: 6.8 / 10

TOP 3 LEGAL/REGULATORY STRENGTHS
- No field operations: remote document-only delivery eliminates the premises-injury/field-crew/workers'-comp/auto/background-check stack and the 1099-misclassification trap (4 and 9).
- Clean data and IP posture: commercial documents with only incidental PII (no HIPAA/BIPA/COPPA/GLBA-consumer) plus original software with no restricted-API/platform dependency (3 and 6).
- Founders drew the two correct protective lines — no claims negotiation, no certification of repair truth — keeping the activity out of the public-adjuster definition and out of fraud/false-attestation exposure.

TOP 3 LEGAL/REGULATORY RISKS
- State public-adjuster/insurance-consultant licensing attaching at the edges of "submitting a carrier-ready package on the insured's behalf for compensation," which the founders cannot satisfy without a licensed individual.
- The missed-deadline liability tail: the service's reason for existing is preventing coverage loss, so a failure is causally adjacent to a catastrophic, well-quantified loss.
- Marketing-claim exposure from "never lose your coverage" as a results guarantee under FTC §5 / state UDAP.

BIGGEST SINGLE RISK
State insurance-licensing classification of the core paid activity. The value prop is acting, for compensation and on the insured's behalf, in the loss-control/renewal process — collecting, assembling, and submitting evidence to the carrier and tracking to closure. In most states that is administrative work outside the licensed-adjuster and -consultant definitions (anchored to claims settlement and coverage advice). But "for compensation, on behalf of the insured, in dealings with the insurer" is exactly the statutory language, and a handful of DOIs read it broadly. If even three or four high-value states (CA, FL, NY, TX) require a public-adjuster or consultant license, the founders face either a per-state licensed-individual requirement or a forced narrowing of scope to pure deadline-tracking/document-storage that strips the "we submit it for you" feature. Not fatal — the activity is closer to compliance administration than adjusting — but must be resolved with a state-by-state opinion before selling into those states.

QUESTIONS FOR REAL COUNSEL BEFORE LAUNCH
1. In each top-5 target state, does assembling and submitting loss-control/renewal evidence to a carrier, for a fee, on the insured's behalf, require a public-adjuster, insurance-consultant, or producer license — and where is the line between administrative document management and adjusting/consulting?
2. Does interpreting what a loss-control letter "requires," or advising on consequences of non-compliance, risk UPL or unlicensed insurance consulting, and how must we script the workflow/communications?
3. What MSA structure (scope limitation, no-guarantee-of-renewal disclaimer, liability cap, indemnity for owner misrepresentations) holds up if an owner loses coverage and sues, and is our E&O carrier comfortable with both the contract and the marketing claim?
4. Does "never lose your coverage" create FTC §5 / state UDAP exposure as an implied results guarantee, and what disclaimer reconciles marketing with contract?
5. Do we inherit GLBA, state-DOI vendor, or carrier-imposed data-security obligations contractually when carriers/brokers route documents through us?

RECOMMENDATION: REFINE (leaning GO)
Structurally clean — remote, document-only, original IP, minimal sensitive data, no field-labor exposure — and the founders drew the two most important protective lines. The 6.8 reflects a workable posture held back by one genuine open question (licensing classification) and one genuine liability tail (missed-deadline), neither fatal. To a clean GO: (1) per-state legal opinion in initial target states confirming the activity sits outside public-adjuster/consultant licensing, with a licensed-individual partnership or scope-narrowing fallback; (2) paper the missed-deadline risk with a real MSA (no-guarantee disclaimer, liability cap, indemnity); (3) soften the headline to a process guarantee. With those, the profile is well within what two non-credentialed founders can carry, and the hard-market trajectory helps.
