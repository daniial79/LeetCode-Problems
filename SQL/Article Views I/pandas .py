import pandas as pd

def article_views_v0(views: pd.DataFrame) -> pd.DataFrame:
    mask = views["author_id"] == views["viewer_id"]
    return pd.DataFrame(data={"id": views[mask]["author_id"].unique()}).sort_values(by="id")

def article_views_v1(views: pd.DataFrame) -> pd.DataFrame:
    mask = views["author_id"] == views["viewer_id"]
    result_series = views[mask]["author_id"]
    result_series.drop_duplicates(inplace=True, keep="first")
    result_series.sort_values(inplace=True)
    return pd.DataFrame({"id": result_series})