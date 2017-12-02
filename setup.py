import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "accounting",
    version = "0.0.1",
    author = "ECLA",
    author_email = "andrewjcarter@gmail.com",
    description = ("Accounting software for accountants."),
    license = "The Unlicense",
    keywords = "accounting",
    packages=['transaction', 'transaction.tests'],
    long_description=read('readme.md'),
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'nose'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
    ],
)
