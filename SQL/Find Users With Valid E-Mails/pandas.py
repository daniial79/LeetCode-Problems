import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    mask = users["mail"].str.match(r"^[a-zA-Z][a-zA-Z0-9_.-]*@leetcode[.]com$")
    return users[mask]

