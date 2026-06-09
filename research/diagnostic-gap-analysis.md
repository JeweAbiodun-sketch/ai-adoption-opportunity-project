# Gap Analysis & Recommendations
## Project vs. Cleo Company AI Readiness Diagnostic Report

**Date:** 8 June 2026  
**Basis:** Comparing this project's methodology and outputs against the external AI Readiness Diagnostic Report for Cleo Company (Electronics & Technology retail, 51-250 staff, 10+ stores)

---

## Executive Summary

The project and the external diagnostic report are broadly aligned on the most important call: **demand forecasting is the right first move, and data quality is the blocker**. That is a meaningful validation. However, the two documents diverge significantly on infrastructure cost, ROI assumptions, change management budget, and deployment timeline. The project is consistently more optimistic on cost and faster on timelines. These gaps would put a real implementation at risk if uncorrected.

---

## Where the Project and the Report Agree

| Finding | Project | Report |
|---|---|---|
| Primary opportunity | AI Demand Forecasting (#1) | AI Demand Forecasting (#1) |
| Critical blocker | Data quality must be fixed first | Data Quality Will Block Demand Forecasting |
| First action | Data audit before any AI spend | 30-Day Data and Process Audit (£5k–£8k) |
| Weakest dimension | People/workforce readiness | Workforce Readiness: 3/10 (lowest score) |
| Leadership posture | Cautious, demands ROI evidence | Leadership Commitment 5/10, appropriately skeptical |
| Baseline check | Need measurable KPIs before launch | Project fails baseline-and-attribution checkpoint |

The alignment on the top recommendation and the data blocker is strong. The diagnostic tool and the external report are asking similar questions and reaching the same primary conclusion. That is the most important thing to get right.

---

## Gap 1 — Infrastructure Cost Is Significantly Underestimated

**Project position:** SaaS-first, £700–£5,800/month ongoing, £9.4K–£82.6K annual TCO.

**Report finding:** Recommended approach is a **Hybrid Operating Model** at £70,560 setup + £120,485/year = **£393,623 over 3 years**.

**The gap:** The project's SaaS-only model (API-first SaaS stack in the report's terminology) scores only **4/10 fit** for a company at this maturity level. The report explicitly rejects it as the primary architecture. The hybrid model is ~5× more expensive annually than the project's midpoint estimate.

**Why this matters:** If the project is used as a cost reference in a real engagement, the client will face sticker shock when actual vendor and integration costs arrive. The SaaS tools named in the project (Inventory Planner, Relex Lite) are the right short-list for a Phase 1 pilot, but they sit *inside* a larger hybrid infrastructure that includes data integration, middleware, and internal tooling costs the project does not account for.

**Recommendation:** Revise `cost_estimation/cost_analysis.md` to include a hybrid TCO scenario alongside the SaaS scenario. Use the report's structure: setup cost, annual cost, 3-year TCO. Label the SaaS scenario as the **pilot phase cost** and the hybrid scenario as the **scale cost**. This gives a credible two-stage cost story.

---

## Gap 2 — ROI Model Is Too Optimistic

**Project position:** £675K/year benefit on a £15M revenue base, ~30:1 ROI, 9–18 month payback.

**Report finding:**
- Revenue lift proxy: **4% on £120 AOV × 600 customers × 60% attribution** — a much more conservative framing
- Overall value frame: £400K–£1.5M for the whole AI programme, not from a single use case
- Explicitly warns: measure success at **12–18 months post-launch**, not 3–6 months

**The gap:** The project applies optimistic multipliers (15% inventory cost reduction, 2% margin improvement, 1% revenue uplift simultaneously) without an attribution haircut. The report builds in a 60% attribution share specifically to prevent this. Applied to the project's numbers, a 60% attribution haircut reduces the £675K estimate to roughly £405K — still strong, but materially different.

The 30:1 ROI figure is a red flag for a CFO. It signals the model is built to sell rather than to test.

**Recommendation:** Add an attribution discount factor to `cost_estimation/cost_analysis.md`. Show three scenarios: pessimistic (30% attribution), base (60%), and optimistic (80%). Replace the single 30:1 headline with a range. This is more honest and more defensible in a boardroom.

---

## Gap 3 — Change Management Is Underbudgeted

**Project position:** Change management is mentioned but not costed separately. Training is implied in Phase 2.

**Report finding:**
- Change management: **£20k–£40k** explicitly budgeted
- Per-employee training: **£500–£1,000 per affected employee** + 20–30 hours of protected learning time
- Without this, well-designed AI tools will see **30–50% underutilisation** in the first 6 months
- The IT-led ownership problem is flagged as a standalone risk flag, not just a note

**The gap:** The project names workforce readiness as the weakest dimension but does not translate that diagnosis into a budget line. The external report treats it as one of three named risk flags (equal weight to data quality). For a company at Stage 2 with Workforce Readiness 3/10, the change management cost is not optional — it is the difference between adoption and shelf-ware.

**Recommendation:** Add a dedicated change management section to `implementation/implementation_plan.md` with:
1. Named roles required (executive sponsor, merchandising champion, store pilot lead)
2. Training budget: £500–£1,000 × number of affected buyers/merchandisers
3. Protected time allocation: 20–30 hours per person in Phases 1–2
4. Success metric for adoption (not just accuracy): target >70% active tool usage by week 16

---

## Gap 4 — Pilot Evaluation Timeline Is Too Short

**Project position:** Phase 3 evaluation at weeks 17–20 (~5 months from start).

**Report finding:** "Measure success at 12–18 months post-launch, not 3–6 months. Leadership must commit to this timeline or not start — partial implementations fail and waste money."

**The gap:** The project's Phase 3 gate is at roughly the point where the report says you should not even be drawing conclusions yet. Demand forecasting accuracy improves as the model learns seasonal patterns; a 5-month window captures at best one partial season cycle. An early evaluation at week 20 risks a premature stop decision based on incomplete data.

**Recommendation:** Restructure the implementation timeline in `implementation/implementation_plan.md`:
- **Week 17–20:** Operational review only — is the tool being used? Is data flowing correctly?
- **Month 6:** First accuracy checkpoint — MAPE below threshold? Adoption rate above 70%?
- **Month 12–18:** ROI and scale decision — compare actual inventory cost, stockout rate, and markdown rate against baseline

This aligns with the report's timeline and protects the project from a false negative at month 5.

---

## Gap 5 — Opportunity Ranking Diverges on #2 and #3

**Project position:**
1. Demand Forecasting (INVEST)
2. AI Customer Service (INVEST)
3. Dynamic Pricing (PILOT)
4. Customer Personalization (CONDITIONAL, Phase 2)

**Report finding:**
1. Demand Forecasting — High effort, £300k–£750k value
2. **Customer Personalization Engine** — Medium effort, £100k–£500k value
3. Dynamic Pricing — Medium effort, £60k–£300k value
(Customer service / chatbot not ranked in top 3)

**The gap:** The project elevates AI Customer Service to #2 while the external report does not rank it in the top 3. This is not necessarily wrong — the project's research explicitly notes chatbots are oversold — but the project's `research/opportunities_risks.md` and the diagnostic tool both present customer service as an "INVEST" recommendation, which contradicts the project's own finding that "80% cost reduction claims are unrealistic."

Customer Personalization is ranked #4 (CONDITIONAL) in the project but #2 in the report. Given that the client has omnichannel operations and existing email automation to build on, this ranking deserves reconsideration.

**Recommendation:** Revisit the ranking logic in `ai_diagnostic_tool.html`. Either:
- Downgrade Customer Service from INVEST to PILOT with an explicit note about oversold claims
- Elevate Customer Personalization to #2 for omnichannel profiles, with a dependency flag (requires unified customer view first)

---

## Gap 6 — Diagnostic Tool May Not Produce Stage 2 for This Profile

**Project tool stages:**
1. Ad-hoc — No formal forecasting
2. Process-driven — Manual but organized
3. Partial automation — Some automation in place
4. AI-ready — Infrastructure and culture support AI
5. AI-native — Continuous AI optimization

**Report finding:** Cleo Company = Stage 2 "Experimenting" — basic AI tools deployed (email automation, simple product recommendations) but isolated, vendor-provided, limited integration.

**The gap:** The project's Stage 2 is "Process-driven — manual but organized." A company with email automation and product recommendation tools deployed would likely score higher than that on the project's scale, landing at Stage 3 (Partial Automation). This means the project's diagnostic tool would classify the same company one stage higher than the external report — which changes the recommendations generated.

**Recommendation:** Review the stage definitions and scoring thresholds in `ai_diagnostic_tool.html`. The "Experimenting" label from the external report — tools exist but are isolated and vendor-provided — is a valuable distinction that the project's current framework misses. Consider adding a Stage 2.5 or refining Stage 2/3 to distinguish between "organised manual processes" and "isolated AI experiments."

---

## Gap 7 — Data Remediation Is Not Separately Scoped or Costed

**Project position:** Phase 0 (Weeks 1–2) is a data audit. Assumes data will be usable after this check.

**Report finding:** "3–6 months of data remediation work first" before demand forecasting can be trained. Data cleanup budget: **£30k–£60k**. If audit reveals 9+ month gaps, pause AI investment entirely.

**The gap:** The project's Phase 0 is two weeks and has no budget line. The external report says data remediation could take 3–6 months and cost £30k–£60k. These are not compatible. The project implicitly assumes the data audit will find acceptable data; the external report explicitly accounts for the possibility it will not.

**Recommendation:** Add a conditional branch to the implementation plan:
- **If Phase 0 audit finds < 12 months clean daily sales data:** Insert a 3–6 month data remediation phase with a £30k–£60k budget before any AI tool procurement
- **If Phase 0 audit finds adequate data:** Proceed to Phase 1 as planned

This is the honest version of the plan and matches the report's recommended next step exactly.

---

## Summary of Recommended Changes

| File to Update | Change Required |
|---|---|
| `cost_estimation/cost_analysis.md` | Add hybrid TCO scenario (£393K 3yr); add attribution discount to ROI model; separate out change management as a budget line |
| `implementation/implementation_plan.md` | Extend evaluation to 12–18 months; add data remediation conditional branch; add change management section with named roles and training budget |
| `ai_diagnostic_tool.html` | Downgrade Customer Service from INVEST to PILOT; elevate Personalization to #2 for omnichannel profiles; revise Stage 2/3 thresholds to capture the "isolated AI experiments" profile |
| `research/opportunities_risks.md` | Reconcile the chatbot oversold finding with the INVEST recommendation in the diagnostic tool |
| `implementation/solution_proposal.md` | Note that SaaS tools are the pilot-phase entry point inside a larger hybrid architecture, not the end-state infrastructure |

---

## What the Project Does Better Than the Report

The external report is a diagnostic snapshot. The project goes further in two areas:

1. **Specificity on vendor options.** The project names Inventory Planner and Relex Lite as concrete tools with pricing ranges. The report stays at architectural level and does not recommend specific products. For a CEO in a buying decision, the project is more immediately actionable.

2. **The diagnostic tool itself.** The report describes a problem; the project built a reusable instrument to identify it. The interactive HTML tool — if its scoring thresholds are recalibrated per Gap 6 above — is a genuine consulting asset that the report does not provide.

---

## Overall Assessment

The project is well-structured and its primary recommendation is correct. The external diagnostic report validates the most important judgement calls. The gaps are concentrated in three areas: **cost realism** (infrastructure and change management are underbudgeted), **timeline realism** (evaluation window is too short), and **diagnostic calibration** (stage thresholds and opportunity rankings need tuning). Addressing these gaps would bring the project into full alignment with the external benchmark and make it credible as a deliverable in a real engagement.
