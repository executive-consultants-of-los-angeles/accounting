"""Test cases for the transaction class."""
import datetime
import transaction.transaction as transaction


class TestTransaction(object):
    """Transaction test cases.

    .. attribute:: transaction

       :description: Transaction to be tested

    .. attribute:: yml_path

       :description: Absolute path to yml file for import.
    """
    transaction = transaction.Transaction()
    transactions = []
    yml_file = u''

    def setUp(self):
        """Set up the test object for transactions."""
        self.transaction = transaction.Transaction()
        self.yml_file = '/srv/accounting/transaction/yml/transaction.yml'
        self.transactions = self.transaction.load_from_yaml()
        return

    def test_transaction_class(self):
        """Test that the Transaction class instantiates."""
        transaction_type = type(self.transaction)
        assert isinstance(self.transaction, transaction_type)

    def test_load_from_yml(self):
        """Test that data can be loaded from yaml files."""
        transactions = self.transaction.load_from_yaml()
        assert isinstance(transactions, list)

        for item in transactions:
            assert isinstance(item, dict)

    def test_transaction_date_format(self):
        """Make sure that dates are formatted correctly."""
        for item in self.transactions:
            assert isinstance(item.get('date'), datetime.date)

    def test_transaction_left_account(self):
        """Ensure that every transaction has a left account value."""
        assert False

    def test_transaction_right_account(self):
        """Make sure every transction has a right account or None."""
        assert False

    def test_transaction_amount_is_float(self):
        """All trnsaction amounts should be float precision 3."""
        assert False

    def test_transaction_number(self):
        """Every transaction needs a unique id."""
        assert False

    def test_transaction_name(self):
        """Every transaction needs a description."""
        assert False
