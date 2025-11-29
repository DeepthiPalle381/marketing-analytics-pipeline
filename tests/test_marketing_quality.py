import pandas as pd

FACT = pd.read_csv("data/warehouse/fact_marketing_interactions.csv")
DIM_CUST = pd.read_csv("data/warehouse/dim_customer.csv")
DIM_CAMPAIGN = pd.read_csv("data/warehouse/dim_campaign.csv")


def test_targets_are_binary():
    assert set(FACT["target"].unique()) <= {0, 1}, "Target must be 0 or 1"


def test_customer_id_in_fact_exists_in_dim():
    missing = FACT[~FACT["customer_id"].isin(DIM_CUST["customer_id"])]
    assert len(missing) == 0, "Fact has customer_ids not found in dim_customer"


def test_campaign_id_exists_in_dim():
    missing = FACT[~FACT["campaign_id"].isin(DIM_CAMPAIGN["campaign_id"])]
    assert len(missing) == 0, "Fact has campaign_ids not found in dim_campaign"


def test_no_negative_values():
    # duration should never be negative
    assert (FACT["duration"] >= 0).all(), "Duration cannot be negative"

    # balance can be negative (overdraft), but should not be null
    assert FACT["balance"].notnull().all(), "Balance should not be null"


def test_dim_customer_unique_ids():
    assert DIM_CUST["customer_id"].is_unique, "customer_id must be unique"
