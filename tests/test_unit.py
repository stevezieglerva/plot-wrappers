import json
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import pandas as pd

from StackedHistogram import StackedHistogram


class StackedHistGramUnit(unittest.TestCase):
    def test_constructor__given_df_input__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv("tests/data/stacked_simple.csv")
        subject = StackedHistogram("date", "fruit", "quantity", df)

        # Act
        results = subject.to_json()
        print(json.dumps(results, indent=3))

        # Assert


if __name__ == "__main__":
    unittest.main()
