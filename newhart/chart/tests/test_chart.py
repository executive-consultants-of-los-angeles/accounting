"""Tests for the chart module."""


class TestAccount(object):
    """Test class for chart module."""

    chart = None

    def test_write_charts(self, chart, charts):
        """Test that we can save charts by writing them."""
        self.chart = chart
        for item in charts:
            chart_ins = chart(
                name=item.get('name'),
            )
            chart_ins.save()

            if not chart_ins.id:
                raise AssertionError("Account failed to save.")

    def test_read_charts(self, chart, charts):
        """Test that we can read charts from the db."""
        self.chart = charts
        chart_objects = chart.objects.all()
        if not chart_objects:
            raise AssertionError("Could not read charts.")

    def test_update_chart(self, chart, charts):
        """Test update acccount."""
        self.chart = charts

        up_chart = chart.objects.get(name=charts[0].get('name'))
        up_chart.name = "Not the same."
        up_chart.save()

        if up_chart.name != "Not the same.":
            raise AssertionError("Failed to update chart.")

    def test_delete_chart(self, chart, charts):
        """Test delete chart."""
        self.chart = charts

        del_chart = chart.objects.get(name=charts[0].get('name'))

        if del_chart.delete() != (1, {'chart.Chart': 1}):
            raise AssertionError("Incorrect return on delete.")

        del_chart = chart.objects.filter(
            name=charts[0].get('name'))

        if del_chart:
            raise AssertionError("Did not delete.")
