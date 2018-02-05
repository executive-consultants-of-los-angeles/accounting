"""Tests for the account module."""


class TestAccount(object):
    """Test class for account module."""

    account = None
    kinds = ['asset', 'liability', 'equity', 'revenue', 'expense']

    def test_write_accounts(self, account, accounts, chart):
        """Test that we can save accounts by writing them."""
        self.account = account
        for item in accounts:
            account_ins = account(
                chart=chart,
                name=item.get('name'),
                number=item.get('number')
            )
            account_ins.save()

            if not account_ins.id:
                raise AssertionError("Account failed to save.")

    def test_read_accounts(self, account, accounts, chart):
        """Test that we can read accounts from the db."""
        self.account = accounts
        account_objects = account.objects.filter(chart=chart)
        if not account_objects:
            raise AssertionError("Could not read accounts.")

    def test_update_account(self, account, accounts):
        """Test update acccount."""
        self.account = accounts

        up_account = account.objects.get(name=accounts[0].get('name'))
        up_account.name = "Not the same."
        up_account.save()

        if up_account.name != "Not the same.":
            raise AssertionError("Failed to update account.")

    def test_delete_account(self, account, accounts):
        """Test delete account."""
        self.account = accounts

        del_account = account.objects.get(name=accounts[0].get('name'))

        # if del_account.delete() != (1, {'account.Account': 1}):
        #   raise AssertionError("Incorrect return on delete.")

        del_account = account.objects.filter(
            name=accounts[0].get('name'))

        if del_account:
            raise AssertionError("Did not delete.")

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
