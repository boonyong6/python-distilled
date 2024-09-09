# 1 Python Basics

## 1.1 Running Python

- Programs are executed by an **interpreter**.
- To pick a version, if both Python 2 and Python 3 are installed:

  ```bash
  # In bash
  # Start version 2
  python2

  # Start version 3
  python3
  ```

- In **interactive mode**, variable `_` holds the result of the last operation.

## 1.2 Python Programs

- Common to use `#!` to specify the interpreter:
  ```py
  #!/usr/bin/env python3
  print('Hello World')
  ```

## 1.3 Primitives, Variables, and Expressions

- Basics:

  ```py
  # Primitive types
  # ---------------
  42          # int
  4.2         # float
  'forty-two' # str
  True        # bool

  # Variable
  # --------
  x = 42
  # The type is merely a hint, it does not prevent you from assigning a different kind of value.
  x: int = 42

  # f-string
  # --------
  # Each substitution {} can have an optional formatting specifier.
  # More formatting codes in Chapter 9.
  print(f'{year:>3d} {principal:0.2f}')

  # Falsy values
  # ------------
  False
  None  # null
  0
  ''    # empty
  ```

- Common to use **four spaces** per indentation level.

## 1.4 Arithmetic Operators

- Noteworthy operators:
  Operation | Description
  ----------|------------
  `x / y` | Produce a float when applied to int.<br />E.g. `4 / 2` -> `2.0`
  `x // y` | Truncating division.<br />E.g. `5 // 2` -> `2`
  `x ** y` | Power
- Common Mathematic Functions:
  Function | Description
  ---------|------------
  `abs(x)` | Positive value
  `divmod(x, y)` | Return `(x // y, x % y)` (A tuple)
  `pow(x, y [, modulo])` | Return `(x ** y) % modulo`
  `round(x, [n])` | Implement "**banker's rounding**".
- **Logical Operators:** `x or y`, `x and y`, `not x`
- Python does not have `++` or `--` operators.

## 1.5 Conditionals and Control Flow

- Use `pass` to create an **empty clause** (python doesn't use {} to define scope).
  ```py
  if a < b:
      pass # Do nothing
  else:
      print('Computer says No')
  ```
- Conditional expression:
  ```py
  max_val = a if a > b else b
  ```
- Assignment expression (walrus operator `:=`):
  ```py
  # Use := to assign to a variable and return its value.
  # Example: Combine the assignment of a variable and a conditional.
  x = 0
  while (x := x + 1) < 10: # Print 1, 2, 3, ..., 9
      print(x)
  ```

## 1.6 Text Strings

- String literal:

  ```py
  a = 'Single/double-quoted strings must be specified on one line.'

  b = '''Triple-quoted strings
  can be specified on
  multiple lines.'''

  # Immediately adjacent string literals are concatenated into a single string.
  print(
  'Content-type: text/html\n'
  '\n'
  '<h1> Hello World </h1>\n'
  'Click <a href="http://www.python.org">here</a>.\n'
  )
  ```

- **Alternatives to f-strings** - `format()` method and `%` operator:

  ```py
  print(f'{year:>3d} {principal:0.2f}')

  print('{0:>3d} {1:0.2f}'.format(year, principal))
  print('%3d %0.2f' % (year, principal))
  ```

- **Negative indices** index from the end of the string.
  ```py
  a = 'Hello World'
  c = a[-1]    # c = 'd'
  ```
- Use slicing operator `s[i:j]` to extract a **substring**.
  ```py
  a = 'Hello World'
  c = a[:5]    # c = 'Hello'
  d = a[6:]    # d = 'World'
  e = a[3:8]   # e = 'lo Wo'
  f = a[-5:]   # f = 'World'
  ```
- Common String Methods:
  ![common-string-methods](images/1-6-common-string-methods.png)
- Convert string **to int or float**:
  ```py
  x = '37'
  y = '42.79'
  z = int(x) + float(y) # z = 79.78999999999999 (float arithmetic issue)
  ```
- Convert non-string **to string**:

  ```py
  s = "hello\nworld"

  # Print:
  #   hello
  #   world
  print(str(s))
  # Print:
  #   'hello\nworld'
  print(repr(s))

  print(format(12.34567, "0.2f"))
  print(f'{12.34567:0.2f}')
  ```

- When **debugging**, use `repr(s)` because it shows you more information.

## 1.7 File Input and Output

- `with` statement:
  ```py
  # Once control leaves the with statement block, the file is automatically closed.
  with open("data.txt") as file:
      for line in file:
          print(line, end='')
  ```
- Common file operations:

  ```py
  # To read the entire file as a string.
  with open('data.txt') as file:
      data = file.read() # <-

  # To read in chunks (e.g. 10,000 bytes per chunk)
  with open('data.txt') as file:
      while (chunk := file.read(10000)): # <-
          print(chunk, end='')

  # Print/write to file.
  with open('out.txt', 'wt') as out:
      while year <= num_years:
          principal = principal * (1 + rate)
          print(f'{year:>3d} {principal:0.2f}', file=out) # <-
          out.write(f'{year:3d} {principal:0.2f}\n') # <-
          year += 1
  ```

## 1.8 Lists

- Can contain mix of objects:
  ```py
  mix_objects = [1, "Dave", 3.14, ["Mark", 7, 9, [100, 101]], 10]
  ```
- Common list operations:

  ```py
  names = ["Dave", "Paula", "Thomas", "Lewis"]
  # Replace the first two items with ["Dave", "Mark", "Jeff"]
  names[0:2] = ["Dave", "Mark", "Jeff"]

  # List comprehension (preferred)
  values = [int(row[1]) * float(row[2]) for row in rows]

  # Without list comprehension
  values = []
  for row in rows:
      values.append(int(row[1]) * float(row[2]))
  total = sum(values)
  ```

## 1.9 Tuples

- Pack a collection of values into an **immutable object**.
- Support most of the same operations as lists.
- Best viewed as a single immutable object that consists of several parts, not as a collection of distinct objects like a list.
- The variable `_` can be used to indicate a discarded value:
  ```py
  total = sum([shares * price for _, shares, price in portfolio])
  ```

## 1.10 Sets

- Elements are **restricted to immutable objects**. E.g. you can't make a set containing lists.
- **Unordered** (the order of items can't be predicted) and cannot be indexed by numbers.
- Set comprehension:
  ```py
  names = {s[0] for s in portfolio}
  ```
- Set operations:

  ```py
  t = {"IBM", "MSFT", "HPE", "IBM", "CAT"}
  s = {"IBM", "MSFT", "AA"}

  a = t | s  # Union {'MSFT', 'CAT', 'HPE', 'AA', 'IBM'}
  b = t & s  # Intersection {'IBM', 'MSFT'}
  c = t - s  # Difference { 'CAT', 'HPE' }
  d = s - t  # Difference { 'AA' }
  e = t ^ s  # XOR { 'CAT', 'HPE', 'AA' }

  s.update({"JJ", "GE", "ACME"})  # Adds multiple items

  t.remove("IBM")    # Raise KeyError if absent
  t.discard("SCOX")  # Remove if exists
  ```

## 1.11 Dictionaries

- Dictionary operations:

  ```py
  # Use case 1: Used as a mapping for performing fast lookups.
  prices = {
      "GOOG": 490.1,
      "AAPL": 123.5,
      "IBM": 91.5,
      "MSFT": 52.13,
  }

  # Use case 2: To define an object that consists of named fields.
  stock = {
      "name": "GOOG",
      "shares": 100,
      "price": 490.10
  }

  # To test the presence of a key.
  if "IBM" in prices:
      ...

  # To remove an element.
  del prices["GOOG"]

  # Use tuple to construct composite key.
  prices = {} # Alternative: prices = dict()
  prices["IBM", "2015-02-04"] = 91.42

  # Dictionary comprehension
  total_shares = {s[0]: 0 for s in portfolio}

  # To create from key-value values.
  pairs = [("IBM", 125), ("ACME", 50), ("PHP", 40)]
  d = dict(pairs)

  # To get a list of keys/values/items (actively reflects changes).
  price_keys = prices.keys()
  price_values = prices.values()
  price_items = prices.items() # List of tuples
  ```

- **Mutable data structures** such as lists, sets and dictionaries **can't be used as keys**.
- In Python 3.6 or later, the dictionary preserves the input order.

## 1.12 Iteration and Looping

- Example:

  ```py
  # To loop over a range of integers.
  for n in range(1, 10):  # stop = 10 (exclusive)
      print(f"2 to the {n} power is {2**n}")

  # Descending sequence
  for i in range(8, 1, -1):  # step = -1
      print(i)

  # To loop over a dictionary.
  prices = {"GOOG": 490.10, "IBM": 91.50, "AAPL": 123.15}
  for key in prices:
      print(key, "=", prices[key])
  ```

- `range()` object computes the values it represents **on demand** when lookups are requested.

## 1.13 Functions

- To include a **documentation string** as the first statement.
  ```py
  # Annotated with types.
  def compute_remainder(dividend: int, divisor: int) -> int:
      """
      Computes the remainder.
      """
      quotient = dividend // divisor
      result = dividend - quotient * divisor
      return result
  ```
- Annotations are **merely informational** and are not enforced at runtime.
- Parameter default value:

  ```py
  def connect(hostname, port, timeout=300):
      print(f"{hostname}:{port}")

  # Recommended to specify optional arguments using keyword arguments.
  connect("www.python.org", 80, timeout=500)
  ```

- When variables are defined inside a function, their **scope is local** (more detail in **Chapter 5**).

## 1.14 Exceptions

- Catch and handle exceptions using `try` and `except` statement:
  ```py
  try:
      price = float(price_str)
  except ValueError as err:
      print("Reason:", err)
  ```
- To throw an exception:
  ```py
  raise RuntimeError("Computer says no")
  ```

## 1.15 Program Termination

- Example:

  ```py
  import atexit


  def cleanup():
      print("Cleaning up...")
      print("Program terminated.")


  atexit.register(cleanup)

  print("Program started.")

  raise SystemExit("Exit on error.")

  # Output:
  #   Program started.
  #   Exit on error.
  #   Cleaning up...
  #   Program terminated.
  ```

## 1.16 Objects and Classes

- **All values** are objects.
- `dir()` lists the methods available on an object. Useful in the interactive mode.
- `__<method>__()` - A special method that implements a operator. E.g. `__add__()` implement the `+` operator.
- In the **class**, the **first argument** in each method always refers to the object itself (`self`).
- **Internal attributes** are prefixed with underscore. E.g. `self._name`.
- Python does not have any mechanism for hiding or protecting data.
- A good idea to define `__repr__()` to facilitate **debugging**.
- **Inheritance** example:

  ```py
  class NumericStack(Stack):
      # New method
      def swap(self):
          a = self.pop()
          b = self.pop()
          self.push(a)
          self.push(b)

      # To change the behavior of an existing method.
      def push(self, item):
          if not isinstance(item, (int, float)):
              raise TypeError("Expected an int or float")
          super().push(item)  # <-
  ```

- Often, inheritance is not the best solution.
- **Composition** example:

  ```py
  class Calculator:
      def __init__(self):
          self._stack = Stack()  # <-

      def push(self, item):
          self._stack.push(item)

      def pop(self):
          return self._stack.pop()

      def add(self):
          self.push(self.pop() + self.pop())
  ```

## 1.17 Modules

- The module name is the same as the **file name**.
- `import` statement creates a new **namespace**.
- If the import statement fails (`ImportError`), check a few things:
  - Make sure the target `.py` file exists.
  - Check the directories in `sys.path`.
- `dir()` lists the contents of a module. Useful in the interactive mode.
- Package manager - https://pypi.org
- Example:

  ```py
  # To import a module.
  import readport

  # To import a module under a different name.
  import readport as rp

  # To import specific definitions.
  from readport import read_portfolio
  ```

## 1.18 Script Writing

- Any file can execute either as a **script** or as a **module**.
- Example:

  ```py
  # File: readport.py

  # If this file is run as the main script,
  #   the __name__ variable is set to "__main__".
  # else,
  #   the __name__ variable is set to "readport".
  if __name__ == "__main__":
      import sys

      main(sys.argv)
  ```

## 1.19 Packages

- A package is a **collection of modules**.
- `__init__.py` is used to mark a directory as a package.
- To import a module within the same package:

  ```py
  # pcost.py

  # Consider the following directory structure:
  #   tutorial/
  #     __init__.py
  #     readport.py
  #     pcost.py

  # Fully qualified import
  from tutorial import readport

  # Package-relative import
  from . import readport
  ```

## 1.20 Structuring an Application

- The **primary purpose** of the package is to manage `import` statements and the namespaces of modules.
- Example:
  ```
  tutorial-project/
      tutorial/
          __init__.py
          readport.py
          pcost.py
          stack.py
          ...
      tests/
          test_stack.py
          test_pcost.py
          ...
      examples/
          sample.py
          ...
      doc/
          tutorial.txt
          ...
  ```

## 1.21 Managing Third-Party Packages

- To install a package:
  ```bash
  pip install <package>
  ```
- Installed packages are stored in the `site-packages` directory.
- Inspect the `__file__` attribute of a package to find the path.
- Use a **virtual environment** to install packages for a specific project:
  ```
  python -m venv <venv_name>

  # To activate on Windows.
  <venv_name>\Scripts\activate
  ```

# 2 Operators, Expressions, and Data Manipulation

## 2.1 Literals

- Example:

  ```py
  # Integer
  x = 42  # Decimal integer
  bin(x)  # -> "0b101010"
  oct(x)  # -> "0o52"
  hex(x)  # -> "0x2a"

  # Float (IEEE 754 double-precision (64-bit))
  4.2
  42.
  .42
  4.2e+2
  ```

## 2.3 Standard Operators

- Example:

  ```py
  [1, 2, 3] + [4, 5]  # -> [1, 2, 3, 4, 5]
  [1, 2, 3] * 3       # -> [1, 2, 3, 1, 2, 3, 1, 2, 3]
  "%s has %d messages" % ("Dave", 37)

  # Mixed data types
  from factions import Fraction
  a = Fraction(2, 3)
  b = 5
  a + b  # -> Fraction(17, 3)
  ```

## 2.4 In-Place Assignment

- Example:

  ```py
  a = 3
  a += 1

  a = [1, 2, 3]
  a += [4, 5]  # In-place update.
  ```

## 2.5 Object Comparison

- An equality comparison between objects of incompatible types does not trigger an error but returns `False`.
- Example:

  ```py
  file == 2.0  # -> False
  2 == 2.0     # -> True

  a = [1, 2, 3]
  b = [1, 2, 3]
  # Identity operator
  a is b  # -> False
  # Equality operator
  a == b  # -> True
  ```

- Comparing objects with the `is` operator is almost never what you want, use `==` operator instead.

## 2.6 Ordered Comparison Operators - `<`, `<=`, `>`, `>=`

- For **sets**, `x < y` tests if `x` is **strict subset** of `y`.
- For **subsequences**, `x < y` tests if `x` is a **subsequence** of `y`.
- Dictionary does not support the ordered comparison operators.

## 2.9 Operations Involving Iterables

![2-5-operations-on-iterables](images/2-5-operations-on-iterables.png)
- For **strings**, `in` operator checks if the substring is contained in the string.
- `in` operator does not support wildcards or pattern matching.
- If the ***-expansion** is used on one-time iteration objects (e.g. files), the subsequent iteration yields no result.

## 2.10 Operations on Sequences

![2-7-operations-on-sequences](images/2-7-operations-on-sequences.png)
- `s * n` creates shallow copies (**reference**) of the list.
- `s[-1]` returns the **last element**.
- Slicing example:
  ```py
  a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

  a[2:5]      # [2, 3, 4]
  a[:3]       # [0, 1, 2]
  a[-3:]      # [7, 8, 9]
  a[::2]      # [0, 2, 4, 6, 8 ]
  a[::-2]     # [9, 7, 5, 3, 1 ]
  a[0:5:2]    # [0, 2, 4]
  a[5:0:-2]   # [5, 3, 1]
  a[:5:1]     # [0, 1, 2, 3, 4]
  a[:5:-1]    # [9, 8, 7, 6]
  a[5::1]     # [5, 6, 7, 8, 9]
  a[5::-1]    # [5, 4, 3, 2, 1, 0]
  a[5:0:-1]   # [5, 4, 3, 2, 1]

  # Named slice
  first_five = slice(0, 5)
  s = "hello world"
  print(s[first_five])  # -> "hello"
  ```

# 2.14 List, Set, and Dictionary Comprehensions

- Useful for transforming a collection of data into another data structure.
- Also possible to apply a **filter**:
  ```py
  squares = [n * n for n in nums if n > 2]
  ```
- Variables used inside a comprehension are **private**.
- **Set comprehension** will give you a set of **distinct values**.
- When creating **sets** and **dictionaries**, later entries might **overwrite** earlier entires.
- Within a comprehension, it's not possible to include any exception handling. Consider wrapping exceptions with a function:
  ```py
  def to_int(x):
      try:
          return int(x)
      except ValueError:
          return None

  # Note: Double evaluation of to_int().
  data2 = [to_int(x) for x in values if to_int(x) is not None]

  # Use := operator to avoid double evaluation.
  data3 = [v for x in values if (v := to_int(x)) is not None]
  ```
