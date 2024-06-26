import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    diab1_mask = patients["conditions"].str.contains(r"\bDIAB1")
    return patients[diab1_mask]    
    
