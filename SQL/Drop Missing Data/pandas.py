import pandas as pd

def drop_missing_data(students: pd.DataFrame) -> pd.DataFrame:
    cleaned_df = students.dropna(subset=["name"])
    return cleaned_df