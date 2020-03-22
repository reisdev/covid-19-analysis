import pandas as pd
import numpy as np
from datetime import datetime, timedelta


class COVID:
    DATE = "date"
    LOCATION = "location"
    NEW_CASES = "new_cases"
    NEW_DEATHS = "new_deaths"
    TOTAL_CASES = "total_cases"
    TOTAL_DEATHS = "total_deaths"

    def __init__(self):
        self.data = pd.read_csv("https://covid.ourworldindata.org/data/ecdc/full_data.csv",
                                delimiter=",", header=0, parse_dates=[self.DATE])

    def by_location(self, *argv):
        if(not argv):
            argv = ["World"]
        return self.data.loc[self.data[self.LOCATION].isin(argv)]

    def from_date(self, date, *argv):
        if(not argv):
            argv = ["World"]
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
        mask = (self.data[self.DATE] >=
                parsed_date) & self.data[self.LOCATION].isin(argv)
        data = self.data[mask]
        data.reset_index(inplace=True)
        data = data.drop(["index"], axis=1)
        if(len(argv) == 1):
            data = data.drop(["location"], axis=1)
        return data

    def plot_total_deaths(self, *argv):
        if(not argv):
            argv = ["World"]
        mask = (
            self.data[self.LOCATION].isin(argv)) & (self.data[self.TOTAL_DEATHS] > 0)
        data = self.data.loc[mask]
        data = data.pivot(index=self.DATE, columns=self.LOCATION,
                          values=self.TOTAL_DEATHS)
        chart = data.plot(kind="line", title="Total Deaths")
        chart.set_xlabel("Date")
        chart.set_ylabel("Total Deaths")
        return chart

    def plot_total_cases(self, *argv):
        if(not argv):
            argv = ["World"]
        mask = (self.data[self.LOCATION].isin(argv)) & (
            self.data[self.TOTAL_CASES] > 0)
        data = self.data.loc[mask]
        data = data.pivot(index=self.DATE, columns=self.LOCATION,
                          values=self.TOTAL_CASES)
        chart = data.plot(kind="line", title="Total cases")
        chart.set_xlabel("Date")
        chart.set_ylabel("Total Cases")
        return chart

    def get_status(self, *argv):
        if(not argv):
            argv = ["World"]
        mask = (self.data[self.LOCATION].isin(argv))
        data = self.data.loc[mask]
        data = data[data[self.DATE] == max(data[self.DATE])]
        data = data.drop([self.DATE], axis=1)
        data.reset_index(inplace=True)
        data = data.drop(["index"], axis=1)
        return data
