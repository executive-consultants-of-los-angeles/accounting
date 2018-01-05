"""Tests for the chart module."""
from chart.chart import Chart


class TestChart(object):
    """Test class for chart module."""

    def test_chart_object(self, chart):
        """Test chart fixture object."""
        assert isinstance(chart, Chart)

    def test_chart_name(self, chart):
        """Test the chart's name."""
        chart = Chart()
        chart.name = 'Test Chart'
        chart_name = chart.name
        
        assert isinstance(chart.name, str)
        assert isinstance(chart_name, str)

    def test_chart_related_accounts(self, charts):
        """Test chart assignment of accounts to a side of the equation."""
        chart = Chart()
        chart.accounts = []
        chart_accounts = chart.accounts

        assert False
