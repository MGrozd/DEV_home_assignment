import configparser
from pandas import read_feather

from app.influence_score import simple_influence_score, complicated_influence_score
from app.influence_category import calculate_influence_category

CONFIG_FILENAME = 'conf.ini'
TEST_PATH = 'tests/assets/followers_example.feather'


def main():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)
    followers_dataframe = read_feather(TEST_PATH)
    activity_dataframe = read_feather('tests/assets/activity_example.feather')

    simple_influence_dataframe = calculate_influence_category(
        simple_influence_score(followers_dataframe)
    )
    print(simple_influence_dataframe.head())
    simple_influence_dataframe.to_feather('./test.feather')
    complicated_influence_score(followers_dataframe, activity_dataframe)

    complicated_influence_dataframe = calculate_influence_category(
        complicated_influence_score(followers_dataframe, activity_dataframe)
    )
    print(complicated_influence_dataframe.head())
    complicated_influence_dataframe.to_feather('./test_complicated.feather')


if __name__ == '__main__':
    main()
