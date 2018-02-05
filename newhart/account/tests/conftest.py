"""Make an Account fixture available."""
import os
import yaml
import pytest

import newhart.loadapps

from account.models import Account
from chart.models import Chart

newhart.loadapps.main()

@pytest.fixture(scope='session')
def chart():
    """Save and return a chart object."""
    path = os.path.join(os.path.dirname(__file__), "../../chart/yml")

    yml_file = open('{}/chart.yml'.format(path), 'r')
    charts_yml = yml_file.read()
    yml_file.close()

    for item in yml_file.safe_load(charts_yml):
        local_chart = Chart(
            name=item.get('name')
        )
        local_chart.save()
    return local_chart

@pytest.fixture(scope='session')
def account():
    """Return an Account object."""
    return Account


@pytest.fixture(scope='function')
def accounts():
    """Define accounts fixture."""
    path = os.path.join(os.path.dirname(__file__), "../yml")

    yml_file = open('{}/account.yml'.format(path), 'r')
    accounts_yml = yml_file.read()
    yml_file.close()

    for item in yaml.safe_load(accounts_yml):
        local_account = Account(
            chart_id=1,
            name=item.get('name'),
            number=item.get('number')
        )
        local_account.save()

    return yaml.safe_load(accounts_yml)
