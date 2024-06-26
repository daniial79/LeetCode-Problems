import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    report_frequency = pd.DataFrame(employee['managerId'].value_counts().reset_index())
    at_least_five = report_frequency[report_frequency['count'] >= 5]
    return employee[employee['id'].isin(at_least_five['managerId'])][["name"]]