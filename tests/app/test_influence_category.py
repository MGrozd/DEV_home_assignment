import unittest
from pandas import DataFrame, Series
from pandas.testing import assert_frame_equal

from app.influence_category import calculate_influence_category


class TestInfluenceCategory(unittest.TestCase):

    def setUp(self) -> None:
        self.test_data = DataFrame({'user_id': Series(['11', '22', '33', '55']), 'influence_score': Series([4, 3, 2, 2])})
        self.expected_data = DataFrame({'user_id': Series(['11', '22', '33', '55']),
                                        'influence_score': Series([4, 3, 2, 2]),
                                        'influence_category': Series(['high', 'mid', 'low', 'low'])
                                        })

    def test_calculate_influence_category(self):
        assert_frame_equal(calculate_influence_category(self.test_data), self.expected_data)


if __name__ == '__main__':
    unittest.main()
