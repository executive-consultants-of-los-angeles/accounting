"""
.. module:: newhart.transaction.views
   :platform: Unix, Windows
   :synopsis: Views module for transaction app.

.. moduleauthor:: info@gahan-corporation.com

"""
# pylint: disable=no-member
from django.shortcuts import render
from transaction.models import Transaction

# Create your views here.


def index(request):
    """Render the index for transactions.

    :param request: A request sent from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    """
    context = {
        'transactions': Transaction.objects.all()
    }

    return render(request, 'transaction/transaction.html', context)


def update(request, transaction_id):
    """Render the index for transactions.

    :param request: A request sent from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    """
    return render(request, 'transaction/transaction.html')


def add(request):
    """Render the index for transactions.

    :param request: A request sent from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    """
    return render(request, 'transaction/transaction.html')


def delete(request, transaction_id):
    """Render the index for transactions.

    :param request: A request sent from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    """
    return render(request, 'transaction/transaction.html')
