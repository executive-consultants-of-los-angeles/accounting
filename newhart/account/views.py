"""
.. module:: newhart.account.views
   :platform: Unix, Windows
   :synopsis: Views module for account app.

.. moduleauthor:: info@gahan-corporation.com

"""
from django.shortcuts import render

# Create your views here.

def index(request):
    """Render the index for the account app.

    :param request: A request from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    :raises: AttributeError, KeyError
    """

    return render(request, 'account/index.html')
