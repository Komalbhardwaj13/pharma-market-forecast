import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ==============================
# 1. Assumptions
# ==============================

# Population & epidemiology
population = 10_000_000
prevalence = 0.08
diagnosed_rate = 0.70
eligible_rate = 0.60
treatment_rate = 0.75

# Pricing
price_per_patient = 12_000

# Launch timeline
years = [2026, 2027, 2028, 2029, 2030]

# Market share ramp
market_share = [0.05, 0.10, 0.15, 0.20, 0.25]


# ==============================
# 2. Patient Funnel
# ==============================

patients = population * prevalence
diagnosed = patients * diagnosed_rate
eligible = diagnosed * eligible_rate
treated = eligible * treatment_rate

print(f"Total treated patients: {treated:,.0f}")


# ==============================
# 3. Forecast Calculation
# ==============================

results = []

for i in range(len(years)):
    year = years[i]
    share = market_share[i]

    brand_patients = treated * share
    revenue = brand_patients * price_per_patient

    results.append([year, share, brand_patients, revenue])


# ==============================
# 4. Create DataFrame
# ==============================

df = pd.DataFrame(
    results,
    columns=["Year", "Market Share", "Brand Patients", "Revenue"]
)

# make output clean
df["Brand Patients"] = df["Brand Patients"].round(0)
df["Revenue"] = df["Revenue"].round(0)
df["Revenue ($M)"] = (df["Revenue"] / 1_000_000).round(2)

print(df)


# ==============================
# 5. Plot
# ==============================

plt.plot(df["Year"], df["Revenue ($M)"], marker="o")
plt.title("Revenue Forecast")
plt.xlabel("Year")
plt.ylabel("Revenue ($M)")
plt.show()


# ==============================
# 6. Export
# ==============================

df.to_excel("basic_forecast.xlsx", index=False)
