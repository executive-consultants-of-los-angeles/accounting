"""
.. module:: newhart.transaction.views
   :platform: Unix, Windows
   :synopsis: Views module for transaction app.

.. moduleauthor:: info@gahan-corporation.com

"""
from django.shortcuts import render

# Create your views here.


def index(request):
    """Render the index for transactions.

    :param request: A request sent from Django.
    :type request: :any:`django:django.http.HttpRequest`
    :rtype: :any:`django:django.http.HttpResponse`
    """
    return render(request, 'transaction/index.html')
