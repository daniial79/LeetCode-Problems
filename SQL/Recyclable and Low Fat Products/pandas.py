import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    mask = (products["recyclable"] == "Y") & (products["low_fats"] == "Y")
    return products[mask][["product_id"]]