import pandas as pd

def select_first_rows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)