"""
.. module:: newhart.account.models
   :platform: Unix, Windows
   :synopsis: Module for the account model.

.. moduleauthor:: info@gahan-corporation.com

"""
# pylint: disable=too-few-public-methods
from django.db import models
from django.forms import ModelForm

from chart.models import Chart

# Create your models here.
class Account(models.Model):
    """Class that defines account objects.

    .. attribute:: name

       :description: The name of the Chart of Accounts being manipulated.
       :type: :any:`django:django.db.models.CharField`

    .. attribute:: kind

       :description: The type of account.
       :type: :any:`django:django.db.models.CharField`

    .. attribute:: number

       :description: Unique account number.
       :type: :any:`django:django.db.models.IntegerField`

    .. attribute:: chart

       :description: Related chart.
       :type: :any:`django:django.db.models.ForeignKey`

    .. attribute:: balance

       :description: Current balance of the account.
       :type: :any:`django:django.db.models.FloatField`
    """
    ACCOUNT_KIND = (
        ('recievable', 'Recievable'),
        ('payable', 'Payable'),
        ('equity', 'Equity'),
        ('revenue', 'Revenue'),
        ('expense', 'Expense')
    )
    name = models.CharField("Name", max_length=255)
    kind = models.CharField('Type', max_length=30, choices=ACCOUNT_KIND)
    number = models.IntegerField("Number")
    chart = models.ForeignKey(Chart, on_delete=models.CASCADE)
    balance = models.FloatField("Balance", default=0)

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


class AccountForm(ModelForm):
    """Class that defines account objects.

    .. attribute:: name

       :description: The name of the Chart of Accounts being manipulated.
       :type: :any:`django:django.db.models.CharField`
    """
    class Meta:
        """Meta class for AccountForm.

        .. attribute:: fields

           :description: List of fields to includet

        .. attribute:: model

           :description: Model this form is about.
        """
        fields = "__all__"
        model = Account
