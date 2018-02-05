"""Fixture for transaction tests."""
# pylint: disable=no-member
import os
import yaml
import pytest

import newhart.loadapps

from account.models import Account
from transaction.models import Transaction
from chart.models import Chart

newhart.loadapps.main()


@pytest.fixture(scope='function')
def charts():
    """Return inserted charts."""
    path = os.path.join(os.path.dirname(__file__), "../../chart/yml")

    yml_file = open('{}/chart.yml'.format(path), 'r')
    chart_yml = yml_file.read()
    yml_file.close()

    for item in yaml.safe_load(chart_yml):
        local_chart = Chart(
            name=item.get('name')
        )
        local_chart.save()

    return Chart.objects.all().first()

@pytest.fixture(scope='module')
def transaction():
    """Return transaction object."""
    return Transaction

@pytest.fixture(scope='module')
def account():
    """Return account manager."""
    return Account


@pytest.fixture(scope='function')
def transactions():
    """Return transactions from file."""
    path = os.path.join(os.path.dirname(__file__), "../yml")

    yml_file = open('{}/transaction.yml'.format(path), 'r')
    transactions_yml = yml_file.read()
    yml_file.close()

    accounts()

    for item in yaml.safe_load(transactions_yml):
        left_account = Account.objects.filter(
            name=item.get('left_account')).first()
        right_account = Account.objects.filter(
            name=item.get('right_account')).first()
        ltr = Transaction(
            amount=item.get('amount'),
            date=item.get('date'),
            description=item.get('description'),
            left_account=left_account,
            right_account=right_account
        )
        ltr.save()

    return yaml.safe_load(transactions_yml)


@pytest.fixture(scope='function')
def accounts():
    """Define accounts fixture."""
    path = os.path.join(os.path.dirname(__file__), "../../account/yml")

    yml_file = open('{}/account.yml'.format(path), 'r')
    accounts_yml = yml_file.read()
    yml_file.close()

    charts()

    local_chart = Chart.objects.all().first()

    for item in yaml.safe_load(accounts_yml):
        lay = Account(
            number=item.get('number'),
            name=item.get('name'),
            kind=item.get('kind'),
            chart=local_chart,
        )
        lay.save()

    return yaml.safe_load(accounts_yml)
