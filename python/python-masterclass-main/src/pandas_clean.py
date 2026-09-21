import pandas as pd 

df = pd.read_csv("data/raw/dirty_orders.csv")

df["amount"] = df["amount"].fillna(0)

df["amount"] = df["amount"].astype(int)

df["country"] = df["country"].str.upper()

print(df)

country_summary = (
    df.groupby("country")
    .agg(
        total_orders=("order_id", "count"),
        total_amount=("amount", "sum")
    )
)

print(country_summary)

df["running_total"] = df["amount"].cumsum()
print(df)