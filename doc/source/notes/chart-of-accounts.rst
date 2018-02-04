Chart of Accounts
=================

Definition
----------

This is usually kept as a list the names and numbers of accounts.  

Approach
--------

While that sounds simple, the author has yet to see software that could accomplish this apparently fundamental to accounting task.  Indeed, to my knowledge most accountants (at least in part due to this)  keep at least two sets of books: one in Excel and one in whatever accounting software their employer is using.  The implication here is that so far the best accounting software yet produced is Excel.  Excel does not produce meaningful charts of accounts without more effort than the author is willing to put in.  So, the aim here is to create something that will by default allow easy examination of a company's chart of accounts and the relationships contained therein.

As for the rest of the accounting software currently extant, at least as far as the author has seen, the closest anything comes to what would properly be called a chart is a list of names and numbers that may or may not also provide links to the data contained inside the accounts described.

Testing
-------

.. _`this helpful guide`: http://fishi.devtail.io/weblog/2015/03/02/functional-headless-ui-testing-django-selenium/

The main components of the Chart of Accounts from Newhart's perpsective are all in the user interface and so they require mostly user interface tests.  Because Newhart uses the Django web framework, we can make use of the information in `this helpful guide`_ for setting up basic functional ui tests with Selenium.
