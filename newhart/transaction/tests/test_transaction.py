"""Test cases for the transaction class."""
import datetime


class TestTransaction(object):
    """Transaction test cases."""

    accounts = None
    transaction = None

    def test_save_transaction(self, account, transactions, transaction, accounts):
        """Save transactions to the db."""
        self.accounts = accounts
        self.transaction = transaction()
        for item in transactions:
            local_left = account.objects.filter(name=item.get('left_account')).first()
            local_right = account.objects.filter(name=item.get('right_account')).first()
            ltr = transaction.objects.create(
                amount=item.get('amount'),
                date=item.get('date'),
                description=item.get('description'),
                left_account=local_left,
                right_account=local_right
            )
            ltr.save()

            if not ltr.id:
                raise AssertionError("Object was not saved correctly.")

    def test_get_transactions(self, transactions, transaction):
        """Get transaction from the db."""
        self.transaction = transaction.objects.all()

        if not transactions:
            raise AssertionError()

        if not self.transaction:
            raise AssertionError()

    def test_update_transaction(self, transactions, transaction):
        """Update a transaction."""
        self.transaction = transaction.objects.get(
            amount=transactions[0].get('amount'))
        self.transaction.amount = 149281.11
        self.transaction.save()

        if self.transaction.amount != 149281.11:
            raise AssertionError()

    def test_delete_transaction(self, transactions, transaction):
        """Delete a transaction."""
        self.transaction = transaction.objects.get(
            amount=transactions[0].get('amount')).delete()

        if self.transaction != (1, {'transaction.Transaction': 1}):
            raise AssertionError()

        self.transaction = transaction.objects.filter(
            amount=transactions[0].get('amount'))

        if self.transaction:
            raise AssertionError()

    def test_transaction_amount(self, transactions, transaction):
        """Test the amount is a float."""
        self.transaction = transaction()
        for item in transactions:
            self.transaction.amount = item.get('amount')
            amount = self.transaction.transaction_amount()

            if not isinstance(amount, float):
                raise AssertionError()
            if not isinstance(self.transaction.amount, float):
                raise AssertionError()

    def test_transaction_left_account(self, account, transactions, transaction, accounts):
        """Test that the left account exists."""
        self.accounts = accounts
        self.transaction = transaction()
        for item in transactions:
            local_account = account.objects.filter(name=item.get('left_account')).first()
            self.transaction.left_account = local_account
            if self.transaction.left_account != local_account:
                raise AssertionError()
            if not isinstance(item, dict):
                raise AssertionError()

    def test_transaction_right_account(self, account, transactions, transaction, accounts):
        """Test the right account exists."""
        self.accounts = accounts
        self.transaction = transaction()
        for item in transactions:
            local_account = account.objects.filter(name=item.get('right_account')).first()
            self.transaction.right_account = local_account

            if self.transaction.right_account != local_account:
                raise AssertionError()
            if not isinstance(item, dict):
                raise AssertionError()

    def test_transaction_date(self, transactions, transaction):
        """Test that the date is correctly formatted."""
        self.transaction = transaction()
        for item in transactions:
            self.transaction.date = item.get('date')
            t_date = self.transaction.transaction_date()

            if not isinstance(t_date, datetime.date):
                raise AssertionError()
            if not isinstance(self.transaction.date, datetime.date):
                raise AssertionError()

    def test_transaction_description(self, accounts, transactions, transaction):
        """Test the description of the transaction."""
        self.accounts = accounts
        self.transaction = transaction()
        for item in transactions:
            self.transaction.description = item.get('description')
            description = self.transaction.transaction_description()

            if not isinstance(description, str):
                raise AssertionError()
            if not isinstance(self.transaction.description, str):
                raise AssertionError()
            if description != self.transaction.description:
                raise AssertionError()
