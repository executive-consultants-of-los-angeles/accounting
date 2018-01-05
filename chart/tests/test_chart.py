"""Tests for the chart module."""
from chart.chart import Chart


class TestChart(object):
    """Test class for chart module."""

    chart = Chart

    def test_chart_object(self, chart):
        """Test chart fixture object."""
        assert isinstance(chart, self.chart)

    def test_chart_name(self, chart):
        """Test the chart's name."""
        chart = self.chart()
        chart.name = 'Test Chart'
        chart_name = chart.name

        assert isinstance(chart.name, str)
        assert isinstance(chart_name, str)

    def test_chart_related_accounts(self, chart):
        """Test chart assignment of accounts to a side of the equation."""
        chart = self.chart()
        chart.accounts = []
        chart_accounts = chart.accounts

        assert isinstance(chart.accounts, list)
        assert isinstance(chart_accounts, list)
