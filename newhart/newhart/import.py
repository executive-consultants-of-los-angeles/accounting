"""Import yml files into db."""
# pylint: disable=no-member
import os
import yaml
import newhart.loadapps

from account.models import Account
from chart.models import Chart

newhart.loadapps.main()


def get_yml_file(directory):
    """Take the directory and return a yml object."""
    path = os.path.join(os.path.dirname(__file__), "../{}/yml".format(directory))

    yml_file = open('{}/{}.yml'.format(path, directory), 'r')
    import_yml = yml_file.read()
    yml_file.close()

    return import_yml

def main():
    """Execute import"""
    chart_yml = get_yml_file('chart')

    for item in yaml.safe_load(chart_yml):
        import_chart = Chart(
            name=item.get('name')
        )
        import_chart.save()

    accounts_yml = get_yml_file('account')

    for item in yaml.safe_load(accounts_yml):
        local_chart = Chart.objects.get(pk=item.get('chart_id'))
        local_account = Account(
            name=item.get('name'),
            number=item.get('number'),
            chart=local_chart
        )
        local_account.save()

    transactions_yml = get_yml_file('transaction')

    for item in yaml.safe_load(transactions_yml):
        local_account = Account.objects.get(pk=item.get('account_id'))
        print(local_account)

main()
