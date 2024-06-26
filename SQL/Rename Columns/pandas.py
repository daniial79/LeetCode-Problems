import pandas as pd

def rename_columns_v0(students: pd.DataFrame) -> pd.DataFrame:
    students.columns = ["student_id", "first_name", "last_name", "age_in_years"]
    return students