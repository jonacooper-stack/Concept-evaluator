COO REVIEW — Member Engagement & Dues-Collection Overlay for Labor Unions

ONE-PARAGRAPH OPERATIONS READ

This is a software overlay with a payments rail and an SMS rail bolted on — structurally a remote-first, low-touch SaaS-plus-fintech business that two founders can build and operate, NOT a field-ops business. The operational core is sound: send email/SMS, capture re-enrollment data, move money via card/ACH. The real operational friction is not "trucks and installs," it is three less obvious things: (1) integrating with a long tail of heterogeneous legacy union databases (UnionWare, Union Link, plus homegrown Access/Excel/FileMaker systems) which is bespoke, slow, and the throughput bottleneck; (2) becoming, in practical effect, a money-services operation — handling dues-money flows, chargebacks, ACH returns, reconciliation, and payout disputes, which is recurring high-stakes ops work; and (3) the deliverability/compliance machinery behind sending SMS to millions of members (10DLC registration, opt-in/opt-out handling, carrier filtering). None of these are fatal, but they are where the two-person team actually gets pinned down. The model can be operated lean if onboarding is genuinely productized and payments/messaging are ridden on top of established providers (Stripe/Adyen, Twilio/Telnyx) rather than built.

THE TUESDAY-IN-MARCH WALKTHROUGH

Assume month 12. The business has roughly 18 union-body customers signed (a mix of state-level affiliates and a couple of national bodies that rolled the free tier down to their locals), translating to perhaps 280 active chapters/locals using the tool and around 220,000 members loaded into the system [ASSUMED: see capacity math; verify by counting that a single mid-size state affiliate is ~150–400 locals and 50K–250K members via that union's LM-2 filing on the DOL OLMS public database]. March matters because spring is a heavy re-enrollment and dues-drive season for public-sector unions tied to budget and school-year cycles — so this is a near-peak day, which is exactly when you want to stress-test.

7:30am — Founder A (engineering/ops) checks the overnight payments dashboard. Yesterday the platform processed roughly $90K in dues across card and ACH. Overnight, 140 ACH debits returned (R01 insufficient funds, R02 closed account, R10 unauthorized) and 22 card chargebacks/disputes posted. Each ACH return and each chargeback is a money event that flows back to a specific chapter's expected dues total, so a reconciliation job has to re-attribute them and flag the members whose dues failed. Founder A spends the first hour confirming the automated reconciliation matched correctly and manually handling ~15 edge cases the matcher couldn't resolve (a member whose employer changed, a duplicate enrollment). This is recurring daily work and it grows linearly with dues volume.

8:30am — A new state affiliate that signed two weeks ago needs its legacy database connected. Their system of record is UnionWare on-prem with a SQL backend, but the IT contact is a part-time staffer who is nervous about exporting member PII. Founder A is on a screen-share walking them through a one-time CSV export and field-mapping (which of their 40 columns is "personal cell" vs "work cell," how membership status is coded). This single onboarding integration consumes 4–8 hours of founder time spread across the week and cannot be fully self-served because every union's schema and data hygiene differ. This is the throughput bottleneck.

10:00am — Founder B (marketing/sales/success) runs a working session with a national union's communications director who wants to push a statewide SMS blast to 60,000 members for a contract-vote drive. Before it can send, the campaign's sending numbers must be properly 10DLC-registered and the message must respect opt-outs; Founder B checks the campaign won't trip carrier spam filtering at that volume and schedules it in tranches. Two locals message that members are replying "STOP" and then complaining they no longer get vote reminders — a support thread about opt-out semantics.

12:30pm — A chapter officer calls: a member disputes that $47 was charged twice. Founder B pulls the payment record, sees a double-submit on the renewal form, issues a refund through the processor dashboard, and files a note. Three more support tickets sit in the queue (a password reset for a local officer, a permissions question about who at the district can see member phone numbers, a request to bulk-correct 300 mis-imported emails).

2:00pm — Founder A ships a small fix to the renewal workflow (a state added a legally-required disclosure checkbox to the dues-authorization form; several states mandate specific authorization language post-Janus, so the form must be configurable per state). This is recurring product work driven by a patchwork of state rules.

4:00pm — Founder B does a renewal/expansion call with leadership of an existing customer, showing them a dashboard of re-enrollment conversion (e.g., "62% of texted members who opened the renewal link completed re-sign"). This is the metric that justifies the whole relationship and drives the land-and-expand down to more locals.

Where it breaks: the day is survivable, but two pressure points are visible. First, onboarding new union databases is bespoke and founder-gated — at ~2 founders you can absorb maybe 2–4 new union-body integrations per month before it crowds out everything else. Second, payments operations (returns, chargebacks, reconciliation, disputes) is a permanent daily tax that scales with dues throughput and is unforgiving — getting member dues money wrong is reputationally and contractually severe for a union.

CAPACITY MATH (show the work)

Target: the income ladder — ~$300K/founder (~$600K total) by month 12, ~$500K+/founder (~$1M+ total) by month 24. I'll size against the month-24 figure of ~$1M total net revenue to the company, since that is the harder operational test. [Relabeling note: the council doc's "$2M/founder in 24 months" is overridden by 01-objectives.md's ladder; I score Path-to-income against ~$300K→$500K+/founder.]

Two revenue lines:

1) Payments take-rate on dues. Public-sector union dues run roughly $40–$100/member/month [ASSUMED: $50/member/month average; verify against published dues schedules — e.g., NEA/AFSCME local dues tables are often public]. Suppose a take-rate (net spread above processor cost) of ~0.5% on dues processed [ASSUMED: 0.3–0.8% net margin above Stripe/ACH interchange; verify with a Stripe Connect platform-fee quote]. To net $700K/year from payments at 0.5% net, you must process $140M/year in dues. At $50/member/month = $600/member/year, that is ~233,000 members paying digitally through the platform. That is a large but not absurd number — a single large state affiliate can be 100K–250K members. So the math closes on the order of a handful of large affiliates fully converting their dues to digital collection. The operational catch: those members must be converted off payroll-deduction onto card/ACH, which is exactly the painful re-enrollment the union is struggling with; conversion is not automatic.

2) SMS markup. If 233K members each receive ~30 platform messages/year (renewal drives, votes, actions) = ~7M messages/year. At a markup of ~$0.005/message net [ASSUMED: $0.003–$0.01 over Twilio/Telnyx wholesale; verify with a Telnyx 10DLC price sheet] = ~$35K/year. SMS is a real but secondary line; payments carry the model.

So ~$1M company revenue is roughly $700K payments + small SMS + the rest from larger member counts or higher dues. The decisive operational variable is digital dues throughput, which depends on re-enrollment conversion, not on headcount.

Staffing test. The recurring delivery units are: (a) database onboarding integrations, (b) payment-operations handling, (c) support tickets, (d) messaging-campaign assistance.
- Onboarding: at ~233K members across, say, 6–10 union bodies and ~300 locals, you onboard ~10 bodies in year one to two. At 6 founder-hours per body integration plus per-local activation, that is light once the integration tooling exists — call it 1 founder-week per major body, front-loaded, not steady-state.
- Payment ops: processing $140M/year ≈ ~233K monthly debits. At a 3–5% combined ACH-return + dispute rate [ASSUMED; verify with processor benchmarks], that is ~8,000–12,000 money-fail events/month. If automation resolves 90%, ~800–1,200 manual touches/month at ~3 min each = ~40–60 hours/month = ~0.3 FTE. Manageable by one founder + automation, but it is the line that forces the first hire.
- Support: at 300 local officers + member-level escalations, ticket volume is moderate; ~10–25 tickets/day at month 12, ~10 min each ≈ 2–4 hours/day = within two founders, but pushes toward a part-time support/ops hire (~$50–70K/year) somewhere between month 12 and 24.

Verdict on capacity: two founders + ONE ops/support hire by ~month 18 can plausibly operate this at the ~$1M revenue level, BECAUSE the revenue scales with dues-dollars-processed (a software/payments throughput, near-zero marginal labor per dollar) rather than with seats or installs. The bottleneck is bespoke onboarding early and payment-operations later — both bounded, neither field-ops.

SCORES (1–10)

1. Delivery clarity & repeatability: 6 — The send/collect/re-enroll workflow is standardized, but the load-bearing first step (integrating a heterogeneous legacy database of record per customer) is bespoke per union and only semi-repeatable; "deploys in days across chapters" holds only after the body-level integration is done.

2. Supply chain resilience: 7 — Inputs are cloud + payments + SMS providers; payments (Stripe/Adyen) and SMS (Twilio/Telnyx/Bandwidth) each have 2+ swappable named vendors, so no single-source MOQ/deposit exposure — but a switch mid-flight is non-trivial because money rails carry migration cost.

3. Logistics tractability: 9 — Zero physical logistics: no trucks, installs, routing, or on-site work; entirely remote software/data/money movement deliverable from anywhere to all 50 states, which is the structural opposite of field ops.

4. Customer-ops scalability: 5 — Mixed: messaging and dues collection are low-touch and self-scaling, but money-handling support (chargebacks, ACH returns, refunds, reconciliation disputes) and per-state form/authorization configuration are recurring high-stakes touches that grow with volume and cap pure self-serve.

5. Vendor/partner dependency risk: 6 — You ride payment processors and carriers whose terms you don't control; a processor de-risking "political/union money" or a carrier tightening 10DLC could pinch, but each has named alternatives so it is a manageable, not bet-the-business, dependency.

6. Hiring feasibility: 8 — First hire is a remote ops/support generalist handling payment exceptions and tickets at ~$50–70K/year, drawn from a deep, geographically-unconstrained labor pool; no scarce specialized labor and no field crew required.

7. Throughput capacity at target: 8 — Revenue is a take-rate on dues-dollars and a markup on messages — ~$140M processed and ~7M messages map to near-zero marginal labor per dollar, so 2 founders + 1 ops hire clear ~$1M revenue without a 50-person org (see capacity math).

8. Quality control simplicity: 5 — Standardizable on the software side, but money correctness is unforgiving: a mis-applied dues charge or a botched reconciliation against a union's member is a severe failure mode (refunds, reputation, contract risk), so variance tolerance is low and QA burden is real.

9. Geographic / seasonality risk: 7 — National (all 50 states), weather-neutral, year-round; there is real seasonality (re-enrollment/dues drives cluster around budget and school-year cycles and election/contract events), creating peaky campaign load but no structural off-season since dues recur monthly.

10. Tooling maturity available: 7 — The core stack is buyable/composable (Stripe Connect for split payments, Twilio/Telnyx for 10DLC SMS, standard CRM/ticketing), so most operating tooling is off-the-shelf; the per-union integration connectors and per-state form engine must be built, which is normal product work, not exotic.

AVERAGE SCORE: 6.8 / 10

TOP 3 OPERATIONAL STRENGTHS
- No field operations whatsoever: 50-state reach with zero trucks/installs/routing, deliverable remotely by two founders (logistics 9).
- Revenue scales with dues-dollars and message volume, not seats or labor — ~$140M processed maps to near-zero marginal staffing, so 2 founders + 1 ops hire can reach ~$1M revenue (throughput 8, hiring 8).
- The operating stack is largely buyable: Stripe Connect + Twilio/Telnyx + off-the-shelf CRM cover most needs, with only the integration connectors and per-state form engine to build (tooling 7).

TOP 3 OPERATIONAL RISKS
- Bespoke per-union database integration with heterogeneous, poorly-maintained legacy systems is the real onboarding bottleneck and is founder-gated early (delivery 6).
- Becoming a de facto money-movement operation: ACH returns, chargebacks, reconciliation, and refunds are a permanent daily tax that scales with dues throughput and is unforgiving of error (customer-ops 5, QC 5).
- Dependency on payment processors and SMS carriers whose policies you don't control — processor appetite for "union/political money" and carrier 10DLC/spam filtering can throttle the two revenue lines (vendor risk 6).

BIGGEST SINGLE RISK

The operational issue most likely to pin two people down is that this is, underneath the "engagement overlay" framing, a payments-operations business handling other people's mission-critical dues money at scale — and money operations do not self-serve. At ~$140M/year processed, you are reconciling roughly a quarter-million debits a month against specific chapters, absorbing thousands of ACH returns and hundreds of disputes, issuing refunds, and answering "why was my member charged twice" from chapter officers who treat every cent as sacred because dues are the union's lifeblood. Every one of those events maps back to a particular local's expected revenue, so errors are not cosmetic — they break trust with the exact buyer who mandated the rollout. This is survivable with strong automation and one ops hire, but it is the function that quietly forces headcount earliest and where a two-person team is most exposed, because unlike a pure SaaS bug, a money error is immediate, public, and contractually serious. The founders must treat reconciliation, dispute handling, and per-state authorization compliance as first-class operating systems from day one, not as something to "figure out" after the first big affiliate goes live.

QUESTIONS THE FOUNDERS MUST ANSWER BEFORE I'M COMFORTABLE
- What is the real per-union integration cost in founder-hours across the top 3 systems of record (UnionWare, Union Link, and homegrown Access/Excel), and can you build a reusable connector/import tool that gets a new body live without bespoke engineering each time? Verify by attempting one real import end-to-end.
- Which payment processor will underwrite union/political-adjacent dues money at $100M+ scale, what is their reserve/rolling-hold and chargeback-threshold policy, and what is your contingency if they offboard you mid-flight? Get a written platform-fee and risk-policy quote from Stripe Connect and one alternate.
- What is your realistic re-enrollment conversion rate from payroll-deduction to direct card/ACH (the variable the entire revenue model rests on), and how much founder/ops labor does each dues-drive campaign require — i.e., is conversion a product event or a high-touch services event?

RECOMMENDATION: REFINE

Operationally this clears the bar that matters most to me: it is genuinely remote-first, field-ops-free, and 50-state capable, and the revenue scales with dues-dollars rather than headcount, so two founders plus one ops hire can plausibly run it to ~$1M revenue. I'm not at GO because two operating realities need to be designed down before launch, not after: (1) productize the legacy-database onboarding so each new union body is a tooling event, not a bespoke engineering project — this is the early throughput ceiling; and (2) stand up payment-operations as a first-class system (automated reconciliation, return/chargeback handling, per-state dues-authorization form configuration, and a named processor with documented risk appetite for union money) before the first large affiliate's dues flow through you. If the founders can show a reusable connector working on one real union database and a processor committed to underwriting this money at scale, this moves to GO.
