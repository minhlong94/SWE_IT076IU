# Coding Style
Here I list some coding style requirements for this project. Please read it carefully before committing.  
This markdown file is based on [Google Python Styleguide](https://google.github.io/styleguide/pyguide.html) and the book [Clean Code: A Handbook of Agile Software Craftsmanship](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) and [PEP8](https://www.python.org/dev/peps/pep-0008/).

## Basic coding style
Follow [PEP8](https://www.python.org/dev/peps/pep-0008/). In PyCharm, use `Ctrl+Alt+Shift+L` for every file.  
Functions: use lowercase, each word seperates by `_`, for example: `def multiply_x_by_y():`  
Class: use Capitalized words, no seperator needed, for example: `class PositionalEncoding():`  
Variables: use lowercase for variables. `customer_list = []`  
Constant variables: use uppercase. `GRAVITY_CONSTANT = ...`
Documentation: every function/method should make documentation. For example:
```python
def multiply_x_by_y(x, y):
"""
Function multiplies x by y times

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
## Imports
Use `import` statement for packages and modules only. For example:
```python
import x             # For packages and modules
from x import y      # x must be a prefix, y must be a module
from x import y as z # when two modules named y are to be imported or if y's name is long
import y as z        # only if z is a well-known abbreviation, for example np as numpy, tf as tensorflow
```
Imports each individual packages and seperate modules on seperate lines. For example:
```python
import x, y # NO

import x
import y # YES
```
## Packages
Import packages using the full pathname location. For example:
```python
from doctor.who import jodie # YES
import jodie                 # NO (assume this file is in the path doctor/who/)
