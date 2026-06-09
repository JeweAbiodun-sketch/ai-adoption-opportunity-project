# Implementation Plan — AI Demand Forecasting
**Mid-Market Retail · 51–250 employees**

---

## Phase 0 — Data Audit (Weeks 1–2)
**Owner:** Internal ops lead + vendor pre-sales
**Actions:**
- Audit POS/ERP data quality: completeness, consistency, history depth
- Confirm minimum 12 months of daily sales data by SKU exists
- Identify data gaps (missing categories, location splits, returns data)
- Select 1 category or 1 store as pilot scope

**Go/no-go gate:** If less than 12 months of clean daily sales data exists, pause and invest in data cleaning first (estimated 4–8 weeks additional).

---

## Phase 1 — Vendor Selection & Pilot Setup (Weeks 3–6)
**Owner:** CEO + ops lead
**Actions:**
- Evaluate 2–3 vendors (Inventory Planner, Relex Lite, Brightpearl AI)
- Run free trial on pilot category/store
- Compare forecast accuracy vs current buyer method
- Negotiate contract terms: monthly SaaS, data ownership clause, no lock-in

**Budget:** £0 (free trials) + £500–£1,500 setup support if needed

---

## Phase 2 — Pilot Deployment (Weeks 7–16)
**Owner:** Buying/merchandising lead
**Actions:**
- Connect vendor to ERP/POS via API or CSV export
- Run AI forecast alongside manual forecast for 4 weeks (shadow mode)
- Compare accuracy, adjust model parameters
- Train buying team on reviewing and overriding AI recommendations
- Track: stockout rate, overstock flags, forecast MAPE

**Budget:** £500–£2,000/month (vendor SaaS)

---

## Phase 3 — Evaluation & Scale Decision (Week 17–20)
**Owner:** CEO + buying team
**Actions:**
- Review pilot metrics vs baseline (see Solution Proposal for targets)
- Calculate actual ROI from pilot period
- Decide: expand to all categories, expand to all stores, or stop
- If expanding: negotiate annual contract (typically 20–30% discount)

---

## Phase 4 — Full Rollout (Months 6–12)
**Owner:** Ops lead
**Actions:**
- Roll out to all SKUs and all stores
- Integrate with buying calendar and OTB (Open-to-Buy) process
- Connect to supplier reorder system if available
- Build internal reporting: weekly AI forecast accuracy dashboard in Tableau

**Budget:** £2,000–£5,000/month (full implementation)

---

## Risks and Mitigations

| Risk | Mitigation |
|---|---|
| Data gaps block Phase 1 | Run data audit before vendor demos |
| Buyer team resists AI recommendations | Shadow mode first — AI advises, buyer decides |
| Vendor oversells accuracy | Negotiate performance clause in contract |
| Seasonal edge cases fool the model | Manual override process documented from day one |
