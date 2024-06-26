import pandas as pd

def drop_duplicate_emails(customers: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = customers.drop_duplicates("email")
    return cleaned_df