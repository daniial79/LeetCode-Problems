import pandas as pd

def sales_analysis_v0(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(
        left=sales,
        right=product,
        left_on="product_id",
        right_on="product_id",
        how="inner"
    )
    
    return merged_df[["product_name", "year", "price"]]

def sales_analysis_v1(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    return sales.merge(product, on="product_id", how="inner")[["product_name", "year", "price"]]