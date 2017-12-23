"""Test cases for the transaction class."""
import datetime
from transaction.transaction import Transaction


class TestTransaction(object):
    """Transaction test cases."""
    def test_transaction_amount(self, transactions):
        """Test the amount is a float."""
        for item in transactions:
            transaction = Transaction()
            transaction.amount = item.get('amount')
            amount = transaction.transaction_amount()

            assert isinstance(amount, float)
            assert isinstance(transaction.amount, float)

    def test_transaction_left_account(self, transactions, accounts):
        """Test that the left account exists."""
        for item in transactions:
            transaction = Transaction()
            transaction.left_account = item.get('left_account')
            left_account = transaction.transaction_left_account()

            assert isinstance(left_account, str)
            assert left_account in [
                account.get('name') for account in accounts]
            assert transaction.left_account in [
                account.get('name') for account in accounts]
            assert isinstance(item, dict)

    def test_transaction_right_account(self, transactions, accounts):
        """Test the right account exists."""
        for item in transactions:
            transaction = Transaction()
            transaction.right_account = item.get('right_account')
            right_account = transaction.transaction_right_account()

            assert right_account in [
                account.get('name') for account in accounts]
            assert isinstance(right_account, str)
            assert transaction.right_account in [
                account.get('name') for account in accounts]
            assert isinstance(item, dict)

    def test_transaction_date(self, transactions):
        """Test that the date is correctly formatted."""
        for item in transactions:
            transaction = Transaction()
            transaction.date = item.get('date')
            t_date = transaction.transaction_date()

            assert isinstance(t_date, datetime.date)
            assert isinstance(transaction.date, datetime.date)

    def test_transaction_description(self, transactions):
        """Test the description of the transaction."""
        for item in transactions:
            transaction = Transaction()
            transaction.description = item.get('description')
            description = transaction.transaction_description()

            assert isinstance(description, str)
            assert isinstance(transaction.description, str)
            assert description == transaction.description

    def test_transaction_tid(self, transactions):
        """Test that a tid is returned."""
        for item in transactions:
            transaction = Transaction()
            transaction.tid = item.get('tid')
            tid = transaction.transaction_tid()

            assert isinstance(tid, int)
            assert isinstance(transaction.tid, int)
            assert tid == transaction.tid
