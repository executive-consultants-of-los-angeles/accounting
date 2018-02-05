"""
.. module:: newhart.account.views
   :platform: Unix, Windows
   :synopsis: Tests for the account module's views.

.. moduleauthor:: info@gahan-corporation.com
"""
from django.test import Client


class TestAccountViews(object):
    """Test class for account module views."""

    #: Client instance for testing requests.
    client = Client()
    chart = None
    kinds = ['asset', 'liability', 'equity', 'revenue', 'expense']

    def test_get_index(self):
        """Get the index for testing.

        :return: :any:`django:django.http.HttpResponse`
        :raises: :any:`AttributeError`
        """
        response = self.client.get('/')
        if response.status_code != 200:
            raise AssertionError("Other than 200 status code.")

        return response

    def test_post_values(self):
        """Post values to the index."""
        response = self.client.get('/')
        if response.status_code != 200:
            raise AssertionError()
