import pandas as pd

def find_customers(visits: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    # find behaviour of each customer per visit using visit's transaction value
    customer_behaviour_df = pd.merge(left=visits, right=transactions, on="visit_id", how="left")
    # return customer_behaviour_df

    # narrow down the general behaviour of customers to "no paied visit" or "NA transactions visits"
    no_transaction_df = customer_behaviour_df[customer_behaviour_df["transaction_id"].isna()]
    # return no_transaction_df

    # count occurence of customer ids
    no_transactions_frequency_sries = no_transaction_df.groupby("customer_id")["customer_id"].agg("count")

    return pd.DataFrame(
        data=no_transactions_frequency_sries, 
        index=no_transactions_frequency_sries.index).rename(columns={"customer_id": "count_no_trans"}).reset_index()