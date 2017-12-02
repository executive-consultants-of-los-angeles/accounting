#!/usr/bin/env python
"""Test cases for the transaction class."""


class TransactionTestClass(object):
    """Transaction test cases."""
    
    def test_transaction_class():
        """Test that the TransactionClass instantiates."""
        assert False 

    def test_load_from_yml():
        """Test that data can be loaded from yaml files."""
        assert False

    def test_transaction_date_format():
        """Make sure that dates are formatted correctly."""
        assert False

    def test_transaction_left_account():
        """Ensure that every transaction has a left account value."""
        assert False

    def test_transaction_right_account():
        """Make sure every transction has a right account or None."""
        assert False

    def test_transaction_amount_is_float():
        """All trnsaction amounts should be float precision 3."""
        assert False

    def test_transaction_number():
        """Every transaction needs a unique id."""
        assert False

    def test_transaction_name():
        """Every transaction needs a description."""
        assert False
