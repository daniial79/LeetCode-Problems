import pandas as pd

def get_dataframe_size(players: pd.DataFrame) -> list[int]:
    return [players.shape[0], players.shape[1]]

def get_dataframe_size_v1(players: pd.DataFrame) -> list[int]:
    return [len(players.index), len(players.columns)]

