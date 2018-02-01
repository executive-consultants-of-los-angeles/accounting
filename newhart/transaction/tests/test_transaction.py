"""Test cases for the transaction class."""
import datetime

from transaction.transaction import Transaction


class TestTransaction(object):
    """Transaction test cases."""

    transaction = Transaction

    def test_transaction_amount(self, transactions):
        """Test the amount is a float."""
        for item in transactions:
            transaction = self.transaction()
            transaction.amount = item.get('amount')
            amount = transaction.transaction_amount()

            if not isinstance(amount, float):
                raise AssertionError()
            if not isinstance(transaction.amount, float):
                raise AssertionError()

    def test_transaction_left_account(self, transactions, accounts):
        """Test that the left account exists."""
        for item in transactions:
            transaction = self.transaction()
            transaction.left_account = item.get('left_account')
            left_account = transaction.transaction_left_account()
            if not isinstance(left_account, str):
                raise AssertionError()
            if left_account not in [
                    account.get('name') for account in accounts]:
                raise AssertionError()
            if transaction.left_account not in [
                    account.get('name') for account in accounts]:
                raise AssertionError()
            if not isinstance(item, dict):
                raise AssertionError()

    def test_transaction_right_account(self, transactions, accounts):
        """Test the right account exists."""
        for item in transactions:
            transaction = self.transaction()
            transaction.right_account = item.get('right_account')
            right_account = transaction.transaction_right_account()

            if right_account not in [
                    account.get('name') for account in accounts]:
                raise AssertionError()
            if not isinstance(right_account, str):
                raise AssertionError()
            if transaction.right_account not in [
                    account.get('name') for account in accounts]:
                raise AssertionError()
            if not isinstance(item, dict):
                raise AssertionError()

    def test_transaction_date(self, transactions):
        """Test that the date is correctly formatted."""
        for item in transactions:
            transaction = self.transaction()
            transaction.date = item.get('date')
            t_date = transaction.transaction_date()

            if not isinstance(t_date, datetime.date):
                raise AssertionError()
            if not isinstance(transaction.date, datetime.date):
                raise AssertionError()

    def test_transaction_description(self, transactions):
        """Test the description of the transaction."""
        for item in transactions:
            transaction = self.transaction()
            transaction.description = item.get('description')
            description = transaction.transaction_description()

            if not isinstance(description, str):
                raise AssertionError()
            if not isinstance(transaction.description, str):
                raise AssertionError()
            if description != transaction.description:
                raise AssertionError()

    def test_transaction_tid(self, transactions):
        """Test that a tid is returned."""
        for item in transactions:
            transaction = self.transaction()
            transaction.tid = item.get('tid')
            tid = transaction.transaction_tid()

            if not isinstance(tid, int):
                raise AssertionError()
            if not isinstance(transaction.tid, int):
                raise AssertionError()
            if tid != transaction.tid:
                raise AssertionError()
