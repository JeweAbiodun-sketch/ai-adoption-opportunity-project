import pandas as pd

# ── Retail sales ──────────────────────────────────────────────────────────────
df = pd.read_csv("data/raw/retail_sales_dataset.csv")

# Standardise column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Parse dates
df["date"] = pd.to_datetime(df["date"])
df["month"] = df["date"].dt.to_period("M").astype(str)
df["month_num"] = df["date"].dt.month
df["year"] = df["date"].dt.year

# Drop nulls
df = df.dropna()

df.to_csv("data/processed/retail_sales_cleaned.csv", index=False)
print(f"✓ Retail sales cleaned: {len(df)} rows")
print(df.columns.tolist())

# ── AI adoption ───────────────────────────────────────────────────────────────
try:
    ai = pd.read_csv("data/raw/global_ai_tool_adoption.csv")
    ai.columns = ai.columns.str.strip().str.lower().str.replace(" ", "_")
    ai.to_csv("data/processed/ai_adoption_retail_filtered.csv", index=False)
    print(f"✓ AI adoption cleaned: {len(ai)} rows")
    print(ai.columns.tolist())
except Exception as e:
    print(f"AI adoption file: {e}")