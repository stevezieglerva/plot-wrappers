import json

import pandas as pd


class StackedHistogram:
    def __init__(self, date_column_name, grouping_column, value_column, df):
        self._input_df = df
        self._grouped_df = df.groupby([date_column_name, grouping_column])[
            value_column
        ].sum()
        pass

    def to_json(self):
        json_str = self._grouped_df.to_json()
        return json.loads(json_str)
