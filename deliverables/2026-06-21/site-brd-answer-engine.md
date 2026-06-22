# BRD — Add the Questionnaire Answer-Engine to the Muster Site

**Prepared:** 2026-06-22
**Repo to edit:** `jonacooper-stack/cmmc` (the site behind `cmmc-bay.vercel.app`)
**Stack:** Next.js (App Router) + React + Tailwind + TypeScript
**How to use this doc:** This is the plan of work. Build in the order shown. Exact file
names below come from a prior review — confirm them in the repo before editing.

**Goal in one sentence:** Turn the site from an operated, fixed-price service that only
*collects leads* into a self-serve product whose core job is **answering the security
questionnaires that defense primes send to small suppliers** — and that gets smarter
every time it is used.

---

## 1. What we're building (plain English)
Today the site is a marketing site with a fake "assessment" (a 6-field form that emails
nobody and loses the lead). We are turning it into a working self-serve product with
three connected parts:

1. **Free hook — "Check your score."** A visitor uploads their security *policy*
   documents and instantly gets a free gap analysis and an estimated SPRS score (their
   government cybersecurity self-score). This is the front door and the lead magnet.
2. **Paid core — "Answer my forms."** After they sign up, when a prime sends them a
   security questionnaire, they drop it in and the tool auto-answers about 80% of it
   from what it already knows about that customer. For the rest, the tool asks the owner
   simple questions (and flags the deeply technical ones to send to their IT provider),
   then assembles the finished answers to export.
3. **The learning loop.** Every completed questionnaire is saved back to that customer's
   private "answer library," so the next form is faster. The tool gets better the more
   they use it. **This is the point — build it in from the start, not later.**

**New one-line positioning:** *"When a prime sends you another security questionnaire,
drop it in — we answer most of it for you, and keep you ready for the next one."*

## 2. Where the site is today (starting point)
- A polished marketing site (~8 pages) selling an **operated, fixed-price service**
  ("we keep your SPRS score correct every quarter, one fixed price, we never touch your
  CUI").
- The "assessment" at `/assessment` is a 6-field lead form (`AssessmentStartForm.tsx`).
  There is **no upload, no analysis, no scoring** — even though the homepage promises it.
- The backend (`app/api/assessment/start/route.ts`) only `console.log`s the lead and
  returns `{ok:true}` — **leads are silently lost.**
- The site currently says "we never ask you to upload CUI." Keep the spirit (never CUI),
  but we now DO ask for **policy documents** (which are *not* CUI) — so that wording must
  change (see §4-E).
- There are **no user accounts, no login, no saved data, no billing.** Those are new.

## 3. The experience we want (build to this flow)
1. Visitor lands → clicks "Check your score."
2. Uploads their security **policy** documents. A short notice says: upload policies,
   **not** CUI or live security data.
3. Gets an **instant free gap analysis + estimated SPRS score** + a short "fix these
   first" list.
4. Creates an account (email + password or magic link) to save it and unlock the core.
5. Adds their prime(s).
6. **Drops in a prime's security questionnaire** (Excel/Word/PDF).
7. The tool **auto-answers ~80%** from the customer's saved answers + policies, each
   answer marked with a confidence level.
8. For the gaps, a **plain-English interview** asks the owner simple questions; the
   **deeply technical ones are flagged "send this to your IT provider."**
9. The owner **reviews every answer** (each clearly marked a **draft they decide to
   send**), edits, and **exports** the finished questionnaire.
10. Every approved answer is **saved to that customer's private answer library** → the
    next form auto-fills more.
11. The tool sends **quarterly reminders** to keep their score and answers current.

## 4. The work list (build in this order)

### A. Stop losing leads + add accounts (foundation — do first)
- Replace the stub in `app/api/assessment/start/route.ts` so it **persists every lead
  and submission** to a real datastore (e.g., Postgres/Supabase) **and emails the
  founders**. No paid traffic until this works.
- Add **self-serve accounts**: sign up, log in, a logged-in dashboard. Each account has
  its own private data (documents, answers, questionnaires).

### B. Make the free gap analysis + SPRS estimate real (the hook)
- Build the upload → analyze flow the homepage already promises: accept policy docs
  (PDF / Word / Markdown / text), map findings to the **110 NIST 800-171 control
  objectives**, and produce an **estimated SPRS score** (current + target) plus a short,
  plain-English "fix these first" list.
- Label the score an **estimate** everywhere. Put it behind an email signup so leads are
  captured.

### C. The questionnaire answer-engine (the new paid core — biggest build)
- A signed-in customer can **upload a prime's security questionnaire** (Excel / Word /
  PDF) into their workspace.
- The tool **auto-answers** each question by matching it to the customer's saved answers
  + policy documents, drafting an answer **with a confidence level**.
- For questions it can't confidently answer, it runs a **plain-English interview**, and
  **routes the deeply technical ones to "your IT provider"** instead of guessing.
- The customer **reviews every answer** (each marked "draft — you decide what to send"),
  edits, and **exports** the completed questionnaire (a clean file is fine to start).
- Every approved answer is **saved back** to that customer's private answer library so
  future forms auto-fill more. **Build this learning loop now.**

### D. Reposition the messaging (copy only)
- **Home hero:** lead with the answer-the-forms promise (§1 one-liner). Demote "fixed
  price / operated for you" to a supporting line.
- **`/the-difference`, `/how-it-works`, FAQ:** rewrite to describe the **self-serve,
  answer-your-forms** product (not a founder-led operated service). Keep the strong
  "we hold the proof, you keep your CUI" boundary message.

### E. Fix contradictions + trust gaps
- Change "we never ask you to upload CUI" → **"Upload your policies — never your CUI or
  security data."** (We now ask for policy docs; we still never want CUI/configs/logs.)
- `/about` (`app/about/page.tsx`): replace the placeholder bios ("The delivery founder"
  etc.) with **real founder names** + the DoD/DIB advisor.
- Reconcile the "15 minutes" promise so it matches the now-real instant experience.

## 5. Guardrails — do NOT break these
- **Data boundary (this is the moat):** only ever accept **written policies, procedures,
  and questionnaire answers.** Never ask for or store **CUI, network/data-flow diagrams,
  device configs, log files, vulnerability-scan results, or credentials.** At the upload
  control, show a short "don't upload these" notice and add a simple check that
  warns/blocks obvious CUI or secret content. (This boundary is what keeps Muster out of
  the customer's CMMC assessment scope — it is both legal protection and a selling point.)
- **Claims discipline (legal):** every score is an **estimate**; every answer is a
  **draft the customer reviews and submits**; **never promise a guaranteed CMMC pass or
  score.** Keep "we prepare; you attest; we are not an accredited assessor."
- **Privacy / isolation:** each customer's data is private to them. **Never use one
  customer's answers to fill another customer's form.** Encrypt data, require login, add
  basic spam protection to public forms.

## 6. Out of scope for now (keep it simple)
Do **not** build yet (note as "later"): exporting into each prime's exact form template;
integrations with Vanta / Drata / MSP tools; a public blog/resources section; automated
CUI-enclave hosting.

## 7. Decisions for the founder (confirm while building)
- **Pricing/model:** the validated concept is a **self-serve subscription, ~$200–$600 /
  month** (credit-card signup, no sales call). The current site shows operated tiers at
  $1.5K–$3.5K/mo. *Decision:* switch to self-serve low-cost pricing, or keep one higher
  "done-with-you" tier alongside? (Recommended: lead self-serve; optionally keep one
  higher tier.)
- **Human-review gate:** fully self-serve at launch, or a light "a person checks the
  riskiest answers" step? (Recommended: self-serve, with the tool routing the hardest
  questions to the customer's own IT provider.)
- **Brand/domain:** confirm the name/domain (a trademark check was flagged as still
  pending).
