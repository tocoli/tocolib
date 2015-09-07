tocolib
=======

The tocolib is a multipurpose utility library.


Structure
---------

    :namespace:

        |   ``tocoli``  - six (Python 2 and 3 compatibility utilities) and more

    :modules:


        |   ``cmp``     - compare utilities
        |               For those who like to compare apples with pears.

        |    ``dsl``    - python like it should be.
        |               The module is a wrapper for other `tocoli` modules. It
        |               contains a domain specific language for common functions
        |               like filtering, sorting, mapping and more. All functions
        |               have a consistent API and results.

        |   ``enc``     - encoding
        |               Provides universal and powerful encoding functions.

        |   ``filter`` - filter functions

        |   ``fn``     - common lambda functions

        |   ``join``   - join functions

        |   ``map``    - recursive mapping

        |   ``ratio``  - ratio functions
        |              Provides ratio functions for varios purposes.

        |   ``regex``  - regular expression utilities
        |              Contains helper functions to generate common regular expressions.

        |   ``sort``   - sort functions

        |   ``spell``  - spelling utilities

        |   ``string`` - string functions

        |   ``test``   - testing and benchmarking

        |   ``type``   - type conversion utilities


What's New
----------

    * The tocolib proudly supports Python 2 and 3.
        The library makes internally usage of the six utilities to provide
        universal Python 2 and 3 support.

    * Sorting functions are easier to use.
        Sorting dictionaries by value can now be achieved with **kwargs, which
        enables custom naming for keys.

    * Powerful mapping.
        Use the recursive mapping to apply functions to complex data struc-
        tures.

    * Meta ratio:
        The meta() function from module `ratio` can combine varios ratios in a
        weighted manner.

For more information on current changes check the `CHANGELOG.md`.
