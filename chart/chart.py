"""Module for the chart of accounts class. (Chart)"""
import os
import yaml


class Chart(object):
    """Class for Chart objects."""

    name = str()
    accounts = list()

    def __init__(self):
        """Initialize a chart of accounts."""
        chart = yaml.safe_load(
            open('{}/chart.yml'.format(
                os.environ.get('YML_PATH')), 'r')
            )[0]
        print(chart)

        self.name = chart.get('name')
        self.accounts = chart.get('accounts')

    def assemble_chart(self):
        """This should pull a workable chart from the data."""
        return self.name

    def update_chart(self):
        """Change a relationship in the chart."""
        return self.accounts
