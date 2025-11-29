import pandas as pd
from pathlib import Path
import hashlib

CLEAN_DIR = Path("data/clean")
WAREHOUSE_DIR = Path("data/warehouse")

def create_customer_id(row) -> str:
    """Create synthetic unique customer_id using hash."""
    raw = f"{row['age']}-{row['job']}-{row['marital']}-{row['balance']}"
    return hashlib.md5(raw.encode()).hexdigest()

def build_dim_customer(df: pd.DataFrame) -> pd.DataFrame:
    dim = df[[
        "age", "job", "marital", "education",
        "default", "balance", "housing", "loan"
    ]].drop_duplicates().reset_index(drop=True)

    dim["customer_id"] = dim.apply(create_customer_id, axis=1)
    cols = ["customer_id"] + [c for c in dim.columns if c != "customer_id"]
    return dim[cols]

def build_dim_campaign(df: pd.DataFrame) -> pd.DataFrame:
    dim = df[[
        "contact", "month", "campaign", "previous", "poutcome", "pdays"
    ]].drop_duplicates().reset_index(drop=True)
    
    dim["campaign_id"] = dim.index + 1
    cols = ["campaign_id"] + [c for c in dim.columns if c != "campaign_id"]
    return dim[cols]

def build_fact_marketing(df: pd.DataFrame, dim_customer: pd.DataFrame, dim_campaign: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # Generate customer_id
    df["customer_id"] = df.apply(create_customer_id, axis=1)

    # Merge campaign_id
    fact = df.merge(
        dim_campaign,
        how="left",
        on=["contact", "month", "campaign", "previous", "poutcome", "pdays"]
    )

    # Convert target y (yes/no) → 1/0
    fact["target"] = fact["y"].map({"yes": 1, "no": 0})

    fact = fact[[
        "customer_id",
        "campaign_id",
        "day",
        "month",
        "duration",
        "contact",
        "campaign",
        "previous",
        "poutcome",
        "pdays",
        "balance",
        "housing",
        "loan",
        "target"
    ]]
    return fact

def main():
    print("Loading cleaned training data...")
    df = pd.read_csv(CLEAN_DIR / "bank_marketing_train_clean.csv")

    print("Building dimensions...")
    dim_customer = build_dim_customer(df)
    dim_campaign = build_dim_campaign(df)

    print("Building fact table...")
    fact = build_fact_marketing(df, dim_customer, dim_campaign)

    WAREHOUSE_DIR.mkdir(parents=True, exist_ok=True)

    dim_customer.to_csv(WAREHOUSE_DIR / "dim_customer.csv", index=False)
    dim_campaign.to_csv(WAREHOUSE_DIR / "dim_campaign.csv", index=False)
    fact.to_csv(WAREHOUSE_DIR / "fact_marketing_interactions.csv", index=False)

    print("✔ Warehouse tables generated!")

if __name__ == "__main__":
    main()
