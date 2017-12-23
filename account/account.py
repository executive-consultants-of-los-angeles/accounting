"""This code handles accounts."""


class Account(object):
    """Class that defines account objects."""
    name = ''
    kind = 0
    number = 0

    def __init__(self):
        self.name = str()
        self.kind = int()
        self.number = int()

    def account_name(self):
        """Returns the name of the current account object."""
        return self.name

    def account_kind(self):
        """Returns the integer value of the account kind."""
        return self.kind

    def account_number(self):
        """Returns the account number."""
        return self.number
