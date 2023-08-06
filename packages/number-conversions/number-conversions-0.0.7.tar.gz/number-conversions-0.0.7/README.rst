Number Conversion
=================

This package allows you to convert a number between any of the 82
standard bases described by
`Wikipedia <https://en.wikipedia.org/wiki/List_of_numeral_systems>`__
and `here </prep/systems.csv>`__. It provides both commandline options
and in code options to convert.

| The chosen 360 characters are available
  `here </prep/numbers_map.csv>`__ along with their unicode indexes.
| `Use in command line <#in-command-line>`__
| `Use in python code <#in-python-code>`__

--------------

In Command Line
---------------

There are several ways to use from command line with
``python -m convert_numbers.*`` command.

.. _a-convert_numbersconvert:

a) convert_numbers.convert
~~~~~~~~~~~~~~~~~~~~~~~~~~

| This is the simplest one time conversion command. It takes two
  positional arguments and one optional.
| a. **number**: The number to be converted.
| b. **new_base**: Base to convert the number two.
| c. **current_base**: The base of the number currently. This is an
  optional argument. If it's not included the base is assumed to be base
  10/Decimal. The marker is ``--current_base`` or ``-cb``.

::

   python -m convert_numbers.convert number new_base --current_base
   python -m convert_numbers.convert number new_base -cb

   python -m convert_numbers.convert 12 2 -cb 10

.. _b-convert_numbersloop:

b) convert_numbers.loop
~~~~~~~~~~~~~~~~~~~~~~~

This converts the input and waits for more input to convert until it's
quit. The user types in 3 numbers separated by a space.

::

   number_to_convert base_to_convert_to current_base

If current_base is not provided base 10 is assumed. Runs until user
types 'q'. For help type 'h'.

::

   python -m convert_numbers.loop
   Enter 'number new_base current_base': number new_base current_base*

   Enter 'number new_base current_base': 12 2 10*
   '12' in Decimal (base 10) to Binary (base 2) = '1100'
   Enter 'number new_base current_base': q

.. _c-convert_numberstable:

c) convert_numbers.table
~~~~~~~~~~~~~~~~~~~~~~~~

| Takes a list from input and converts it to the new base and returns a
  nice table as output. Takes 5 arguments, 2 positional and 3 optional.
| a) **numbers**: A list of numbers to convert separated by comma, no
  spaces. These numbers must be in the same base.
| b) **new_base**: Base to convert all the numbers to.
| c) **current_base**: Current base of all the numbers. This is an
  optional argument. When ignored, the base is assumed to be 10.The
  marker is ``--current_base`` or ``-cb``.
| d) **file**: The file to write the output to. This is an optional
  argument. When ignored, the output is the console. The marker is
  ``--file`` or ``-f``
| e. **in_file**: The file to be treated as input. This is an optional
  argument. If it is included **numbers** is ignored. So it can be left
  as 0 or anything, but never blank :( The format for in file is
  comma-separated numbers (new lines are treated as commas). The marker
  is ``--in_file`` or ``-if``.

::

   python -m convert_numbers.table 12,13,14 2 -cb=16

      
   Base 16 to base 2
   ----------------------------
   |  Hexadecimal  |  Binary  |
   ----------------------------
   |       12      |  10010   |
   |       13      |  10011   |
   |       14      |  10100   |
   ----------------------------

An example of input file is found
`here </convert_numbers/table_input.txt>`__.

.. _d-convert_numbersfile:

d) convert_numbers.file
~~~~~~~~~~~~~~~~~~~~~~~

This takes input completely from a file and outputs to another file. In
the file, the first line is the list of comma-separated numbers to
convert, the second is the new base, while the third is the current
base, if any otherwise it's base 10. Example input is
`here </convert_numbers/file_input.txt>`__

::

   python -m convert_numbers.file input_file.txt output_file.txt

   Written to 'out_file.txt'

Writes a csv like file, two columns old number, new number. The first
two rows are informational.

--------------

In python code
--------------

Several functions are described by the package. They are
``convert_number``, ``convert_from_base_10``,
``convert_float_from_base_10``, ``convert_to_base_10`` and
``convert_float_to_base_10``. To check user input refer to `this
section <#utility-functions>`__

Main Functions
~~~~~~~~~~~~~~

These, only one, can be used in isolation to convert a number from any
base to any other base.

.. _1-convert_number:

1. convert_number
^^^^^^^^^^^^^^^^^

| Used to convert a number between bases. Takes 3 arguments;
| a) ``number``: string = The number to be converted in string form.
| b) ``base_from``: integer = The base of ``number``.
| c) ``base_to``: integer = The base to convert to. Return a string with
  the new converted number

Usage

.. code:: python

   from conversions import convert_number

   convert_number('12', 10, 2) # return '1100'

Helper Functions
~~~~~~~~~~~~~~~~

| They are found in ``conversions.convert`` module. These are used to
  perform one simple action. These functions can be divided by four
  categories;
| 1. Category 1: Converts a number from **base 10** to **any other
  base**.
| 2. Category 2: Converts a number from **any base** to **base 10**.
| 3. Category 3: Converts a number that is a whole number. These
  functions typically belong to either of the categories above.
| 4. Category 4: Converts a number that is a floating number. These
  functions typically belong to either of the categories above.
| This means that a function can be from two points of view; one, does
  it convert a **whole number or a floating number**? two does it
  convert **from or to base 10**? All functions typically belong to two
  categories.

.. _1-convert_from_base_10:

1. convert_from_base_10
^^^^^^^^^^^^^^^^^^^^^^^

| Converts a whole number in base 10 to any base. This function is
  category 1 and category 3. Takes 2 arguments;
| a) ``decimal``: integer = This is the whole number to be converted.
| b) ``new_base``: integer = The base to convert to.
| Return a list ``['converted_digit', new_base]``

Usage

.. code:: python

   from conversions.convert import convert_from_base_10

   result = convert_from_base_10(12, 2) # returns ['1100', 2]

.. _2-convert_float_from_base_10:

2. convert_float_from_base_10
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Converts a floating number in base 10 to any base. This function is
  category 1 and category 4. It returns the maximum possible number
  decimal points. However in case of recurring decimal points, the
  maximum points is 15. The number has to be less than 1.
| Returns a list ``['converted_digit', new_base]``
| Takes two arguments:
| a) ``floating_decimal``: float = A number less than 1 but greater than
  0, to be converted.
| b) ``new_base``: integer = The base to convert the number to.

Usage

.. code:: python

   from conversions.convert import convert_float_from_base_10

   result = convert_float_from_base_10(0.25, 2) # ['0.01', 2]

.. _3-convert_to_base_10:

3. convert_to_base_10
^^^^^^^^^^^^^^^^^^^^^

| Converts a whole number from any base back to base 10. This function
  is category 2 and category 3. Returns an integer that is base 10.
  Takes two arguments:
| a) ``number``: string = The number to be converted in string form.
| b) ``current_base``: integer = The base of the number currently.
| Usage

.. code:: python

   from conversions.convert import convert_to_base_10

   result = convert_to_base_10('1001', 2) # returns 9

.. _4-convert_float_to_base_10:

4. convert_float_to_base_10
^^^^^^^^^^^^^^^^^^^^^^^^^^^

| Converts a floating number from any base back to base 10. This
  function is category 2 and category 4. It returns a float. Takes two
  arguments:
| a) ``number``: string = The string representation of the number to
  convert. It should be less than 1 but greater than 0.
| b) ``current_base``: integer = The base of the number currently.
| Usage

.. code:: python

   from conversions.convert import convert_float_to_base_10

   result = convert_float_to_base_10('0.2', 16) # returns 0.125

Utility functions
~~~~~~~~~~~~~~~~~

| Since none of these functions care whether the user input is factually
  correct, e.g., G4 cannot be base 16 or 63 is not a standard base or
  whether a character is used to represent these numbers, use
  ``n_utils`` to check. It provides the following functions:
| a. ``n_utils.ensure_base_is_standard`` - Takes the base, in integer
  form, and checks whether it's one of the 82 standard ones. Returns
  ``True`` or ``False``.
| b. ``n_utils.base_limits`` - Takes the number, in string form, and the
  base provided, in integer form and checks whether its factually
  correct. Returns ``True`` or ``False``.

To check the name of a base given the base, use ``n_utils.base_find``
which takes the base as argument and returns a string of the name of the
base.

.. code:: python

   from n_utils import base_find, ensure_base_is_standard, base_limits


   ensure_base_is_standard(63) # False
   ensure_base_is_standard(64) # True

   base_limits('G4', 16) # False
   base_limits('G4', 20) # True

   base_find(2) # Binary
   base_find(10) # Decimal
