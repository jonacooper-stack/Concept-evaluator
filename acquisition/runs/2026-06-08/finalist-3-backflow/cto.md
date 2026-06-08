CTO REVIEW — Backflow-Prevention Testing & Cross-Connection-Control Compliance Co.

ONE-PARAGRAPH TECHNICAL READ
This is a near-textbook "sleepy" target from a systems standpoint: the entire business
runs on paper, spreadsheets, and the owner's memory, with the core asset — a recurring
annual renewal list of backflow assemblies — sitting in a filing cabinet rather than in
software. That is bad for the seller and good for the buyer: there is almost no legacy
tech debt to unwind (you can't be locked into a system that doesn't exist), and the
modernization upside is unusually clean because the right answer is entirely
off-the-shelf SaaS plus a thin automation layer, not custom build. The single biggest
technical risk is not the stack — it's getting the renewal data OUT of paper and the
owner's head, structured correctly (assembly serial numbers, device types, test-due
dates, water-authority filing requirements), before he walks. Get the data migration
right and this is one of the most automatable recurring-revenue books a small-business
buyer can find.

INHERITED-SYSTEMS SKETCH
- Renewal/customer book: a spreadsheet and/or paper filing cabinet listing properties,
  assemblies, and approximate annual test-due dates. This IS the business; everything
  else is secondary. Condition: fragile, owner-dependent, almost certainly incomplete
  or inconsistent (missing serial numbers, stale contacts, no normalized due-date field).
- Scheduling/dispatch: manual — the owner knows the route in his head and works off the
  list. No dispatch software, no route optimization, no mobile field app.
- Certificates & test reports: generated manually (paper forms or fillable PDFs), then
  filed with each local water authority via that authority's process (paper, fax, email,
  or — increasingly — a web portal like SwiftComply / BSI Online / Aqua Backflow /
  Tokay, which many purveyors now mandate for filing).
- Authority filing: a patchwork of jurisdiction-specific submission methods. This is the
  one place real external system dependency lives — not in the seller's tech, but in the
  water authorities' required portals.
- Accounting/invoicing: likely QuickBooks Desktop or paper invoices; payments probably
  check/manual. No recurring-billing automation.
- CRM / marketing: none. No website worth the name, no CRM, no review presence, no SEO,
  no automated renewal reminders. Lead flow is incumbency + water-authority referral.
- Data debt: the principal debt is data capture quality, not data extraction from a bad
  system — there's almost no system to extract from. The debt is in paper.
- Lock-in: effectively none on the seller side. Replaceable everything. The only
  "lock-in" is to each water authority's mandated filing portal, which you must use
  regardless of buyer.

MODERNIZATION PLAN
This is a buy-SaaS, don't-build situation. The flagship move is converting the manual
renewal list into an automated recurring-renewal engine. There is purpose-built vertical
SaaS for exactly this niche, plus a generic-stack fallback.

90-DAY QUICK WINS
1. Stand up the renewal engine on backflow-specific SaaS. Named options: SwiftComply,
   BSI Online, Aqua Backflow, Tokay (Waterger), or TestRevTrack — all built for backflow
   testers and many already integrated with the water authorities' filing portals.
   Effort: 2–4 weeks [ASSUMED, range 2–6 wks] to configure and load the book. Verify by
   requesting a vendor demo + a sample import template during diligence. Expected gain:
   automated test-due tracking and renewal reminders replace the single most fragile,
   owner-dependent process in the business — this is the core value capture.
2. Data migration of the renewal book into that SaaS (the critical-path task). Effort:
   2–5 weeks [ASSUMED] depending on whether the list is a usable spreadsheet (fast) or
   paper-only (slow; needs manual entry of each assembly's serial, type, location, and
   due date). Verify by getting a copy of the actual list early in diligence and counting
   how many assemblies have complete records.
3. Digital invoicing + payments: QuickBooks Online + Stripe/QBO Payments. Effort: 1–2
   weeks. Gain: faster cash collection, recurring/auto-invoicing on the renewal cadence,
   eliminates paper.
4. Automated renewal reminders: SMS/email sequences (built into the vertical SaaS, or
   via a layer like Twilio/SendGrid) triggered off test-due dates. Effort: 1 week on top
   of #1. Gain: this is the recurring-revenue retention machine — reduces lapsed renewals
   and the labor of chasing them by phone.
5. Basic web presence + Google Business Profile + review generation. Effort: 1–2 weeks.
   Gain: capture the inbound and water-authority-referred demand the seller never did.

LONGER PROGRAM (months 3–12)
6. Mobile field app for testers: on-site test entry on a phone/tablet (built into
   SwiftComply/BSI/Aqua class apps), auto-generating the certificate and pushing it to
   the authority portal. Effort: 4–8 weeks of rollout + crew adoption. Gain: eliminates
   paper double-entry, cuts time-per-test, reduces filing errors.
7. Route optimization across the testing routes. Effort: 2–4 weeks (often included in
   the vertical SaaS or via a tool like Routific/Workwave). Gain: more tests/day/tester
   = direct capacity and margin gain, the lever that grows the book without new hires.
8. AI/automation layer: an AI booking/reminder agent on the phones (e.g., a voice agent
   or Twilio-based assistant) to schedule renewals and answer routine property-manager
   calls; AI-assisted drafting of renewal/outreach comms; AI to reconcile the messy
   inherited list (de-dupe, flag missing serials). Effort: 3–6 weeks [ASSUMED]. Be
   honest about limits: AI will NOT reliably interpret a failed-test diagnosis or file a
   legal certification autonomously — those stay human-in-the-loop. AI's reliable wins
   here are scheduling, reminders, comms, and data cleanup.

Overall: a competent operator can hit the core quick wins (renewal engine + reminders +
digital billing) in the first 60–90 days; the full modernized, mobile, AI-assisted
operation is a 6–12-month program. Expected aggregate gain [ASSUMED]: 10–20% capacity
uplift per tester from route + mobile efficiency, and a measurable lapse-rate reduction
on renewals — verify the current lapse rate against the seller's year-over-year retained
assembly count.

CRITICAL ASSUMPTIONS
1. The renewal list can be exported/captured into structured data. If it's a clean
   spreadsheet, easy; if it's paper-only with the real schedule in the owner's head, the
   migration is the whole risk. Verify: demand the actual list in diligence and audit
   completeness (how many assemblies have serial #, type, location, due date, authority).
2. The local water authorities' filing methods are compatible with the chosen SaaS. Many
   already mandate portals like SwiftComply/BSI; your SaaS must support filing to the
   specific authorities this book covers. Verify: list the authorities served, confirm
   each one's filing method and SaaS integration before buying.
3. The crew/testers will adopt mobile software. Long-tenured field testers may resist a
   phone-based workflow. Verify: meet the testers; gauge tech comfort; budget for the
   slowest adopter.
4. Certified-tester capacity transfers independently of the owner. This is an ops/legal
   point but it gates everything technical — automation is worthless if no certified
   person can legally perform/sign the test. Verify: confirm a non-owner certified tester
   is employed and retainable, or that one can be hired/certified in reasonable time.
5. The book's due-date distribution is real and recurring. The whole automation thesis
   assumes a genuine annual renewal cadence. Verify: reconcile the list against the last
   2–3 years of invoices to confirm assemblies actually re-test annually.

INHERITED INFORMATION-SECURITY POSTURE
Data held: customer/property-owner and property-manager contact info (PII — names,
addresses, emails, phones), assembly/site location data, test certifications, and
payment info if cards are taken. Where it lives today: paper in a filing cabinet and a
spreadsheet on the owner's PC — meaning the inherited threat model is mundane but real:
no backups (a fire/flood/dead hard drive could destroy the renewal book = the entire
business), no access controls, a likely-shared/unpatched home-office PC, and payment
data possibly handled informally. There is little classic cyber attack surface today
precisely because there's little online — but there's also zero resilience. First-90-day
controls: (a) immediately back up and digitize the renewal list to cloud SaaS with
versioning — this is a business-continuity control, not just security; (b) move payments
to a PCI-compliant processor (Stripe/QBO) so you never store card data; (c) enable MFA
and per-user accounts on QuickBooks Online, the SaaS, and email; (d) company-owned,
encrypted devices with a password manager, retiring the shared home PC. At scale: a
written backup/retention policy, vendor due-diligence on the SaaS providers (they now
hold your crown-jewel data), and basic phishing awareness for staff. Incident readiness
today is effectively zero and must be built from scratch — but it's a short, cheap list.

SCORES (1–10)
1.  Inherited systems condition:        3  — Paper filing cabinet + a spreadsheet + owner's memory; no scheduling, CRM, or billing software in place.
2.  Technical & data debt:              5  — Almost no legacy-system extraction debt (nothing to be locked into), but the renewal book's data-capture quality is the whole risk; paper-to-structured migration is the debt.
3.  Modernization upside — tech/AI:     9  — Glaring, high-ROI fit: purpose-built backflow SaaS (SwiftComply, BSI Online, Aqua Backflow, Tokay) turns the manual list into an automated renewal engine with reminders, mobile entry, and authority e-filing — a rare clean match.
4.  Effort to modernize:                7  — Core renewal engine + reminders + digital billing configurable in ~6–8 weeks of off-the-shelf setup; only real work is data migration, not a build.
5.  Critical dependency risk:           6  — No seller-side software lock-in, but a real external dependency on each water authority's mandated filing portal (e.g., SwiftComply/BSI), which the SaaS must support.
6.  Cybersecurity posture inherited:    4  — No backups of the crown-jewel renewal list and a likely-shared owner PC create real business-continuity exposure; small online attack surface but zero resilience.
7.  Data ownership & migration:         5  — Data is owned and not vendor-trapped, but if it's paper/in-head rather than a clean export, migration is slow and error-prone — the central diligence question.
8.  Automation / AI leverage:           8  — Concrete reliable wins: automated renewal reminders (SMS/email off due-dates), route optimization for tests/day, AI booking/reminder phone agent, and AI list de-dup; signing/diagnosing stays human.
9.  Scaling / tech headroom:            8  — Vertical SaaS scales to more testers, routes, and tuck-in books natively (e.g., SwiftComply multi-user/route); bolt-ons fold in without re-platforming.
10. Ongoing maintenance burden:         9  — Pure managed SaaS once configured; no custom code, no on-call burden for two owner-operators — it self-runs.

AVERAGE SCORE: 6.4 / 10

TOP 3 TECHNICAL STRENGTHS
- A rare, clean off-the-shelf fit: backflow-specific SaaS (SwiftComply, BSI Online, Aqua
  Backflow, Tokay) exists precisely to turn this manual list into an automated recurring-
  renewal engine — buy-SaaS, don't-build, with mobile field entry and authority e-filing.
- Almost no inherited tech debt or lock-in: there's no ancient custom system to escape,
  so modernization is additive, not a costly migration off a legacy platform.
- Once configured, the stack is fully managed SaaS — near-zero ongoing maintenance burden
  for two owner-operators, and it scales to more testers, routes, and bolt-on books.

TOP 3 TECHNICAL RISKS
- The crown-jewel renewal book may live on paper and in the owner's head, making the
  data migration the make-or-break technical task — slow, error-prone, and time-boxed by
  his retirement.
- Zero backups / single-PC fragility today: the entire business asset is one hard-drive
  failure or filing-cabinet fire from gone until it's digitized.
- External dependency on each water authority's mandated filing portal — the chosen SaaS
  must integrate with the specific authorities this book serves, or filing stays manual.

BIGGEST SINGLE RISK
The single most dangerous technical issue is that the recurring-renewal book — the only
asset you're really buying — appears to live in a filing cabinet and the retiring owner's
memory, not in software. The automation thesis (reminders, mobile entry, route
optimization, AI booking) is only as good as the structured data underneath it, and if
each assembly's serial number, device type, install location, water authority, and
true test-due date aren't captured cleanly BEFORE the owner leaves, you will spend the
first year reconstructing the schedule from invoices and angry property managers — bleeding
exactly the renewals that justify the price. This is not a stack problem; it's a data-
capture-and-knowledge-transfer problem, and it is fully front-loaded into diligence and
the transition window. Mitigate by making a complete, audited export of the renewal list
a closing condition and structuring the seller's transition/training period explicitly
around digitizing the book with him in the room.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- In what form does the renewal list actually exist — a usable spreadsheet, or paper plus
  the owner's memory — and for what fraction of assemblies are serial number, device type,
  location, water authority, and test-due date all recorded?
- Which specific water authorities does this book file to, what is each one's mandated
  filing method/portal (SwiftComply, BSI Online, Aqua Backflow, Tokay, or paper), and does
  a single chosen vertical SaaS support filing to all of them?
- What is the current renewal lapse rate — how many assemblies on the book actually got
  re-tested in each of the last 2–3 years — and can it be reconciled against invoices to
  prove the recurring cadence the automation depends on?
- Who, besides the owner, currently knows the route and the schedule, and is any non-owner
  certified tester employed and retainable so capacity (and signing authority) survives
  his exit?
- Is any payment-card data stored or handled informally today, and where do customer
  records and any backups currently reside?

RECOMMENDATION: GO
From a systems and modernization standpoint this is exactly the kind of target the
thesis is built for: minimal inherited tech debt, no legacy lock-in, a glaring off-the-
shelf modernization fit, reliable automation/AI leverage, and near-zero ongoing
maintenance burden once configured. The GO is conditioned on diligence proving the
renewal data can be captured into structured form before the owner leaves — make a
complete, audited export of the renewal book a closing condition and build the seller's
transition period around digitizing it with him present. If diligence reveals the book
is paper-only and incomplete with no cooperative knowledge transfer, that flips toward
RE-TRADE (lower price to fund the reconstruction labor and lapse risk), not a walk.
