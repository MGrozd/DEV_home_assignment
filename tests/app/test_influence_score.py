import unittest
from pathlib import Path
from pandas import read_feather, DataFrame, Series
from pandas.testing import assert_frame_equal

from app.influence_score import simple_influence_score, complicated_influence_score


class TestInfluenceCategory(unittest.TestCase):

    def setUp(self) -> None:
        followers_example_file_path = Path(__file__).parent.parent / 'assets' / 'followers_example.feather'
        activity_example_file_path = Path(__file__).parent.parent / 'assets' / 'activity_example.feather'
        self.followers_example_data = read_feather(followers_example_file_path)
        self.activity_example_data = read_feather(activity_example_file_path)
        self.expected_simple_influence_score_data = DataFrame({'user_id': Series(['11', '22', '33', '55']),
                                                               'influence_score': Series([4, 3, 2, 2]),
                                                               })
        self.expected_complicated_influence_score_data = DataFrame({'user_id': Series(['11', '22', '33', '55']),
                                                                    'influence_score': Series([5.0, 2.5, 1.5, 1.0]),
                                                                    })

    def test_simple_influence_score(self):
        assert_frame_equal(simple_influence_score([self.followers_example_data]),
                           self.expected_simple_influence_score_data)

    def test_complicated_influence_score(self):
        assert_frame_equal(complicated_influence_score([self.followers_example_data, self.activity_example_data]),
                           self.expected_complicated_influence_score_data)


if __name__ == '__main__':
    unittest.main()
