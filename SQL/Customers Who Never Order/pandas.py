import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    no_order_customer_mask = ~customers['id'].isin(orders['customerId'])
    res = customers[no_order_customer_mask][['name']].rename(columns={'name': 'Customers'})
    return res
    