"""Module for the account model."""
from django.db import models

from chart.models import Chart

# Create your models here.
class Account(models.Model):
    """Class that defines account objects."""

    name = models.CharField("Name", max_length=255)
    kind = 0
    number = models.IntegerField("Number")
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)

    def account_name(self):
        """Return account name."""
        return self.name

    def account_kind(self):
        """Return the integer value of the account kind."""
        return self.kind

    def account_number(self):
        """Return the account number."""
        return self.number

    def __str__(self):
        """String for repr."""
        return "{} {}".format(self.number, self.name)
