# Cost Analysis — AI Demand Forecasting for Mid-Market Retail
**Assumptions documented · All figures estimated from public vendor pricing**

---

## Scenario: £10M–£50M revenue retailer, 51–250 staff

---

## Scenario 1 — SaaS Pilot (Phase 1–2 Entry Point)

| Item | Low Estimate | High Estimate | Notes |
|---|---|---|---|
| Monthly SaaS | £500 | £5,800 | Inventory Planner ~£99/mo; enterprise tools up to £5.8K |
| Annual running cost | £6,000 | £70,000 | |
| Setup & integration support | £500 | £1,500 | Vendor API or CSV; varies by system |
| **SaaS Pilot Total (Year 1)** | **£19,000** | **£83,000** | **Test value at low commitment** |

*The SaaS pilot is the entry point — not the end-state infrastructure. It tests whether AI demand forecasting works for Cleo before any significant capital commitment.*

---

## Scenario 2 — Hybrid Model (Full Programme Scale)

| Item | Cost | Notes |
|---|---|---|
| Setup (one-time) | £70,560 | Data integration, middleware, internal tooling |
| Year 1 running cost | £120,485 | SaaS + internal resource + integration |
| Year 2 running cost | £120,485 | |
| Year 3 running cost | £120,485 | |
| **3-Year Total** | **£393,623** | **~5× more expensive than SaaS pilot** |

*The hybrid model is the scale architecture. Present both figures from the start so the client is not surprised when growth requires infrastructure investment.*

---

## Add-Ons — Budget These Separately

### Change Management (Not Optional at This Maturity Level)

| Item | Low | High |
|---|---|---|
| Programme budget | £20,000 | £40,000 |
| Per affected employee (training) | £500 | £1,000 |
| Protected learning time per person | 20 hrs | 30 hrs |
| **Without this: 30–50% tool underutilisation in first 6 months** | | |

### Data Remediation (Conditional — Only if Audit Fails)

| Audit Finding | Next Step | Budget |
|---|---|---|
| 12+ months clean daily SKU data | Proceed to Phase 1 | £0 |
| < 12 months usable data | 3–6 month remediation phase | £30,000–£60,000 |
| 9+ month gaps / no SKU history | Pause — prioritise data infrastructure first | TBD |

---

## Other Costs — Not on Any Vendor Quote

### 01 Internal Staff Time

| Role | Commitment | Estimated Cost |
|---|---|---|
| Executive sponsor | 2–4 hrs/wk × 18 months | £8,000–£18,000 |
| Buying / merchandising champion | 4–6 hrs/wk × 12 months | £12,000–£20,000 |
| IT lead (integration) | 8–12 hrs/wk at setup | £10,000–£18,000 |
| Buyers using tool daily | 1–2 hrs/wk × 12 months | £6,000–£15,000 |
| **Total** | | **£36,000–£71,000** |

*This is existing payroll redirected — easy to overlook, impossible to avoid.*

### 02 Data Audit Underestimate (Even Passing Audits Cost More)

| Item | Notes | Cost |
|---|---|---|
| Light data cleaning (always needed) | SKU name standardisation | £5,000–£10,000 |
| Zero-sale day fill-in | ETL scripting | £2,000–£5,000 |
| Returns reconciliation | QA & validation | £1,000–£3,000 |
| **Total extra** | | **£5,000–£15,000** |

*The £5K–£8K audit fee covers finding problems, not fixing them.*

### 03 Vendor Procurement & Legal (Often Forgotten Entirely)

| Item | Notes | Cost |
|---|---|---|
| Vendor evaluation (3 trials) | 2–4 weeks management time | £3,000–£6,000 |
| Contract review — data ownership | Legal counsel | £1,000–£3,000 |
| GDPR / data compliance review | POS data obligation | £500–£2,000 |
| **Total** | | **£3,000–£8,000** |

*Data ownership clauses are critical — who owns the demand model after the contract ends?*

### 04 Ongoing Model Maintenance (Year 2 Onwards — Not in TCO)

| Item | Notes | Annual Cost |
|---|---|---|
| Retraining after range changes | New lines, store openings | £3,000–£8,000 |
| Forecast drift monitoring | Recalibration cycles | £2,000–£5,000 |
| Integration maintenance | API updates, patches | £1,000–£3,000 |
| **Total per year** | | **£5,000–£15,000** |

*The hybrid TCO shows Years 2 & 3 at £120K — model maintenance sits on top of that.*

### 05 AI Consultant Fees (Biggest Omission)

| Item | Phase | Cost |
|---|---|---|
| Diagnostic & strategy | Phase 0 design | £8,000–£25,000 |
| Implementation oversight | Ph0–Ph1 vendor selection | £15,000–£40,000 |
| Advisory retainer during pilot | Monthly check-ins | £2,000–£5,000/mo |
| Full programme management | Ph0–Ph3, 18-month support | £60,000–£120,000 |
| **Total** | | **£60,000–£120,000** |

*Technology costs and consulting fees are quoted separately. Clients see two invoices — and are often surprised by the second.*

---

## True Full Programme Cost — What a CFO Should Budget

| Cost Category | Slide Estimate | What Is Hidden | Full Realistic Budget |
|---|---|---|---|
| SaaS Pilot (Year 1) | £19K–£83K | ✓ shown | £19K–£83K |
| Hybrid Scale (3yr) | £393,623 | £55K–£95K overrun risk | £450K–£490K |
| Change Management | £20K–£40K | ✓ shown | £20K–£40K |
| Data Remediation | £30K–£60K | Light clean always needed | £35K–£75K |
| Internal Staff Time | Not shown | £36K–£71K | £36K–£71K |
| Data Audit Extras | Understated | £5K–£15K | £5K–£15K |
| Procurement & Legal | Not shown | £3K–£8K | £3K–£8K |
| Model Maintenance (yr 2+) | Not shown | £5K–£15K/yr | £5K–£15K/yr |
| AI Consultant Fees | Not shown | £60K–£120K | £60K–£120K |
| **TRUE FULL PROGRAMME COST** | **Slide estimate: ~£550K** | | **Realistic: £700K–£900K** |

---

## ROI Model — With Attribution Discount

**Assumptions:**
- Annual revenue: £15M
- Inventory holding cost: 25% of stock value (~£1.5M annually on a £6M stock base)
- Gross benefit estimate: £650K/year (inventory reduction + margin + stockouts)

| Scenario | Attribution | Estimated Annual Benefit | Notes |
|---|---|---|---|
| Pessimistic | 30% | ~£200,000 | Weak adoption, partial data |
| **Base case** | **60%** | **~£405,000** | **CFO-defensible; use in boardroom** |
| Optimistic | 80% | ~£540,000 | Strong adoption, clean data |

*Replace the 30:1 ROI headline with this range. The base case (£405K) is still compelling and is defensible against scrutiny. The 30:1 figure signals the model is built to sell rather than to test.*

---

## Pilot Budget Recommendation

**For Cleo's first investment decision:**
- Commit to: SaaS pilot, one product category, free trial then monthly SaaS — no lock-in
- Maximum budget at pilot stage: **£19,000–£83,000 (Year 1)**
- Name three roles before launch: Executive Sponsor · Merchandising Champion · Store Pilot Lead
- Evaluate accuracy at Month 6 (MAPE < 15%), make ROI and scale decision at Month 12–18
