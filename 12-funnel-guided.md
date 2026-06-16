# 12 — Guided Funnel (human-in-the-loop, checkpoints)

The supervised mode. The generator makes the first cut, then YOU steer at two
checkpoints before any expensive council runs. This is NOT one fire-and-forget
/goal — it is THREE prompts you paste in sequence, with your input in between. Your
judgment kills bad branches early.

Requires the `idea-generator` + `idea-triage` agents and the six council agents in
`.claude/agents/` (including `competitive-analyst`). Reads 00-evaluation-stage.md,
01-objectives.md (must-have taxonomy + tiers + legal risk gate), and
08-founder-profile.md.

---

## PROMPT 1 — Generate + first cut + STOP for your ranking
Paste this as a normal message (not /goal):

```
Run the guided funnel, Stages 1-2 only, then STOP and wait for me.

1) GENERATE: dispatch idea-generator to produce >= 100 diverse, on-thesis concept theses per 00/01/08. Enforce the thesis: need-to-have/painkiller only (a strong forcing function of ANY of the five doc-01 types — regulatory, contractual, critical-input, continuity, risk-mitigation; regulation is one path, NOT required and NOT excluded); beatable stale incumbents; NO field-ops-core models; recurring revenue; low capital. A bridgeable regulatory/expertise/supply moat with sleepy incumbents is a PLUS, not a disqualifier. Maximize diversity across forcing-function types. Save the full pool to a file.
2) FIRST CUT: dispatch idea-triage over the full pool in batches; rank by consensus (must-have weighted heaviest, competition next). Take the TOP 30.
3) STOP. Present the top 30 as a numbered, ranked list. For EACH: a 1-2 line description (customer + the must-have/forcing function + revenue mechanism) and its consensus score. Then ask me for my own ranking / keeps / kills. Do NOT proceed until I reply.
```

→ You reply with your ranking, keeps, and kills.

---

## PROMPT 2 — Narrow to ~10 + STOP for your picks
After you've sent your ranking, paste:

```
Incorporate my ranking and feedback (my input outweighs the model ranking). Narrow to the TOP ~10. Present them with a deeper read each: one short paragraph covering customer, the must-have/forcing function & why-now, the recurring revenue mechanism, and why these founders win it (marketing/positioning vs stale incumbents). Then STOP and ask me which of the ~10 should advance to the full council (I will pick 3-5). Do NOT start the council until I reply.
```

→ You reply with the finalists to deep-dive.

---

## PROMPT 3 — Full six-member council deep dive on YOUR picks (this one is /goal)
After you've named the finalists, paste:

```
/goal Run the full six-member council deep dive on the finalists I selected, with full rigor, and produce plain-English deliverables.

END STATE (done when ALL true):
- Each selected finalist has a clean-room one-pager and a COMPLETE, uncompressed council packet: cfo-reviewer, cmo-reviewer, coo-reviewer, legal-reviewer, cto-reviewer, competitive-analyst dispatched as a fresh parallel batch (each sees only the one-pager + its own doc + 00 + 01, never the target or each other), each review written to a file, then pm-synthesizer with a two-directional red-team.
- Each finalist is labeled TIER A (Advisor-Ready) / B (Promising) / C (Pass) on the Objectives Weighted Score (with the Legal risk-gate rating). Surface the honest top 2-3. Do not pad and do not inflate to reach a tier.
- For each finalist, the doc-14 deliverables exist (plain-English Concept Dossier + Scorecard as .docx/.txt/.md, saved to the repo and delivered as attachments — NO Google Drive) + a master comparison sheet in Excel (.xlsx).

CHECK (plain text + saved files):
- Scoreboard: each finalist's six expert averages, the Objectives Weighted Score, lowest sub-score, Legal risk-gate rating, TIER.
- For each finalist: the full council packet with inline evidence + the documented two-directional red-team.
- One line per finalist: why it is distinct, and the single biggest open question for the manual deep-dive.

CONSTRAINTS:
- Score on absolute merit per 00-evaluation-stage.md: symmetric (no inflation AND no deflation), stage-aware (no penalty for missing interviews/build/traction — list as next experiments). A genuinely strong, evidenced concept SHOULD earn 8s and 9s.
- INCOME TARGET = the ladder in 01-objectives.md (~$300K/founder mo12, ~$500K+ mo24, growing; $2M is upside, not required).
- "Must-have" = a strong forcing function of ANY of the five doc-01 types. Legal is a RISK GATE — do NOT down-tier a regulated-but-navigable concept; only a FATAL rating gates down. Penalize field-ops models. The Competitive Analyst must NAME real players with researched data.
- Clean-room each candidate; never refine in place; never disclose tiers/target to a council subagent.
- Read docs 00-08 + 06b + 14 first.
- Keep going until the END STATE is met.
```

---

## Going unsupervised later
Once this earns your trust, collapse Prompts 1-2 into a single /goal that auto-cuts
to ~5 without stopping (the funnel in `11-funnel.md`), and keep only Prompt 3's deep
dive. Keep the checkpoints for now.
