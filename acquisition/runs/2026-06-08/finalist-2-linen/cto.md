CTO REVIEW — Independent Uniform & Linen Rental-Route Business (~$2.8M rev / ~$650K SDE)

ONE-PARAGRAPH TECHNICAL READ
This is a classic sleepy route business running on paper route sheets, no CRM, no
customer portal, and pricing untouched for years — which is exactly the profile where
off-the-shelf route/field-service software plus a billing/pricing engine produces real,
near-term efficiency and revenue gains. The hard part is NOT the software (it is all
boring, buyable SaaS); it is that the operating reality — items-in-service counting,
per-item weekly billing, soil/clean inventory tracking, and route geography — is
unusually data-heavy, and uniform/linen rental is enough of a niche that the founders
will land on a smaller pool of industry-specific systems (ABS/SPSI/Smartlinen class)
rather than the big generic FSM brands. The biggest inherited technical risk is that the
"system of record" for who has which items, at which account, at which price is the route
reps' heads and a paper card/route sheet — and that data must be reconstructed and
cleaned before any portal, automated billing, or price increase can be trusted. Treat
this as a 6–9 month data-and-systems program with strong 90-day quick wins on billing,
payments, and routing, not a weekend digitization.

INHERITED-SYSTEMS SKETCH
- Accounting/billing: almost certainly QuickBooks (Desktop or Online) [ASSUMED — range:
  QuickBooks Desktop most likely for a 30-yr owner; verify by asking the bookkeeper] with
  per-item weekly invoicing likely done semi-manually or via a bolt-on; this is the
  single most load-bearing and most error-prone system in the business.
- Route/dispatch: PAPER route sheets — no telematics, no digital manifest, no
  stops-per-mile optimization software; route knowledge lives with the route sales reps
  (RSRs). This is both the debt and the modernization headline.
- CRM / sales pipeline: none. Account relationships, contract renewal dates, and pricing
  history live in reps' memory, a paper card file, and the owner's head (he "handles big
  accounts and pricing").
- Customer portal / online ordering: none. No self-service for add-ons, count
  reconciliation, or invoice viewing — a switching-cost and upsell gap.
- Inventory / items-in-service: the core operational data (which textiles are at which
  account, in soil vs clean vs replacement) is likely tracked on paper/spreadsheets or
  inside a legacy garment-tracking tool, possibly with barcode/RFID at the plant — or
  possibly not tracked rigorously at all, which is a shrinkage and billing-leakage risk.
- Laundry-plant systems: if in-house wash, there may be plant equipment with embedded
  controllers and a separate production/scheduling sheet; if outsourced wash, a vendor
  handoff with its own (probably manual) reconciliation.
- Payments: likely check/paper invoice with manual A/R follow-up; little to no
  card/ACH-on-file autopay — a working-capital and DSO drag.
- Website/marketing: weak-to-nonexistent web presence; growth is referral and
  route-knock; no analytics, no lead capture, no review pipeline.

MODERNIZATION PLAN
Stance: buy SaaS, don't build. The only genuinely custom work is data migration and a
thin automation/AI layer on top. Note the niche caveat: generic FSM (Jobber/Housecall
Pro) does not natively model rental items-in-service and per-item weekly billing well, so
the route/billing core likely wants an industry-specific platform.

90-day quick wins (highest ROI, lowest risk):
- Payments + autopay: put every account on ACH/card-on-file via QuickBooks Payments or
  Stripe; convert paper invoicing to automated recurring per-item invoices. ~2–4 weeks
  [ASSUMED] config + account enrollment. Expected gain: DSO cut from ~45+ to ~15–20 days
  [ASSUMED — verify against the A/R aging in diligence] and reclaimed admin hours.
- Route digitization v1: load routes into a routing tool (Route4Me/OptimoRoute class, or
  the industry platform's native module) and add GPS telematics (Samsara/Verizon Connect
  class) to the trucks. ~3–6 weeks [ASSUMED]. Expected gain: 5–12% route-mile/time
  reduction [ASSUMED — verify with one route's before/after fuel + hours], plus proof of
  service for disputes.
- Pricing reset, instrumented: build a simple per-account margin/price model in a
  spreadsheet or the billing system, surface accounts under market, and execute a
  contracted annual escalator + selective increase. ~2–3 weeks of analysis. Expected
  gain: this is the single largest near-term dollar lever — even a 3–5% blended price
  lift on ~$2.8M is ~$84K–$140K to the top line, largely flowing to SDE.

The longer program (months 3–9):
- Core route/billing platform: migrate to a uniform/linen-rental-specific system
  (ABS Enterprise / SPSI / Smartlinen / similar [ASSUMED — pull 2–3 vendor demos]) OR a
  rental-capable FSM, modeling items-in-service, per-item weekly billing, soil/clean
  cycles, and replacement charges. Implementation + data migration ~10–16 weeks
  [ASSUMED — range driven entirely by how clean the source data is]. Expected gain:
  eliminates billing leakage (under-billed items), gives a true items-in-service count,
  and is the foundation for everything else.
- CRM: HubSpot (or the platform's native CRM) for accounts, contract-renewal tracking,
  and upsell pipeline. ~2–4 weeks config + data load. Expected gain: renewals stop
  depending on rep memory; structured upsell of mats/restroom/ancillary lines.
- Customer portal: self-service invoice view, count reconciliation, and add-on ordering
  (native module of the route platform if available, else a light build). ~4–6 weeks.
  Expected gain: raises switching costs and cuts inbound service calls.
- Inventory/RFID: if not already present, evaluate UHF-RFID item tracking at the plant
  for shrinkage control. Hardware + config ~6–10 weeks [ASSUMED]; defer if payback is
  unclear — verify shrinkage rate first.
- Automation/AI thin layer: AI-assisted A/R dunning and collections sequences; an
  AI phone/booking agent for inbound account inquiries; automated Google review
  requests post-delivery; AI-drafted pricing-increase and renewal letters. Each is days,
  not weeks, on top of the SaaS once data is clean.

CRITICAL ASSUMPTIONS
- Items-in-service data is recoverable. The plan assumes you can reconstruct, per account,
  which items are in service at which price — from billing history + reps + paper. If this
  data is unreliable, automated per-item billing and any portal launch stall. Verify: in
  diligence, sample 10 accounts and reconcile their paper/route-sheet item counts against
  the last 3 invoices; measure the discrepancy rate.
- Source data is exportable. Assumes QuickBooks and any garment-tracking tool can export
  customers, items, contracts, and A/R to CSV/standard formats. Verify: have the
  bookkeeper run the actual exports during diligence — do not accept "it can be exported."
- Route reps adopt mobile/telematics. Assumes RSRs will accept GPS and a handheld manifest;
  resistance from long-tenured drivers who "own" their routes can sink digitization and
  even trigger churn. Verify: ask the owner how reps are paid/incentivized and gauge
  tenure and attitude before closing.
- Pricing power is real. Assumes contracts allow escalators / increases and the market
  bears a 3–5% lift without churn. Verify: read 10 representative contracts for escalator
  and term language; check the big-three's small-account pricing as a ceiling.
- The wash arrangement is stable and transferable. Assumes the in-house plant equipment is
  serviceable / the outsourced wash contract transfers. Verify: equipment age/maintenance
  logs, or the wash vendor's assignment terms.

INHERITED INFORMATION-SECURITY POSTURE
Data held: B2B customer records (contacts, addresses, contract terms, pricing), A/R and
bank/ACH details once autopay is enabled, employee PII and payroll for RSRs/plant staff,
and — if any accounts are paid by card — payment data. Today this almost certainly lives
on one or two office PCs and in paper, likely with shared logins, no MFA, no documented
backups, an aging Windows install, and QuickBooks files on a local drive — a textbook
ransomware and single-point-of-failure exposure for a 30-year sleepy operator [ASSUMED —
verify by inspecting the office IT setup and asking "where is the backup and when was it
last tested?"]. First-90-day controls: enforce MFA on email/QuickBooks/banking; move
QuickBooks and files to a managed cloud (QBO + Microsoft 365/Google Workspace) with
automatic versioned backup; replace shared logins with per-user accounts; deploy managed
endpoint protection on every PC; and, critically, NEVER store card numbers in-house —
push all payment data to a PCI-compliant processor (Stripe/QuickBooks Payments) so the
business stays out of cardholder-data scope. At scale: written backup/restore test
cadence, basic vendor security review of the route platform, and a simple incident-response
runbook. Incident readiness today is effectively zero; this is fixable cheaply but must be
funded in the transition, not "later."

SCORES (1–10)
1.  Inherited systems condition:        3  — Paper route sheets, no CRM, no portal,
    likely QuickBooks Desktop on one PC; near worst-case for a route business.
2.  Technical & data debt:              3  — Core items-in-service/pricing data lives on
    paper and in reps' heads; must be reconstructed and cleaned before automation works.
3.  Modernization upside — tech/AI:     9  — Glaring high-ROI stack (route platform +
    QBO/Stripe autopay + telematics + pricing engine); a 3–5% price lift alone is
    ~$84K–$140K on $2.8M, plus DSO and route-mile gains.
4.  Effort to modernize:                6  — Quick wins (autopay, routing, pricing) land
    in ~2–6 weeks each; the core route/billing migration is a ~10–16 week data project,
    not a weekend — configure-and-migrate, not build.
5.  Critical dependency risk:           5  — No proprietary lock-in, but the niche steers
    you to a smaller pool of industry platforms (ABS/SPSI/Smartlinen) and the real
    dependency is route reps who hold the relationships and route knowledge.
6.  Cybersecurity posture inherited:    4  — Presumed shared logins, no MFA, local
    QuickBooks, untested backups; ransomware-ripe, but the fix list is cheap and standard.
7.  Data ownership & migration:         5  — You own the data, but exportability and
    cleanliness are unproven; migration risk is moderate and entirely data-quality-driven.
8.  Automation / AI leverage:           7  — Reliable, real uses: AI A/R dunning, review
    generation, inbound phone/booking agent, drafted price/renewal letters — days of work
    on clean SaaS, not hype.
9.  Scaling / tech headroom:            8  — A modern route platform (e.g., ABS
    Enterprise class) is built for multi-route, multi-location growth and tuck-ins
    without a re-platform; headroom is genuinely strong once installed.
10. Ongoing maintenance burden:         8  — Target stack is all SaaS/managed (QBO,
    Stripe, HubSpot, route platform, telematics); near-zero permanent engineering load
    on two owner-operators after configuration.

AVERAGE SCORE: 5.8 / 10

TOP 3 TECHNICAL STRENGTHS
- The modernization upside is real and bankable: per-item autopay billing, route
  optimization with telematics, and instrumented pricing each have clear, near-term ROI,
  with a 3–5% price lift worth ~$84K–$140K on ~$2.8M revenue.
- The end-state is all boring, off-the-shelf, managed SaaS (QBO/Stripe, HubSpot, an
  industry route platform, Samsara-class telematics) — low ongoing maintenance burden and
  strong multi-route/tuck-in scaling headroom.
- No proprietary or contractor lock-in: there is no custom dead system to reverse-engineer;
  the work is migration and configuration, which a software-capable founder can lead.

TOP 3 TECHNICAL RISKS
- The operational system of record (items-in-service, per-account pricing) is paper +
  reps' heads; reconstructing and cleaning it is the gating task for every other upgrade.
- Route-rep adoption and retention: GPS/mobile manifests and a pricing reset can provoke
  long-tenured drivers who "own" their routes, risking both digitization and account churn.
- Inherited security neglect (no MFA, local QuickBooks, untested backups) leaves the
  business ransomware-exposed during the most fragile moment — the ownership transition.

BIGGEST SINGLE RISK
The single most dangerous systems issue is that the true state of the business — exactly
which textile items are in service at which account, at which negotiated price, under
which contract renewal date — is not reliably written down anywhere. It lives in paper
route sheets, a card file, the route reps' memory, and the retiring owner's personal
handling of "big accounts and pricing." Every high-ROI modernization move (automated
per-item billing, a customer portal, a defensible price increase, billing-leakage
recovery) depends on first reconstructing that data accurately. If diligence reveals the
item counts and pricing can't be reconciled against billing history, the modernization
timeline stretches from months to a year-plus, the price-increase thesis becomes guesswork,
and — worst case — the data effectively walks out the door with the owner and the reps,
turning a "buy proven cash flow and modernize it" deal into a partial rebuild of the
operational backbone.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What system actually produces the weekly per-item invoices today, can its customer /
  item / contract / A/R data be EXPORTED to CSV (demonstrated live in diligence, not
  promised), and who administers it?
- For a sample of 10 accounts, do the paper/route-sheet item counts reconcile to the last
  three invoices — i.e., how much billing leakage and data drift actually exists?
- How are route reps tenured, paid, and incentivized, and how will they react to GPS
  telematics, mobile manifests, and a pricing reset — what is the realistic adoption and
  churn risk?
- Is there any item-level inventory/RFID tracking at the plant today, or is shrinkage
  effectively unmeasured — and what is the current loss/replacement rate?
- What is the office IT reality: shared logins or per-user, MFA anywhere, where do the
  QuickBooks files live, and when was a backup last successfully restored?

RECOMMENDATION: GO
On a systems-and-modernization basis this is a GO — but a conditional, eyes-open one. The
inherited tech is genuinely poor (scores of 3–4 on condition, debt, and security), yet
that is precisely the sleepy-operator gap the founders are paid to close, and the
modernization path is high-ROI, off-the-shelf, low-maintenance, and scalable. The GO is
contingent on diligence confirming three things: (1) the customer/item/pricing/contract
data is exportable and reconcilable to billing within an acceptable error rate; (2) the
route reps can be retained and brought onto mobile/telematics without triggering account
churn; and (3) the security fix list is funded inside the transition budget, not deferred.
If diligence shows the items-in-service and pricing data cannot be reconstructed
reliably, downgrade to RE-TRADE — the modernization scope (and therefore the price-increase
and billing-leakage thesis the deal partly rests on) would need to be rescoped and the
purchase price adjusted for a longer, riskier systems rebuild.
