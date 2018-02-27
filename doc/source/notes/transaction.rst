============
Transactions
============

Transaction Modules
===================

.. toctree::

   modules/transaction

Transaction Theory
==================

The aim of this document is to define clearly what an accounting transaction
is in such a way that it can be easily understood by both machines and
humans.

Transaction as the Atom of Accounting
-------------------------------------

If you look at the accounting equation (assets = liabilities - equity) long
enough it will eventually occur to you that accounting as an idea can be
analyzed and dissected into its constituent parts, which parts can then
be further analyzed.  This process begins at the chart of accounts, continues
through the individual accounts and their relationships to the various
reports required at end of period, and finally ends at the transaction.

There is no more fundamental concept than the trnsaction, so it seems
like a reasonable thing to define.  I'll give it a shot: a transaction
is the movement of money from one place to another.  That is to say,
a transaction can be fully defined as requiring the following:
from
to
time
amount
Additionally, a description and various other fields may be associated
with a given transaction but do not necessarily need to be.  In order
for a transaction to have meaning for the purposes of bookkeeping, we might
refer to the same fields as left account, right account, date posted, amount.

This provides all of the required information because only one amount
is required so long as both the left and right accounts are known since
any amount will be either a credit or debit in the left account and that
implies a credit or debit in the right account.

Testing Transactions
--------------------

That's great, but what's this mean for the lowly developer of accounting
software?  Well, it means that an at least not terrible place to start
writing such software would be to write tests that check for the four
required fields of a transaction and perhaps also add a few for the optional
description and so forth.

The way that will be done is to instantiate a Transaction object, which
will then be populated with data imported from a .yml file and that 
data will be used to test that object for the presence of the 
four required bits of information and any required relationships.
