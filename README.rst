A sample Python project
=======================

A sample project that exists as an aid to the `Python Packaging User Guide
<https://packaging.python.org>`_'s `Tutorial on Packaging and Distributing
Projects <https://packaging.python.org/en/latest/distributing.html>`_.


Install
=======

install all dependencies:
    ```
    virtualenv ./venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

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
