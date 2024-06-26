import pandas as pd

def rank(df: pd.DataFrame) -> pd.DataFrame:
    initial_rank = 1
    
    for i in range(len(df["score"])):
        # insert rank for current score
        df.iloc[i, 1] = initial_rank
        print(df.iloc[i, 1])

        # check if next score is less than current score or not 
        try:        
            if df.iloc[i]["score"] > df.iloc[i+1]["score"]:
                initial_rank += 1
        except IndexError:
            pass

    return df

def order_scores_v0(scores: pd.DataFrame) -> pd.DataFrame:
    # initiate new dataframe with rank column
    result_df = pd.DataFrame(data={
        "score": scores["score"], 
        "rank": 0
    })

    # sort dataframe by score column
    result_df.sort_values(by="score", ascending=False, inplace=True)

    # update the rank column based on sorted scores
    ranked_df = rank(result_df)
    
    return ranked_df


def order_scores_v1(scores: pd.DataFrame) -> pd.DataFrame:
    scores["rank"] = scores["score"].rank(method="dense", ascending=False)
    return scores[["score", "rank"]].sort_values(by="score", ascending=False)