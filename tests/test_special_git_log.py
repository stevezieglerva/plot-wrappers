import json
import unittest
from unittest.mock import MagicMock, Mock, PropertyMock, patch

import pandas as pd

from StackedHistogram import StackedHistogram


class GitLogUnit(unittest.TestCase):
    def test_constructor__given_gov_uk__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv(
            "/Users/sziegler/Documents/Github/git-log-to-csv/samples/govuk.csv"
        )
        # commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
        # ce783c7,1576172319,2019-12-12T12:38:39,2019-12-12,2019,12,12,"Steve Ziegler",.gitignore,3,,,,

        df["new_date"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.to_period("M")

        filtered = df
        print(filtered)
        subject = StackedHistogram(
            "new_date",
            "dir_1",
            "churn_count",
            filtered,
        )
        subject.set_aggregation("count")

        filename = "temp_git_log_dir_1_govuk.png"
        subject.save_plot(filename)

    def test_constructor__given_gov_uk__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv(
            "/Users/sziegler/Documents/Github/git-log-to-csv/samples/govuk.csv"
        )
        # commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
        # ce783c7,1576172319,2019-12-12T12:38:39,2019-12-12,2019,12,12,"Steve Ziegler",.gitignore,3,,,,

        df["new_date"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.to_period("M")
        df["two_dirs"] = df["dir_1"] + "/" + df["dir_2"]

        filtered = df
        print(filtered)
        subject = StackedHistogram(
            "new_date",
            "two_dirs",
            "churn_count",
            filtered,
        )
        subject.set_aggregation("count")

        filename = "temp_git_log_two_dirs_govuk.png"
        subject.save_plot(filename)

    def test_constructor__given_ops_aws__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv(
            "/Users/sziegler/Documents/Github/git-log-to-csv/samples/ops_aws_git_log.csv"
        )
        # commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
        # ce783c7,1576172319,2019-12-12T12:38:39,2019-12-12,2019,12,12,"Steve Ziegler",.gitignore,3,,,,

        df["new_date"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.to_period("M")
        df["two_dirs"] = df["dir_1"] + "/" + df["dir_2"]

        filtered = df[df["dir_1"] != "useful_scripts"]
        print(filtered)
        subject = StackedHistogram(
            "new_date",
            "two_dirs",
            "churn_count",
            filtered,
        )
        subject.set_aggregation("count")

        filename = "temp_git_log_ops_aws.png"
        subject.save_plot(filename)

    def test_constructor__given_forem__count_then_json_is_correct(self):
        # Arrange
        df = pd.read_csv(
            "/Users/sziegler/Documents/Github/git-log-to-csv/forem_git_log.csv"
        )
        # commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
        # ce783c7,1576172319,2019-12-12T12:38:39,2019-12-12,2019,12,12,"Steve Ziegler",.gitignore,3,,,,

        df["new_date"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.to_period("M")
        df["two_dirs"] = df["dir_1"] + "/" + df["dir_2"]

        filtered = df
        print(filtered)
        subject = StackedHistogram(
            "new_date",
            "two_dirs",
            "churn_count",
            filtered,
        )
        subject.set_aggregation("count")

        filename = "temp_git_log_forem_count.png"
        subject.save_plot(filename)

    def test_constructor__given_forem_author__count_then_json_is_correct(self):
        # Arrange
        df = pd.read_csv(
            "/Users/sziegler/Documents/Github/git-log-to-csv/forem_git_log.csv"
        )
        # commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
        # ce783c7,1576172319,2019-12-12T12:38:39,2019-12-12,2019,12,12,"Steve Ziegler",.gitignore,3,,,,

        df["new_date"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.to_period("M")

        filtered = df
        print(filtered)
        subject = StackedHistogram(
            "new_date",
            "author",
            "churn_count",
            filtered,
        )
        subject.set_aggregation("count")

        filename = "temp_git_log_forem_author.png"
        subject.save_plot(filename)

    def test_constructor__given_forem_sum__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv(
            "/Users/sziegler/Documents/Github/git-log-to-csv/forem_git_log.csv"
        )
        # commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
        # ce783c7,1576172319,2019-12-12T12:38:39,2019-12-12,2019,12,12,"Steve Ziegler",.gitignore,3,,,,

        df["new_date"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.to_period("M")
        df["two_dirs"] = df["dir_1"] + "/" + df["dir_2"]

        filtered = df
        print(filtered)
        subject = StackedHistogram(
            "new_date",
            "two_dirs",
            "churn_count",
            filtered,
        )

        filename = "temp_git_log_forem_sum.png"
        subject.save_plot(filename)

    def test_constructor__given_react__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv(
            "/Users/sziegler/Documents/Github/git-log-to-csv/samples/react.csv"
        )
        # commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
        # ce783c7,1576172319,2019-12-12T12:38:39,2019-12-12,2019,12,12,"Steve Ziegler",.gitignore,3,,,,

        df["new_date"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.to_period("M")
        df["two_dirs"] = df["dir_1"] + "/" + df["dir_2"]

        filtered = df
        print(filtered)
        subject = StackedHistogram(
            "new_date",
            "two_dirs",
            "churn_count",
            filtered,
        )
        subject.set_aggregation("count")

        filename = "temp_git_log_react.png"
        subject.save_plot(filename)

    def test_constructor__given_cw_api__then_json_is_correct(self):
        # Arrange
        df = pd.read_csv(
            "/Users/sziegler/Documents/Github/git-log-to-csv/cw_api_git_log.csv"
        )
        # commit_hash,epoch,timestamp,date,year,month,day,author,file,churn_count,dir_1,dir_2,dir_3,dir_4
        # ce783c7,1576172319,2019-12-12T12:38:39,2019-12-12,2019,12,12,"Steve Ziegler",.gitignore,3,,,,

        df["new_date"] = pd.to_datetime(df["date"], format="%Y-%m-%d").dt.to_period("M")
        df["two_dirs"] = df["dir_1"] + "/" + df["dir_2"]

        filtered = df
        print(filtered)
        subject = StackedHistogram(
            "new_date",
            "two_dirs",
            "churn_count",
            filtered,
        )
        subject.set_aggregation("count")

        filename = "temp_git_log_cw_api.png"
        subject.save_plot(filename)


if __name__ == "__main__":
    unittest.main()
