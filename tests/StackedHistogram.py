import json

import pandas as pd


class StackedHistogram:
    def __init__(self, date_column_name, grouping_column, value_column, df):
        self._max_groupings = 5
        self._date_column_name = date_column_name
        self._grouping_column = grouping_column
        self._value_column = value_column
        self._input_df = df
        self._grouped_df = self._group_data()

    def _group_data(self):
        largest_df = (
            self._input_df.groupby([self._grouping_column])[self._value_column]
            .sum()
            .nlargest(self._max_groupings)
            .to_frame()
        )
        largest_categories = largest_df.index.values.tolist()
        print(largest_categories)
        filtered_to_largest = self._input_df[
            self._input_df[self._grouping_column].isin(largest_categories)
        ]
        new_group = filtered_to_largest.groupby(
            [self._date_column_name, self._grouping_column]
        )[self._value_column].sum()
        return new_group

    def to_json(self):
        json_str = self._grouped_df.to_json()
        return json.loads(json_str)
