from pandas import concat, DataFrame

INFLUENCE_CATEGORY = {
    'top 10%': 'high',
    'top 10-50%': 'mid',
    'bottom 50%': 'low'
}


def calculate_influence_category(dataframe):
    influence_category = []
    influence_scores = dataframe['influence_score'].values
    number_of_users = len(influence_scores)
    for influence_score in influence_scores:
        percent_of_user = float(influence_score / number_of_users)
        if percent_of_user >= 0.9:
            influence_category.append(INFLUENCE_CATEGORY['top 10%'])
        elif percent_of_user < 0.9 and percent_of_user > 0.5:
            influence_category.append(INFLUENCE_CATEGORY['top 10-50%'])
        elif percent_of_user <= 0.5:
            influence_category.append(INFLUENCE_CATEGORY['bottom 50%'])
    influence_category_df = DataFrame({'influence_category': influence_category})
    new_df = concat([dataframe, influence_category_df], axis=1)
    print(new_df)
    return new_df
