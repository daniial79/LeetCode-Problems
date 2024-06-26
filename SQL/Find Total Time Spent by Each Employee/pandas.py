import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    employees = employees.assign(
        total_time=employees['out_time'] - employees['in_time']
    )

    result = employees.groupby(['event_day', 'emp_id']).agg({
        'total_time': 'sum'
    }).reset_index()

    result = result.rename(columns={
        'event_day': 'day'
    })

    return result