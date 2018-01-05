"""Module for the chart of accounts class. (Chart)"""
import os
import yaml


class Chart(object):
    """Class for Chart objects."""

    name = str()
    accounts = list()

    def __init__(self):
        """Initialize a chart of accounts."""
        chart = yaml.load(
            open('{}/chart.yml'.format(
                os.environ.get('YML_PATH')), 'r')
            )[0]
        print(chart)

        self.name = chart.get('name')
        self.accounts = chart.get('accounts')
