"""Tests for the account module."""
from account.account import Account


class TestAccount(object):
    """Test class for account module."""

    account = Account
    kinds = ['asset', 'liability', 'equity', 'revenue', 'expense']

    def test_account_object(self, account):
        """Test account fixture object."""
        if not isinstance(account, self.account):
            raise AssertionError()

    def test_account_name(self, accounts):
        """Make sure an account name contains only characters."""
        for item in accounts:
            account = self.account()
            account.name = item.get('name')
            account_name = account.account_name()

            if not isinstance(account.name, str):
                raise AssertionError()
            if not isinstance(account_name, str):
                raise AssertionError()

    def test_account_type(self, accounts):
        """Test account types."""
        for account in accounts:
            account_obj = self.account()
            kind = account_obj.account_kind()
            account_obj.kind = account.get('kind')

            if not isinstance(kind, int):
                raise AssertionError()
            if not self.kinds[kind] in self.kinds:
                raise AssertionError()

    def test_account_number(self, accounts):
        """The account number should be integer."""
        for item in accounts:
            account = self.account()
            account.number = item.get('number')
            number = account.account_number()

            if not isinstance(number, int):
                raise AssertionError()
            if not isinstance(account.number, int):
                raise AssertionError()
