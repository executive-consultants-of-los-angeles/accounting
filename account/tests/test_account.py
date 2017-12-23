"""Tests for the account module."""
from account.account import Account


class TestAccount(object):

    def test_account_object(self, account):
        """Test account fixture object."""
        assert isinstance(account, Account)

    def test_account_name(self, accounts):
        """Make sure an account name contains only characters."""
        for item in accounts:
            account = Account()
            account.name = item.get('name')
            account_name = account.get_name()

            assert isinstance(account.name, str)
            assert isinstance(account_name, str)

    def test_account_type(self, accounts):
        """Account types should be
        [asset, liability, equity, revenue, expense."""
        kinds = ['asset', 'liability', 'equity', 'revenue', 'expense']
        for item in accounts:
            account = Account()
            account.kind = account.kind

        assert isinstance(account.kind, int)
        assert kinds[account.kind] in kinds

    def test_account_number(self):
        """The account number should be an integer."""
        assert False
