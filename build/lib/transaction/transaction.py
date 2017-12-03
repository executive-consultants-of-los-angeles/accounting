import yaml

class Transaction(object):
    """A class for modeling accounting transactions."""

    def __init__(self):
        """Instantiate a Transaction object."""
        return

    def load_yaml(self):
        """Load values for transactions from yaml file."""
        f = open('/srv/accounting/transaction/yml/transaction.yml', 'r')
        d = f.read()
        f.close()
        print(d)
