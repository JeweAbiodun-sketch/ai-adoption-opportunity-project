# Implementation Plan — AI Demand Forecasting

Mid-Market Retail · 51–250 employees

---

## Phase 0 — Data Audit (Weeks 1–2)

**Owner:** Internal ops lead + vendor pre-sales

**Actions:**

- Audit POS/ERP data quality: completeness, consistency, history depth
- Confirm minimum 12 months of daily sales data by SKU exists
- Identify data gaps (missing categories, location splits, returns data)
- Select 1 category or 1 store as pilot scope

**Go/no-go gate — Data Readiness:**

| Audit finding | Next step |
| --- | --- |
| 12+ months of clean daily sales data available | Proceed to Phase 1 |
| Significant gaps or < 12 months of usable data | Insert **Data Remediation Phase** (see below) before Phase 1 |
| 9+ month data gaps or no SKU-level history | Pause AI investment; prioritise data infrastructure first |

### Data Remediation Phase (conditional — insert if audit fails)

**Trigger:** Phase 0 audit finds less than 12 months of clean daily sales data.

**Duration:** 3–6 months

**Budget:** £30k–£60k

**Actions:**

- Identify and reconcile gaps in POS transaction history
- Standardise SKU identifiers across locations
- Backfill missing returns and markdown data where possible
- Rerun Phase 0 audit at end of remediation before proceeding

> Do not proceed to vendor selection until the data audit passes. Demand forecasting models trained on patchy data produce inaccurate recommendations and erode buyer trust faster than the status quo.

---

## Change Management Requirements

Workforce readiness is the weakest dimension at this company profile (3/10 in external benchmarking). A well-designed tool with poor adoption delivers nothing. These requirements must be in place before Phase 2 begins.

**Named roles — must be assigned before pilot launch:**

| Role | Responsibility |
| --- | --- |
| Executive sponsor (CEO or COO) | Accountable for the programme; escalation point for blockers |
| Merchandising champion | Day-to-day owner of the tool within the buying team |
| Store pilot lead | Coordinates data flow and feedback from the pilot store |

**Training budget:** £500–£1,000 per affected buyer or merchandiser

**Protected time:** 20–30 hours per person during Phases 1–2 for onboarding and supervised use

**Adoption target:** >70% active tool usage by Week 16 — this is a success criterion, not a nice-to-have. Without it, expect 30–50% tool underutilisation in the first 6 months regardless of technical quality.

---

## Phase 1 — Vendor Selection & Pilot Setup (Weeks 3–6)

**Owner:** CEO + ops lead

**Actions:**

- Evaluate 2–3 vendors (Inventory Planner, Relex Lite, Brightpearl AI)
- Run free trial on pilot category/store
- Compare forecast accuracy vs current buyer method
- Negotiate contract terms: monthly SaaS, data ownership clause, no lock-in
- Confirm executive sponsor and merchandising champion are assigned

**Budget:** £0 (free trials) + £500–£1,500 setup support if needed

---

## Phase 2 — Pilot Deployment (Weeks 7–16)

**Owner:** Merchandising champion

**Actions:**

- Connect vendor to ERP/POS via API or CSV export
- Run AI forecast alongside manual forecast for 4 weeks (shadow mode — AI advises, buyer decides)
- Compare accuracy, adjust model parameters
- Train buying team on reviewing and overriding AI recommendations (use protected time allocation)
- Track weekly: stockout rate, overstock flags, forecast MAPE, tool adoption rate

**Budget:** £500–£2,000/month (vendor SaaS)

---

## Phase 3 — Operational Review (Weeks 17–20)

**Owner:** CEO + merchandising champion

> This is an **operational review only** — not the ROI decision gate. The evaluation window is too short to draw meaningful conclusions about demand forecasting accuracy. The model needs at least one seasonal cycle to learn patterns. ROI conclusions drawn here risk a false negative that terminates a programme before it has had a chance to deliver.

**Actions:**

- Confirm the tool is in active use (adoption rate vs >70% target)
- Confirm data is flowing correctly from ERP/POS to the vendor
- Identify and resolve any integration or workflow blockers
- Document buyer feedback: overrides, confidence in recommendations, missing features
- Decide: continue to Month 6 checkpoint, pause to fix blockers, or stop

**Gate:** If adoption rate is below 70% or data pipeline has unresolved failures, pause and fix before continuing. Do not proceed to full rollout.

---

## Phase 4 — First Accuracy Checkpoint (Month 6)

**Owner:** CEO + ops lead

**Actions:**

- Review forecast accuracy: is MAPE below 15%?
- Review adoption: is active tool usage above 70%?
- Compare stockout rate and overstock flags against baseline
- Assess whether the pilot category/store results justify expanding scope
- Decide: expand pilot to additional categories, expand to additional stores, or stop

**Budget:** £500–£2,000/month (ongoing SaaS — no additional cost at this stage)

---

## Phase 5 — Full Rollout (Months 6–12, if Phase 4 gate passes)

**Owner:** Ops lead

**Actions:**

- Roll out to all SKUs and all stores
- Integrate with buying calendar and OTB (Open-to-Buy) process
- Connect to supplier reorder system if available
- Build internal reporting: weekly AI forecast accuracy dashboard in Tableau
- Continue tracking adoption rate — target >85% active users by end of rollout

**Budget:** £2,000–£5,000/month (full implementation)

---

## Phase 6 — ROI and Scale Decision (Months 12–18)

**Owner:** CEO + CFO

> This is the correct point to evaluate ROI and decide on infrastructure investment. Demand forecasting accuracy improves as the model learns seasonal patterns; a 5-month window captures at best one partial season cycle. Leadership must commit to this timeline or not start — partial implementations fail and waste money.

**Actions:**

- Compare actual inventory days-on-hand, stockout rate, and markdown rate vs documented baseline
- Apply attribution discount (use 60% base case) to calculate AI-attributable benefit
- Evaluate against three scenarios: pessimistic (30% attribution), base (60%), optimistic (80%)
- Decide: maintain SaaS model, invest in hybrid architecture, or exit

**Scale investment trigger:** If base-case ROI is positive and adoption is above 85%, consider moving from SaaS-only (~£9k–£83k/year) to hybrid operating model (~£70k setup + £120k/year) to support additional use cases (personalisation, dynamic pricing).

---

## Risks and Mitigations

| Risk | Mitigation |
| --- | --- |
| Data gaps block Phase 1 | Conditional remediation phase before vendor selection |
| Buyer team resists AI recommendations | Shadow mode first; named merchandising champion accountable for adoption |
| Low adoption at Week 16 review | Pause and investigate — do not proceed to full rollout with <70% usage |
| Vendor oversells accuracy | Negotiate performance clause in contract; MAPE gate at Month 6 |
| Seasonal edge cases fool the model | Manual override process documented from day one |
| ROI decision made too early | Phase 3 is operational review only; ROI gate is Months 12–18 |
| Infrastructure cost sticker shock at scale | Present hybrid TCO (£393k/3yr) alongside SaaS pilot cost from the start |
