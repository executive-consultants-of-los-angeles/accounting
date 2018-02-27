"""
.. module:: newhart.account.views
   :platform: Unix, Windows
   :synopsis: Views module for account app.

.. moduleauthor:: info@gahan-corporation.com
"""
# pylint: disable=no-member,invalid-name
from django.shortcuts import render
from django.shortcuts import redirect

from account.models import Account

# Create your views here.


def index(request, account_id=0):
    """Render the index for the account app.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    :raises: AttributeError, KeyError
    """
    context = {'accounts': Account.objects.all().order_by('number').values()}

    if account_id:
        context.update({
            'edit_account': Account.objects.filter(id=account_id).values()[0]
        })

    return render(request, 'account/account.html', context)


def update(request, account_id):
    """Update an account then return the original view.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    """
    Account.objects.filter(id=account_id).delete()
    print(request)

    return redirect('accounts_list')


def delete(request, account_id):
    """Delete an account and all related data.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    """
    Account.objects.filter(id=account_id).delete()
    print(request)

    return redirect('accounts_list')
