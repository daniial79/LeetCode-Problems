import pandas as pd

# solution I
def largest_orders_v0(orders: pd.DataFrame) -> pd.DataFrame:
    return orders.groupby(['customer_number']).agg({
        'order_number': 'count'
    }).reset_index().sort_values(by='order_number', ascending=False)[['customer_number']].head(1)
    
# solution II
def largest_orders_v1(orders: pd.DataFrame) -> pd.DataFrame:
    return orders['customer_number'].mode().to_frame()