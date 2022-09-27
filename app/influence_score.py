import pandas as pd

def simple(dataframe):
    influence_score_series = dataframe['user_id'].value_counts()
    df = pd.DataFrame(
        {'user_id': influence_score_series.index.values, 'influence_score': influence_score_series.values})
    print(df)
    return df


def complicated():
    pass
