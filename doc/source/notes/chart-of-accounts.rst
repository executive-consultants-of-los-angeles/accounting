Chart of Accounts
=================

Definition
----------

Theoretically at least this is meant to be a chart that displays in a meaninful way all of the accounts contained in a company's books.

Approach
--------

While that sounds simple, the author has yet to see software that could accomplish this apparently fundamental to accounting task.  Indeed, to my knowledge most accountants (at least in part due to this)  keep at least two sets of books: one in Excel and one in whatever accounting software their employer is using.  The implication here is that so far the best accounting software yet produced is Excel.  Excel does not produce meaningful charts of accounts without more effort than the author is willing to put in.  So, the aim here is to create something that will by default allow easy examination of a company's chart of accounts and the relationships contained therein.

As for the rest of the accounting software currently extant, at least as far as the author has seen, the closest anything comes to what would properly be called a chart is a list of names and numbers that may or may not also provide links to the data contained inside the accounts described.

Testing
-------

So that's a lofty goal: how the hell do we get there?  The first thing, I'd say, is to write some tests that describe what a chart of accounts looks like to a computing machine, then maybe see if we can get the software to pass those tests.

Once we're realtively certain of our ability to produce data that can be understood and maniuplated by the machines we'll want to write some tests (perhaps with Selenium?) of a functional nature so that we can be sure of our ability to make the machine-readable data meaningful to humans as well. This is the second layer of the interface, as well as the second layer of the field of accounting, at least as it is being defined in the extremely limited scope of this software.
