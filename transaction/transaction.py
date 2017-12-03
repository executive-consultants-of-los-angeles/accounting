"""Module for transaction objects."""
import yaml

class Transaction(object):
    """A class for modeling accounting transactions.

    .. attribute:: yml_file

       :description: file containing transactions
    """
    yml_file = ''

    def __init__(self):
        """Instantiate a Transaction object."""
        return

    def load_from_yaml(self):
        """Load values for transactions from yaml file."""
        self.yml_file = open('/srv/accounting/transaction/yml/transaction.yml', 'r')
        transactions_yml = self.yml_file.read()
        self.yml_file.close()
        transactions = yaml.load(transactions_yml)
        print(transactions)
        return transactions
