"""Views module for chart app."""
# pylint: disable=no-member
from django.shortcuts import render

from chart.models import Chart
from account.models import Account

# Create your views here.

def index(request):
    """Render the index page."""
    context = {
        'charts': [
            {'name': Chart.objects.get(pk=1).name,
             'accounts': [account for account in Account.objects.all()]}
        ]
    }

    return render(request, 'chart/index.html', context)
