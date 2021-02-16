import json
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import pandas as pd

from Histogram import Histogram


class HistogramUnit(unittest.TestCase):
    def test_constructor__given_simple_csv__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_simple.csv")
        subject = Histogram("category", "quantity", df)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))
        subject.save_plot("temp_unit_Histogram_simple.png")

        # Assert
        expected = {"fruit": 7, "meat": 6}
        self.assertEqual(results, expected)

    def test_constructor__given_simple_csv_horizonal__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_simple.csv")
        subject = Histogram("category", "quantity", df)
        subject.set_chart_type("barh")

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))
        subject.save_plot("temp_unit_Histogram_simple_horizontal.png")

        # Assert
        expected = {"fruit": 7, "meat": 6}
        self.assertEqual(results, expected)

    def test_constructor__given_more_than_max_csv__then_only_max_shown(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = Histogram("category", "quantity", df)
        subject.set_max_groupings(5)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))
        subject.save_plot("temp_unit_Histogram_more_than_max.png")

        # Assert
        expected = {"candy": 20, "fruit": 7, "meat": 6, "paper": 18, "spices": 4}
        self.assertEqual(results, expected)

    def test_constructor__given_unlimited_max__then_all_values_shown(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = Histogram("category", "quantity", df)
        subject.set_chart_type("bar")
        subject.set_max_groupings(0)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))
        subject.save_plot("temp_unit_Histogram_unlimited.png")

        # Assert
        expected = {
            "baking": 3,
            "candy": 20,
            "fruit": 7,
            "meat": 6,
            "paper": 18,
            "spices": 4,
        }
        self.assertEqual(results, expected)

    def test_set_chart_type__given_bar__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = Histogram("category", "quantity", df)

        # Act
        subject.set_chart_type("bar")

        # Assert

    def test_set_chart_type__given_barh__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = Histogram("category", "quantity", df)

        # Act
        subject.set_chart_type("barh")

        # Assert

    def test_set_chart_type__given_xyz__then_assertion(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = Histogram("category", "quantity", df)

        # Act

        # Assert
        with self.assertRaises(AssertionError) as context:
            subject.set_chart_type("xyz")

    def test_set_max_groupings__given_5__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = Histogram("category", "quantity", df)

        # Act
        subject.set_max_groupings(5)

        # Assert

    def test_set_max_groupings__given_0__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = Histogram("category", "quantity", df)

        # Act
        subject.set_max_groupings(0)

        # Assert

    def test_set_max_groupings__given_negative__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = Histogram("category", "quantity", df)

        # Act

        # Assert
        with self.assertRaises(AssertionError) as context:
            subject.set_max_groupings(-1)


if __name__ == "__main__":
    unittest.main()
