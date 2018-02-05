"""Fixture for transaction tests."""
import os
import yaml
import pytest

import newhart.loadapps

from account.models import Account
from transaction.models import Transaction

newhart.loadapps.main()


@pytest.fixture(scope='module')
def transaction():
    """Return transaction object."""
    return Transaction


@pytest.fixture(scope='function')
def transactions():
    """Return transactions from file."""
    path = os.path.join(os.path.dirname(__file__), "../yml")

    yml_file = open('{}/transaction.yml'.format(path), 'r')
    transactions_yml = yml_file.read()
    yml_file.close()

    for item in yaml.safe_load(transactions_yml):
        ltr = Transaction(
            amount=item.get('amount'),
            date=item.get('date'),
            description=item.get('description')
        )
        ltr.save()

    return yaml.safe_load(transactions_yml)


@pytest.fixture(scope='session')
def accounts():
    """Define accounts fixture."""
    path = os.path.join(os.path.dirname(__file__), "../../account/yml")

    yml_file = open('{}/account.yml'.format(path), 'r')
    accounts_yml = yml_file.read()
    yml_file.close()

    for item in yaml.safe_load(accounts_yml):
        lay = Account(
            number=item.get('number'),
            name=item.get('name'),
            kind=item.get('kind'),
            chart=1
        )
        lay.save()

    return yaml.safe_load(accounts_yml)
