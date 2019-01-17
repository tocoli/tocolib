tocolib
=======

|build-status| |docs|

A multipurpose utility library for Python 2 and 3.

The library namespace is ``tocoli``. For information on 
available packages, modules and functionality see `Structure`_.

Highlights
----------

Sorting dictionaries
>>>>>>>>>>>>>>>>>>>>

    Sort a 'list' of 'dict' by simply defining the `keys` you like to sort
    by in order from last to first.

    Example:

        >>> dicts = [{'firstname': 'Bob',   'lastname': 'Abel'},
                     {'firstname': 'Alice', 'lastname': 'Bond'},
                     {'firstname': 'Carol', 'lastname': 'Bond'},
                     {'firstname': 'Bob',   'lastname': 'Bond'},
                     {'firstname': 'Carol', 'lastname': 'Abel'},
                     {'firstname': 'Alice', 'lastname': 'Abel'}]

        >>> from tocoli.sort import sort_dicts_by_value
        >>> sort_dicts_by_value(dicts, ['lastname', 'firstname'])
        [{'firstname': 'Alice', 'lastname': 'Abel'},
         {'firstname': 'Bob',   'lastname': 'Abel'},
         {'firstname': 'Carol', 'lastname': 'Abel'},
         {'firstname': 'Alice', 'lastname': 'Bond'},
         {'firstname': 'Bob',   'lastname': 'Bond'},
         {'firstname': 'Carol', 'lastname': 'Bond'}]

A Domain Specific Language for intuitive function calls
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    The ``dsl`` package provides a coherent style to access the `tocolib`
    modules and functions as module or static class functions.

    Example:

        >>> from tocoli.dsl import sort

        >>> sort.dicts.by.value(dicts, ['lastname', 'firstname'])
        [{'firstname': 'Alice', 'lastname': 'Abel'},
         {'firstname': 'Bob',   'lastname': 'Abel'},
         {'firstname': 'Carol', 'lastname': 'Abel'},
         {'firstname': 'Alice', 'lastname': 'Bond'},
         {'firstname': 'Bob',   'lastname': 'Bond'},
         {'firstname': 'Carol', 'lastname': 'Bond'}]

        >>> sort.dicts.by.similarity(dicts, 'Karol', ['firstname'])
        [{'firstname': 'Carol', 'lastname': 'Bond'},
         {'firstname': 'Carol', 'lastname': 'Abel'},
         {'firstname': 'Alice', 'lastname': 'Bond'},
         {'firstname': 'Alice', 'lastname': 'Abel'},
         {'firstname': 'Bob',   'lastname': 'Abel'},
         {'firstname': 'Bob',   'lastname': 'Bond'}]

Powerful mapping
>>>>>>>>>>>>>>>>

    Use recursive mapping to apply functions to nested data structures.

    Example:

        >>> from tocoli.dsl import map

        >>> def upper(item, parent):
                return item.upper()

        >>> map.recursive(dicts, upper)
        [{'firstname': 'BOB', 'lastname': 'ABEL'},
         {'firstname': 'ALICE', 'lastname': 'BOND'},
         {'firstname': 'CAROL', 'lastname': 'BOND'},
         {'firstname': 'BOB', 'lastname': 'BOND'},
         {'firstname': 'CAROL', 'lastname': 'ABEL'},
         {'firstname': 'ALICE', 'lastname': 'ABEL'}]

        >>> map_keys = (map.DEFAULT | map.DICT_KEY) ^ map.DICT_VALUE
        >>> map.recursive(dicts, upper, map_keys)
        [{'FIRSTNAME': 'Bob', 'LASTNAME': 'Abel'},
         {'FIRSTNAME': 'Alice', 'LASTNAME': 'Bond'},
         {'FIRSTNAME': 'Carol', 'LASTNAME': 'Bond'},
         {'FIRSTNAME': 'Bob', 'LASTNAME': 'Bond'},
         {'FIRSTNAME': 'Carol', 'LASTNAME': 'Abel'},
         {'FIRSTNAME': 'Alice', 'LASTNAME': 'Abel'}]


What's New
----------

* Changed minimum requirement: passlib>=1.7.0
* The former ``dsl`` module is now an own subpackage.
* The `keys` parameter notation for sorting functions changed.
* There are new `flags` paramter options for mapping functions.

For more detailed information on current changes check the `change log <https://github.com/tocoli/tocolib/blob/master/CHANGELOG.md>`_.

Structure
---------

Namespace
>>>>>>>>>

``tocoli``  **- root**
    The tocolib wraps the ``six`` library (Python 2 and 3 compatibility utilities)
    at the root. Thus all ``six`` packages and modules are also available under the
    root namespace.


Subpackages
>>>>>>>>>>>

``dsl``     **- a domain specific language for tocolib**
    Python, like it should be. The module contains a domain specific language
    for common functions like filtering, sorting, mapping and more. All
    functions have a consistent API and results.


Modules
>>>>>>>

``auth``    **- common authetication helpers**
    Its dangerous out there. This module is all about passwords, hashes, salts,
    tokens and api keys.

``cmp``     **- compare utilities**
    For those who like to compare apples with pears. Make different data types
    comparable.

``enc``     **- encoding functions**
    Encoding without pain. Provides universal encoding functions.

``filter``  **- filter functions**
    The good ones go into the pot, the bad ones go into your crop. Advanced
    functions to filter dictionaries or lists of strings.

``fn``      **- common lambda functions**
    To Be or not to Be: That is the question! Short value extractor functions
    and more.

``join``    **- join/reduce/folding functions**
    Bring together what belongs together.

``map``     **- mapping functions**
    It's still magic even if you know how it's done. Map data by applying any
    higher-order function to it.

``ratio``   **- ratio functions**
    Comparisons make unhappy, but can be quite useful. Provides ratio
    functions for varios purposes.

``regex``   **- regular expression utilities**
    Find what you are searching for. Generate common regular expressions.

``sort``    **- sort functions**
    Chuck Norris is able to sort black pens by color. Sort data by value or keys.

``spell``   **- spelling utilities**
    Life doesn't come with spell-check, but tocolib does.

``test``    **- testing and benchmarking**
    Tests cant prove the absence of bugs. Thus test as good as you can.

``type``    **- type conversion utilities**
    What doesn't fit is made to fit. Universal type transformations.


.. |build-status| image:: https://api.travis-ci.org/tocoli/tocolib.svg?branch=master
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.org/tocoli/tocolib

.. |docs| image:: https://readthedocs.org/projects/tocolib/badge/?version=latest
    :alt: Documentation Status
    :scale: 100%
    :target: https://tocolib.readthedocs.io/en/latest/?badge=latest
