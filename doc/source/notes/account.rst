========
Accounts
========

Account Notes
=============

What is an account?
-------------------

A collection of related transactions that can be used to describe an aspect of a business.


What the fundamental parts of an account?
-----------------------------------------

Name, number, type, transactions.

.. note:: type

   Type is a reserved word in Python, so we'll use kind instead.


What are the qualities of an account that can be tested?
--------------------------------------------------------

We can test the name for length and composition.

We can test the number for correct placement in the chart of accounts.

We can test the type for its presence in a pre-defined list.

We can test the transactions elsewhere.


Account Modules
===============

.. toctree::

   modules/account

How do we test these qualities?
-------------------------------

Names should contain only letters.

Numbers should contain only numbers.

Types should be one of the following: [asset, liability, equity, revenue, expense].

.. topic:: Equation

   assets = liabilities + equity

   This makes accounts that can reconcile only those of the first three types.


Some thanks due to `smallbusinessdoer.com <http://www.smallbusinessdoer.com/lessons/ae-cheat-sheet-part-4-the-5-main-types-of-accounts/>`_. 
