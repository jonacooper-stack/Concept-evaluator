# Line-by-Line Website Review — cmmc-bay.vercel.app ("Muster")

Reviewed from source: public repo `jonacooper-stack/cmmc` @ `main` (the deployment
behind `cmmc-bay.vercel.app`). Stack: **Next.js 16.2.9 + React 19 + Tailwind v4 +
TypeScript**, App Router, app at repo root (zero-config Vercel deploy). Reviewed
every page, component, and the one API route.

## Verdict in one line
A genuinely well-built, well-positioned **marketing site** with disciplined,
legally-clean messaging — but the "assessment" is **not a product yet**: it is a
6-field lead-capture form wired to a stub endpoint that only `console.log`s and is
**silently dropping leads**. The self-serve analysis engine the homepage promises
does not exist in this build.

---

## What's strong (keep)
- **Positioning discipline is excellent and consistent across all 8 pages + footer.**
  The wedge — *"we keep your SPRS score correct, every quarter, one fixed price, and
  we never touch your CUI"* — is stated the same way everywhere (home hero, the
  difference, pricing, about, FAQ, footer). This is rare and valuable.
- **Claims discipline is legally clean.** Every score is labeled an *estimate*; the
  no-certification-guarantee line ("we prepare; you attest; we are not a C3PAO") is
  repeated in the assessment page, FAQ, and footer disclaimer. The Legal reviewer
  specifically credited this. Don't loosen it.
- **The 3-way contrast graphic** (self-serve tools vs. enclave bundles vs. Muster)
  on the home page and `/the-difference` is the sharpest asset on the site — it makes
  "artifact-only" legible in one glance.
- **Design/brand reads modern and credible** (navy/steel/"cleared-green" palette,
  Geist, clean Tailwind). That modern feel IS the competitive wedge against the
  sleepy RPO incumbents — it's doing real work.
- **Page-level SEO metadata** is present and specific on every route (good titles +
  descriptions).

---

## The critical gap: the "upload policies → start the analysis" flow
You described "a place where people can upload their policies and start the analysis."
**That does not exist in this build** — and the gap matters because it's the whole
product:

1. **There is no file/policy upload anywhere.** In fact the site says the opposite,
   twice: `/assessment` reads *"We never ask you to upload CUI"* and the form footer
   repeats *"We never ask you to upload CUI."* (`AssessmentStartForm.tsx:88`). So
   either you have a newer local iteration than `main`, or this refers to the
   *intended* vision rather than what's deployed. Worth reconciling.
2. **The "assessment" is a 6-field lead form, not a questionnaire.**
   `AssessmentStartForm.tsx` collects: name, email, company, employees (dropdown),
   primes (optional), and SPRS status (dropdown). There is **no 110-control
   questionnaire, no control mapping, no SPRS scoring, no report generator** — even
   though `/assessment` and the home page promise *"We map your answers to all 110
   NIST 800-171 control objectives and produce an honest estimate of your current and
   target SPRS score."*
3. **The backend is a stub that loses the lead.** `api/assessment/start/route.ts`
   validates the fields then does `console.log("[assessment:lead]", …)` and returns
   `{ ok: true }`. The inline TODO (`route.ts:33-35`) admits the CRM forward, the
   transactional email, and the assessment+report generation (WS-4) are unbuilt. On
   Vercel, `console.log` goes to ephemeral function logs — so **every lead from a live
   ad campaign is effectively discarded.** This is the #1 thing to fix before any
   traffic hits the page.
4. **The promise/*reality gap*.** Home + assessment say "find out your score in ~15
   minutes." The form's success state actually says *"a founder will make sure your
   report is on its way within one business day"* (`AssessmentStartForm.tsx:43-46`) —
   i.e., it's **human-fulfilled and asynchronous**, not the instant self-serve
   experience the headline implies. Fine for a smoke-test of demand; not fine as a
   durable promise, and directly relevant to your "pure SaaS, no manual work"
   question (see the chat summary).

---

## Specific issues found (ranked)
**P0 — fix before sending traffic**
- Leads are not persisted (no DB/CRM/email; just `console.log`). Wire to a store +
  notification (even a Google Sheet / Resend email / HubSpot form) or you'll pay for
  clicks and lose the leads.
- No analytics or conversion tracking (GA4/GTM noted "pending" in the README). The
  entire validation plan is "measure completion → proposal → paid"; right now nothing
  is measured.

**P1 — credibility & funnel integrity**
- `/about` ships **placeholder bios** ("The delivery founder" / "The go-to-market
  founder") with a literal `TODO` to add names, bios, headshots (`about/page.tsx:32`).
  Trust is the whole sale (both CMO and Competitive flagged the missing RP/CCP badge);
  an anonymous About page actively undercuts it. Name yourselves + the DoD advisor.
- No bot/spam protection on the public form (no honeypot, rate-limit, or captcha).
- The headline "15 minutes" vs. the "one business day" reality should be reconciled so
  early prospects aren't surprised (a small trust leak at the exact conversion point).

**P2 — polish**
- No `/resources` or `/blog` routes exist yet, though README WS-3 lists SEO cornerstone
  articles + sitemap/schema as the plan. The organic-search engine the CMO is counting
  on isn't started.
- `getmuster.com` domain + `hello@getmuster.com` are referenced but the naming doc
  notes USPTO TESS clearance (classes 035/042) is still pending, and a defense app
  "Mustr" and an advocacy "Muster" exist. Clear the mark before heavy brand spend.

---

## Page-by-page (quick)
- **Home (`page.tsx`)** — Hero, stakes ("blank/stale SPRS can freeze POs today"),
  how-it-works (3 steps), the difference (3-way), what-we-do (6 bullets), pricing
  teaser (Core/Plus/Scale), credibility, final CTA. Tight and persuasive. The 3 steps
  honestly disclose step 2 is a **founder-led** mock review and step 3 is human
  onboarding+quarterly ops — i.e., the site itself is upfront that this is an operated
  service, not pure software.
- **How it works** — Good honesty: H1 literally says *"A product sources and qualifies
  you. A founder closes. Then software keeps you ready."* That is the real operating
  model, stated plainly.
- **The difference** — Best page. Clean comparison table; "we hold the proof, you keep
  your CUI."
- **Pricing** — Published Core $1.5K/mo (+$9.5K), Plus $2.5K/mo (+$12.5K), Scale
  $3.5K/mo (+$15K); clear "what's included" vs "paid separately." Strong.
- **Why now** — Timeline (DFARS today → Nov 10 2025 acq rule → Nov 10 2026 L2 gating →
  2027–28 full). Timely and accurate framing.
- **About** — Placeholder bios (see P1).
- **FAQ** — 7 well-written Q&As; reinforces no-custody / no-guarantee / estimate.
- **Contact** — Minimal; routes to the assessment + `hello@getmuster.com`.

---

## How this bears on the "pure-SaaS" question (full analysis in the chat)
The site as written sells an **operated service** and says so. The council's read is
that the *defensible* version is exactly that operated layer (the funded platforms
own pure self-serve), but the *margin/scale* upside is in automating the assessment →
scoring → SSP/POA&M → questionnaire-answer work behind a thin human-review gate. The
fastest, highest-value build is therefore the very thing currently stubbed: turn
`/assessment` into the real deterministic SPRS engine + report generator, and make the
backend persist + notify. That single build closes the promise/reality gap, starts the
metrics flowing, and is the load-bearing step toward a software-leveraged (not
purely-manual) business.
