"""
.. module:: newhart.account.views
   :platform: Unix, Windows
   :synopsis: Views module for account app.

.. moduleauthor:: info@gahan-corporation.com

"""
# pylint: disable=no-member
from django.shortcuts import render

from account.models import Account

# Create your views here.

def index(request):
    """Render the index for the account app.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    :raises: AttributeError, KeyError
    """
    context = {'accounts':Account.objects.all().values()}
    return render(request, 'account/index.html', context=context)

def create_account(self, request):
    """Render the index for the account app.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    :raises: AttributeError, KeyError
    """
    print(self)

    return render(request, 'account/create.html')
