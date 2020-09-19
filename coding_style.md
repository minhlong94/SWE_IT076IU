# Coding Style
Here I list some coding style requirements for this project. Please read it carefully before committing.  
This markdown file is based on [Google Python Styleguide](https://google.github.io/styleguide/pyguide.html) and the book [Clean Code: A Handbook of Agile Software Craftsmanship](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) and [PEP8](https://www.python.org/dev/peps/pep-0008/).

![alt text](https://i2.wp.com/commadot.com/wp-content/uploads/2009/02/wtf.png?resize=550%2C433)


## Basic coding style
Follow [PEP8](https://www.python.org/dev/peps/pep-0008/). In PyCharm, use `Ctrl+Alt+Shift+L` for every file.  

Indentation of tab is **FOUR** spaces.  

Functions/Methods: use lowercase, each word separates by `_`, for example: `def multiply_x_by_y():`  

Class: use Capitalized words, no separator needed, for example: `class PositionalEncoding():`  

Variables: use lowercase for variables with `_` separator. `customer_list = []`  

Constant variables: use uppercase. `GRAVITATIONAL_CONSTANT = 6.67e11`

Packages and Modules: lowercase with separator `_`

Documentation: every function/method should make documentation, following this format:
```python
def multiply_x_by_y(x, y):
"""Multiplying function

Function description goes here...

Args:
    x: a number, can be any type of number
    y: a number, can be any type of number
Returns:
    result: the result of x*y
Raises:
    TypeError: if either x or y is not a type of number
"""
    ...
    return ...
```
The class's documentation should follow the following format:
```Python
class PositionalEncoding():
    """Positional encoding layer

    Class description goes here.

    Attributes:
        sin: sine wave
        cos: cosine wave
        value: value
    Example:
    >>> posienco = PositionalEncoding()
    >>> posienco.value
    5
    """
```

Make meaningful names, for example:
```Python
# NO
d = 24 # Hours in a day

# YES
hours_in_a_day = 24

# NO
def gendmyhms(): # generate  day month year hour minute second
    return

# YES
def generate_day_month_year_hour_minute_second():
    return
```
Avoid disinformation. For example `customerList`: it is actually a `List`, or `Dict`?

## Imports
Use `import` statement for packages and modules only. For example:
```python
import x             # For packages and modules
from x import y      # x must be a prefix, y must be a module
from x import y as z # when two modules named y are to be imported or if y's name is long
import y as z        # only if z is a well-known abbreviation, for example np as numpy, tf as tensorflow
```
Imports each individual packages and separate modules on separate lines. For example:
```python
# NO
import x, y

# YES
import x
import y
```

## Functions
First, functions should be short, and second, it should be shorter than that. Use function to serve only for one purpose, and that purpose only.

## Packages
Import packages using the full pathname location. For example:
```python
from doctor.who import jodie # YES
import jodie                 # NO (assume this file is in the path doctor/who/)
```
## Exceptions
Try using build-in Exceptions (raise ValueError if program asks for positive integer but you pass a negative integer). Do **NOT** use `assert` for validation arguments: it is used for internal correctness, not to enforce correct usage nor to indicate that some unexpected event occurred.

**NEVER** use catch all exceptions: `except Exception`. Indicate clearly what exception is expected.

Minimize `try/catch` code blocks as much as possible.

## Global variables
**NEVER** use global variables. It has the potential to change the module behavior.

## Default operators and Iterators
Use default operators and iterators for types that support them. For example in list, dictionary it is `for x in dict1`, `if key not in dict2`.

## Generators
Use if needed. Change the docstring to `Yields` instead of `Returns`.

## Lambda Functions
OK if it is only one line.

## Conditional Expressions
OK for simple cases, for example `x = 1 if condition else 2`.

## True-False Evaluations
Use implict False if possible. For example `if foo` instead of `if foo != []`.

Use `if foo is None` (and `is not None`) instead of `if not foo`.

**NEVER** use `if foo == False`, use `if not foo` instead.

## String format
Use `"{}".format()` or `print(f"Number two is: {two}")`.

Avoid using `+=`, since Strings are immutable objects so this causes quadratic runtime.

Use double quote `""` instead of `''`.
