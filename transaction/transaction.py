"""Module for transaction objects."""
import os
import yaml


class Transaction(object):
    """A class for modeling accounting transactions.

    .. attribute:: yml_file

       :description: file containing transactions

    .. attribute:: yml_file_path

       :description: path to yaml file
    """
    yml_file = ''
    yml_file_path = ''

    def __init__(self):
        """Instantiate a Transaction object."""
        self.yml_file_path = (
            "{yml_file_path}/transaction.yml"
        ).format(yml_file_path=os.environ.get('YML_PATH'))
        return

    def load_from_yaml(self):
        """Load values for transactions from yaml file."""
        self.yml_file = open(self.yml_file_path, 'r')
        transactions_yml = self.yml_file.read()
        self.yml_file.close()
        transactions = yaml.load(transactions_yml)
        print(transactions)
        return transactions
