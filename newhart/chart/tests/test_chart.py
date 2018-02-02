"""Tests for the chart module."""
from chart.chart import Chart


class TestChart(object):
    """Test class for chart module."""

    chart = Chart

    def test_chart_object(self, chart):
        """Test chart fixture object."""
        if not isinstance(chart, self.chart):
            raise AssertionError()

    def test_chart_name(self, chart):
        """Test the chart's name."""
        chart = self.chart()
        chart.name = 'Test Chart'
        chart_name = chart.name

        if not isinstance(chart.name, str):
            raise AssertionError()
        if not isinstance(chart_name, str):
            raise AssertionError()

    def test_chart_related_accounts(self, chart):
        """Test chart assignment of accounts to a side of the equation."""
        chart = self.chart()
        chart.accounts = []
        chart_accounts = chart.accounts

        if not isinstance(chart.accounts, list):
            raise AssertionError()
        if not isinstance(chart_accounts, list):
            raise AssertionError()
