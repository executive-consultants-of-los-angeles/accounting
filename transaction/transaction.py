"""Module for transaction objects."""
import datetime


class Transaction(object):
    """A class for modeling accounting transactions."""
    amount = float()
    left_account = str()
    right_account = str()
    date = datetime.date
    description = str()
    tid = int()

    def __init__(self):
        """Instantiate a Transaction object."""
        self.amount = float()
        self.left_account = str()
        self.right_account = str()
        self.date = datetime.date
        self.description = str()
        self.tid = int()

    def transaction_amount(self):
        """Return amount for transaction."""
        return self.amount

    def transaction_left_account(self):
        """Return the left (credit) account."""
        return self.left_account

    def transaction_right_account(self):
        """Return the right (debit) account."""
        return self.right_account

    def transaction_description(self):
        """Return the description."""
        return self.description

    def transaction_tid(self):
        """Return the tid."""
        return self.tid
