"""Import yml files into db."""
import os
import newhart.loadapps

from account.models import Account

newhart.loadapps.main()


def main():
    """Execute import"""
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

main()
