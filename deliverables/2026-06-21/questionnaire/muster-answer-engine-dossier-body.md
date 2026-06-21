# Muster Answer Engine — Concept Dossier
**Tier: B (Promising — worth a deep dive, sitting right at the edge of the top "A" tier)  |  Objectives Score: 78/100  |  June 21, 2026**

*Plain-English write-up for a smart non-expert. The full council packet and the documented red-team are in the Appendix.*

## 1. IN ONE PARAGRAPH
Small companies that supply parts to big defense contractors get hit, over and over, with long security questionnaires they have to fill out to keep their orders. It is boring, technical, and never-ending — a new form shows up every few weeks, forever. Most of these small shops have no security expert on staff. Muster is a simple, low-cost online tool that fills out those forms for them. The shop uploads the documents it already has, and when a new questionnaire arrives, Muster automatically answers about 80% of it from what it already knows. For the rest, it asks the owner easy, plain-English questions (and tells them which questions to forward to their outside IT person). Every finished form teaches the tool more, so the next one is even easier. They pay a monthly subscription, like Netflix, and the tool keeps them ready all the time.

## 2. WHO PAYS — AND WHY THEY CAN'T SAY NO
**The buyer:** the owner of a small U.S. defense-supplier business — think a 35-person machine shop that makes parts handling sensitive government information ("CUI" — Controlled Unclassified Information, basically defense data that isn't secret but still has to be protected). They have one outside IT company and no in-house security person, and the owner personally carries this headache.

**Why they can't say no — the forcing function:** this is two kinds of "forced to buy" stacked on top of each other, which is unusually strong.
- **A government rule (a regulatory mandate).** Federal rules (named DFARS 7012/7019/7020) legally require any supplier touching this defense data to keep a current cybersecurity score posted in a government system and to keep answering these security forms. It's the law for them, not optional.
- **A customer requirement (a contractual requirement).** The big contractors ("primes") will not keep buying from a supplier who can't answer their security questionnaire. No answer, no order.

**What breaks if they don't buy, and how fast:** they lose work. A prime sends a form; if the shop can't answer it (or answers too slowly), the order goes to a competitor who can. And starting November 10, 2026, the rules get stricter (a tougher outside check called CMMC Level 2 phases in), so the pain is about to increase, not fade. This is a painkiller, not a vitamin.

## 3. THE MONEY (PLAIN TERMS)
**Price:** a published monthly subscription, roughly **$200–$600 per month** depending on company size (about **$2,400–$7,200 per year**). You sign up with a credit card — no salesperson needed. This is far cheaper than the alternative: a consultant doing a single gap assessment can charge **$9,000–$21,000**, and full prep is often quoted at **$100,000–$300,000+**. So saying "yes" is easy.

**The simple math to each founder making about $300K/year:**
- Assume the typical customer pays about **$350/month** (an estimate — the real number depends on who signs up; we should test it).
- $350/month is about **$4,200/year** per customer.
- To get each of the two founders to about **$300K/year** (≈ $600K/year for the business) you need roughly **143 paying customers**.
- To get to about **$500K/year each** (≈ $1.0M/year) by month 24, you need roughly **240 paying customers**.
- Because almost all the cost is just running software, about **90 cents of every dollar** is profit margin — so the business mostly needs *customers*, not a big team.

**The recurring / "gets better" upside:** this isn't a one-time sale. They pay every month, and the tool gets *stickier* over time, because every form it fills out makes it smarter about *that* customer. Leaving would mean throwing away their whole answer history and starting over with a competitor — which nobody wants to do. That "it remembers everything and gets easier" quality is what makes this worth more than a one-time tool, and it's the strongest money point in the whole concept.

*(Honest flags: the $350 average is an estimate. The biggest money question is whether enough small shops will sign up on their own without a sales team. And we need them to keep paying in the quiet months between forms, not cancel and re-subscribe.)*

## 4. WHY WE WIN
**The empty spot nobody is standing in.** Picture a grid. One side: tools made *just for defense* — but they focus on getting your *score*, not on answering your customers' forms, and they're sleepy little companies. Another side: excellent tools that *do* answer security forms — but they're built and priced for big tech companies ($9,600–$20,000+/year), not a machine shop. Nobody today sells the exact thing in the middle: a **cheap, self-serve, defense-specific tool, built for a non-technical owner, whose main job is answering your customers' forms — and that learns as it goes.** That middle square is empty. Two different expert reviewers, looking separately, both confirmed it's genuinely empty.

**The "built-in, not an add-on" insight.** The big platforms (Vanta, Drata) *do* offer form-answering — but only as an expensive extra (a **$10,000–$25,000/year** add-on) on top of a platform a small shop can't justify. We sell answering *and* staying-ready together, as one low monthly price. The big players won't copy this easily, because doing it cheaply would eat into the expensive product they already sell to big companies. That reluctance is part of our protection.

**The compounding answer-history.** The more you use it, the more it knows you, the less work each new form is. That builds a real reason to stay.

**The founders' edge.** Two founders who are excellent at marketing and messaging, can build the software themselves, and — importantly — **have built this exact kind of "answer engine" before, in production, at a previous company.** They know it works.

**Honest about how copyable it is:** the *underlying trick* (a tool that auto-fills forms from a saved knowledge base) is well-understood and could be rebuilt by a competitor in roughly 90 days if they decided to. So our real protection isn't a secret technology — it's **speed, sharp marketing, the bundled positioning the big players won't match, and stacking up each customer's answer-history fast** so we're already in before anyone copies us.

## 5. THE COMPETITION (PLAIN ENGLISH)
- **FutureFeed — the one to watch most.** A small (about 12 people), bootstrapped defense-compliance tool, priced like us ($99–$399/month). Today it focuses on your *score*, not on answering your customers' forms — that's the gap we attack. **The danger:** it already has the same customers we want and reaches them through **300+ IT-partner companies**. If FutureFeed sees our idea working, adding form-answering to an account it *already owns* is a small, cheap step — and it can reach those shops faster than two founders can. This is the single biggest competitive risk: not a giant attacking us, but a sleepy neighbor who already owns the customer waking up.
- **Vanta and Drata — the big, well-funded platforms.** Excellent and modern, and they *do* sell form-answering — but as a pricey add-on aimed at funded tech companies, not $300/month machine shops. They could one day make a cheaper "small defense" version (a real future risk to watch), but it's unlikely while this market is still small.
- **Conveyor / Loopio — great form-answering tools, wrong customer.** Best-in-class at answering security forms, but built and priced for big tech vendors ($9,600–$20,000+/year). No reason for them to chase a small shop.
- **Exostar's "CCRA" — a sneaky substitute we have to respect.** The biggest primes (Boeing, Lockheed, Raytheon, Northrop, BAE, Rolls-Royce) let a supplier fill out one standard security questionnaire *once* and reuse it across all of them, for free or cheap. That quietly removes *part* of the "endless forms" pain we're charging for — at least for the biggest customers. It doesn't cover the custom, one-off forms or the broader compliance grind, but we need to find out how big a bite it takes and aim our pitch at the forms it *doesn't* cover.
- **Consultants and IT shops (MSPs) — the default today.** Most small shops just hand the form to "their guy." Beating "I already have a guy" is its own challenge.

## 6. THE BIGGEST RISKS (TOP 3, PLAIN)
1. **The owner gets stuck on the hard questions.** The tool answers ~80% automatically, but the last ~20% are deep technical questions (encryption, access controls). The owner can't answer those and has to ask their outside IT person — who might be slow, charge extra, or not know either. If this happens a lot, our "we answer your forms for you" promise quietly turns into "we made a homework list for your IT guy," and customers either get frustrated and quit or beg us to just answer for them (which we don't want to do). Three separate expert reviewers flagged this as the number-one thing to prove.
2. **FutureFeed (or a similar player) copies us using the customers it already has.** They own the account and the distribution channel; we'd be racing an opponent with a head start.
3. **Not enough shops sign up on their own.** Our whole plan is to grow with no sales team — using a free tool, helpful articles, and referrals from government small-business help centers. If too few free users become paying customers, the business grows too slowly to hit the year-one income goal, even though the profit margins are great.

## 7. WHAT WE'D TEST NEXT (CHEAP EXPERIMENTS, BEFORE BUILDING MUCH)
1. **The "can the owner actually finish it?" test.** Take 8–10 *real* prime security questionnaires and walk real shop owners through our intended flow. Measure: how much the tool auto-fills, how often it's confidently *wrong*, and what % the owner can finish *without* their IT person. This one test decides whether this is a great business or a so-so one. Do it first.
2. **The free-tool-to-paid test.** Put up a simple web page offering the free score check (behind an email signup) *before* building the full product. Measure how many people show up and how many would pay. If too few convert, we rethink price or channel — not the whole idea.
3. **The accuracy spike.** A quick technical trial to confirm the tool can fill ~80% of a real, messy form correctly (real forms come as Excel, Word, PDF, locked portals — they're ugly). Confirm before writing the real product code.
4. **The Exostar overlap question.** Ask 5–10 target shops how much of their form-pain Exostar's reuse system already covers. If it covers a lot, we aim our pitch squarely at the forms it *doesn't*.
5. **The channel test.** Ask 5–10 government small-business counselors and 2–3 prime supplier-managers: "Would you refer a non-certified software tool, and on what terms?" Their answer tells us if the referral plan is real.

## 8. THE SCORECARD (PLAIN ENGLISH)
- **Must-have / forced to buy — 8/10.** Two forced reasons stacked (government law + the customer demands it), getting stronger with the Nov-2026 rule change. Not a 9 only because Exostar's free reuse system removes part of the pain we charge for.
- **Competition — 7/10.** A genuinely empty spot in the market, plus a real "gets stickier over time" advantage — but a sleepy neighbor (FutureFeed) who already owns the customer could copy us, so it's contested, not wide open.
- **Path to founder income — 7/10.** Hitting ~$500K each by month 24 looks very doable; hitting ~$300K each by month 12 is reachable but tight without a sales team.
- **Recurring revenue — 8/10.** A true monthly subscription that gets harder to leave the longer you use it. Held at 8 because a shop might cancel in the quiet months between forms.
- **Probability / proof of demand — 7/10.** The need is real and required by law; the open question is whether the product actually delivers for a non-technical owner.
- **Capital to start — 9/10.** Cheap to launch (two founders + some software costs), profitable fast, no inventory or equipment.
- **Operations — 8/10.** It's just software running; no trucks, no installs, no field visits. Held at 8 by the "owner gets stuck and emails us" support risk.
- **Founder fit — 9/10.** Exactly their strengths — marketing, messaging, building software — and they've built this exact tool before.
- **Room to grow — 9/10.** Gets cheaper to run as it scales, and it's the kind of clean software business that bigger companies like to buy.
- **Legal risk: SERIOUS BUT MANAGEABLE.** This lives in the defense world, so there's real legal homework — mainly making sure the tool always says "this is a draft, you decide what to send," never promises a score or a pass, and keeps each customer's data walled off from every other's. None of it is a dealbreaker; it's a checklist, and the founders have done compliance work before.

**Honest tier: B (Promising), right at the edge of A.** It already clears the two highest bars (forced-demand and competition), but the overall number (78) sits just under the top tier, and one big risk (the "owner gets stuck" question) is still unproven.
**What would move it up to A:** prove the "owner can actually finish a real form mostly on their own" test, and sharpen the pitch around the bundled, gets-smarter answer engine (the part competitors won't easily copy) rather than the free score check (which FutureFeed already gives away). Do that, and this becomes a strong A.
