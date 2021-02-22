import json
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import pandas as pd

from StackedDateHistogram import StackedDateHistogram


class StackedHistogramUnit(unittest.TestCase):
    def test_constructor__given_simple_csv__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stacked_simple.csv")
        subject = StackedDateHistogram("date", "fruit", "quantity", df)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {
            "apple": {"2021-01-01": 35, "2021-01-02": 10},
            "pears": {"2021-01-01": 5, "2021-01-02": 20},
        }
        self.assertEqual(results, expected)

    def test_constructor__given_different_date_format_csv_month__then_json_is_correct(
        self,
    ):
        # Arrange
        df = pd.read_csv("tests/data/stacked_different_date.csv")
        subject = StackedDateHistogram("date", "fruit", "quantity", df)
        subject.set_date_period("%m/%d/%y", "M")

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {"apple": {"2021-01": 45}, "pears": {"2021-01": 25}}
        self.assertEqual(results, expected)

    def test_constructor__given_different_date_format_csv_year__then_json_is_correct(
        self,
    ):
        # Arrange
        df = pd.read_csv("tests/data/stacked_different_date.csv")
        subject = StackedDateHistogram("date", "fruit", "quantity", df)
        subject.set_date_period("%m/%d/%y", "Y")

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {"apple": {"2021": 45}, "pears": {"2021": 25}}
        self.assertEqual(results, expected)

    def test_constructor__given_dates_spread__then_chart_shows_gaps_in_dates(
        self,
    ):
        # Arrange
        df = pd.read_csv("tests/data/stacked_dates_spread_on_chart.csv")
        subject = StackedDateHistogram("date", "fruit", "quantity", df)
        subject.set_date_period("%m/%d/%y", "m")

        # Act
        subject.save_plot("temp_unit_StackedDateHistogram_dates_spread.png")

    def test_constructor__given_more_than_max_csv__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stacked_more_than_max.csv")
        subject = StackedDateHistogram("date", "fruit", "quantity", df)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {
            "apple": {"2021-01-01": 35, "2021-01-02": 1},
            "bananas": {"2021-01-01": 7, "2021-01-02": 6},
            "oranges": {"2021-01-01": 13, "2021-01-02": 10},
            "pears": {"2021-01-01": 5, "2021-01-02": 9},
            "pineapple": {"2021-01-01": 7, "2021-01-02": 6},
        }
        self.assertEqual(results, expected)
        subject.save_plot("temp.png")

    def test_constructor__given_larger_grouping__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stacked_more_than_max.csv")
        subject = StackedDateHistogram("date", "fruit", "quantity", df)
        subject.set_max_groupings(10)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert
        expected = {
            "apple": {"2021-01-01": 35, "2021-01-02": 1},
            "bananas": {"2021-01-01": 7, "2021-01-02": 6},
            "grapes": {"2021-01-01": 7, "2021-01-02": 5},
            "oranges": {"2021-01-01": 13, "2021-01-02": 10},
            "pears": {"2021-01-01": 5, "2021-01-02": 9},
            "pineapple": {"2021-01-01": 7, "2021-01-02": 6},
        }
        self.assertEqual(results, expected)
        subject.save_plot("temp.png")


if __name__ == "__main__":
    unittest.main()
