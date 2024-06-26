import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_salaries_count = accounts[accounts["income"] < 20000].shape[0]
    average_salaries_count = accounts[(20000 <= accounts["income"]) & (accounts["income"] <= 50000)].shape[0]
    high_salaries_count = accounts[accounts["income"] > 50000].shape[0]

    return pd.DataFrame({
        "category": ["Low Salary", "Average Salary", "High Salary"],
        "accounts_count": [low_salaries_count, average_salaries_count, high_salaries_count]
    })