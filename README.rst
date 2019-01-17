tocolib
=======

|build-status| |docs|

The ``tocolib`` contains utility functions to make your life as developer easier.

For more information see: `DESCRIPTION <https://github.com/tocoli/tocolib/blob/master/DESCRIPTION.rst>`_

Install
=======

System Dependencies
-------------------

Make sure that ``pip2`` or ``pip3`` is globally available.

For example, if you like to use the library under ubuntu do:

For Python 2 install ``pip2``::
    sudo apt-get install python-pip

For Python 3 install ``pip3``:
    sudo apt-get install python3-pip

Library Dependencies
--------------------

Install all runtime dependencies (locally) into the virtual environment.

.. note:: Make sure you have ``virtualenv`` installed globally on your system.

For Python 2::

    virtualenv -p /usr/bin/python2.7 py27
    source py27/bin/activate
    pip install -r requirements.txt

For Python 3::

    virtualenv -p /usr/bin/python3.6 py36
    source py36/bin/activate
    pip install -r requirements.txt

To leave a ``virtualenv`` run:
    ``deactivate``

.. note:: If you don't like to built the heavy weighted dependencies by yourself, 
    then you might want to install some prebuild version globally. Under ubuntu do:

    ``sudo apt-get install python-levenshtein python-numpy``

Testing
=======

Run all tests with the built-in test discovery or with ``pytest``.

.. note:: Make sure you have ``pytest`` installed with ``pip install pytest``.

built-in testing:
    ``python -m unittest discover -s './tests' -p 'test_*.py'``

with ``pytest``:
    ``pytest tests``

If you want to test just some parts of the library, then one can invoke more specficic commands.

Replace ``test_module``, ``TestClass``, ``test_function`` by the actual name.

run a test suite:
    ``python -m unittest tests.test_module``

run a test class:
    ``python -m unittest tests.test_module.TestClass``

run a test function:
    ``python -m unittest tests.test_module.TestClass.test_function``



.. |build-status| image:: https://api.travis-ci.org/tocoli/tocolib.svg?branch=master
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.org/tocoli/tocolib

.. |docs| image:: https://readthedocs.org/projects/tocolib/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://tocolib.readthedocs.io/en/latest/?badge=latest
