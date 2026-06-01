# Stage 3 — Fine Triage + Orchestrator Deep-Dive Selection

## Fine-triage agent output (stricter, harsher grader)
The fine-triage run was markedly more skeptical than the coarse graders (grader variance
is expected and acknowledged in 11-funnel.md). Its strict ranking of the 15:

1. A14 Dehumidification/Mold (white-label SaaS) — consensus 7.2, obj 77
2. A11 Dock Door & Loading Bay Maintenance — 6.6, obj 77
3. A35 Electrical Panel Thermography — 5.8, obj 72.5
4. A26 Commercial Lighting Efficiency + Controls — ~5.8, obj ~72
5. B5 ClaimSpeed — 5.6, obj 65.5 (flagged thin $2M path, weak CMO)
... A19, A23, A4, A29 (audit cluster, mid pack); C24, C35, C13, C10 lower;
C1 and B39 marked FATAL on path-to-$2M math (low-ARPU SaaS: ~$250–300k and ~$1.2–1.5M
revenue respectively vs. $2M target).

Its distinctness-driven top 5: **A14, A11, A35, A26, B5.**

## Agent's FINAL top 5 (it self-corrected the clustering)
The agent's strict 1–15 ranking ended: A29(7.4), B5(7.2), A4(7.2), A35(7.2), C10(7.0),
A14(7.0), C1, A26, A23, B39, A11, A19, C24, C35, C13. In its final selection it explicitly
performed a DISTINCTNESS-DRIVEN DISPLACEMENT — dropping A35 (a third field-service IR audit)
for A14 (white-label channel SaaS) — landing on a genuinely diverse final 5:
**A29, B5, A14, A4, C10.**

## Orchestrator reconciliation (documented)
My intermediate read of the agent's output showed a clustered 4-field-service slate and I
drafted an override (A26/A14/B5/C10/C24). But the agent's FINAL answer already solved the
clustering and is triage-faithful (higher-consensus picks) AND diverse. I therefore ACCEPT
the agent's final 5 rather than impose my override. Rationale: respecting the triage signal,
A4 (consensus 7.2) > C24 (6.0, plus a funded incumbent Vendr); and A29+A4, though both
field-service, are maximally distinct on buyer + ROI (manufacturing energy-savings-share vs.
municipal water revenue-recovery). Field-service audits were the highest-scoring archetype
across every grader — unsurprising, since fragmented + low-incumbent + capital-light +
recurring is exactly the doc-01 green-flag profile.

### Deep-dive 5 (materially distinct on customer AND revenue mechanism)
| # | Concept | Archetype | Customer | Revenue mechanism |
|---|---------|-----------|----------|-------------------|
| 1 | A29 Compressed Air Leak Detection | Field-service / energy | Manufacturing/automotive/food-processing ops | Quarterly audit contract + energy cost-savings share |
| 2 | B5 ClaimSpeed | Vertical software + founder domain | Independent insurance claims adjusters | Per-adjuster SaaS retainer / per-claim |
| 3 | A14 Dehumidification & Mold Monitoring (white-label) | Channel SaaS / monitoring | Restoration & waterproofing firms (channel) → homeowners | Per-property monitoring subscription, white-labeled |
| 4 | A4 Utility Meter Audit Service | Field-service / public-sector | Municipal water/utility districts | Annual audit contract (meter-error revenue recovery) |
| 5 | C10 Fractional CDO for SMBs | Productized expert retainer | 20–200-person company finance/ops execs | Monthly advisory retainer ($2.5–4k/mo) |

Held just below the line: A35/A26/A23/A11/A19 (more field-service near-dups), C1/B39
(low-ARPU $2M-path risk the agent flagged FATAL), C24 (Vendr incumbent), C35/C13 (second
retainer flavors). The agent flagged real demand/$2M-path risks on B5, C10, A4 — the full
council now tests those honestly. Quality floor applied AFTER honest scoring, never as a target.

NOTE on B5, C10, C24: the fine-triage agent flagged real demand/$2M-path risks on these.
That is exactly what the full council will now test honestly — they enter the deep dive as
candidates, not winners. Quality floor (mean >= 8.0, no sub-score < 7, objectives >= 80)
is applied AFTER honest scoring.
