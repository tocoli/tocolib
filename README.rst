tocolib
=======================

The `tocolib` contains utility functions to make your life as developer easier.

Install
=======

Install this dependencies if you don't like to build them by yourself:

    sudo apt-get install python-levenshtein python-numpy

under Ubuntu make sure that you also have `pip3` if you like to use the library with Python 3:

    sudo apt-get install python3-pip

install all dependencies (globally):

    virtualenv ./venv
    source venv/bin/activate
    sudo pip install -r requirements.txt
    sudo pip3 install -r requirements.txt


Testing
=======

run all tests:
    `python -m unittest discover -s './tests' -p 'test_*.py'`


replace `test_module`, `TestClass`, `test_function` by the actual name

run a test suite:
    `python -m unittest tests.test_module`

run a test class:
    `python -m unittest tests.test_module.TestClass`

run a test function:
    `python -m unittest tests.test_module.TestClass.test_function`
