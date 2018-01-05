"""Make an Account fixture available."""
import os
import yaml
import pytest

from chart.chart import Chart 


@pytest.fixture(scope='session')
def chart():
    return Chart()


@pytest.fixture(scope='session')
def charts():
    """Define accounts fixture."""
    path = os.environ.get('YML_PATH')

    yml_file = open('{}/chart.yml'.format(path), 'r')
    chart_yml = yml_file.read()
    yml_file.close()

    return yaml.load(chart_yml)
