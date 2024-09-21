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
      data = file.read() # <--

  # To read in chunks (e.g. 10,000 bytes per chunk)
  with open('data.txt') as file:
      while (chunk := file.read(10000)): # <--
          print(chunk, end='')

  # Print/write to file.
  with open('out.txt', 'wt') as out:
      while year <= num_years:
          principal = principal * (1 + rate)
          print(f'{year:>3d} {principal:0.2f}', file=out) # <--
          out.write(f'{year:3d} {principal:0.2f}\n') # <--
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
- When variables are defined inside a function, their **scope is local** (more details in **Chapter 5**).

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
          self._stack = Stack()  # <--

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
- If the **\*-expansion** is used on one-time iteration objects (e.g. files), the subsequent iteration yields no result.

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

## 2.14 List, Set, and Dictionary Comprehensions

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

## 2.15 Generator Expressions

- Same computation as a list comprehension but produce the result iteratively.
- Produce values on demand, which improve performance and memory use.
- Example:
  ```py
  nums = [1, 2, 3, 4]
  squares = (num * num for num in nums)

  next(squares)  # 1
  next(squares)  # 4

  for square in squares:
      print(square)  # 9, 16


  # Convert to a list.
  squares_list = list(squares)


  # Pass as a single function argument.
  sum((x * x for x in values))
  sum(x * x for x in values)  # Parentheses are optional.
  ```
- Can only be used/iterated once.
- Can't be indexed.

## 2.18 Order of Evaluation

![2-11-order-of-evaluation](images/2-11-order-of-evaluation.png)

- A common confusion:

  ```py
  a = 10
  result = a <= 10 and 1 < a  # -> True

  # bitwise-and (&) has higher precedence than the comparison operators.
  result = a <= 10 & 1 < a    # a <= (10 & 1) < a -> False
  ```

## 2.19 Final Words: The Secret Life of Data

- Python is frequently used in applications involving **data manipulation and analysis**.

# 3 Program Structure and Control Flow

## 3.1 Program Structure and Execution

- Structured as a sequence of statements.
- The interpreter executes statements in the order they appear.

## 3.3 Loops and Iteration

- `for` statement works with any object that implements the [**iteration protocol**](#414-iteration-protocol).
- The scope of the iteration variable is not private to the `for` statement.
- Use `enumerate()` to keep track of a numerical index:
  ```py
  # _ is a throw-away variable.
  # start=1 is an optional argument to specify a start index.
  for i, (x, _, *extra) in enumerate(s, start=1):
      print("i:", i, "x:", x, "extra:", extra)
  ```
- Common looping problem - **iterating in parallel** over two or more iterables:
  ```py
  seq1 = [0, 1, 2, 3, 4, 5, 6]
  seq2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

  # Use zip() to combine iterables into an iterator of tuples.
  # Stop when the shortest iterable is exhausted.
  # zip() returns an iterator that produces the results when iterated.
  for seq1_item, seq2_item in zip(seq1, seq2):
      print("seq1_item:", seq1_item, "|", "seq2_item:", seq2_item)
  ```
- Python doesn't provide a "goto" statement.
- Can attach the `else` statement to loop constructs (for-else):
  ```py
  # Use case: In code that iterates over data but needs to set or check some kind of flag or condition.
  with open("foo.txt") as file:
      for i, line in enumerate(file):
          stripped = line.strip()
          if not stripped:  # If the line is empty.
              break  # Skip the else clause. (Loop is exited early.)
          print(f"=> Line {i + 1}: {stripped}")
      else:  # Execute only if the loop runs to completion.
          raise RuntimeError("No empty lines found.")  # Assuming an empty line is expected.
  ```

## 3.4 Exceptions

- Standard attributes (`e` is an exception object):
  Attribute | Description
  ----------|------------
  `e.args` | Tuple. In most cases, this is a one-item tuple.
  `e.__cause__` | Previous exception if the exception (**expected**) was raised and chained while handling another exception.<br />E.g. `raise ValueError("Bad input") from e`
  `e.__context__` | Previous exception if the exception (**unexpected**) was raised while handling another exception. (Programming mistake)
  `e.__traceback__` | Stack trace object.
- `e` is only accessible inside the associated except block.
- Use `Exception` type to catch all exceptions except those related to program exit (e.g. `SystemExit`):
  ```py
  try:
      nan = int("NaN")
  except Exception as e:
      # Use !r to convert to string with __repr__.
      print(f"An error occurred: {e!r}")
  ```
- `try` statement supports an `else` clause (try-except-else):
  ```py
  try:
      file = open("bar.txt", "rt")
  except FileNotFoundError as e:
      print(f"Unable to open bar: {e}")
      data = ""
  else:  # executed if the try block doesn't raise an exception.
      data = file.read()
      file.close()
  ```

### 3.4.1 The Exception Hierarchy

- Exceptions are organized into a **hierarchy via inheritance**. Instead of targeting specific errors (e.g. `IndexError`, `KeyError`), you can focus on more general **categories of errors** (e.g. `LookupError`).
  ![3-1-exception-categories](images/3-1-exception-categories.png)
- `BaseException` class is **rarely used** because it matches all possible exceptions. This includes **exceptions used for control flow**.
- `ValueError` exception is commonly raised when a **bad input** value is given to an operation.
- Other built-in exceptions that inherit from `Exception` (aren't part of any exception group):
  ![3-2-other-built-in-exceptions](images/3-2-other-built-in-exceptions.png)

### 3.4.2 Exceptions and Control Flow

- Normally, exceptions are for handling errors. But, a few exceptions are used for control flow.
  ![3-3-exceptions-used-for-control-flow](images/3-3-exceptions-used-for-control-flow.png)
- `signal` library module can be used to control the delivery of SIGINT (`KeyboardInterrupt`).

### 3.4.5 Exception Tracebacks

- Use `traceback` module to produce the traceback message:
  ```py
  import traceback
  
  # To get a list of traceback messages.
  tb_lines = traceback.format_exception(type(e), e, e.__traceback__)
  ```

## *3.5 Context Managers and the `with` Statement

- `with <obj>` statement allows a sequence of statements to execute inside a **context** that is controlled by a **context manager** - the value returned by `__enter__()`.
- When the `with <obj>` statement executes, `<obj>.__enter__()` is called to signal that a new context is being entered.
- When the `with <obj>` statement ends, `<obj>.__exit__(type, value, traceback)` is called. 
  - If **no exception** is raised, all three arguments are set to `None`. 
  - Return `True` to indicate that the raised exception was handled and will not propagate.
  - Return `None` or `False` to **propagate** the exception.
- `with <obj> [as <var>]` - The value returned by `<obj>.__enter__()` is placed into `<var>`.
- `contextlib` standard library module contains utilities for context managers.
- [4.17 Context manager protocol reference](#417-context-manager-protocol)

## 3.6 Assertions and `__debug__` - `assert`

- Introduce **debugging code**.
- Example:
  ```py
  # test is an expression that evaluate to True or False.
  # Raise an "AssertionError" exception if test evaluates to False.
  assert test [, msg]
  ```
- Won't be executed if Python is run in **optimized mode**.
- Primarily used to check invariants that should always be true. Else, it indicates a bug.
  ```py
  # Assuming n is always valid.
  def factorial(n):
      assert n > 0, "must supply a positive value"
      result = 1
      while n > 1:
          result *= n
          n -= 1
      return result
  ```
- Serve as a kind of "**smoke test**" (crash with a failed assertion upon import).

# 4 Objects, Types, and Protocols

## 4.1 Essential Concepts

- Operators are ultimately mapped to methods. E.g. `a + 10` executes `a.__add__(10)`.

## 4.2 Object Identity and Type

- `id()` returns the identity of an object.
- `is` and `is not` operators compare the **identities** of two objects.
- Different ways to compare two objects:
  ```py
  def compare(a, b):
      if a is b:
          print("Same object")
      if a == b:
          print("Same value")
      if type(a) is type(b):
          print("Same type")
  ```
- Preferred way to check a value against a type (inheritance):
  ```py
  if isinstance(a, (list, tuple)):  # Can check against many types.
      max_val = max(a)
  ```
  - Often not as useful as you might imagine (due to inheritance).

## 4.3 Reference Counting and Garbage Collection

- Reference count examples:
  ```py
  # Increase the reference count.
  a = 37
  b = a        
  c = []  # Except this.
  c.append(b)
  
  # Decrease the reference count.
  del a
  b = 42
  c[0] = 2

  # To get the reference count.
  import sys
  sys.getrefcount(a)
  ```
- Reference count is often much higher. For immutable data (e.g. `int`, `str`), the interpreter shares objects between different parts of the program in order to converse memory.
- An object is garbage collected when its reference count reaches zero.
- In case of circular dependency, objects can't be garbage collected immediately in response to `del <obj>` statements. The destruction of the objects will be **delayed** until a **cycle detector** executes (run periodically).
- Use `gc.collect()` to immediately invoke the cyclic garbage collector.
- One of the use cases for manually deleting objects:
  ```py
  # Example: When working with gigantic data structures.
  def some_calculation():
      data = create_giant_data_structure()
      # Use data for some part of a calculation...

      # Release the data - Indicate that the data is no longer needed, and can be garbage collected at this point.
      del data

      # Calculation continues...
  ```

## 4.4 References and Copies

- Two types of copy:
  ```py
  a = [1, 2, [3, 4]]

  # 1. Shallow copy
  b = list(a)           # <--

  # 2. Deep copy (Discouraged)
  import copy
  b = copy.deepcopy(a)  # <--
  b[2][0] = -100
  print("b:", b)        # b: [1, 2, [-100, 4]]
  print("a:", a)        # a: [1, 2, [3, 4]]
  ```
- Deep copy:
  - Create a new object and **recursively copies** all the objects it contains.
  - Use of `deepcopy()` is **discouraged**.
  - Slow and often unnecessary.
  - **Won't work** with objects that involve system or runtime state (e.g. open files, network connections, threads, generators)

## 4.6 First-Class Objects

- All values are objects.
- All objects (**everything**) are first-class objects.
- All objects that can be **assigned to a name** can be **treated as data** (can be stored as variables, passed as arguments, returned from functions, and compared against other objects).
- Placing functions or classes in a dictionary is a **common technique** for eliminating complex `if-elif-else` statements:
  ```py
  # Write using if-elif-else statements.
  if format == "text":
      formatter = TextFormatter()
  elif format == "csv":
      formatter = CSVFormatter()
  elif format == "html":
      formatter = HTMLFormatter()
  else:
      raise RuntimeError("Bad format")
  
  # Rewrite using a dictionary.
  _formats = {
    "text": TextFormatter,
    "csv": CSVFormatter,
    "html": HTMLFormatter
  }

  if format in _formats:
      formatter = _formats[format]()
  else:
      raise RuntimeError("Bad format")
  ```

## 4.7 Using `None` for Optional or Missing Data

- Frequently used as the default value of optional arguments.
- `None` is a **singleton**.
- To test against `None`:
  ```py
  if value is None:
      print('"value" data is missing.')
  ```
- **Not recommended** to test `None` using `==`, even though it also works.

## 4.8 Object Protocols and Data Abstraction

- Python does not verify correct program behavior in advance.
- The behavior of an object is determined by a dynamic process that involves the **dispatch of special methods** - `__<method>__()`.
- E.g. `x * y` is mapped to `x.__mul__(y)` internally.
- **Special methods** are associated with different **categories of core interpreter features** (aka **protocol**).

## *4.9 Object Protocol

![4-1-methods-for-object-management](images/4-1-methods-for-object-management.png)
- `SomeClass(args)` is translated into:
  ```py
  x = SomeClass.__new__(SomeClass, args)
  if isinstance(x, SomeClass):  # <-- Ref. 1
      x.__init__(args)
  ```
- `__init__()` is the most common method to be implemented.
- Use of `__new__()` almost always indicates the presence of **advanced logic** related to instance creation. E.g. to bypass `__init__()`, to implement singleton or caching.
- *Ref. 1:* `__new__()` doesn't need to return an instance of the class in question. If not, the call to `__init__()` is **skipped**.
- `__del__()` is invoked when an instance **is about to** be garbage-collected.
  - **Note:** `del <obj>` **only decrements the reference count** and doesn't necessarily result in a call to `__del__()`.
- `__repr__()` is called by `repr()`.
- `__repr__()` **conventions**:
  ```py
  a = [2, 3, 4, 5]    

  # Return an expression string that can be evaluated to re-create the object using eval().
  s = repr(a)         
  b = eval(s)     # <-- Turns `s` back into a list.

  # Return a string of form <...message...>, if a expression string can't be re-created.
  g = (x + 1 for x in a)
  print(repr(g))  # <-- "<generator object <genexpr> at ...>"
  ```

## 4.10 Number Protocol

![4-2-methods-for-mathematical-operations](images/4-2-methods-for-mathematical-operations.png)
- How the interpreter evaluates `x + y`:
  - **Normal case** - Invoke `x.__add__(y)`. If it fails by returning `NotImplemented`, invoke the method with reversed operand - `y.__radd__(x)`.
  - **Special case** - If `y` is a subtype of `x`, invoke `y.__radd__(x)`.
- If in-place operators, such as `__iadd__()`, `__isub__()`, are undefined, `a += b` is evaluated using `a = a + b`.
- There're **no methods** to redefine logical operators (`and`, `or`, `not`).

## 4.11 Comparison Protocol

![4-3-methods-for-instance-comparison-and-hashing](images/4-3-methods-for-instance-comparison-and-hashing.png)
- `is` operator can't be redefined.
- `__bool__()` is executed when an object is tested as conditional expression:
  ```py
  if a:  # Execute a.__bool__()
      pass
  ```
  - If `__bool_()` is undefined, `__len__()` is used.
  - If both `__bool_()` and `__len__()` are undefined, an object is considered to be `True`.
- The **default implementation** of `__eq__()` compares objects by identity using the `is` operator.
- `__ne__()` can be used to implement special processing for `!=`, but is **usually not required** as long as `__eq__()` is defined.
- How the interpreter evaluates `a < b` (Same rules for `<`,`>`, `<=`, `>=`):
  - **Normal case** - Invoke `a.__lt__(b)`. If it fails by returning `NotImplemented`, invoke the method with reversed operand - `b.__gt__(a)`.
  - **Special case** - If `b` is a subtype of `a`, invoke `b.__gt__(a)`.
- `NotImplemented` object is **not the same** as the `NotImplementedError` exception.
- To **sort** objects or use `min()` or `max()`, `__lt__()` must be minimally defined.
- `@total_ordering` **class decorator** in the `functools` module can generate all comparison methods as long as you minimally implement `__eq__()` and one of the other comparisons.
- **Sets** and **dictionary keys** rely on the object's `__hash__()` to work properly.
- `__eq__()` should always be defined together with `__hash__()`. Since it's possible for two objects to have the same hash value, `__eq__()` is necessary to resolve collisions.

## 4.12 Conversion Protocols

![4-4-methods-for-conversions](images/4-4-methods-for-conversions.png)
- `__format__()` examples:
  ```py
  # Call x.__format__("spec")
  f"{x:spec}"
  format(x, "spec")
  "x is {0:spec}".format(x)
  ```
  - There's a standard set of conventions used for the built-in types.
  - More details about **string formatting** in **Chapter 9**.
- Python **never performs implicit type conversions** using conversion methods.
- `__index__()`:
  - Performs an **integer conversion** of an object when it's used in an operation that requires an integer value.
  - E.g. if `items` is a list, `items[x]` executes `items[x.__index__()]` if `x` is not an integer.
  - Used in base conversions such as `oct(x)` and `hex(x)`.

## 4.13 Container Protocol

![4-5-methods-for-containers](images/4-5-methods-for-containers.png)
- Used by objects that want to implement containers (e.g. `list`, `dict`, `set`)
- Example:
  ```py
  a = [1, 2, 3, 4, 5, 6]
  len(a)                  # a.__len__()
  x = a[2]                # a.__getitem__(2)
  a[1] = 7                # a.__setitem__(1, 7)
  del a[2]                # a.__delitem__(2)
  5 in a                  # a.__contains__(5)


  # Slicing operations
  x = a[1:5]              # a.__getitem__(slice(1, 5, None))
  a[1:3] = [10, 11, 12]   # a.__setitem__(slice(1, 3, None), [10, 11, 12])
  del a[1:4]              # a.__delitem__(slice(1, 4, None))
  ```
- **Multidimensional slicing**:
  - No part of Python or its standard library make use of it.
  - Purely for third-party libraries such as `numpy`.
  ```py
  from numpy import matrix
  
  m = matrix([
      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
      [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
      [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
      [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
  ])

  a = m[0:3:2]
  b = m[1:3, 5:9]
  c = m[0:3:2, 5:9:3]
  m[1:4, 6:7] = 666

  # Use ... to denote trailing or leading dimensions
  m[1:3, ...] = 888

  # The value passed to methods is a tuple.
  a = m[..., 5:7]  # a = m.__getitem__((Ellipsis, slice(5, 7, None)))
  ```

## *4.14 Iteration Protocol

- `__iter__()`:
  - Implemented by instances that support iteration. 
  - Returns an **iterator**. 
    - An iterator implements `__next__()` that returns the next object or raises `StopIteration` to signal the end of iteration.
  - A **generator function** involving `yield` is common way to implement an iterator because it conform to the iteration protocol.
    - `yield` pauses the execution and returns a value, while maintaining its state so it can be resumed later.
    ```py
    class FRange:
        def __init__(self, start, stop, step):
            self.start = start
            self.stop = stop
            self.step = step

        def __iter__(self):
            x = self.start
            while x < self.stop:
                # Return `x` and pause the function.
                yield x  # <--
                # Run the next time the function resumes.
                x += self.step
    ```
- `__reversed__()`:
  - An **optional** reversed iterator.
  - Used by the built-in `reversed()`:
    ```py
    for x in reversed(s):
        print(x)
    
    # Output:
    #   3
    #   2
    #   1
    ```

## 4.15 Attribute Protocol

![4-6-methods-for-attribute-access](images/4-6-methods-for-attribute-access.png)
- `__getattr__()`:
  - Invoked when the `__getattribute__()` can't locate the attribute.
  - **Default behavior** is to raise an `AttributeError` exception.
- User-defined classes can define **properties** and **descriptors** for more fine-grained control of attribute access. More details in **Chapter 7**.

## 4.16 Function Protocol

- An object can implement `__call__()` to emulate a function.
- E.g. `x(arg1, arg2)` invokes `x.__call__(arg1, arg2)`.

## *4.17 Context Manager Protocol

![4-7-methods-for-context-managers](images/4-7-methods-for-context-managers.png)
- Primary use - To simplify the resource control involving system state (e.g. open files, network connections, locks).
- [More details in 3.5](#35-context-managers-and-the-with-statement)

## 4.18 Final Words: On Being Pythonic

- Three **commonly used** protocols:
  1. [Object Protocol](#49-object-protocol)
      - `__repr__()` makes the state of an object easy to observe, facilitating debugging using `print()` or a logging library.
  2. [Iteration Protocol](#414-iteration-protocol)
      - Many core parts of Python and the standard library are designed to work with iterable objects. By supporting iteration, you'll automatically get extra functionality.
  3. [Context Manager Protocol](#417-context-manager-protocol)

# 5 Functions

## 5.1 Function Definitions

- `TypeError` exception is raised when the order and number of arguments mismatch the parameters given in the function definition.

## 5.2 Default Arguments

- Default arguments are **evaluated once** when the function is first defined.
  - Often leads to **surprising behavior** if **mutable objects** are used as a default:
    ```py
    # Buggy code:
    def func(x, items=[]):
        items.append(x)
        return items
    
    func(1)  # -> [1]
    func(2)  # -> [1, 2]
    func(3)  # -> [1, 2, 3]
    
    
    # Proper way:
    def func(x, items=None):
        if items is None:
            items = []
        items.append(x)
        return items
    ```
- **Best practice:** Only use **immutable objects** for default arguments.

## 5.3 Variadic Arguments (Positional)

- `*` is used as a **prefix** on the **last parameter**.
  ```py
  def product(first, *args):
      pass
  ```
- All of the extra arguments are placed into the `args` as a **tuple**.

## 5.4 Keyword Arguments

- Explicitly naming parameters:
  ```py
  def func(w, x, y, z):
      pass
  
  # Keyword arguments.
  func(x=3, y=22, w="hello", z=[1, 2])
 
  # TypeError: Multiple values fo w.
  func(3, 22, w="hello", z=[1, 2])
  ```
- ***`TypeError` exception** is raised when:
  - Omit any of the required parameters.
  - Keyword name doesn't match any of the parameter names.
- Parameters after a `*` argument **forces** the use of keyword arguments:
  ```py
  def read_data(filename, *, debug=False):
      data = "Some data"
      return data
  
  data = read_data("Data.csv", True)  # TypeError exception is raised
  data = read_data("Data.csv", debug=True)
  ```

## 5.5 Variadic Keyword  Arguments

- Prefix the last argument with `**` to place all the extra keyword arguments in a **dictionary**.
- The order of items in the dictionary is guaranteed to match the order in which keyword arguments were provided.
- Useful for defining functions that accept a large number of potentially open-ended configuration options.

## 5.6 Functions Accepting All Inputs

- The combined use of `*args` and `**kwargs` is **commonly used to write wrappers, decorators, proxies** and so on.
- Example:
  ```py
  # The function you want to create a wrapper for.
  def parse_lines(lines, separator=",", types=(), debug=False):
      for line in lines:
          print("Processing...")

  # Wrapper
  # Benefit: 
  # - Doesn't need to know about the arguments of parse_lines().
  # - Simplify the maintenance of the parse_file().
  def parse_file(filename, *args, **kwargs):          # <--
      with open(filename, "rt") as file:
          return parse_lines(file, *args, **kwargs)   # <--
  ```

## 5.7 Positional-Only Arguments

- Many built-in functions only accept arguments by position, indicated by the presence of `/` in the function signature. E.g. `len()`, `abs()`, `range()`, and so on. 
- Example:
  ```py
  # All arguments before the `/` can only be specified by position.
  def func(x, y, /):
      pass

  func(1, 2)    # Ok
  func(1, y=2)  # Error


  # Use case: To avoid name clashes between argument names.
  import time

  # **kwargs might causes name clashes. E.g. seconds parameter.
  def after(seconds, func, /, *args, **kwargs):
      time.sleep(seconds)
      return func(*args, **kwargs)

  # Force the use of keyword arguments.
  def duration(*, seconds, minutes, hours):
      return seconds + 60 * minutes + 3600 * hours

  # seconds=20 will be placed in **kwargs.
  after(5, duration, seconds=20, minutes=3, hours=2)
  ```

## 5.8 Names, Documentation Strings, and Type Hints

Attribute | Description
----------|------------
`__name__` | Get the function name.
`__doc__` | Store the documentation string.
`__annotations__` | Store hints in a dictionary that maps argument names to hints.

## 5.9 Function Application and Parameter Passing

- It's common for **functions with side effects** to return `None`.
- Use `*` or `**` to pass arguments using a sequence or mapping:
  ```py
  def func(x, y, z):
      print("Processing...")

  # Pass a sequence as arguments.
  s = (1, 2, 3)
  result = func(*s)

  # Pass a mapping as keyword arguments.
  d = {"x": 1, "y": 2, "z": 3}
  result = func(**d)
  ```

## 5.10 Return Values

- If **no value** is specified or you **omit** the `return` statement, `None` is returned.
- Return **named tuple** example:
  ```py
  from typing import NamedTuple

  class ParseResult(NamedTuple):
      name: str
      value: str

  def parse_value(text):
      parts = text.split("=", 1)
      return ParseResult(parts[0].strip(), parts[1].strip())
  ```

## 5.12 Scoping Rules

- Each time a function executes, a **local namespace** is created.
- Names (free variables) that are **used but not assigned** in the function body are found in the **global namespace** (enclosing module).
- Two types of **name-related errors**:
  1. `NameError` - Looking up an **undefined variable** in the **global environment**.
  2. `UnboundLocalError`
      - Looking up a **local variable** that **hasn't been assigned** a value.
      - Often a result of **control flow bugs**.
      ```py
      # Example 1: Control flow bugs.
      def func(x):
          if x > 0:
              y = 42
          return x + y  # y not assigned if conditional is false.
      
      func(10)    # Returns 52
      func(-10)   # UnboundLocalError: y referenced before assignment.


      # Example 2: Careless use of in-place assignment operators.
      def func():
          n += 1  # UnboundLocalError: n is used before being assigned an initial value (n = n + 1).
      ```
- *Variables **never change their scope** (either global or local), determined at **function definition time**.
  ```py
  x = 42
  def func():
      print(x)  # Since x is declared inside func(), x is determined as a local variable. Accessing x (unassigned) raises a UnboundLocalError.
      x = 13    # Mark x as local variable.
  ```
- `global` declares names as belonging to the global namespace.
  - **Note:** Use of `global` is usually considered **bad practice**.
  - Use an instance of a `class` to modify and manage state instead.
  ```py
  x = 42
  y = 37

  def modify_global_var():
      global x          # <--
      x = 13
      y = 0

  modify_global_var()   # x: 13, y: 37


  # Alternative to modifying global variables to manage state.
  class Config:
      x = 42
  
  def func():
      Config.x = 13
  ```
- **Nested function**
  - Variables in nested functions are resolved first in the local scope, then in successive enclosing scopes (from innermost to outermost).
  - Inner functions can't modify local variables in outer functions.
  - Use `nonlocal` to **modify** outer function variables.
  - Use of nested functions and `nonlocal` declarations is **not common**.
    - No outside visibility, which complicate testing and debugging.
    - **Use case:** To break complex calculations into smaller parts and hiding internal implementation details.

## 5.13 Recursion

- There's a limit (**default: 1,000**) on the depth of recursive function calls.
- Use `sys.getrecursionlimit()` to check the current maximum recursion depth.
- Although the limit can be increased via `sys.setrecursionlimit()`, programs are still limited by the stack size enforced by the host OS.
- If the **limit is exceeded**, a `RuntimeError` exception is raised.
- In practice, limit issues only arise when working with **deeply nested recursive data structures** (e.g. **trees**, **graphs**).

## 5.14 The `lambda` Expression

- Anonymous (aka unnamed) function
  ```py
  # Arguments are comma-separated.
  a = lambda x, y: x + y
  r = a(2, 3)
  ```
- **Can't have** multiple statements or non-expression statements (e.g. `try`, `while`).
- **Use case:** To define small callback functions.
  ```py
  result = sorted(words, key=lambda word: len(set(word)))
  ```
- Caution when contains **free variables**.
  ```py
  x = 2
  f = lambda y: x * y
  x = 3
  g = lambda y: x * y

  # x is 3 at the time of evaluation (aka late binding).
  print(f(10))  # 30
  print(g(10))  # 30

  
  # To capture variable values at the time of definition.
  # This works because default arguments are only evaluated at the time of definition.
  x = 2
  f = lambda y, x=x: x * y  # <--
  x = 3
  g = lambda y, x=x: x * y  # <--
  
  print(f(10))  # 20
  print(g(10))  # 30
  ```

## 5.15 High-Order Functions

- Means that functions can be **passed as arguments**, **placed in data structures**, and **returned by a function**.
- When a function is **passed as arguments**, it implicitly **carries information related to the environment** (aka **closure**) in which the function was defined.
  - **Closures** and **nested functions** are useful when writing **lazy or delayed evaluation** code.
  - In closure, binding to variables is **not a "snapshot"**. Closure points to variables and values that they were **most recently assigned**. See example 2 below.
  - **Ref. 1:** Use **default arguments** to capture a copy of variables.
  ```py
  # Example 1:
  def main():
      name = "Guido"
      
      def greeting():
          print("Hello", name)

      after(1, greeting)  # Print "Hello Guido"

  # Example 2:
  def make_greetings(names):
      funcs = []
      for name in names:
          funcs.append(lambda: print("Hello", name)) # <--

          # Ref. 1
          # funcs.append(lambda name=name: print("Hello", name))

      return funcs

  a, b, c = make_greetings(["Guido", "Ada", "Margaret"])
  
  # All print "Hello Margaret"
  a()
  b()
  c()
  ```

## 5.16 Argument Passing in Callback Functions

- A design issue concerning the use of functions and functional programming (**function composition**).
- **Method 1:** Use a **zero-argument** `lambda` expression (aka thunk):
  - A general-purpose way to delay the evaluation.
  ```py
  after(10, lambda: add(2, 3))  # <--
  ```
- **Method 2:** Use `functools.partial()` to create a **partially evaluated** function.
  ```py
  from functools import partial
  
  def func(a, b, c, d):
      print(a, b, c, d)
  
  g = partial(func, 1, 2, d=4)  # <--
  g(3)    # func(1, 2, 3, 4)
  g(10)   # func(1, 2, 3, 4)
  ```
- Semantic distinction:
  Subject | `partial()` | Zero-argument `lambda`
  --------|-------------|-----------------------
  Arguments are evaluated and bound | when the partial function is first defined. | when the `lambda` function is executed (everything is delayed).
- Objects (aka callables) created by `partial()` can be **serialized into bytes**, **saved in files**, and **transmitted across network connections** (Using the `pickle` standard library module).
- **Method 3:** Accept callback arguments separately **as arguments to the outer calling function**.
  ```py
  def after(seconds, func, *args):
      time.sleep(seconds)
      func(*arg)
  
  after(10, add, 2, 3)
  ```

## 5.17 Returning Results from Callbacks

- It's difficult for the caller to identify the cause of the exception because it could be raised by either the **outer function** or the **callback function**.
- **To distinguish** between these two cases:
  - Option 2 works by deferring the result reporting - when accessing the result via `result()`.
  - Option 2 style of **boxing a result** is an increasingly common pattern. E.g. You can find its use in **concurrency primitives** such as threads and processes.
  ```py
  # Option 1: Use chained exceptions.
  class CallbackError(Exception):
      pass

  def after(seconds, func, *args):
      time.sleep(seconds)
      try:
          return func(*args)
      except Exception as e:
          raise CallbackError("Callback function failed.") from e  # <--

  try:
      r = after(1, add, "5", 6)
  except CallbackError as e:
      print("It failed. Reason:", e.__cause__)

  # Option 2: Use some kind of result instance.
  class Result:
      def __init__(self, value=None, error=None):
          self._value = value
          self._error = error

      def result(self):
          if self._error:
              raise self._error
          return self._value
  
  def after_r(seconds, func, *args):
      time.sleep(seconds)
      try:
          return Result(value=func(*args))    # <--
      except Exception as e:
          return Result(error=e)              # <--

  r = after_r(1, add, 2, 3)
  print(r.result())  # Print 5

  t = after_r(1, add, "2", 3)
  print(t.result())  # Raise TypeError
  ```

## 5.18 Decorators

- A function that create a **wrapper** around another function to **alter** or **enhance** the behavior.
- Denoted using the `@` symbol.
  ```py
  # After func() definition, it is passed to decorate(), which returns 
  #   an object that replaces the original func().
  @decorate
  def func(x):
      pass
  
  # The preceding code is shorthand for the following:
  def func(x):
      pass

  func = decorate(func)
  ```
- Decorator implementation example (**no arguments**):
  - Wrappers hide the original function metadata (see [Section 5.8](#58-names-documentation-strings-and-type-hints)).
  - **Best practice:** Use `@wraps()` decorator to **copy function metadata**.
  ```py
  from functools import wraps

  # Decorator definition:
  def trace(func):
      @wraps(func)  # Copy func() metadata to call().
      # Wrapper
      def call(*args, **kwargs):  # Arguments for func()
          # Additional processing that the decorator adds.
          print("Calling", func.__name__)
          
          # execute func() and return its result.
          return func(*args, **kwargs)
      return call

  # Decorator usage:
  @trace
  def square(x):
      return x * x
  ```
- The **order** in which decorators appear **might matter**.
  - In **class definitions**, `@classmethod` and `@staticmethod` often have to be placed at the outermost level because they return objects that're different than a normal function.
- Decorators can **accept arguments** (via **decorator factory**).
  ```py
  from functools import wraps

  def create_decorator(arg):  # Decorator factory
      def decorator(func):
          @wraps(func)
          def wrapper(*args, **kwargs):
              print(arg)      # Use arg inside the wrapper.
              return func(*args, **kwargs)
          return wrapper
      return decorator

  # To reuse the decorator instance.
  decorator = create_decorator("argument value")

  @decorator
  def func1():
      pass
  
  @decorator
  def func2():
      pass
  ```
- Decorators **don't necessarily have to replace** the original function.
  ```py
  _event_handlers = {}

  def event_handler(event):  # Decorator factory
      def register_function(func):  # Decorator without wrapper
          # Register an event handler at function definition time.
          _event_handlers[event] = func  
          return func
      return register_function

  @event_handler("BUTTON")
  def handle_button(msg):
      pass

  @event_handler("RESET")
  def handle_reset(msg):
      pass
  ```

## 5.19 Map, Filter, and Reduce

- Common list operations.
- Can be implemented using **list comprehensions**, **generator expressions** and built-in functions.
- `map()` and `filter()` are the same as their **generator** equivalents.
- Example:
  ```py
  nums = [1, 2, 3, 4, 5]

  # Map
  squares_lc = [x * x for x in nums]
  squares_gen = (x * x for x in nums)
  squares_fn = map(lambda x: x * x, nums)

  # Filter
  nums_gt_lc = [x for x in nums if x > 2]
  nums_gt_gen = (x for x in nums if x > 2)
  nums_gt_fn = filter(lambda x: x > 2, nums)

  # Reduce
  from functools import reduce
  total_fn = reduce(lambda x, y: x + y, nums)
  
  total_agg = sum(nums)
  ```

## 5.20 Function Introspection, Attributes, and Signatures

![5-1-function-attributes](images/5-1-function-attributes.png)
- Useful in **debugging** and **logging**.
- Functions can have **attributes** attached to them.
  - Attributes are not visible within the function body. (Not local variables and not in the global namespace)
  - **Use case:** To store extra metadata (aka function tagging).
- `inspect.signature()` is useful for obtaining detailed information about the parameters.
  - **Use case:** To compare between signatures (might be useful in frameworks).
    ```py
    import inspect
    
    def func1(x, y):
        pass
    
    def func2(x, y):
        pass
    
    assert inspect.signature(func1) == inspect.signature(func2)
    ```
  - To override signature metadata:
    ```py
    def func(x, y, z=None):
        pass

    # Hide the z parameter from further inspection.
    func.__signature__ = inspect.signature(lambda x, y: None)
    ```

## 5.21 Environment Inspection

- To inspect the execution environment of a function:
  Built-in function | Description
  ------------------|------------
  `globals()` | Return the dictionary that's serving as the global namespace.<br />The same as `<func>.__globals__`. See [Section 5.20](#520-function-introspection-attributes-and-signatures).
  `locals()` | Return a dictionary containing all **local** and **closure** variables.<br />Not the actual data structure (Changing an item in this dictionary has no effect on the underlying variable).
- Use `inspect.currentframe()` or `sys._getframe(0)` to get the **current stack frame** of a function.
- Use `<frame>.f_back` or `sys._getframe(1)` to get the **caller's stack frame**.
- Stack frame attributes:
![5-2-frame-attributes](images/5-2-frame-attributes.png)
- Useful for **debugging** and **code inspection**.

## 5.22 Dynamic Code Execution and Creation

- `exec()` executes within the local and global namespace of the caller.
- Changes to local variables have **no effect**.
  ```py
  def func():
      x = 10
      exec("x = 20")
      print(x)  # Print 10
  ```
- `exec()` can accept dictionary objects that serve as the global and local namespace.
- **Use case:** Creating functions and methods.
  - Used in various parts of the standard library (E.g. `namedtuple()`, `@dataclass`).
  ```py
  def make_init(*names):
      params = ",".join(names)
      code = f"def __init__(self, {params}):\n"
      for name in names:
          code += f"  self.{name} = {name}\n"
      d = {}
      exec(code, d)
      return d["__init__"]


  class Vector:
      __init__ = make_init("x", "y", "z")
  ```

## 5.23 Asynchronous Functions and `await`

- Aka coroutines, awaitables
- Mostly used by programs involving **concurrency** and the `asyncio` module.
- Async functions **never execute on their own**.
- Async functions can call other async functions using an `await`.
  ```py
  async def main():
      for name in ["Paula", "Thomas", "Lewis"]:
          a = await make_greeting(name)  # <--
          print(a)

  asyncio.run(main())
  ```
- Support for asynchronous functions **has to built as a special case**. E.g.:
  - **Async context manager** (context manager protocol):
    ```py
    class AsyncManager(object):
        def __init__(self, x):
            self.x = x
        
        async def yow(self):
            print("yowing...")

        async def __aenter__(self):  # <--
            return self
        
        async def __aexit__(self, ty, val, tb):  # <--
            pass

    async def main_mgr():
        async with AsyncManager(42) as mgr:  # <--
            await mgr.yow()

    asyncio.run(main_mgr())
    ```
  - **Async iterator** (iteration protocol) - Implement `__aiter__()` and `__anext__()`. These are used by the `async for` statement.
