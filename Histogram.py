import json

import pandas as pd
import matplotlib.pyplot as plt


class StackedHistogram:
    def __init__(
        self,
        primary_secondary_grouping_column,
        secondary_grouping_column,
        value_column,
        df,
    ):
        self._max_groupings = 5
        self._primary_secondary_grouping_column = primary_secondary_grouping_column
        self._secondary_grouping_column = secondary_grouping_column
        self._value_column = value_column
        self._aggregation = "sum"
        self._chart_type = "bar"
        self._input_df = df
        plt.style.use("seaborn")

        # plt.show()

    def set_max_groupings(self, max_groupings):
        assert max_groupings >= 0, "max_groupings must be greater or equal to zero"
        self._max_groupings = max_groupings

    def set_aggregation(self, aggregation):
        possible_values = ["sum", "count"]
        assert (
            aggregation in possible_values
        ), f"aggregation must be one of: {possible_values}"
        self._aggregation = aggregation

    def set_chart_type(self, chart_type):
        possible_values = ["bar", "barh"]
        assert (
            chart_type in possible_values
        ), f"chart_type must be one of: {possible_values}"
        self._chart_type = chart_type

    def _group_data(self):
        print(f"prepping: {self._max_groupings}")
        prepped_df = self._input_df
        if self._max_groupings != 0:
            print("filtering")
            prepped_df = self._filter_to_largest_groupings()

        if self._aggregation == "sum":
            new_group = prepped_df.groupby(
                [
                    self._primary_secondary_grouping_column,
                    self._secondary_grouping_column,
                ]
            )[self._value_column].sum()
        if self._aggregation == "count":
            new_group = prepped_df.groupby(
                [
                    self._primary_secondary_grouping_column,
                    self._secondary_grouping_column,
                ]
            )[self._value_column].count()
        return new_group

    def _filter_to_largest_groupings(self):
        largest_df = (
            self._input_df.groupby([self._secondary_grouping_column])[
                self._value_column
            ]
            .sum()
            .nlargest(self._max_groupings)
            .to_frame()
        )
        largest_categories = largest_df.index.values.tolist()
        # print(largest_categories)
        filtered_to_largest = self._input_df[
            self._input_df[self._secondary_grouping_column].isin(largest_categories)
        ]
        return filtered_to_largest

    def to_json(self):
        self._grouped_df = self._group_data().unstack()
        json_str = self._grouped_df.to_json()
        json_dict = json.loads(json_str)
        return json_dict

    def save_plot(self, filename):
        self._grouped_df = self._group_data().unstack()
        self._grouped_df.plot(kind=self._chart_type, stacked=True)
        plt.savefig(filename)
