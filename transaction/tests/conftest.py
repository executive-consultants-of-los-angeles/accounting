"""Fixture for transaction tests."""
import os
import yaml
import pytest

from transaction.transaction import Transaction


@pytest.fixture(scope='session')
def transaction():
    return Transaction()


@pytest.fixture(scope='session')
def transactions():
    path = os.environ.get('YML_PATH')

    yml_file = open('{}/transaction.yml'.format(path), 'r')
    transactions_yml = yml_file.read()
    yml_file.close()

    return yaml.load(transactions_yml)


@pytest.fixture(scope='session')
def accounts():
    """Define accounts fixture."""
    path = os.environ.get('YML_PATH')

    yml_file = open('{}/account.yml'.format(path), 'r')
    accounts_yml = yml_file.read()
    yml_file.close()

    return yaml.load(accounts_yml)
