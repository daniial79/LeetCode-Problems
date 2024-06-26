import pandas as pd

def create_bonus_column(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"] * 2
    return employees