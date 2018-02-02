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
