"""
.. module:: newhart.transaction.models
   :platform: Unix, Windows
   :synopsis: Module for the transaction class.

.. moduleauthor:: info@gahan-corporation.com

"""
# pylint: disable=no-member
from django.db import models

from account.models import Account
# Create your models here.


class Transaction(models.Model):
    """Transaction model class.

    .. attribute:: amount

       :description: Amount of the transaction.
       :type: :any:`django:django.db.models.CharField`

    .. attribute:: left_account

       :description: Left (debit) account.
       :type: :any:`django:django.db.models.ForeignKey`

    .. attribute:: right_account

       :description: Right (credit) account.
       :type: :any:`django:django.db.models.ForeignKey`

    .. attribute:: date

       :description: Effective date of the transaction.
       :type: :any:`django:django.db.models.DateField`

    .. attribute: description

       :description: Transaction details.
       :type: :any:`django:django.db.models.TextField`
    """
    amount = models.FloatField("Amount")
    left_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_left"
    )
    right_account = models.ForeignKey(
        Account,
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_right"
    )
    date = models.DateField("Date")
    description = models.TextField("Description")

    def transaction_amount(self):
        """Return amount for transaction."""
        return self.amount

    def transaction_left_account(self):
        """Return the left (credit) account."""
        return self.left_account

    def transaction_right_account(self):
        """Return the right (debit) account."""
        return self.right_account

    def transaction_date(self):
        """Return date of transaction."""
        return self.date

    def transaction_description(self):
        """Return the description."""
        return self.description

    def calculate_balance(self, account):
        """Calculate current balance for an account.

        :param account: The account to create a balance for.
        :return: The calculated balance of the account.
        :rtype: float
        """
        balance = 0
        transactions = Transaction.objects.filter(
            left_account=account)

        for transaction in transactions:
            balance = balance + transaction.amount
            print(transaction.amount)
            print(transaction.left_account)
        print(transactions)
        print(self)
        return balance
