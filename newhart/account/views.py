"""
.. module:: account.views
   :platform: Unix, Windows
   :synopsis: Views module for account app.

.. moduleauthor:: info@gahan-corporation.com

"""
from django.shortcuts import render

# Create your views here.

def index(request):
    """Render the index for the account app.

    :param request HttpRequest: A request from Django.
    :returns:  HttpResponse
    :raises: AttributeError, KeyError
    """

    return render(request, 'account/index.html')
