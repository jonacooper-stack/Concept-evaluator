# Muster — Site Update Instructions: Specialize, Differentiate, Keep the Gap-Analysis Experience
**Prepared 2026-06-21 · companion to the council evaluation (Tier B, 76/100)**

This is a developer-ready spec. It does three things at once: (1) keep and *elevate*
the upload-policies → gap-analysis experience you like, (2) make that experience the
thing that proves your moat instead of threatening it, and (3) re-point the
positioning at a defensible niche. Copy blocks are drop-in starting points.

---

## Part 0 — The CUI question (read first; it drives everything below)

**Are a company's policies CUI? Almost always NO.** CUI is information the
*government* originates or that you hold *on the government's behalf*, that a law or
regulation requires to be protected — there are ~100+ defined categories (technical
data/CTI, export-controlled data, etc.) in the NARA CUI Registry. A contractor's own
information-security **policies and procedures are the contractor's own business
records describing how they protect CUI — they are not themselves a CUI category.** So
letting a customer upload their policies for a gap analysis does **not** mean you are
"touching their CUI." The feature is compatible with the wedge.

**But the line that actually governs your moat is not CUI — it's "Security Protection
Data" (SPD).** Under the CMMC rule (32 CFR 170.19), an outside vendor becomes an
in-scope **External Service Provider (ESP)** — and gets pulled into your customer's
assessment — if it *processes, stores, or transmits* **CUI OR SPD**. SPD is the
operational security data: **configuration data, log files, vulnerability-scan
results, the security/config status of in-scope assets, and passwords/credentials.**
The rule explicitly says ordinary SaaS (HR, accounting) that holds none of that is
**not** an ESP. **That carve-out is exactly the box Muster must stay inside.**

**The practical rule that becomes your differentiator:**
- **Safe to ingest (not CUI, not SPD):** written policies, procedures, control-
  implementation narratives, POA&M items, SSP *prose*, questionnaire answers, and
  *descriptions/pointers* to evidence. Holding these keeps you out of scope.
- **Never ingest (this is CUI or SPD — it breaks the moat):** raw firewall/device
  configs, log files, vulnerability-scan exports, network/data-flow diagrams,
  credentials, and anything containing controlled technical data or contract data.
- **Precise claim wording** (don't overclaim): *"We analyze your policies and
  compliance documentation. By design, your CUI and your operational security data —
  configs, logs, scans, credentials — never enter Muster, so we stay outside your
  CMMC assessment boundary."*

**Action that turns this from slogan into moat:** get a government-contracts-counsel
opinion confirming the above keeps you out of ESP scope, and publish a **Customer
Responsibility Matrix (CRM)** + data-handling page (Part 3.1). That is the single
highest-leverage differentiation move you can make, because the funded platforms
(Vanta/Drata/Secureframe) and the enclave bundlers *can't* honestly publish that page
without abandoning their hosting business.

---

## Part 1 — One decision to confirm: the niche

The council's sharpest finding: "fixed price" and "operated for you" are already sold
at scale (CyberSheath, OSIbeyond), so they can't be your headline. Specialization is
how a two-person team beats a crowded field.

**Recommended niche (confirm or swap): precision machine / metal-fabrication / CNC
shops, 15–50 employees, 1–3 named primes.** Rationale: it's where your warm leads
likely cluster; horizontal platforms and generalist RPOs literally can't speak
machine-shop; the community is tight and referral-driven; and you can pre-build
shop-specific control templates. Everywhere below, `[NICHE]` = this segment and
`[PRIME]` = a specific prime (Lockheed, RTX, etc.). If you'd rather pick a different
vertical, swap those tokens — the structure holds.

---

## Part 2 — The gap-analysis flow: keep it, make it safe, make it the wedge

You're right not to lose this — an instant gap analysis off real documents converts
far better than a dry questionnaire. Three upgrades:

### 2.1 Keep the upload → analyze → gap-analysis core
Leave the experience intact. Everything below wraps and elevates it.

### 2.2 Bake in the data boundary (this is what makes it safe AND special)
Before/at upload, constrain what can come in:
- **Accept:** `.pdf/.docx/.md/.txt` policy & procedure documents, and structured
  control-status answers. Frame the ask as *"Upload your security policies and
  procedures"* — never *"upload your evidence/configs."*
- **Add an explicit, friendly boundary notice at the upload control** (copy):
  > **Upload policies — not CUI.** Muster reads your written security *policies and
  > procedures* to find gaps. Please don't upload anything containing CUI or live
  > security data — no network diagrams, scan reports, device configs, or contract
  > files. Here's why that matters: it's exactly how we stay out of your CMMC scope.
  > *(link: "What we accept and why")*
- **Guardrails in code:** enforce file-type/size allow-list; run a lightweight
  client- and server-side scan that flags likely CUI/SPD (keywords like
  "ITAR", "export controlled", "SECRET", presence of image-heavy diagram pages, or
  obvious config/log syntax) and *warns/blocks* with the boundary message rather than
  silently accepting. Strip EXIF/metadata. Never log file contents.

### 2.3 Elevate the output (make it the best free gap analysis in the niche)
- Map findings to **all 110 NIST 800-171 objectives** + the **deterministic SPRS
  estimate** (current + target). Label it clearly an **estimate**, not an official
  posting.
- **Vertical-tune the language** to `[NICHE]` (e.g., reference CNC controllers,
  shop-floor workstations, ITAR drawing handling) so it reads like it was built for a
  machine shop, not a generic SaaS.
- Output a **prioritized, plain-English remediation list** ("fix these 5 first, here's
  why each costs you points").
- **End every report with a trust seal:** *"This analysis read only your policies.
  Your CUI and security data never entered Muster."* — this makes the boundary the
  emotional payoff, not a limitation.

### 2.4 Persist + notify (fixes the current lead-drop)
The deployed `/api/assessment/start` only `console.log`s — leads are lost. Wire it to:
persist the lead **and** the generated report to a datastore (Postgres/Supabase or, as
a stopgap, an email + a sheet); send the report to the user; notify the founders;
fire analytics/conversion events (assessment-started, completed, report-viewed,
call-booked). No paid traffic until this is done.

---

## Part 3 — New / changed pages

### 3.1 NEW: "Scope & Data Handling" page (the moat, made visible) — highest priority
The page the competition can't copy. Include: the plain-English data boundary (Part
0); a downloadable **Customer Responsibility Matrix (CRM)**; the explicit statement
that Muster is *not* an ESP under 32 CFR 170 because it holds neither CUI nor SPD; and
(once you have it) a line that counsel has reviewed the posture. Link to it from the
hero, the upload control, and the footer.

### 3.2 CHANGE: Home hero + `/the-difference` → lead with niche + artifact-only
- **New H1 (copy):** *"CMMC and SPRS, handled — for `[NICHE]`. We never touch your
  CUI."*
- **New subhead:** *"Muster keeps your SPRS score correct and your evidence
  audit-ready every quarter — built for `[NICHE]` shops, operated for you, and
  architected so your CUI never enters our systems."*
- Demote "fixed price / operated for you" from headline to a supporting bullet (still
  true, no longer the lead — because it's commoditized).

### 3.3 NEW: "Built for `[NICHE]`" page
Speak the niche's language: their primes, their CUI (drawings/CTI), their reality (no
IT staff, owner owns SPRS). Show a `[NICHE]`-specific sample gap report. This is what
a generalist competitor can't fake.

### 3.4 NEW (programmatic): "For subs to `[PRIME]`" landing pages
One page per major prime ("CMMC & SPRS for Lockheed suppliers"), each pre-loaded with
that prime's flow-down specifics. Strong SEO + the setup for the Part 4 moat feature.

### 3.5 CHANGE: `/about` → remove the placeholder bios
The live page has `TODO` placeholder roles. Name the founders, the senior DoD/DIB
advisor, and "RP/CCP-reviewed." Trust is the whole sale; an anonymous About page
undercuts it.

---

## Part 4 — Differentiation features to build (beyond copy)

Ranked by moat value:

1. **Prime-specific questionnaire auto-answer library.** Specialize in your customers'
   actual primes: ingest each prime's real flow-down security questionnaire and build
   a reusable, mapped answer set. "We've answered the `[PRIME]` supplier questionnaire
   dozens of times" is a *data* moat that compounds with every customer and is genuinely
   hard to copy. This is your strongest defensible asset over time.
2. **The CRM / scope-letter generator.** Productize the ESP boundary: auto-generate the
   Customer Responsibility Matrix and a short "Muster is out of your assessment scope"
   letter each customer can hand their C3PAO. Nobody else leads with this; it directly
   monetizes the artifact-only posture.
3. **"Forever," not "scramble," tooling.** Lean into the recurring obligation the
   one-time consultants ignore: continuous drift alerts, the annual-affirmation
   workflow, automatic quarterly SPRS re-posting reminders. Position: *"built for
   every-quarter-forever, not the one-time project."*
4. **"Works on top of your Vanta / Drata / MSP."** Add an integration message and (later)
   light import. This reframes the platforms as *complements*, not just competitors —
   and blunts the reach-down risk by making you the operated layer on top of their tool.

---

## Part 5 — Claims discipline (keep it legally clean as you sharpen it)
- Keep every score labeled an **estimate**; keep "we prepare, you attest"; never imply a
  **guaranteed** CMMC pass (FTC §5 + the False Claims Act preparer risk the Legal seat
  flagged).
- Use the **precise** CUI wording from Part 0 — "policies and documentation, never your
  CUI or security data" — not a blanket "we never see anything sensitive."
- Have counsel review the Scope & Data Handling page and the CRM before they go live.

---

## Part 6 — Suggested sequence
**This week:** (1) fix lead/report persistence + analytics (Part 2.4) — stop losing
leads; (2) add the upload boundary notice + guardrails (Part 2.2); (3) name the team
on `/about`.
**Next 2–3 weeks:** (4) re-point the hero + the difference to niche + artifact-only
(Part 3.2); (5) ship the Scope & Data Handling page + CRM (Part 3.1); (6) the "Built
for `[NICHE]`" page (Part 3.3).
**This quarter:** (7) prime-specific questionnaire library + landing pages (4.1, 3.4);
(8) the CRM generator (4.2); (9) the counsel scope opinion that upgrades the page from
"our claim" to "counsel-reviewed."

**The single test that proves it worked (by ~month 6):** the share of closed customers
that came through niche/channel/prime referral at near-zero CAC vs. paid search. If the
specialized positioning + the gap-analysis wedge are working, referrals carry it.
