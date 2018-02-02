"""Module for the chart of accounts class. (Chart)"""
from django.db import models

class Chart(models.Model):
    """Class for Chart objects."""

    name = models.CharField("Chart", max_length=255)

    def assemble_chart(self):
        """This should pull a workable chart from the data."""
        return self.name
