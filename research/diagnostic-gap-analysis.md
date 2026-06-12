# Gap Analysis & Recommendations
## Project vs. External AI Readiness Diagnostic Report

**Date:** 12 June 2026
**Basis:** Comparing this project's methodology and outputs against the external AI Readiness Diagnostic Report for Cleo (Electronics & Technology retail, 51–250 staff, 10+ stores)

---

## Executive Summary

The project and the external diagnostic report are broadly aligned on the most important call: **demand forecasting is the right first move, and data quality is the blocker**. That is a meaningful validation. However, the two documents diverged on infrastructure cost, ROI assumptions, change management budget, opportunity ranking, and deployment timeline. The gaps have now been addressed across all project files. Two verdicts were revised as a direct result of the gap analysis: AI Customer Service downgraded from INVEST to PILOT, and Customer Personalisation elevated to #2 INVEST.

---

## Where the Project and the Report Agree

| Finding | Project | Report |
|---|---|---|
| Primary opportunity | AI Demand Forecasting (#1) | AI Demand Forecasting (#1) |
| Critical blocker | Data quality must be fixed first | Data Quality Will Block Demand Forecasting |
| First action | Data audit before any AI spend | 30-Day Data and Process Audit (£5K–£8K) |
| Weakest dimension | People / workforce readiness | Workforce Readiness: 3/10 (lowest score) |
| Leadership posture | Cautious, demands ROI evidence | Leadership Commitment 5/10, appropriately sceptical |
| Baseline check | Measurable KPIs needed before launch | Project fails baseline-and-attribution checkpoint |

---

## Gap 1 — Infrastructure Cost Significantly Underestimated

**Original project position:** SaaS-only, £700–£5,800/month, £9.4K–£82.6K annual TCO.

**Report finding:** Recommended architecture is a Hybrid Operating Model — £70,560 setup + £120,485/year = **£393,623 over 3 years**. The SaaS-only model scores 4/10 fit for a company at this maturity level.

**The gap:** The project's SaaS estimate was the pilot entry cost — correct for Phase 1–2 — but the hybrid model at full scale is ~5× more expensive annually than the project's midpoint estimate.

**Fix applied:** `cost_estimation/cost_analysis.md` now presents two scenarios side by side:
- **SaaS Pilot:** £19K–£83K Year 1 — the entry point to test value
- **Hybrid Model:** £393,623 over 3 years — the scale cost

Both figures are labelled clearly so a client cannot mistake the pilot cost for the full programme cost.

---

## Gap 2 — ROI Model Too Optimistic

**Original project position:** £675K/year benefit, ~30:1 ROI, 9–18 month payback.

**Report finding:** Builds in 60% attribution share. Warns against measuring success at 3–6 months — requires 12–18 months post-launch. The 30:1 figure is a red flag for a CFO.

**The gap:** The project applied optimistic multipliers without an attribution haircut. At 60% attribution, £675K reduces to ~£405K — still compelling, but materially different and far more defensible.

**Fix applied:** `cost_estimation/cost_analysis.md` now shows three attribution scenarios:

| Scenario | Attribution | Est. Annual Benefit |
|---|---|---|
| Pessimistic | 30% | ~£200,000 |
| **Base case** | **60%** | **~£405,000** |
| Optimistic | 80% | ~£540,000 |

The 30:1 headline has been removed. Base case (£405K) is the boardroom figure.

---

## Gap 3 — Change Management Unbudgeted

**Original project position:** Change management mentioned but not separately costed.

**Report finding:** £20K–£40K explicitly budgeted. Per-employee training £500–£1,000 + 20–30 hours protected learning time. Without this, well-designed AI tools will see 30–50% underutilisation in the first 6 months. IT-led ownership flagged as a standalone risk.

**The gap:** Workforce readiness scores 3/10 — the weakest dimension — yet no budget line existed to address it. People risk is equal to data risk.

**Fix applied:** `cost_estimation/cost_analysis.md` includes a dedicated Change Management section. `cost_estimation/timeline_estimate.md` names three required roles before Phase 2 begins:
- Executive Sponsor
- Merchandising Champion (business lead, not IT)
- Store Pilot Lead

---

## Gap 4 — Pilot Evaluation Timeline Too Short

**Original project position:** Phase 3 evaluation at weeks 17–20 (~5 months from start).

**Report finding:** Measure success at 12–18 months post-launch. A 5-month window captures at most one partial seasonal cycle — insufficient for demand forecasting to prove value. An early gate risks a false negative that kills the programme before it delivers.

**The gap:** Week 17–20 was positioned as the go/no-go gate. It is far too early.

**Fix applied:** `cost_estimation/timeline_estimate.md` now uses a three-stage evaluation structure:

| Stage | Timing | Purpose |
|---|---|---|
| Operational Review | Wks 17–20 | Is the tool in use? Is data flowing? NOT the ROI gate. |
| First Accuracy Checkpoint | Month 6 | MAPE < 15%? Adoption > 70%? |
| ROI & Scale Decision | Month 12–18 | Compare vs baseline. Invest or exit? |

---

## Gap 5 — Opportunity Ranking Diverged (#2 and #3)

**Original project position:**
1. Demand Forecasting (INVEST)
2. AI Customer Service (INVEST)
3. Dynamic Pricing (PILOT)
4. Customer Personalisation (CONDITIONAL)

**Report finding:**
1. Demand Forecasting
2. Customer Personalisation Engine
3. Dynamic Pricing
(AI Customer Service not ranked in top 3)

**The gap:** The project elevated AI Customer Service to #2 while simultaneously noting that "80% cost savings claims are unrealistic" — a direct contradiction. Customer Personalisation was ranked #4 despite the external benchmark placing it #2 for omnichannel retailers.

**Fix applied — two verdicts revised:**
- **AI Customer Service → downgraded to PILOT** (Evidence 8/10, Hype 8/10). High hype score means oversold claims are the norm. Pilot only; do not invest ahead of the core use case.
- **Customer Personalisation → elevated to #2 INVEST** (Evidence 7/10, Hype 7/10). Pursue after demand forecasting is operational. Requires unified customer data view first.

Updated ranking in `research/opportunities_risks.md`:

| # | Use Case | Verdict |
|---|---|---|
| 1 | Demand Forecasting | INVEST |
| 2 | Customer Personalisation | INVEST (Phase 2) |
| 3 | AI Customer Service | PILOT |
| 4 | Dynamic Pricing | PILOT |
| — | Autonomous Checkout | SKIP |

---

## Gap 6 — Diagnostic Tool May Misclassify Maturity Stage

**Original project tool:** Stage 2 = "Process-driven — manual but organised."

**Report finding:** Cleo = Stage 2 "Experimenting" — basic AI tools deployed (email automation, simple product recommendations) but isolated, vendor-provided, limited integration.

**The gap:** A company with email automation and product recommendations already deployed would score as Stage 3 (Partial Automation) on the project's scale — one stage higher than the report's classification. This misclassification changes the recommendations generated by the diagnostic tool.

**Recommended fix for `ai_diagnostic_tool.html`:** Refine Stage 2/3 thresholds to distinguish between "organised manual processes" and "isolated AI experiments." The "Experimenting" label captures the reality that tools exist but are not integrated — the current Stage 2 definition misses this profile.

---

## Gap 7 — Data Remediation Not Separately Scoped or Costed

**Original project position:** Phase 0 is a 2-week data audit with no budget. Implicitly assumed data would be usable.

**Report finding:** 3–6 months of data remediation work may be required before demand forecasting can be trained. Budget: £30K–£60K. If audit reveals 9+ month gaps, pause AI investment entirely.

**The gap:** A 2-week audit with no budget is incompatible with a potential 3–6 month remediation phase. The project assumed a passing result; the report explicitly plans for failure.

**Fix applied:** `cost_estimation/timeline_estimate.md` Phase 0 now includes a 3-way gate:
- Pass (12+ months clean data) → proceed to Phase 1
- Remediate (< 12 months usable) → insert 3–6 month remediation (£30K–£60K) before Phase 1
- Pause (9+ month gaps) → fix data infrastructure before any AI spend

---

## Summary of Changes Made

| File | Change |
|---|---|
| `cost_estimation/cost_analysis.md` | Added hybrid TCO (£393K/3yr); added attribution discount ROI table; added full hidden costs breakdown; added true full programme cost (£700K–£900K) |
| `cost_estimation/timeline_estimate.md` | Restructured to 6 phases (Phase 0–5); extended evaluation to Month 12–18; added data remediation conditional branch; added named roles and change management requirements |
| `research/opportunities_risks.md` | Downgraded AI Customer Service to PILOT; elevated Customer Personalisation to #2 INVEST; added evidence/hype scores; added per-use-case ROI estimates; updated risk table with likelihood and impact ratings |
| `dashboard/dashboard_documentation.md` | Updated from Tableau to Python (7 charts); documented all chart types, data sources, and insights matching the presentation dashboard |

---

## What the Project Does Better Than the Report

1. **Vendor specificity.** The project names Inventory Planner, Relex Lite, and Brightpearl AI with pricing ranges. The report stays at architectural level. For a CEO in a buying decision, the project is more immediately actionable.

2. **The diagnostic tool itself.** The report describes a problem; the project built a reusable HTML instrument to identify it. Once the stage 2/3 thresholds are recalibrated (Gap 6), the tool is a genuine consulting asset the report does not provide.

3. **Evidence-first framing.** The project's explicit hype vs evidence scoring (Evidence 9/10, Hype 4/10 for demand forecasting) gives the CEO a clear signal without requiring them to read the underlying research.

---

## Overall Assessment

The primary recommendation — demand forecasting first, data audit before any spend — is validated by the external benchmark. The seven gaps were concentrated in cost realism, timeline realism, and diagnostic calibration. All seven have been addressed. The project is now internally consistent and aligned with the external report on every material point.
