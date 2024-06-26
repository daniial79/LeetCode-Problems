import pandas as pd

def create_dataframe(student_data: list[list[int]]) -> pd.DataFrame:
    return pd.DataFrame(data=student_data, columns=["student_id", "age"])