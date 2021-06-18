import json
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import pandas as pd

from DateHistogram import DateHistogram


class DateHistogramUnit(unittest.TestCase):
    def test_constructor__given_simple_csv__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stacked_simple.csv")
        subject = DateHistogram("date", "quantity", df)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {
            "2021-01-01": 40,
            "2021-01-02": 30,
        }
        self.assertEqual(results, expected)

    def test_constructor__given_simple_csv_unique_count__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stacked_unique.csv")
        subject = DateHistogram("date", "aisle", df)
        subject.set_aggregation("unique_count")

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {
            "2021-05-07": 2,
            "2021-05-08": 3,
        }
        self.assertEqual(results, expected)

    def test_constructor__given_dates_spread__then_chart_shows_gaps_in_dates(
        self,
    ):
        # Arrange
        df = pd.read_csv("tests/data/stacked_dates_spread_on_chart.csv")
        subject = DateHistogram("date", "quantity", df)
        subject.set_date_period("%m/%d/%y", "m")

        # Act
        subject.save_plot("temp_unit_DateHistogram_dates_spread.png")


if __name__ == "__main__":
    unittest.main()
