import json
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import pandas as pd

from StackedHistogram import StackedHistogram


class StackedHistogramUnit(unittest.TestCase):
    def test_constructor__given_simple_csv__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_simple.csv")
        subject = StackedHistogram("category", "item", "quantity", df)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))
        subject.save_plot("temp_unit_StackedHistogram_simple.png")

        # Assert
        expected = {
            "apple": {"fruit": 5.0, "meat": None},
            "chicken": {"fruit": None, "meat": 1.0},
            "pear": {"fruit": 2.0, "meat": None},
            "steak": {"fruit": None, "meat": 5.0},
        }
        self.assertEqual(results, expected)

    def test_constructor__given_simple_csv_horizonal__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_simple.csv")
        subject = StackedHistogram("category", "item", "quantity", df)
        subject.set_chart_type("barh")

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))
        subject.save_plot("temp_unit_StackedHistogram_simple_horizontal.png")

        # Assert
        expected = {
            "apple": {"fruit": 5.0, "meat": None},
            "chicken": {"fruit": None, "meat": 1.0},
            "pear": {"fruit": 2.0, "meat": None},
            "steak": {"fruit": None, "meat": 5.0},
        }
        self.assertEqual(results, expected)

    def test_constructor__given_more_than_max_csv__then_only_max_shown(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = StackedHistogram("category", "item", "quantity", df)
        subject.set_max_groupings(5)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))
        subject.save_plot("temp_unit_StackedHistogram_more_than_max.png")

        # Assert
        expected = {
            "apple": {"candy": None, "fruit": 5.0, "meat": None, "paper": None},
            "chocolate": {"candy": 20.0, "fruit": None, "meat": None, "paper": None},
            "cups": {"candy": None, "fruit": None, "meat": None, "paper": 14.0},
            "plates": {"candy": None, "fruit": None, "meat": None, "paper": 4.0},
            "steak": {"candy": None, "fruit": None, "meat": 5.0, "paper": None},
        }
        self.assertEqual(results, expected)

    def test_constructor__given_unlimited_max__then_all_values_shown(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = StackedHistogram("category", "item", "quantity", df)
        subject.set_max_groupings(0)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))
        subject.save_plot("temp_unit_StackedHistogram_unlimited.png")

        # Assert
        expected = {
            "apple": {
                "baking": None,
                "candy": None,
                "fruit": 5.0,
                "meat": None,
                "paper": None,
                "spices": None,
            },
            "chicken": {
                "baking": None,
                "candy": None,
                "fruit": None,
                "meat": 1.0,
                "paper": None,
                "spices": None,
            },
            "chocolate": {
                "baking": None,
                "candy": 20.0,
                "fruit": None,
                "meat": None,
                "paper": None,
                "spices": None,
            },
            "cups": {
                "baking": None,
                "candy": None,
                "fruit": None,
                "meat": None,
                "paper": 14.0,
                "spices": None,
            },
            "pear": {
                "baking": None,
                "candy": None,
                "fruit": 2.0,
                "meat": None,
                "paper": None,
                "spices": None,
            },
            "plates": {
                "baking": None,
                "candy": None,
                "fruit": None,
                "meat": None,
                "paper": 4.0,
                "spices": None,
            },
            "salt": {
                "baking": None,
                "candy": None,
                "fruit": None,
                "meat": None,
                "paper": None,
                "spices": 4.0,
            },
            "steak": {
                "baking": None,
                "candy": None,
                "fruit": None,
                "meat": 5.0,
                "paper": None,
                "spices": None,
            },
            "sugar": {
                "baking": 3.0,
                "candy": None,
                "fruit": None,
                "meat": None,
                "paper": None,
                "spices": None,
            },
        }
        self.assertEqual(results, expected)

    def test_set_chart_type__given_bar__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = StackedHistogram("category", "item", "quantity", df)

        # Act
        subject.set_chart_type("bar")

        # Assert

    def test_set_chart_type__given_barh__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = StackedHistogram("category", "item", "quantity", df)

        # Act
        subject.set_chart_type("barh")

        # Assert

    def test_set_chart_type__given_xyz__then_assertion(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = StackedHistogram("category", "item", "quantity", df)

        # Act

        # Assert
        with self.assertRaises(AssertionError) as context:
            subject.set_chart_type("xyz")

    def test_set_max_groupings__given_5__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = StackedHistogram("category", "item", "quantity", df)

        # Act
        subject.set_max_groupings(5)

        # Assert

    def test_set_max_groupings__given_0__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = StackedHistogram("category", "item", "quantity", df)

        # Act
        subject.set_max_groupings(0)

        # Assert

    def test_set_max_groupings__given_negative__then_no_error(self):
        # Arrange
        df = pd.read_csv("tests/data/stackedhistogram_more_than_max.csv")
        subject = StackedHistogram("category", "item", "quantity", df)

        # Act

        # Assert
        with self.assertRaises(AssertionError) as context:
            subject.set_max_groupings(-1)


if __name__ == "__main__":
    unittest.main()
