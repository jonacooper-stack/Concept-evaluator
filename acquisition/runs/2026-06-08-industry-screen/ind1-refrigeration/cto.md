# CTO REVIEW — Commercial Refrigeration Service

## ONE-PARAGRAPH TECHNICAL READ
Commercial refrigeration service is a classic un-modernized, dispatch-heavy field-service
trade where the typical sub-$5M operator runs on paper work orders, a whiteboard or wall
calendar for dispatch, QuickBooks Desktop, and a phone-and-relationships sales motion — with
no field-service-management (FSM) software, no CRM, and no digital lead capture. The
modernization gap is large and, crucially, broad: nearly every operator in the fragmented
tail looks the same, so the founders' tech edge applies across essentially the whole field
rather than to one lucky target. The genuinely distinctive upside versus generic HVAC is
**IoT refrigeration monitoring as a recurring service line** (temperature/compressor
telemetry on assets customers literally cannot let fail), which turns a sleepy break-fix
shop into a monitored-recurring-revenue book. The honest caveat: the moneymaker is mature,
boring SaaS configuration and disciplined process change, not exotic AI — AI helps at the
margins (comms, scheduling assist, review generation), but it does not turn a wrench or
replace a 608-certified tech.

## TYPICAL SYSTEMS LANDSCAPE
- **Accounting:** QuickBooks Desktop or QuickBooks Online is near-universal in the
  sub-$5M trades; many still on Desktop with a bookkeeper. Sage 50 appears occasionally.
  This is the one system that usually exists.
- **Dispatch / scheduling:** typically MANUAL — wall calendar, whiteboard, spreadsheet, or
  the owner's head and cell phone. Real FSM adoption is rare in this segment.
- **Work orders / invoicing:** paper tickets the tech fills out, re-keyed later into
  QuickBooks; or PDF invoices. Double entry and lost tickets are the norm.
- **CRM / customer database:** usually nonexistent as a system — customer relationships live
  in the owner's memory, a Rolodex, or QuickBooks customer records. PM-contract renewal
  tracking is manual.
- **Estimating / quoting:** ad hoc, often verbal or a one-line written quote; little
  templated good-better-best.
- **Website / marketing:** thin brochure site or none; no SEO, no Google Business Profile
  optimization, no lead forms; word-of-mouth and inbound calls dominate.
- **Asset / monitoring data:** the high-value gap — most operators do NOT sell or run remote
  IoT monitoring of customer refrigeration assets, leaving recurring monitoring revenue and
  predictive-maintenance data on the table.
- **Payments:** check and ACH heavy; card-on-file and integrated payments uncommon, so
  collections drag DSO.

## MODERNIZATION PLAN (typical)
**Named off-the-shelf stack (works across the industry):**
- **FSM / dispatch / mobile work orders:** **BuildOps** or **ServiceTitan** at the larger
  commercial end (both have strong commercial-refrigeration/mechanical workflows and PM-
  agreement modules); **Jobber** or **Housecall Pro** for smaller books where ServiceTitan
  is overkill/over-priced. **FieldEdge** and **Service Fusion** are mid-market alternatives.
  All carry scheduling, mobile tickets, customer history, PM-agreement automation, and
  integrated invoicing.
- **Accounting:** keep/standardize on **QuickBooks Online**; FSM tools above sync to it
  natively, killing the re-keying.
- **Payments:** **Stripe** or the FSM's embedded payments (ServiceTitan/Jobber payments) for
  card-on-file and faster collections.
- **CRM / pipeline (commercial B2B sales):** **HubSpot** (free–Starter tier is enough early)
  for PM-contract pipeline, renewals, and outbound to multi-location accounts.
- **Marketing:** Google Business Profile + local SEO + a real lead-form site; for B2B,
  targeted outbound to grocery/c-store/restaurant chains.
- **IoT refrigeration monitoring (the differentiated line):** named platforms exist —
  **Therma**, **SmartSense by Digi**, **Axiomatic/Sensaphone**, **Monnit**, plus OEM
  telemetry from **Emerson (Copeland/E2/E3)** and **Danfoss** controllers. Resold as a
  monitored-PM upsell, this creates recurring per-site monthly revenue and feeds break-fix
  dispatch.

**90-day quick wins:** stand up FSM + QBO sync + integrated payments and migrate active
customers/PM agreements — roughly **6–10 weeks** to live on FSM for a single-location
operator [ASSUMED; verify against the FSM vendor's onboarding SOW and the target's customer
count]. Expected gain: eliminate double entry, cut DSO via card-on-file, stop revenue
leakage from untracked PM renewals, and give dispatch real-time visibility. Add Google
Business Profile + lead forms in parallel (~2 weeks).

**Longer program (6–18 months):** roll out IoT monitoring as a paid recurring service line
to the existing base, build the HubSpot B2B pipeline for multi-location chains, and
standardize good-better-best quoting. Expected gain: convert a break-fix book into
monitored recurring revenue with higher retention and predictive dispatch. AI leverage is
real but bounded: **AI scheduling/dispatch assist** inside modern FSM, **AI phone/SMS
agents** (e.g., to triage after-hours emergency calls and book/route them), **AI review and
follow-up automation**, and **AI back-office** (categorization, AP, draft estimates). Be
honest: AI does not diagnose a failed compressor on site, does not replace the 608-certified
tech, and IoT monitoring still requires a human to dispatch and fix — AI compresses
overhead and improves response, it does not remove the labor constraint.

## WHAT I AM DEFERRING TO DUE DILIGENCE
- THIS company's actual systems condition — whether it's already on an FSM, on QuickBooks
  Desktop vs Online, or genuinely all paper — and the real migration effort that follows.
- THIS company's data exportability — whether customer/PM-agreement/asset history can be
  cleanly extracted from whatever it runs today, or is trapped in paper/an owner's head.
- THIS company's inherited security/IT posture — endpoint hygiene, who holds admin/vendor
  logins, any prior breach, and whether stored customer payment data is handled compliantly.

## SCORES (1–10)
1.  Typical systems landscape:          8  — Industry broadly runs on paper tickets + manual dispatch + QuickBooks; FSM adoption rare at sub-$5M, so the gap is real and named.
2.  Off-the-shelf tools available:      9  — Strong, affordable, named SaaS exists end-to-end: BuildOps/ServiceTitan/Jobber/FieldEdge + QBO + Stripe + HubSpot.
3.  Modernization-tech upside:          8  — Big gap (manual ops → FSM) PLUS a differentiated IoT-monitoring recurring line via Therma/SmartSense/Emerson telemetry; edge applies across the fragmented field.
4.  Automation / AI leverage:           6  — Real but bounded: AI dispatch assist, after-hours SMS/voice triage, review/back-office automation; AI can't diagnose or repair, and the 608-tech labor constraint stays.
5.  Data-portability norms:             7  — QuickBooks data exports cleanly and FSM vendors offer standard import paths; the catch is paper/owner's-memory data that must be re-entered, capping this short of an 8.
6.  Integration / lock-in risk:         7  — Mainstream FSM↔QBO↔Stripe integrations are standard and swappable; ServiceTitan/BuildOps carry some switching cost once configured, but the model isn't tied to one proprietary platform.
7.  Cybersecurity exposure:             7  — Mostly B2B operating data plus some card-on-file; lighter than health/consumer-PII businesses, though integrated payments and IoT devices add a managed surface that keeps it below a 9.
8.  Tech scalability (modernized):      8  — FSM (BuildOps/ServiceTitan) is multi-location/multi-crew by design and absorbs bolt-ons without a re-platform; HubSpot scales with the account base.
9.  Implementation effort:              7  — Core FSM + QBO + payments is a weeks-not-years configure-and-migrate (~6–10 weeks [ASSUMED]); the IoT line and full B2B pipeline extend the program, holding this to a 7.
10. Ongoing maintenance burden:         8  — Stack is SaaS/managed (BuildOps/ServiceTitan/QBO/HubSpot/Stripe) and self-running; no custom engineering required, just configuration and admin.

## AVERAGE SCORE: 7.5 / 10

## TOP 3 TECHNICAL STRENGTHS (of the type)
1. A complete, named, affordable off-the-shelf stack already exists for this exact model
   (BuildOps/ServiceTitan/Jobber + QuickBooks Online + Stripe + HubSpot) — nothing custom to build.
2. A genuinely differentiated tech-driven recurring-revenue line — IoT refrigeration
   monitoring (Therma/SmartSense/Emerson telemetry) — that fits the essential, can't-fail
   nature of the assets and is largely unexploited across the field.
3. The modernized stack is SaaS/managed and multi-site by design, so it scales to crews,
   routes, and bolt-ons without re-platforming or ongoing custom engineering.

## TOP 3 TECHNICAL RISKS (of the type)
1. The bottleneck is human, not software — 608-certified technician supply — and no tool or
   AI relieves it; tech can streamline overhead but not manufacture skilled labor.
2. The headline FSM (ServiceTitan/BuildOps) carries configuration and switching cost; a
   sloppy or over-scoped rollout can stall and consume months without value.
3. Source data is often paper or in the owner's head, so the real migration cost is
   re-entry and process change, not the SaaS license — easy to underestimate.

## BIGGEST SINGLE RISK
The single biggest technical-strategy trap in this TYPE is mistaking the easy availability of
great FSM software for an easy transformation. The software is mature, named, and cheap; the
hard part is that the operating data and tribal knowledge in these businesses typically live
on paper tickets and in the retiring owner's memory, and the value-creating work is forcing a
crew of veteran technicians to change how they capture jobs, quote, and renew PM contracts.
If migration and adoption are botched — over-scoping ServiceTitan, failing to clean and
import customer/asset data, or losing tech buy-in — the modernization stalls and the founders
inherit double systems and frustrated crews. This is an implementation-discipline and
change-management risk inherent to the type, not a fatal one, but it is what most often turns
"obvious upside" into a slog. Notably, it is a risk the founders' software capability is well
suited to manage, which is why the industry still reads as attractive.

## QUESTIONS TO ANSWER WHILE SOURCING IN THIS INDUSTRY
1. What share of the target's revenue is recurring PM/monitoring versus one-off break-fix,
   and is any of it already running on an FSM or remote-monitoring platform?
2. Can customer, PM-agreement, and refrigeration-asset history be exported cleanly, or does
   it live on paper / in the owner's head (driving real migration cost)?
3. Which IoT-monitoring platform(s) do the target's customers' OEM controllers support
   (Emerson Copeland/E2-E3, Danfoss, etc.), so a monitoring upsell rides existing hardware?
4. How card-/payment-integrated is the business today, and is any stored payment data handled
   in a way that creates inherited compliance/security cleanup?

## RECOMMENDATION: PURSUE
This is a strong TYPE through the technology lens: a broadly un-modernized, fragmented field
running on paper and QuickBooks, served by a complete named off-the-shelf stack
(BuildOps/ServiceTitan/Jobber + QBO + Stripe + HubSpot) that configures in weeks and runs
itself, plus a differentiated, largely-untapped IoT-monitoring recurring-revenue line that
fits assets customers cannot let fail. The honest discounts — AI can't touch the
608-technician labor constraint, and the real cost is data migration and change management,
not licenses — keep individual dimensions out of 9+ territory but do not undermine the
thesis. The founders' software edge applies across essentially the whole field, so I would
hunt here, prioritizing targets with a service-agreement base and customers whose OEM
controllers already support a monitoring upsell.
