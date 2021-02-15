import json
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import pandas as pd

from StackedHistogram import StackedHistogram


class StackedHistGramUnit(unittest.TestCase):
    def test_constructor__given_simple_csv__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stacked_simple.csv")
        subject = StackedHistogram("date", "fruit", "quantity", df)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {
            "('2021-01-01', 'apple')": 35,
            "('2021-01-01', 'pears')": 5,
            "('2021-01-02', 'apple')": 10,
            "('2021-01-02', 'pears')": 20,
        }
        self.assertEqual(results, expected)

    def test_constructor__given_more_than_max_csv__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stacked_more_than_max.csv")
        subject = StackedHistogram("date", "fruit", "quantity", df)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {
            "('2021-01-01', 'apple')": 35,
            "('2021-01-01', 'bananas')": 7,
            "('2021-01-01', 'oranges')": 13,
            "('2021-01-01', 'pears')": 5,
            "('2021-01-01', 'pineapple')": 7,
            "('2021-01-02', 'apple')": 1,
            "('2021-01-02', 'bananas')": 6,
            "('2021-01-02', 'oranges')": 10,
            "('2021-01-02', 'pears')": 9,
            "('2021-01-02', 'pineapple')": 6,
        }
        self.assertEqual(results, expected)


if __name__ == "__main__":
    unittest.main()
