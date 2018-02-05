"""
.. module:: newhart.account.views
   :platform: Unix, Windows
   :synopsis: Views module for account app.

.. moduleauthor:: info@gahan-corporation.com
"""
# pylint: disable=no-member,invalid-name
from django.shortcuts import render

from account.models import Account
from account.models import AccountForm

# Create your views here.


def index(request):
    """Render the index for the account app.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    :raises: AttributeError, KeyError
    """
    context = {'accounts': Account.objects.all().order_by('number').values()}
    if request.method == "POST":
        formset = AccountForm(
            request.POST,
        )
        if formset.is_valid():
            formset.save()
    else:
        formset = AccountForm()

    context.update({'formset': formset})
    return render(request, 'account/index.html', context)
