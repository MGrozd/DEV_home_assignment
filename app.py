import configparser
from pandas import read_feather

from app.influence_score import simple

CONFIG_FILENAME = 'conf.ini'
TEST_PATH = './data/followers_example.feather'

def main():
    config = configparser.ConfigParser()
    config.read(CONFIG_FILENAME)
    # df = feather.read_dataframe(TEST_PATH)
    # print(df)
    # print(df['post_id'])
    df = read_feather(TEST_PATH)
    df = simple(df)
    print(df)


if __name__ == '__main__':
    main()
