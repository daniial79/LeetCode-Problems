import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    big_country_mask = (world["area"] >= 3e6) | (world["population"] >= 2.5e7) 
    return world[big_country_mask][["name", "population", "area"]]