"""
.. module:: newhart.chart.views
   :platform: Unix, Windows
   :synopsis: Views module for chart app.

.. moduleauthor:: info@gahan-corporation.com

"""
# pylint: disable=no-member
from django.shortcuts import render

from chart.models import Chart
from account.models import Account
from transaction.models import Transaction

# Create your views here.


def index(request):
    """Render the index for the Chart of Accounts.

    :param request: A request sent from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    """
    for account in Account.objects.distinct():
        print(account)
        transactions = Transaction.objects.filter(left_account=account).first()
        print(transactions)
        account.balance = transactions.calculate_balance(account)
        account.save()

    assets = (
        Account.objects.get(name='Accounts Receivable').balance +
        Account.objects.get(name='Revenue').balance
    )

    liabilities = (
        Account.objects.get(name='Accounts Payable').balance +
        Account.objects.get(name='Expenses').balance
    )

    equity = Account.objects.get(name='Equity').balance

    context = {
        'charts': [
            {
                'name': Chart.objects.get(pk=1).name,
                'accounts': [account for account in Account.objects.all()],
                'equation': {
                    'assets': assets,
                    'liabilities': liabilities,
                    'equity': equity
                }
            }
        ]
    }

    return render(request, 'chart/index.html', context)
