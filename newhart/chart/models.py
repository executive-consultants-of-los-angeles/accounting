"""
.. module:: chart.views
   :platform: Unix, Windows
   :synopsis: Module for the chart of accounts class. (Chart)

.. moduleauthor:: info@gahan-corporation.com

"""
# pylint: disable=no-member
from django.db import models

class Chart(models.Model):
    """Class for Chart objects.

    .. attribute:: name

       :description: The name of the Chart of Accounts being manipulated.
       :type: :obj:`django.db.models.Model`
    """

    name = models.CharField("Chart", max_length=255)

    def assemble_chart(self):
        """This should pull a workable chart from the data."""
        return self.name
