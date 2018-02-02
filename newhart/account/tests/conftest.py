"""Make an Account fixture available."""
import os
import yaml
import pytest

from account.models import Account


@pytest.fixture(scope='session')
def account():
    """Return an Account object."""
    return Account


@pytest.fixture(scope='session')
def accounts():
    """Define accounts fixture."""
    path = os.path.join(os.path.dirname(__file__), "../yml")

    yml_file = open('{}/account.yml'.format(path), 'r')
    accounts_yml = yml_file.read()
    yml_file.close()

    for item in yaml.safe_load(accounts_yml):
        local_account = Account(
            name=item.get('name'),
            number=item.get('number')
        )
        local_account.save()

    return yaml.safe_load(accounts_yml)
