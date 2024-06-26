import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    valid_tweet_mask = tweets["content"].str.len() > 15
    return tweets[valid_tweet_mask][["tweet_id"]]