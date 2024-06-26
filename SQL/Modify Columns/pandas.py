import pandas as pd

def modify_salary_column_v0(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"]  = employees["salary"] * 2
    return employees
    
def modify_salary_column_v1(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"].apply(lambda x: x * 2)
    return employees

