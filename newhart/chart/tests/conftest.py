"""Make an Account fixture available."""
import os
import yaml
import pytest

from chart.chart import Chart


@pytest.fixture(scope='session')
def chart():
    """Return a chart object."""
    return Chart()


@pytest.fixture(scope='session')
def charts():
    """Define accounts fixture."""
    path = os.environ.get('YML_PATH')

    yml_file = open('{}/chart.yml'.format(path), 'r')
    chart_yml = yml_file.read()
    yml_file.close()

    return yaml.safe_load(chart_yml)
