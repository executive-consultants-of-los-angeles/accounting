"""Test cases for the transaction class."""
import pytest


class TestTransaction(object):
    """Transaction test cases."""
    def setUp(self):
        """Set up the test object for transactions."""

        return
    
    def test_transaction_class(self):
        """Test that the TransactionClass instantiates."""
        assert False 

    def test_load_from_yml(self):
        """Test that data can be loaded from yaml files."""
        assert False

    def test_transaction_date_format(self):
        """Make sure that dates are formatted correctly."""
        assert False

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
