import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cooperation_frequency_df = actor_director.groupby(['actor_id', 'director_id'])[['timestamp']].count().reset_index()
    return cooperation_frequency_df[cooperation_frequency_df['timestamp'] >= 3][['actor_id', 'director_id']]