import pandas as pd


def find_heavy_animals(animals: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(animals[animals["weight"] > 100].sort_values("weight", ascending=False)["name"])

