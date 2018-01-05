"""This code handles accounts."""


class Account(object):
    """Class that defines account objects."""

    name = ''
    kind = 0
    number = 0

    def __init__(self):
        """Initialize account object."""
        self.name = str()
        self.kind = int()
        self.number = int()

    def account_name(self):
        """Return account name."""
        return self.name

    def account_kind(self):
        """Return the integer value of the account kind."""
        return self.kind

    def account_number(self):
        """Return the account number."""
        return self.number
