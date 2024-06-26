import pandas as pd

def find_customer_referee(customer: pd.DataFrame) -> pd.DataFrame:
    not_referred_by_2 = (customer["referee_id"] != 2) | (customer["referee_id"].isna())
    return customer[not_referred_by_2][["name"]]