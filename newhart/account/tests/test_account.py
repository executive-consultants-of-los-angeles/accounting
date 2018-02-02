"""Tests for the account module."""


class TestAccount(object):
    """Test class for account module."""

    account = None
    kinds = ['asset', 'liability', 'equity', 'revenue', 'expense']

    def test_write_accounts(self, account, accounts):
        """Test that we can save accounts by writing them."""
        self.account = account
        for item in accounts:
            account_ins = account(
                name=item.get('name'),
                number=item.get('number')
            )
            account_ins.save()

    def test_account_name(self, accounts, account):
        """Make sure an account name contains only characters."""
        for item in accounts:
            self.account = account
            account_ins = account()
            account_ins.name = item.get('name')
            account_name = account_ins.account_name()

            if not isinstance(account_ins.name, str):
                raise AssertionError()
            if not isinstance(account_name, str):
                raise AssertionError()

    def test_account_number(self, accounts, account):
        """The account number should be integer."""
        for item in accounts:
            self.account = account
            account_ins = account()
            account_ins.number = item.get('number')
            number = account_ins.account_number()

            if not isinstance(number, int):
                raise AssertionError()
            if not isinstance(account_ins.number, int):
                raise AssertionError()
