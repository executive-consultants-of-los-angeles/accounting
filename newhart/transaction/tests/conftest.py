"""Fixture for transaction tests."""
import os
import yaml
import pytest

import newhart.loadapps

from transaction.models import Transaction

newhart.loadapps.main()


@pytest.fixture(scope='session')
def transaction():
    """Return transaction object."""
    return Transaction()


@pytest.fixture(scope='session')
def transactions():
    """Return transactions from file."""
    path = os.path.join(os.path.dirname(__file__), "../yml")

    yml_file = open('{}/transaction.yml'.format(path), 'r')
    transactions_yml = yml_file.read()
    yml_file.close()

    return yaml.safe_load(transactions_yml)


@pytest.fixture(scope='session')
def accounts():
    """Define accounts fixture."""
    path = os.path.join(os.path.dirname(__file__), "../../../yml")

    yml_file = open('{}/account.yml'.format(path), 'r')
    accounts_yml = yml_file.read()
    yml_file.close()

    return yaml.safe_load(accounts_yml)
