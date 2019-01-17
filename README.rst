tocolib
=======

|build-status| |docs|

The ``tocolib`` contains utility functions for common use cases to make your life as developer easier.

For more information on the functionality included see the `description <https://github.com/tocoli/tocolib/blob/master/DESCRIPTION.rst>`_ file or 
vist the `documentation <https://tocolib.readthedocs.io/en/latest/?badge=latest>`_.

For latest changes see the `change log <https://github.com/tocoli/tocolib/blob/master/CHANGELOG.md>`_.

Install
=======

System Dependencies
-------------------

Make sure that ``pip2`` or ``pip3`` is globally available. For example, if you like to use the library under ubuntu do:

For Python 2 install ``pip2``:

    ``sudo apt-get install python-pip``

For Python 3 install ``pip3``:

    ``sudo apt-get install python3-pip``

.. note:: If you are unfamiliar with installing packages in python you might want to read the 
    documentation on this topic: `Installing Packages <https://packaging.python.org/tutorials/installing-packages/>`_

Library Dependencies
--------------------

Install all runtime dependencies into a virtual environment.

.. note:: Make sure you have ``virtualenv`` installed globally on your system.


For Python 2:
::

    virtualenv -p /usr/bin/python2.7 py27
    source py27/bin/activate
    pip install -r requirements.txt

For Python 3:
::

    virtualenv -p /usr/bin/python3.6 py36
    source py36/bin/activate
    pip install -r requirements.txt

To leave a ``virtualenv`` run:

    ``deactivate``

.. note:: If you don't like to built heavy weighted dependencies by yourself, 
    then you might want to install some prebuild version globally.
    
    E.g. under ubuntu do:
    
        ``sudo apt-get install python-levenshtein python-numpy``

    or

        ``sudo apt-get install python3-levenshtein python3-numpy``

Testing
=======

Run all tests with the built-in test discovery or with ``pytest``.

.. note:: Make sure you have ``pytest`` installed. For example with:

        ``pip install pytest``

built-in testing:

    ``python -m unittest discover -s './tests' -p 'test_*.py'``

or with ``pytest``:

    ``pytest tests``

If you want to test just some parts of the library, then one can invoke more specficic commands. Replace ``test_module``, ``TestClass``, ``test_function`` respectivly by the actual name.

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
