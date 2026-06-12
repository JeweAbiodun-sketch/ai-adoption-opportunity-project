# Implementation Plan — AI Demand Forecasting
**Six Phases · Data Audit to ROI Decision · 12–18 Month Horizon**
**Mid-Market Retail · Electronics & Technology · 51–250 employees**

---

## Phase Summary

| Phase | Name | Duration | Budget | Key Milestone |
|---|---|---|---|---|
| 0 | Data Audit | Wks 1–2 | £0 | 3-way gate: proceed / remediate / pause |
| 1 | Vendor Selection | Wks 3–6 | ~£1,000 | Vendor selected, free trial running |
| 2 | Pilot Deployment | Wks 7–16 | £500–£2,000/mo | AI advising buyers; weekly KPI tracking |
| 3 | Operational Review | Wks 17–20 | — | Tool in use? Data flowing? (NOT the ROI gate) |
| 4 | Full Rollout | Mo 6–12 | £2,000–£5,000/mo | All SKUs + stores; MAPE <15%, adoption >85% |
| 5 | ROI & Scale Decision | Mo 12–18 | See note | Compare vs baseline; SaaS → Hybrid if ROI positive |

---

## Phase 0 — Data Audit
**Weeks 1–2 · £0**

Confirm 12+ months of clean daily SKU-level sales data before any AI spend.

**3-way gate:**
- **Proceed** — 12+ months clean daily data → move to Phase 1
- **Remediate** — < 12 months usable data → insert 3–6 month remediation phase (£30K–£60K) before Phase 1
- **Pause** — 9+ month gaps or no SKU history → prioritise data infrastructure first; do not proceed

*Skip this gate and the model trains on noise. No other phase can substitute for it.*

---

## Phase 1 — Vendor Selection
**Weeks 3–6 · ~£1,000**

Trial 2–3 vendors on one product category using free trials. Evaluate fit before any contract.

**Shortlist:**
- Inventory Planner (~£99/mo entry)
- Relex Lite
- Brightpearl AI

**Negotiation requirements:** Monthly SaaS only — no annual lock-in at pilot stage. Negotiate MAPE performance clause into any contract to guard against vendor accuracy oversell.

---

## Phase 2 — Pilot Deployment
**Weeks 7–16 · £500–£2,000/month**

Shadow mode: AI advises, buyers decide. Buyers retain full control throughout.

**Weekly tracking metrics:**
- MAPE (forecast accuracy) — target trend towards <15%
- Adoption rate — target >70% active tool usage by Week 16
- Stockout rate vs baseline
- Overstock flags acted on vs ignored

**Change management requirement:** Named merchandising champion accountable for adoption. Per-employee training: £500–£1,000 + 20–30 hours protected learning time. Without this, expect 30–50% tool underutilisation.

---

## Phase 3 — Operational Review
**Weeks 17–20 · No additional budget**

**This is not the ROI gate.** Weeks 17–20 is an operational health check only.

| Check | Pass threshold | Fail action |
|---|---|---|
| Tool in active use? | Yes — buyers logging in daily | Pause; identify barrier |
| Data flowing correctly? | No pipeline failures | Fix integration before proceeding |
| Adoption rate? | >70% | Pause full rollout; run change management intervention |

*Do not draw ROI conclusions at this stage. A 5-month window captures at most one partial seasonal cycle — insufficient for demand forecasting to prove value.*

---

## Phase 4 — Full Rollout
**Months 6–12 · £2,000–£5,000/month**

Expand from pilot category to all SKUs and stores. Integrate AI recommendations with the buying calendar.

**Go criteria from Phase 3:**
- Adoption >70% at Week 16 checkpoint
- No unresolved data pipeline failures

**Targets for this phase:**
- MAPE <15% sustained
- Adoption >85%
- Overstock flags resulting in earlier purchase order adjustments
- Stockout rate trending down vs baseline

---

## Phase 5 — ROI & Scale Decision
**Months 12–18 · See note**

Compare actual performance against baselines locked at Phase 0. Apply 60% attribution discount (base case) to isolate AI contribution.

| Metric | Baseline (locked Phase 0) | Target at Month 12–18 |
|---|---|---|
| Inventory days on hand | Recorded | Reduction vs baseline |
| Stockout rate | Recorded | Reduction vs baseline |
| Markdown rate | Recorded | Reduction vs baseline |
| Gross margin | Recorded | Improvement vs baseline |

**ROI scenarios (60% attribution base case):**

| Scenario | Attribution | Est. Annual Benefit |
|---|---|---|
| Pessimistic | 30% | ~£200,000 |
| Base case | 60% | ~£405,000 |
| Optimistic | 80% | ~£540,000 |

**Scale decision gate:** If ROI positive at base case and adoption >85% → upgrade SaaS → Hybrid model (£70,560 setup + £120,485/yr). If ROI not achieved → exit or extend evaluation window before further investment.

---

## Named Roles — Required Before Phase 2 Begins

| Role | Accountability |
|---|---|
| Executive Sponsor | Budget authority; escalation point; removes blockers |
| Merchandising Champion | Business-side adoption lead; not IT-led |
| Store Pilot Lead | Operational contact for pilot location |

*Change management is the difference between adoption and shelf-ware. Name these roles before launch, not after problems emerge.*

---

## Baseline Locking — Do This Before Any Spend

Lock the following metrics at Phase 0 so Month 12–18 ROI can be measured:
1. Inventory days on hand (by category)
2. Stockout rate (by category, by month)
3. Markdown rate and markdown timing
4. Gross margin (by category)

*Without locked baselines, ROI attribution is opinion, not evidence.*
