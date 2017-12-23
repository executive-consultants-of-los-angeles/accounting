"""Make an Account fixture available."""
import os
import yaml
import pytest

from account.account import Account


@pytest.fixture(scope='session')
def account():
    return Account()


@pytest.fixture(scope='session')
def accounts():
    """Define accounts fixture."""
    path = os.environ.get('YML_PATH')

    yml_file = open('{}/account.yml'.format(path), 'r')
    accounts_yml = yml_file.read()
    yml_file.close()

    return yaml.load(accounts_yml)
