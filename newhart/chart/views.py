"""Views module for chart app."""
# pylint: disable=no-member
from django.shortcuts import render

from chart.models import Chart
from account.models import Account
from transaction.models import Transaction

# Create your views here.

def index(request):
    """Render the index page."""

    for account in Account.objects.all():
        transactions = Transaction.objects.filter(left_account=account).first()
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
