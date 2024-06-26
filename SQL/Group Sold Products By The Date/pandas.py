import pandas as pd

def join_comma_separated(row):
    row['product'] = sorted(list(row['product']))
    return ','.join(row['product'])

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    activities.drop_duplicates(inplace=True)
    temp = activities.groupby(['sell_date']).apply(join_comma_separated).reset_index().rename(
        columns={
            0:"products"
        }
    )

    temp["num_sold"] = (temp["products"].str.count(",") + 1)

    return temp.iloc[:,[0,2,1]]