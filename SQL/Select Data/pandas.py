import pandas as pd

def select_data_v0(students: pd.DataFrame) -> pd.DataFrame:
    return students[students["student_id"] == 101][["name", "age"]]


def select_data_v1(students: pd.DataFrame) -> pd.DataFrame:
    boolean_df = students["student_id"] == 101
    return students[boolean_df][["name", "age"]]


def select_data_v2(students: pd.DataFrame) -> pd.DataFrame:
    conditioned_df = students[students["student_id"] == 101]
    return conditioned_df[["name", "age"]]