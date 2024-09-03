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
  ``` py
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
  ![common-string-methods](images/common-string-methods.png)
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
  
  a = t | s # Union {'MSFT', 'CAT', 'HPE', 'AA', 'IBM'}
  b = t & s # Intersection {'IBM', 'MSFT'}
  c = t - s # Difference { 'CAT', 'HPE' }
  d = s - t # Difference { 'AA' }
  e = t ^ s # XOR { 'CAT', 'HPE', 'AA' }
  
  s.update({"JJ", "GE", "ACME"}) # Adds multiple items

  t.remove("IBM")   # Raise KeyError if absent
  t.discard("SCOX") # Remove if exists
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
  for i in range(8, 1, -1):
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
