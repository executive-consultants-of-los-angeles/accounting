import yaml

class Transaction(object):
    """A class for modeling accounting transactions."""

    def __init__(self):
        return

    def load_yaml(self):
        f = open('/srv/accounting/transaction/yml/transaction.yml', 'r')
        d = f.read()
        f.close()
        print(d)
