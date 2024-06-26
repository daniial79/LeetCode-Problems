import pandas as pd

def pivot_table(weather: pd.DataFrame) -> pd.DataFrame:
    pivoted_df = weather.pivot(index="month", columns="city", values="temperature")
    return pivoted_df