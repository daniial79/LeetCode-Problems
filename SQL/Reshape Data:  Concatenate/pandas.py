import pandas as pd

def concatenate_tables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    concatenated_df = pd.concat([df1, df2], axis=0)
    return concatenated_df