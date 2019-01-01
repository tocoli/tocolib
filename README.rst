.. image:: https://api.travis-ci.org/tocoli/tocolib.svg?branch=master

tocolib
=======

The ``tocolib`` contains utility functions to make your life as developer easier.

Install
=======

Install this dependencies globally if you don't like to build them by yourself::

    sudo apt-get install python-levenshtein python-numpy

Under Ubuntu 16.04 make sure that you also have ``pip3`` besides ``pip``, if you like to use the library with Python 3::

    sudo apt-get install python3-pip

Install all dependencies (locally). Make sure you have `virtualenv` installed::

    virtualenv ./venv
    source venv/bin/activate
    # Python 2
    pip install -r requirements.txt
    # Python 3
    pip3 install -r requirements.txt
    deactivate


Testing
=======

run all tests:

* Python 2:
    ``python -m unittest discover -s './tests' -p 'test_*.py'``
    
* Python 3:
    ``python3 -m unittest discover -s './tests' -p 'test_*.py'``


replace ``test_module``, ``TestClass``, ``test_function`` by the actual name

run a test suite:
    ``python3 -m unittest tests.test_module``

run a test class:
    ``python3 -m unittest tests.test_module.TestClass``

run a test function:
    ``python3 -m unittest tests.test_module.TestClass.test_function``
