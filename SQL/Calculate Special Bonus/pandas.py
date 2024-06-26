import pandas as pd

def calculate_special_bonus_v0(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.assign(
        bonus=employees.apply(lambda x: x['salary'] if int(x['employee_id']) % 2 != 0 and 
                              not x['name'].startswith('M') else 0, axis=1)
    )[['employee_id', 'bonus']].sort_values(
        by='employee_id',
    )
    
def calculate_special_bonus_v1(employees: pd.DataFrame) -> pd.DataFrame:
    employees["bonus"] = employees["salary"]
    employees.loc[(employees["employee_id"] % 2 == 0) | (employees["name"].str[0] == "M"), "bonus"] = 0 
    return employees["employee_id", "bonus"].sort_values("employee_id")