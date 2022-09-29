import pandas as pd

SHARED_POST_FACTOR = 0.5
SEEN_FACTOR = 0.5


def simple_influence_score(followers_dataframe):
    influence_score_series = followers_dataframe['user_id'].value_counts()
    influence_score_dataframe = pd.DataFrame(
        {'user_id': influence_score_series.index.values, 'influence_score': influence_score_series.values})
    return influence_score_dataframe


def complicated_influence_score(followers_dataframe, activity_dataframe):
    influencers = followers_dataframe['user_id'].value_counts().index.values
    followers = followers_dataframe['user_id'].value_counts().values
    influencers_followers = {influencers: followers for (influencers, followers) in zip(influencers, followers)}
    influence_score = []

    for influencer in influencers:
        influencer_post_liked_df = activity_dataframe[activity_dataframe['liked_user_id'] == influencer]
        (influencer_post_liked_number, _) = influencer_post_liked_df.shape
        influencer_post_shared_df = activity_dataframe[activity_dataframe['shared_user_id'] == influencer]
        (influencer_post_shared_number, _) = influencer_post_shared_df.shape
        seen_score = influencer_post_liked_number + influencer_post_shared_number
        influencer_shared_post_df = activity_dataframe[(activity_dataframe['post_user_id'] == influencer) &
                                                       (activity_dataframe['shared_post_id'].notna())]
        (influencer_shared_posts_number, _) = influencer_shared_post_df.shape
        influencer_shared_post_score = float(SHARED_POST_FACTOR * influencer_shared_posts_number *
                                             int(influencers_followers[influencer])
                                             )
        can_be_seen_by_followers = int(influencers_followers[influencer]) - seen_score
        if can_be_seen_by_followers < 0:
            can_be_seen_by_followers = 0
        can_be_seen_score = SEEN_FACTOR * (influencer_shared_post_score + influencer_post_shared_number +
                                           can_be_seen_by_followers)
        total_influence_score = seen_score + can_be_seen_score
        influence_score.append(total_influence_score)

    influence_score_series = followers_dataframe['user_id'].value_counts()
    influence_score_dataframe = pd.DataFrame(
        {'user_id': influence_score_series.index.values, 'influence_score': influence_score})
    return influence_score_dataframe
