import pandas as pd
import numpy as np

np.random.seed(42)

# -----------------------------
# Configuration
# -----------------------------
N = 25000
start_date = pd.to_datetime("2024-01-01")

banks = [
    "Sanima Bank", "NMB Bank", "Everest Bank",
    "Global IME Bank", "Machhapuchhre Bank", "NIC Asia Bank"
]

channels = [
    "Facebook Ads", "Google Search",
    "Email Campaign", "Referral", "Organic Search"
]

cities = [
    "Kathmandu", "Lalitpur", "Pokhara",
    "Bharatpur", "Butwal", "Biratnagar", "Nepalgunj"
]

devices = ["Mobile", "Desktop", "Tablet"]

products = {
    "Fixed Deposit": (50000, 200000),
    "Savings Account": (1000, 5000),
    "Loan": (200000, 1000000),
    "Credit Card": (2000, 10000)
}

# Probabilities
p_lead = 0.45
p_customer = 0.25

# -----------------------------
# Generate base data
# -----------------------------
df = pd.DataFrame({
    "visitor_id": [f"V{str(i).zfill(6)}" for i in range(1, N + 1)],
    "date": start_date + pd.to_timedelta(np.arange(N), unit="H"),
    "bank": np.random.choice(banks, N),
    "channel": np.random.choice(channels, N),
    "city": np.random.choice(cities, N),
    "device": np.random.choice(devices, N),
})

df["visited"] = 1

# -----------------------------
# Funnel stages
# -----------------------------
df["lead"] = (np.random.rand(N) < p_lead).astype(int)
df["customer"] = ((df["lead"] == 1) & (np.random.rand(N) < p_customer)).astype(int)

# -----------------------------
# Product & Revenue
# -----------------------------
df["product"] = ""
df["revenue"] = 0

for idx in df[df["customer"] == 1].index:
    product = np.random.choice(list(products.keys()))
    revenue = np.random.randint(*products[product])
    df.at[idx, "product"] = product
    df.at[idx, "revenue"] = revenue

# -----------------------------
# Save file
# -----------------------------
df.to_csv("bank_funnel_lead_data.csv", index=False)

print("Bank funnel lead dataset generated")
print(df.head(10))
