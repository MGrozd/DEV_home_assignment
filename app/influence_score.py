import pandas as pd

SHARED_POST_FACTOR = 0.5

def simple_influence_score(followers_dataframe):
    influence_score_series = followers_dataframe['user_id'].value_counts()
    influence_score_dataframe = pd.DataFrame(
        {'user_id': influence_score_series.index.values, 'influence_score': influence_score_series.values})
    return influence_score_dataframe


def complicated_influence_score(followers_dataframe, activity_dataframe):
    influencers = followers_dataframe['user_id'].value_counts().index.values
    followers = followers_dataframe['user_id'].value_counts().values
    print(influencers, followers)
    influencers_followers = {influencers: followers for (influencers, followers) in zip(influencers, followers)}
    print(influencers_followers)
    influence_score = []
    for influencer in influencers:
        shared_post_df = activity_dataframe[(activity_dataframe['post_user_id'] == influencer) &
                                            (activity_dataframe['shared_post_id'].notna())]
        (shared_posts_number, _) = shared_post_df.shape
        print(shared_posts_number, 'NUM')
        shared_post_score = float(SHARED_POST_FACTOR * shared_posts_number * int(influencers_followers[influencer]))
        print(shared_post_score)
        influence_score.append(shared_post_score)
    pass
    print(influence_score)

