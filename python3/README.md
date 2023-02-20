# Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Brython: Running Python on the Frontend](#brython-running-python-on-the-frontend)
- [Installing Python 3](#installing-python-3)
- [Print Statement, Comments and ProgramFlow](#print-statement-comments-and-programflow)
- [Running a Python (.py) file](#running-a-python-py-file)
- [Variables](#variables)
- [Data Types](#data-types)
- [Type Casting](#type-casting)
  - [Implicit Type Casting](#implicit-type-casting)
  - [Explicit Type Casting](#explicit-type-casting)
- [Numbers](#numbers)
  - [Numbers: Overview](#numbers-overview)
  - [Numbers: Arithmetic Operations](#numbers-arithmetic-operations)
  - [Numbers: Type Casting](#numbers-type-casting)
  - [Numbers: Built-In Functions](#numbers-built-in-functions)
- [Strings](#strings)
  - [Strings: Operations](#strings-operations)
  - [Strings: Built-in Functions](#strings-built-in-functions)
  - [Strings: Basic Methods](#strings-basic-methods)
  - [Strings: Multi-line Strings](#strings-multi-line-strings)
  - [Strings: Formatted Strings](#strings-formatted-strings)
  - [Strings: User Input](#strings-user-input)
  - [Strings: Split and Join](#strings-split-and-join)
- [Boolean](#boolean)
  - [Boolean: Type Casting](#boolean-type-casting)
  - [Boolean: Comparison and Logical Operators and Membership](#boolean-comparison-and-logical-operators-and-membership)
- [Lists](#lists)
  - [Lists: Built-in Functions](#lists-built-in-functions)
  - [Lists: Basic Methods](#lists-basic-methods)
  - [Lists: List Manipulation Methods](#lists-list-manipulation-methods)
  - [Lists: Matrix (Multi-Dimensional Lists)](#lists-matrix-multi-dimensional-lists)
  - [Lists: Example](#lists-example)
- [Tuples](#tuples)
  - [Tuple: Overview](#tuple-overview)
  - [Tuples: Methods](#tuples-methods)
- [Sets](#sets)
  - [Sets: Overview](#sets-overview)
  - [Sets: Methods](#sets-methods)
- [Dictionaries](#dictionaries)
  - [Dictionaries: Overview](#dictionaries-overview)
  - [Dictionaries: Built-In Functions](#dictionaries-built-in-functions)
  - [Dictionaries: Basic Methods](#dictionaries-basic-methods)
  - [Dictionaries: CRUD Operations](#dictionaries-crud-operations)
  - [Dictionaries: Joining Dictionaries](#dictionaries-joining-dictionaries)
  - [Dictionaries: Example](#dictionaries-example)
- [Functions](#functions)
  - [Functions: Overview](#functions-overview)
  - [Functions: Keyword (Named) Arguments](#functions-keyword-named-arguments)
  - [Function: Return Statement](#function-return-statement)
- [Conditionals](#conditionals)
  - [Conditions: if, elif, else](#conditions-if-elif-else)
  - [Conditionals: Example 1](#conditionals-example-1)
  - [Conditionals: Example 2](#conditionals-example-2)
- [Loops](#loops)
  - [Loops: Overview](#loops-overview)
  - [Loops: While-Loop](#loops-while-loop)
  - [Loops: For-Loop](#loops-for-loop)
  - [Loops: Break and Continue](#loops-break-and-continue)
  - [Loops: Using Built-in Function - `enumerate()`](#loops-using-built-in-function---enumerate)
- [Filehandling](#filehandling)
- [Exceptions](#exceptions)
- [Classes and Objects](#classes-and-objects)
  - [Classes: Overview](#classes-overview)
  - [Classes: Inheritance](#classes-inheritance)
  - [Classes: Using a Dictionary to Initialize an Object](#classes-using-a-dictionary-to-initialize-an-object)
  - [Classes: Special Methods](#classes-special-methods)
  - [Classes: Checks and Basic Type Validation](#classes-checks-and-basic-type-validation)
- [Modules](#modules)
- [Zip / Unzip](#zip--unzip)
- [Lambda Functions](#lambda-functions)
  - [Lambda Functions: Examples](#lambda-functions-examples)
- [Comprehensions](#comprehensions)
  - [Comprehensions: Lists](#comprehensions-lists)
  - [Comprehension: Dictionaries](#comprehension-dictionaries)
- [Randomness](#randomness)
- [Timeit and Performance](#timeit-and-performance)
- [Example: Crypto Engine](#example-crypto-engine)
- [References](#references)

---

# Overview

- Outputting data and program flow
- Strings, Variables
- Arithmetic Operations and Comparisons
- Lists, Tuples, Sets and Dictionaries
- Conditionals: If, Elif
- Loops: `while` and `for`
- Functions / Return Statements
- Objects, Classes and Inheritance
- List / Dictionary Comprehensions and Lambda Functions (Anonymous Functions)
- Modules
- Exercises, projects and bits and pieces

---

# Brython: Running Python on the Frontend

Brython (Browser Python) is an implementation of Python 3 running in the browser, with an interface to the DOM elements and events. We can use the Brython (Browser Python) to run Python 3 code on the frontend.

To use:

- In your `index.html` add the following script tag and run the `brython()` function on load of the document.

- Use the Live Server extension to launch the html in the Browser

```html
<!DOCTYPE html>
<html>
  <head>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.8.0/brython.min.js"></script>
    <!-- For full functionality use the standard library:
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.8.0/brython_stdlib.js"></script>
-->
  </head>
  <body onload="brython();">
    <script type="text/python3" src="index.py"></script>
  </body>
</html>
```

---

# Installing Python 3

1. **Check if `python3` is already installed**

   ```s
   python3 --version
   ```

2. **Upgrade Python to the latest version**

   ```s
   # Update all packages and repositories
   sudo apt update && sudo apt upgrade -y

   # Upgrade to latest, if exists or else install Python 3
   sudo apt --only-upgrade install python3
   ```

---

# Print Statement, Comments and ProgramFlow

The `print` statement prints the output to the console. Python executes the Print statement(s) in the order they are written (synchronous).

> **Note**: Unlike a lot of popular programming languages, in Python there is no use (not even optional use) of a semi-colon at the end of a statement. Using so, will result in an error.

```py
# This is a comment
print('This is the first line!') # This line is executed first
print('This is the second line!') # This line is executed second
```

---

# Running a Python (.py) file

**From the Shell**:

```s
# Python2 and lesser
python path/to/filename.py

# Python3
python3 path/to/filename.py
```

**In the Python3 REPL**:

```py
# Python3
exec(open("path/to/filename.py").read())

# Python2
variables = {}
execfile("path/to/filename.py", variables)
print variables
```

---

# Variables

Variables are declared by name and then assigned using the assignment (`=`) operator.

```py
name = "Jayanta"
country = "India"
print('Hi, I am ' + name + ' from ' + country + '.')
```

> **Note**: Variables need to be of the correct data type. An incorrect data type will throw an error. We can get around this using [Type Casting](#type-casting)

```py
fruits = 2
print('I have ' + fruits + ' fruits in my hand.')
# TypeError: Can't convert int to str implicitly
```

**Variables can be re-assigned**

```py
name = "Jayanta"
country = "India"
print('Hi, I am ' + name + ' from ' + country + '.') # Hi, I am Jayanta from India.

# Re-assigning variables
name = "Sam"
country = "USA"
print('Hi, I am ' + name + ' from ' + country + '.') # Hi, I am Sam from USA.
```

**Naming Conventions**

The standard variable naming convention in python is a single `word` or `words_separated_by_underscore`. However one could also use a `camelCasedWord`.

---

# Data Types

**The various Data Types in Python are as follows:**

```py
# A String is text enclosed by quotes.
string = 'John'
string_with_single_quote = "John's"
string_with_single_quote_escaped = 'John\'s'

# An Integer is a whole number
integer = 2

# A Float is a decimal number
float_number = 3.14

# Boolean
truthy = True
falsy = False

# List
fruits_list = ["Apple", "Banana", "Mango"]

# Tuple
fruits_tuple = ("Apple", "Banana", "Mango")

# Set
fruits_set = {"Apple", "Banana", "Mango"}
```

**To find what Data type you are dealing with we can use the `type(arg)` method:**

```py
string = "John"
integer = 2
float_number = 3.14
truthy = True

type(string) # Returns: <class 'str'>
type(integer) # Returns: <class 'int'>
type(float_number) # Returns: <class 'float'>
type(truthy) # Returns: <class 'bool'>
type(fruits_list) # Returns: <class 'list'>
type(fruits_tuple) # Returns: <class 'tuple'>
type(fruits_set) # Returns: <class 'set'>
```

More on Data Types and their methods in the sections below.

---

# Type Casting

The conversion of one data type into the other data type is known as **Type Casting** or **Type Conversion** in python.

Type Casting can be of two types:

1. **Implicit Type Casting**
2. **Explicit Type Casting**

---

## Implicit Type Casting

Python converts data type into another data type automatically. In this process, users don’t have to involved.

```py
# Python program to demonstrate
# implicit type Casting

# Python automatically converts
# a to int
a = 7
print(type(a))                          # <class 'int'>
isinstanceof(n, int)                    # True

# Python automatically converts
# b to float
b = 3.0
print(type(b))                          # <class 'float'>
isinstanceof(n, float)                  # True

# Python automatically converts
# c to float as it is a float addition
c = a + b
print(c)
print(type(c))                          # <class 'float'>
isinstanceof(n, float)                  # True

# Python automatically converts
# d to float as it is a float multiplication
d = a * b
print(d)
print(type(d))                          # <class 'float'>
isinstanceof(n, float)                  # True
```

---

## Explicit Type Casting

In this method, Python need user involvement to convert the variable data type into certain data type in order to the operation required.

Python supports a wide variety of in-built functions for Type Casting like:

- `int()`
- `float()`
- `ord()`
- `bin()`
- `oct()`
- `hex()`
- `str()`
- `set()`
- `list()`
- `dict()`
- `tuple()`

**Examples:**

1. **Int to String**: This allowed the int variable to be used inside a string using string concatenation.

   ```py
   # int variable
   fruits = 2

   # Incorrect Use: TypeError: Can't convert int to str implicitly
   print('I have ' + fruits + ' fruits in my hand.')

   # Correct Use: With Type Casting
   print('I have ' + str(fruits) + ' fruits in my hand.')
   ```

2. **Float to Int**: This makes the float lose the decimal value

   ```py
   # float variable
   a = 5.9

   # typecast to int
   n = int(a)

   print(n) # 5
   print(type(n))                       # <class 'int'>
   isinstanceof(n, int)                 # True
   ```

3. **Int to Float**: Returns the number as floating point number

   ```py
   # int variable
   a = 5

   # typecast to float
   n = float(a)

   print(n) # 5.0
   print(type(n))                       # <class 'float'>
   isinstanceof(n, float)               # True
   ```

4. **Special Case: Decimal String to Int**: Throws an Error. Needs to first be converted to float.

   ```py
   # string variable
   a = "5.9"

   # typecast to int
   n = int(a)                           # ValueError: invalid literal for int() with base 10: '5.9'
   n = int(float(a))                    # Correct Implementation

   print(n)                             # 5
   print(type(n))                       # <class 'int'>
   isinstanceof(n, int)                 # True
   ```

---

# Numbers

## Numbers: Overview

As seen earlier, numbers can either be integers or floats.

```py
type(1)   # int
type(-10) # int
type(0)   # int
type(0.0) # float
type(2.2) # float
type(4E2) # float - 4*10 to the power of 2
```

---

## Numbers: Arithmetic Operations

Arithmetic Operations in Python are similar to other programming languages:

- `+`: Addition
- `-`: Substraction
- `*`: Multiplication
- `/`: Division (float). Returns a floating point number.
- `//`: Division (floor). Floors the float into an integer.
- `%`: Modulus. Returns the remainder.
- `**`: Exponent. Returns first number to the power of the second number.

```py
a = 7
b = 2
print('Addition : ', a + b) # 9
print('Subtraction : ', a - b) # 5
print('Multiplication : ', a * b) # 14
print('Division (float) : ', a / b) # 3.5
print('Division (floor) : ', a // b) # 3
print('Modulus : ', a % b) # 1
print('Exponent : ', a ** b) # 49
```

---

## Numbers: Type Casting

```py
# Type Casting Boolean to Int
print(int(True))                # 1
print(int(False))               # 0
```

---

## Numbers: Built-In Functions

```py
pow(5, 2)           # 25 --> like doing 5**2
abs(-50)            # 50 --> Returns the absolute value
round(5.46)         # 5
round(5.468, 2)     # 5.47 --> round to nth digit
bin(512)            # '0b1000000000' -->  binary format
oct(512)            # '0o1000' ---> octal format
hex(512)            # '0x200' --> hexadecimal
ord("A")            # 65 ---> returns an integer representing the Unicode character.
```

---

# Strings

## Strings: Operations

```py
msg = "This is a string."

# Concatenation
print(msg + " " + msg) # This is a string. This is a string.

# Printing multiple strings
print(msg, msg) # This is a string. This is a string.

# Concatenation (using Multiplication)
print(msg * 2) # This is a string.This is a string.
```

---

## Strings: Built-in Functions

```py
str(55.98)          # '55.98'
chr(65)             # 'A' ---> Returns a character based on the ASCII code
```

---

## Strings: Basic Methods

```py
msg = "my name is Jayanta"

# Upper Case: Makes the entire string uppercase
print(msg.upper()) # MY NAME IS JAYANTA

# Lower Case: Makes the entire string lowercase
print(msg.lower()) # my name is jayanta

# Capitalize: Capitalizes only the first character of the string and lowercases the rest
print(msg.capitalize()) # My name is jayanta

# Title: Capitalizes the first character of each word
# Has a quirk: Interprets the word after an apostrophe as a new word so capitalizes it
print(msg.title()) # My Name is Jayanta

home = "this is jayanta's home"
print(home.title()) # This is Jayanta'S Home

# Length of the string
print(len(msg)) # 18

# `String.strip()`: Trims all whitespace characters OR the passed substring from both ends
msg.strip()                         # 'my name is Jayanta' --> No change
" This is Jayanta's home. ".strip() # 'This is Jayanta's home.'
'On an island'.strip('d')           # 'On an islan' --> # Strips all passed characters from both ends.
'anna had a banana'.strip('a')      # 'nna had a banan'

# `String.count(str)`: Count the number of instances of a substring in a string. Case Sensitive.
print(msg.count('jayanta')) # 0
print(msg.count('Jayanta')) # 1
print(msg.count('a'))       # 4

# `String.startsWith(str)`: Returns a boolean whether the string starts with the substring passed
# `String.endsWith(str)`: Returns a boolean whether the string starts with the substring passed
'Need to make fire'.startswith('Need')  # True
'and cook rice'.endswith('rice')        # True

# Slicing: Slicing refers to getting parts of a string. Uses the format: [ start : end : step ]
# - Uses indexes starting at 0.
# - Can use negative indexes to return characters, from the end of the string.
# - Use `string[startIndex:endIndex]` to grab all characters between the specified character at the start index (inclusive) and an end index (not inclusive, i.e. doesn't take the end index).
# - If no end index is specified, Python returns all characters from the start index to the end of the string.
# - If no start index is specified, Python returns all characters from index 0 upto the end index - 1.
# - The `step` allows values to be skipped and chosen with a gap. Default is 1. 2 means skipping one and choosing every second character within the selection.

print(msg[0]) # m
print(msg[0:7]) # my name
print(msg[-1]) # a
print(msg[-7]) # J
print(msg[-7:]) # Jayanta
print(msg[-7:-4]) # Jay
print(msg[:-4]) # my name is Jay
print(msg[0:10:2]) # m aei

# Reversing a string
print(msg[::-1]) # atnayaJ si eman ym

# `String.find(str)`: Find the index of the first occurence of a substring in a string. Returns -1 if not found.
print(msg.find('a'))    # 4
print(msg.find("z"))    # -1

# `String.index(str)`: Find the index of the first occurence of a substring in a string. Returns an error if not found.
print(msg.index('a'))   # 4
print(msg.index("z"))   # ValueError: substring not found

# `String.replace('str', 'str2')`: Replaces all occurences of a substring with another. Returns a new string.
print(msg) # my name is Jayanta
print(msg.replace("Jayanta", "Rohit")) # my name is Rohit

# Membership: Check if a substring exists in a string. Returns boolean: `True` or `False`
print("Jayanta" in msg) # True
print("Jayanta" not in msg) # False
print("Rohit" in msg) # False
print("Rohit" not in msg) # True
```

---

## Strings: Multi-line Strings

Use triple-quotes to start and end a string for it to be a multi-line string

```py
sentence = """The quick brown fox...
...jumps over...
...the lazy dog.
"""

print(sentence)

# Prints the following
# ---------------------
# The quick brown fox...
# ...jumps over...
# ...the lazy dog.
```

---

## Strings: Formatted Strings

Concatenating strings can look messy and hard to read. Python provides us with a function to handle long strings that read in a cleaner format.

> **Similarities with other Languages**: JavaScript Template Strings

```py
name='TERRY'
color = 'RED'

# Using String Concatenation
msg = '[' + name.capitalize() + '] loves the color ' + color.capitalize() + '!'
print(msg) # [Terry] loves the color Red!

# Using Formatted Strings
msg1 = f'[{name.capitalize()}] loves the color {color.capitalize()}!' # As of Python 3.6
print(msg1) # [Terry] loves the color Red!

msg2 = '{} loves the color {}!'.format(name.capitalize(), name2.capitalize())
print(msg2) # [Terry] loves the color Red!
```

---

## Strings: User Input

By default Inputs are type casted into strings.

```py
# Example 1: Strings
name= input('What is your name?: ') # Input: Jayanta
age=input('What is your age?: ') # Input: 31
print('Hello '+ name.title() + '! You are '+ age + ' years old.') # Hello Jayanta! You are 31 years old.

# Example 2: Addition
num1 = input("Enter a digit:") # Input: 4
num2 = input("Enter a second digit:") # Input: 6
print(float(num1) + float(num2)) # 10

# Example 3: Distance Converter
# -----------------------------
# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name
name = input('Enter your name: ')
distance_km = input('Enter distance in km: ')
distance_mi = float(distance_km)/1.609
print(f'Hi {name.title()}! {distance_km}km is equivalent to {round(distance_mi,1)} miles.')
```

---

## Strings: Split and Join

```py
# `String.split(separator)`: Takes in an optional separator and divides a string into an List of substrings separated by the separator. Default separator is " " (space)
str1 = "The quick brown fox jumps over the lazy dog"
str2 = "ABC, DEF, GHI, JKL"

print(str1.split())         # ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
print(str2.(", "))          # ['ABC', 'DEF', 'GHI', 'JKL']


# `separator.join(List)`: Joins a List into a single string separated by the separator
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(", ".join(friends))           # John, Michael, Terry, Eric, Graham
```

---

# Boolean

True or False. Used in a lot of comparison and logical operations in Python

## Boolean: Type Casting

```py
print(bool(True))   # True
print(bool(1))      # True

# All of the below evaluate to False. Everything else will evaluate to True in Python.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool({}))
print(bool(()))
print(bool(''))
print(bool(range(0)))
print(bool(set()))

# See Logical Operators and Comparison Operators section for more on booleans.
```

---

## Boolean: Comparison and Logical Operators and Membership

```py
a = 7
b = 3
a2 = 7
c = a
name = "John"
ex_list = ["ABC", "DEF", "GHI"]
ex_tuple = ("ABC", "DEF", "GHI")
ex_set = {"ABC", "DEF", "GHI"}

# Comparison Operators
print(a == b)                   # False
print(a != b)                   # True
print(a > b)                    # True
print(a >= b)                   # True
print(a < b)                    # False
print(a <= b)                   # False

# Logical Operators
print(not(a == b))              # True

# Membership
print("o" in "John")            # True
print("k" not in "John")        # True
print("ABC" in ex_list)         # True
print("ABC" not in ex_list)     # False
print("ABC" in ex_tuple)        # True
print("ABC" not in ex_tuple)    # False
print("ABC" in ex_set)          # True
print("ABC" not in ex_set)      # False

# Check if they are identical objects occupying the same space in memory (having the same id)
print(a is c)                   # True
print(id(a) == id(c))           # True

print(a == a2)                  # True
print(a is a2)                  # False
print(id(a) == id(a2))          # False

# Check whether specified object is of specified type
isinstanceof(a, int)            # True
isinstanceof(a, float)          # False
isinstanceof(name, str)         # True
isinstanceof(ex_list, list)     # True
isinstanceof(ex_tuple, tuple)   # True
isinstanceof(ex_set, set)       # True
```

---

# Lists

## Lists: Built-in Functions

```py
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911, 130, 328, 535, 740, 308]
animal_list = ["Tiger", "Elephant", "Zebra", "Cheetah", "Boar"]
animal_tuple = ("Tiger", "Elephant", "Zebra", "Cheetah", "Boar")
animal_set = {"Tiger", "Elephant", "Zebra", "Cheetah", "Boar"}
animal_str = "Tiger"

list(animal_tuple)                  # ["Tiger", "Elephant", "Zebra", "Cheetah", "Boar"]
list(animal_set)                    # ["Tiger", "Elephant", "Zebra", "Cheetah", "Boar"]
list(animal_str)                    # ["T", "i", "g", "e", "r"]

# `sorted(iterable, key=key, reverse=reverse)`: Returns a new sorted List (either in ascending or descending).
## key --> wrapper function
## reverse --> Default: False

## Ascending Order
sorted(animal_list)                 # ['Boar', 'Cheetah', 'Elephant', 'Tiger', 'Zebra']
sorted(animal_str)                  # ['T', 'e', 'g', 'i', 'r'] ---> Note: "T" appears first because of ASCII uppercase characters (65 - 90) appearing before the lowercase characters (97 - 122)

## Descending Order
sorted(animal_list, reverse=True)   # ['Zebra', 'Tiger', 'Elephant', 'Cheetah', 'Boar']

## Using key
numbers = [1,5,-3,7,-2]
sorted(numbers)                     # [-3, -2, 1, 5, 7]
sorted(numbers, key = abs)          # [1, -2, -3, 5, 7]

# `reversed(iterable)`: Returns a 'list_reverseiterator' object
reversed = reverse(animal_list)
print(reversed)                     # <list_reverseiterator object at 0x7f213f4cd070>
print(type(reversed))               # <class 'list_reverseiterator'>
list(reversed(animal_list))         # ['Boar', 'Cheetah', 'Zebra', 'Elephant', 'Tiger']

# `min(list)`: Find the minimum value in a List of Integers or Floats OR find the First element of the list when in ascending order
print(min(cars))            # 130
print(min(friends))         # Eric

# `max(list)`: Find the minimum value in a List of Integers or Floats OR find the First element of the list when in descending order
print(max(cars))            # 911
print(max(friends))         # Terry

# `sum(list)`: Find the sum of the values in a List of Integers or Floats. Throws an error for other types
print(sum(cars))            # 2952
print(sum(friends))         # TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

---

## Lists: Basic Methods

```py
friends = ['John','Michael','Terry','Eric','Graham']
cars = [911, 130, 328, 535, 740, 308]

# Empty List
empty_list = []
empyt_list2 = list()

print(friends)                  #  ['John','Michael','Terry','Eric','Graham']

# Accessing Lists
print(friends[1])               # Michael
print(friends[-1])              # Graham
print(friends[2:4])             # ['Terry', 'Eric']
print(friends[:4])              # ['John','Michael','Terry','Eric']

# Reversing a List
print(friends[::-1])            # ['Graham', 'Eric', 'Terry', 'Michael', 'John']

# `len(list)`: Length of the List
print(len(friends))             # 5

# `List.index(value)`:
print(friends.index('Eric'))    # 3

# `List.count(value)`: Count the number of occurences of the element
print(friends.count('Eric'))    # 1

# `List.reverse()`: Reverse the order of the current List (Doesn't matter if it's an unordered list)
friends.reverse()           # Reverse the current order of the List
cars.reverse()
print(friends)              # ['Graham', 'Eric', 'Terry', 'Michael', 'John']
print(cars)                 # [308, 740, 535, 328, 130, 911]

# `List.sort()`: Sorts an unordered List. Sorts in place, i.e. Mutates original List. Returns None.
friends.sort()              # Sort in Ascending Order
cars.sort()
print(friends)              # ['Eric', 'Graham', 'John', 'Michael', 'Terry']
print(cars)                 # [130, 308, 328, 535, 740, 911]

friends.sort(reverse=True)  # Sort in Descending Order
cars.sort(reverse=True)
print(friends)              # ['Terry', 'Michael', 'John', 'Graham', 'Eric']
print(cars)                 # [911, 740, 535, 328, 308, 130]
```

---

## Lists: List Manipulation Methods

```py
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [911, 130, 328, 535, 740, 308]

# `List.append(element)`: Push element to the end of the stack
friends.append('Fred')
print(friends)                  # ['John', 'Michael', 'Terry', 'Eric', 'Graham', 'Fred']

# `List.insert(index, element)`: Insert element at a particular index
friends.insert(1, 'Allan')
print(friends)                  # ['John', 'Allan', 'Michael', 'Terry', 'Eric', 'Graham', 'Fred']

# `List[index] = element`: Overwrite element at index with new element
friends[1] = 'Tim'
print(friends)                  # ['John', 'Tim', 'Michael', 'Terry', 'Eric', 'Graham', 'Fred']

# `List.extend(list)`: Concatenate a list to the first list. Mutates first list.
friends.extend(cars)
print(friends)      # ['John', 'Tim', 'Michael', 'Terry', 'Eric', 'Graham', 'Fred', 911, 130, 328, 535, 740, 308]

# `List + List`: Concatenates two lists but does not mutate existing list. Returns a new list.
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
cars = [911, 130, 328, 535, 740, 308]
print(friends + cars)   # ['John', 'Tim', 'Michael', 'Terry', 'Eric', 'Graham', 'Fred', 911, 130, 328, 535, 740, 308]
print(friends)          # ['John', 'Michael', 'Terry', 'Eric', 'Graham'] ---> not mutated
print(cars)             # [911, 130, 328, 535, 740, 308] --> not mutated

# `List.remove(element)`: Removes the first occurence of the element from the List or raises ValueError.
friends = ['John', 'Michael', 'Terry', 'John', 'Eric', 'Graham', 'John']
friends.remove('John')
print(friends)                  # ['Michael', 'Terry', 'John', 'Eric', 'Graham', 'John']
friends.remove("Sebastian")     # ValueError: list.remove(x): x not in list

# `List.pop(index)`: Remove the specific index from the List for use. If no index is specified, by default pops off index `-1` or the last element of the List.
lastElement = friends.pop()
print(lastElement)                      # John
print(friends)                          # ['Michael', 'Terry', 'John', 'Eric', 'Graham']
secondElement = friends.pop(1)
print(secondElement)                    # Terry
print(friends)                          # ['Michael', 'John', 'Eric', 'Graham']
secondLastElement = friends.pop(-2)
print(secondLastElement)                # Eric
print(friends)                          # ['Michael', 'John', 'Graham']

# `List.clear()`: Clears the entire list
friends.clear()
print(friends)                          # []

# `del List`: Removes part of the list or deletes the list completely
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']

del friends[2]                          # Removes index 2
print(friends)                          # ['John', 'Michael', 'Eric', 'Graham']

del friends                             # Deletes the entire List
print(friends)                          # NameError: name 'friends' is not defined

# Membership: Check if a element exists in a list. Returns boolean: `True` or `False`
print("Jayanta" in friends)                                 # False
print("Jayanta" not in friends)                             # True
print("Terry" in friends)                                   # True
print("Terry" not in friends)                               # False
print("Terry" in friends and "Jayanta" not in friends)      # True
print("Terry" not in friends or "Jayanta" in friends)       # False

# Copying a List
# - Method 1: `List[:]`
# - Method 2: `List.copy()`
# - Method 3: `list(List)`
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
new_friends = friends[:]                # Copies the entire List
friends.pop()
new_friends2 = friends.copy()           # Copies the entire List
friends.pop()
new_friends3 = list(friends)            # Copies the entire List

print(friends)                          # ['John', 'Michael', 'Terry']
print(new_friends)                      # ['John', 'Michael', 'Terry', 'Eric', 'Graham']
print(new_friends2)                     # ['John', 'Michael', 'Terry', 'Eric']
print(new_friends2)                     # ['John', 'Michael', 'Terry']


# Destructuring / Unpacking
person = ["Bob", 42, 'Manhattan', 'USA', 'Mechanic']
name, *details, profession = person

print(name, profession)                 # Bob Mechanic
print(details)                          # [42, 'Manhattan', 'USA']
```

---

## Lists: Matrix (Multi-Dimensional Lists)

```py
# Sorting
# -------

## Given: Two-dimensional List where each sub-list contains [name_of_item, quantity, total]
groceries=[['milk', 2, 20], ['biscuits', 4, 120], ['juice', 3, 90], ['chocolates', 1, 70]]

## Return sorted list based on first element
sorted(groceries)  ## [['biscuits', 4, 30], ['chocolates', 1, 70], ['juice', 3, 50], ['milk', 2, 10]]

## Return sorted list based on second element
## Instead of a built-in-function to pass as key, we can use lambda functions.
sorted(groceries, key = lambda items: items[1]) ## [['chocolates', 1, 70], ['milk', 2, 20], ['juice', 3, 90], ['biscuits', 4, 120]]

## Return sorted list based on the most expensive item purchase
sorted(groceries, key = lambda items: items[-1], reverse = True)    ## [['biscuits', 4, 120], ['juice', 3, 90], ['chocolates', 1, 70], ['milk', 2, 20]]
```

---

## Lists: Example

**Problem**: You sell lemonade over two weeks, the lists number of lemonades sold per week. The profit for each lemonade is $1.5.

- Add another day to week 2 list by capturing a number as input
- Combine the two lists into the list called `sales`
- Calculate / print how much you earned on:
  - Best Day
  - Worst Day
  - Separately and in Total

Total 3 print statements.

```py
sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
new_day = input("Please add sales to Week 2:")  # 14
sales_w2.append(int(float(new_day)))
sales = sales_w1 + sales_w2
sales.sort()
print(f'Best Day: ${sales[-1] * 1.5}')          # Best Day: $63.0
print(f'Worst Day: ${sales[0] * 1.5}')          # Worst Day: $4.5
print(f'Total: ${sum(sales) * 1.5}')            # Total: $346.5
```

---

# Tuples

## Tuple: Overview

Tuples are used to store multiple items in a single variable, like Lists. It is one of the 4 built-in data types in Python. But unlike Lists, Tuple is a collection which is ordered and immutable.

Tuples are written with round brackets. They are also faster to work with than Lists.

Since Tuples are immutable, List methods like `append`, `insert`, `remove`, do not work with Tuples.

```py
friends_list = ['John', 'Michael', 'Terry', 'Eric', 'Graham']           # A List
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')          # A Tuple

# Empty Tuple
empty_tuple = ()
empty_tuple2 = tuple()

# Immutability
friends_tuple[1] = 'Ted'                # TypeError: 'tuple' object does not support item assignment
friends_tuple.append('Ted')             # AttributeError: 'tuple' object has no attribute 'append'

# Destructuring / Unpacking
person = ("Bob", 42, 'Manhattan', 'USA', 'Mechanic')
name, *details, profession = person

print(name, profession)                 # Bob Mechanic
print(details)                          # [42, 'Manhattan', 'USA']
print(tuple(details))                   # (42, 'Manhattan', 'USA')
```

---

## Tuples: Methods

```py
friends_tuple = ('John','Michael','Terry','Eric','Graham', 'Eric')
print(friends_tuple[2:4])                                               # ('Terry', 'Eric')

len(friends_tuple)                                                      # 6
friends_tuple.index('Michael')                                          # 1
friends_tuple.count('Eric')                                             # 2

# Membership: Check if a element exists in a Set. Returns boolean: `True` or `False`
print("Jayanta" in friends_tuple)                                       # False
print("Jayanta" not in friends_tuple)                                   # True
print("Terry" in friends_tuple)                                         # True
print("Terry" not in friends_tuple)                                     # False
print("Terry" in friends_tuple and "Jayanta" not in friends_tuple)      # True
print("Terry" not in friends_tuple or "Jayanta" in friends_tuple)       # False
```

---

# Sets

## Sets: Overview

A set is an unordered collection of unique elements.
The difference between a List and a Set is that a set is an unordered list that maintains cardinality or uniqueness of its elements, i.e. it doesn't allow duplicates.

Sets are written with curly brackets. They are also faster to work with than Lists.

```py
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
print(friends_set)                                      # {'John','Michael','Terry','Eric','Graham'}

# Empty Set
empty_set = set()
```

---

## Sets: Methods

```py
friends_set = {'John','Michael','Terry','Eric','Graham','Eric'}
friends_set2 = {'Reg','Loretta','Colin','Eric','Graham'}
print(friends_set)                                      # {'John','Michael','Terry','Eric','Graham'}

# `Set.add(element)`: Add a new element to a set only if it doesn't exist
friends_set.add('Graham')                   # Does not add as element already exists
print(friends_set)                          # {'John','Michael','Terry','Eric','Graham'}

friends_set.add('Ted')                      # Add is successful as element doesn't exist
print(friends_set)                          # {'Graham', 'John', 'Terry', 'Michael', 'Eric', 'Ted'}

# `Set.remove(element)`: Removes an element from the set or throws a KeyError if not found
friends_set.remove('Ted')                   # Removal successful as element exists
print(friends_set)                          # {'Graham', 'John', 'Terry', 'Michael', 'Eric'}
friends_set.remove('Ted')                   # KeyError: 'Ted'

# `Set.discard(element)`: Removes an element from the set. Doesn't throw any error if not found
friends_set.discard('Ted')                  # Element not found
print(friends_set)                          # {'Graham', 'John', 'Terry', 'Michael', 'Eric'}
friends_set.discard('Eric')                 # Element found and removed
print(friends_set)                          # {'Graham', 'John', 'Terry', 'Michael'}

# `Set.intersection(Set2)`: Returns a new set with the common elements between two sets
friends_set.add("Eric")
print(friends_set.intersection(friends_set2))           # {'Eric', 'Graham'}
print(friends_set & friends_set2)                       # {'Eric', 'Graham'}

# `Set.difference(Set2)`: Returns a new set with the elements of the first set that doesn't exist in the second.
print(friends_set.difference(friends_set2))             # {'John', 'Terry', 'Michael'}
print(friends_set - friends_set2)                       # {'John', 'Terry', 'Michael'}

# `Set.symmetric_difference(Set2)`: Returns a new set with the elements of the uncommon elements of both the sets. Opposite of intersection.
print(friends_set.symmetric_difference(friends_set2))   # {'John', 'Loretta', 'Reg', 'Michael', 'Colin', 'Terry'}
print(friends_set ^ friends_set2)                       # {'John', 'Loretta', 'Reg', 'Michael', 'Colin', 'Terry'}

# `Set.union(Set2)`: Returns a new set that is the union of the two sets without any duplicates
print(friends_set.union(friends_set2))  # {'Graham', 'John', 'Loretta', 'Eric', 'Terry', 'Michael', 'Reg', 'Colin'}
print(friends_set | friends_set2)       # {'Graham', 'John', 'Loretta', 'Eric', 'Terry', 'Michael', 'Reg', 'Colin'}

# `Set.clear()`: Clears the set, removing all elements
friends_set.clear()
print(friends_set)                      # set()

# `Set.copy()`: Copying Sets
new_set = {1, 2, 3}.copy()
print(new_set)                          # {1, 2, 3}

# `Set.issubset(Set2)`: Check if the first set is a subset of the second set
# `Set.issuperset(Set2)`: Check if the first set is a superset of the second set
# `Set.isdisjoint(Set2)`: Check if the two sets have a null intersection
friends_set = {'John','Michael','Terry','Eric','Graham'}
friends_subset = {'Eric', 'Graham'}
random_set = {'Apple', 'Banana', 'Cat'}

print(friends_subset.issubset(friends_set))                         # True
print(friends_subset.issubset(random_set))                          # False

print(friends_set.issuperset(friends_subset))                       # True
print(friends_set.issuperset(random_set))                           # False

print(friends_set.isdisjoint(friends_subset))                       # False
print(friends_set.isdisjoint(random_set))                           # True

# Membership: Check if a element exists in a Set. Returns boolean: `True` or `False`
print("Jayanta" in friends_set)                                     # False
print("Jayanta" not in friends_set)                                 # True
print("Terry" in friends_set)                                       # True
print("Terry" not in friends_set)                                   # False
print("Terry" in friends_set and "Jayanta" not in friends_set)      # True
print("Terry" not in friends_set or "Jayanta" in friends_set)       # False
```

---

# Dictionaries

## Dictionaries: Overview

Dictionaries in Python store `key:value` pairs.

```py
# Initializing Dictionary
# -----------------------
movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John','Eric','Michael','George','Terry']
}
print(movie)        # {'title': 'Life of Brian', 'year': 1979, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']}

print('title' in movie)         # True
print('budget' in movie)        # False
print('budget' not in movie)    # True
```

---

## Dictionaries: Built-In Functions

```py
movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John','Eric','Michael','George','Terry']
}

# Length of the dictionary: Number of key:value pairs
len(movie)                          # 3
```

---

## Dictionaries: Basic Methods

```py
movie = {
    'title': 'Life of Brian',
    'year': 1979,
    'cast': ['John','Eric','Michael','George','Terry']
}
movie.keys()                        # dict_keys(['title', 'cast'])
movie.values()                      # dict_values(['Life of Brian',1979,['John', 'Eric', 'Michael', 'George', 'Terry']])
movie.items()                       # dict_items([('title', 'Life of Brian'),('year', 1979),('cast', ['John', 'Eric', 'Michael', 'George', 'Terry'])])
```

---

## Dictionaries: CRUD Operations

```py
# READ Dictionary value
# ---------------------
movie['title']                      # 'Life of Brian'
movie.get('title')                  # 'Life of Brian'
movie['year']                       # 1979
movie['cast'][-1]                   # 'Terry'
movie['budget']                     # KeyError: budget
movie.get('budget')                 # None (empty object)
movie.get('budget', 'Not found')    # 'Not found'

# UPDATE Dictionary value
# -----------------------
movie['title'] = 'The Holy Grail'
print(movie)                        # {'title': 'The Holy Grail', 'year': 1979, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']}

movie.update({ 'title': 'The Last Song', 'year': 1975 })
print(movie)                        # {'title': 'The Last Song', 'year': 1975, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']}

# CREATE Dictionary entry
# -----------------------
movie['director'] = 'Tarantino'
print(movie)                        # {'title': 'The Last Song', 'year': 1975, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry'], 'director': 'Tarantino'}

# DELETE Dictionary entry
# -----------------------
del movie["director"]
print(movie)                        # {'title': 'The Last Song', 'year': 1975, 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']}
# Remove the item with the key and return the value
year = movie.pop("year")
print(year)                         # 1975
print(movie)                        # {'title': 'The Last Song', 'cast': ['John', 'Eric', 'Michael', 'George', 'Terry']}
# Remove the last item and return the item. Returns a Tuple.
cast_item = movie.popitem()
print(cast_item)                    # ('cast', ['John', 'Eric', 'Michael', 'George', 'Terry'])
```

---

## Dictionaries: Joining Dictionaries

```py
item = { 'item': 'Whey Protein', 'price': 5500, 'quantity': 1, 'amount': 5500 }
info = { 'weight': '2.2kg', 'serving_size': "30g" }
ingredients = { 'protein': '25g', 'carbs': '1g', 'bcaa': '3g', 'fat': '1g' }

# Method 1: Update
# ----------------
groceries = {}
groceries.update(item)
groceries.update(info)
groceries.update(ingredients)
print(groceries)        # {'item': 'Whey Protein', 'price': 5500, 'quantity': 1, 'amount': 5500, 'weight': '2.2kg', 'serving_size': '30g', 'protein': '25g', 'carbs': '1g', 'bcaa': '3g', 'fat': '1g'}

# Method 2: Comprehension
# -----------------------
groceries1 = {}
for dictionary in (item, info, ingredients): groceries1.update(dictionary)
print(groceries)        # {'item': 'Whey Protein', 'price': 5500, 'quantity': 1, 'amount': 5500, 'weight': '2.2kg', 'serving_size': '30g', 'protein': '25g', 'carbs': '1g', 'bcaa': '3g', 'fat': '1g'}

# Method 3: Destructuring / Unpacking (Python 3.5 and later)
# ----------------------------------------------------------
groceries = {**item, **info, **ingredients}
print(groceries)        # {'item': 'Whey Protein', 'price': 5500, 'quantity': 1, 'amount': 5500, 'weight': '2.2kg', 'serving_size': '30g', 'protein': '25g', 'carbs': '1g', 'bcaa': '3g', 'fat': '1g'}
```

---

## Dictionaries: Example

```py
#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
freelancers = {'name':'freelancing Shop','brian': 70, 'black knight':20, 'biccus diccus':100, 'grim reaper':500, 'minstrel':-15}
antiques = {'name':'Antique Shop','french castle':400, 'wooden grail':3, 'scythe':150, 'catapult':75, 'german joke':5}
pet_shop = {'name':'Pet Shop','blue parrot':10, 'white rabbit':5, 'newt': 2}

def start_game(stores):
    cart = {}
    purse = 1000
    department_store = {**freelancers, **antiques, **pet_shop}
    department_store.pop('name')
    print('Morning inventory of stores', sorted(department_store.items()))
    print('---------------------------')

    def prompt(store, key = ''):
        text = f"Welcome to {store['name']}! What do you want to buy: {store}"
        if key != '' and key not in store or key == 'name' or key == 'exit':
            text = f"Welcome to {store['name']}!\n----------------------------\nItem chosen is not available\nWhat do you want to buy from {store}: "
        return text

    #loop through stores
    for store in stores:
        key = input(prompt(store)).lower()
        if key == 'exit': continue
        while(key not in store or key == 'name' or key == ''):
            key = input(prompt(store, key)).lower()

        cart.update({ key: store.pop(key) })   # Add to cart

    cart_total = sum(cart.values())
    purse -= cart_total

    print(f'You Purchased {", ".join(cart.keys())}! Today it is all free. Have a nice day of mayhem!')
    print(f'Total Cost: {cart_total}, Remaining Gold: {purse}')

    department_store_after = {**freelancers, **antiques, **pet_shop}
    department_store_after.pop('name')
    print('Evening inventory of stores', sorted(department_store_after.items()))
    print('---------------------------')


start_game((freelancers, antiques, pet_shop))
```

---

# Functions

## Functions: Overview

We can create a function using the `def` keyword followed by the function name and round brackets followed by a colon. The following lines in a functions need to be indented. A `return` statement in a function returns a value that can be reused in the code.

The function is invoked using the function name followed by paranthesis, like: `function_name()`

```py
# Basic Hello World function
def hello_world():
    print("Hello World")

hello_world()                   # Hello World

# Function with parameter that takes in an argument
def hello(name):
    print(f'Hello {name}!')

hello("Jayanta")                # Hello Jayanta!

# Function that returns a computed value that has default values for parameters
def sum_of_two(first = 0, second = 0):
    return first + second

print(sum_of_two(25, 75))       # 100
print(sum_of_two())             # 0
print(sum_of_two(25))           # 25
```

---

## Functions: Keyword (Named) Arguments

Keyword arguments are one of those Python features that often seems a little odd for folks moving to Python from many other programming languages.

When coming from a programming language like JavaScript for example that doesn't support Keyword Arguments, arguments in a function need to be passed in order:

```js
function greeting(name, age = 28, color = 'red') {
  const capitalName = name[0].toUpperCase() + name.slice(1).toLowerCase();
  console.log(
    `Hello ${capitalName}, you will be ${parseInt(age) + 1} next birthday!`
  );
  console.log(`We hear you like the color ${color.toLowerCase()}!`);
}

greeting('jayanta', 31, 'black');
/** Prints
 * --------
 * Hello Jayanta, you will be 32 next birthday!
 * We hear you like the color black!
 */
```

If the arguments are not passed in order, we would likely get an error. A programming language like JavaScript wouldn't automatically assign the named arguments to the corresponding parameters.

```js
/** The order of these arguments matters when they’re passed positionally: */
greeting(31, 'black', 'jayanta'); // Uncaught TypeError: Cannot read properties of undefined (reading 'toUpperCase') at greeting

/** Attempting named arguments */
greeting((age = 31), (color = 'black'), (name = 'jayanta')); // Uncaught TypeError: Cannot read properties of undefined (reading 'toUpperCase') at greeting
```

However, in **Python**, when we use keyword/named arguments, it’s the name that matters, not the position:

```py
def greeting(name, age=28, color="red"):
   print(f"Hello {name.capitalize()}, you will be {int(age) + 1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting("jayanta", 31, "black")                        # This works
greeting(age = 31, color = "black", name = "jayanta")   # This works too!

# Hello Jayanta, you will be 32 next birthday!
# We hear you like the color black!
```

---

## Function: Return Statement

```py
# When returning single values, return type is the type of the single return value
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return total_amount

price = value_added_tax(100)
print(price, type(price))       # 125.0 <class 'float'>

# When returning multiple values, return type is Tuple
def value_added_tax(amount):
    tax = amount * 0.25
    total_amount = amount * 1.25
    return amount, tax, total_amount

price = value_added_tax(100)
print(price, type(price))       # (100, 25.0, 125.0) <class 'tuple'>
```

---

# Conditionals

## Conditions: if, elif, else

```py
# if statement
is_raining = True
print("Good Morning")
if is_raining:
    print("Bring an Umbrella")                              # Executes this as conditional is true

# if-else statement
is_fruit = False
if is_fruit:
    print("This is a fruit")
else:
    print("This is not a fruit")                            # Executes this as conditional is false

# if-else statement with or
is_fruit = False
is_vegetable = True
if is_fruit or is_vegetable:
    print("This is either a fruit or a vegetable!")         # Executes this as conditional is true
else:
    print("This is neither a fruit, nor a vegetable!")

# if-else statement with and
is_fruit = False
is_red = True
if is_fruit and is_red:
    print("This is a red fruit!")
else:
    print("This is either not a fruit or not red!")         # Executes this as conditional is false

# if-elif-else statement with not()
is_fruit = False
is_vegetable = True
is_raw = True
if is_fruit and is_raw and not(is_vegetable):
    print("This is a raw fruit!")
elif is_vegetable and is_raw and not(is_fruit):
    print("This is a raw vegetable!")                           # Executes this line
else:
    print("This is either not a raw fruit or a raw vegetable!")
```

---

## Conditionals: Example 1

```py
print('if elif else - Exercise')
# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def calculator(first_number = 0, operation = "+", second_number = 0):
    num1 = float(first_number)
    if isinstance(num1, float) and operation.lower() == "f":
        return f'Temperature in Fahrenheit: {(num1 * 9 / 5) + 32}F'
    elif isinstance(float(first_number), float) and isinstance(float(second_number), float):
        num2 = float(second_number)
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            return num1 / num2
        else:
            return "Invalid operator"
    else:
        return "Please enter valid numbers"

first_number = input("Enter first number: ")
operation = input("Enter the Operation you want to perform (+, -, *, /, f): ")
if(operation.lower() != 'f'):
    second_number = input("Enter second number: ")

print(calculator(first_number, operation, second_number))
```

---

## Conditionals: Example 2

**Problem**: Optimize the following function by reducing the number of conditionals

```py
# optimize/shorten the code in the function
# try to reduce the number of conditionals
def num_days(month):

    if month == 'jan':
        print('number of days in',month,'is',31)
    elif month == 'feb':
        print('number of days in',month,'is',28)
    elif month == 'mar':
        print('number of days in',month,'is',31)
    elif month == 'apr':
        print('number of days in',month,'is',30)
    elif month == 'may':
        print('number of days in',month,'is',31)
    elif month == 'jun':
        print('number of days in',month,'is',30)
    elif month == 'jul':
        print('number of days in',month,'is',31)
    elif month == 'aug':
        print('number of days in',month,'is',31)
    elif month == 'sep':
        print('number of days in',month,'is',30)
    elif month == 'oct':
        print('number of days in',month,'is',31)
    elif month == 'nov':
        print('number of days in',month,'is',30)
    elif month == 'dec':
        print('number of days in',month,'is',31)

num_days('oct')
```

**Solution:**

```py
def num_days(month):
    fMonth = month.lower()
    month_30 = {'sep', 'apr', 'jun', 'nov'}
    if fMonth not in (month_30 | {'jan', 'feb', 'mar', 'may', 'july', 'aug', 'oct', 'dec'}):
        return print('Please enter a valid month in MMM format')

    days = 31
    if fMonth in month_30:
        days = 30
    elif fMonth == 'feb':
        days = 28
    return print('number of days in',fMonth,'is',days)

num_days('APR')         # number of days in apr is 30
num_days('Feb')         # number of days in feb is 28
num_days('dEc')         # number of days in dec is 31
num_days('ABC')         # Please enter a valid month in MMM format
```

---

# Loops

## Loops: Overview

Loops are used to do repeatable tasks.

**Three Loop Questions**:

1. What do I want to repeat?
2. What do I want to change each time?
3. How long should we repeat?

---

## Loops: While-Loop

**Syntax**:

```py
'''
while condition
    code
    iterator
'''
```

**Example**:

```py
print("1.*Loops are great*")
print("2.**Loops are great**")
print("3.***Loops are great***")
print("4.****Loops are great****")
print("5.*****Loops are great*****")

# Execute the above print statements using a while loop
i = 0
while i < 5:
    i += 1
    print(f'{i}.{"*" * i}Loops are great{"*" * i}')
```

**Example: Guessing Game**

In

> **Tip**: Use `import random` and `number = random.randrange(1, 100)` to get the number that has to be guessed. Modules are covered in a later section.

```py
# Guess the correct number in 10 guesses. If you don’t get it right after 10 guesses you lose the game.
# Give user input box to capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during while loop, print to the input box.

import random
def guessing_game():
    number = random.randrange(1, 100)
    chances = 10
    proximity = ""
    while(chances > 0):
        guess = input(f"Enter your guess: {proximity} \nChances remaining: {chances}")
        chances -= 1
        if number == int(guess):
            return print("Congratulations! You won the game!")
        elif int(guess) < number:
            proximity = "\n(Your last guess was lower than the number)"
        else:
            proximity = "\n(Your last guess was higher than the number)"

        if(chances == 0):
            return print(f"Sorry, you Lost! The right number is: {number}")

guessing_game()
```

---

## Loops: For-Loop

```py
# Loop over characters in a string
for char in "Red Dragon":
    print(char.upper())

# R
# E
# D
#
# D
# R
# A
# G
# O
# N

# Loop over elements in an iterable (Works for List, Tuple and Set, Range and Enumerate Object)
for element in ["Apple", "Banana", "Cat", "Dog", "Elephant"]:
    print(element)              # Print each element in a new line


# Loop over a range
for i in range(10):
    print((i + 1) * 9)          # Multiplication table of 9 (each in a new line)

for odd in range(1, 10, 2):
    print(odd)                  # Print odd numbers - 1, 3, 5, 7, 9 (each in a new line)

# Loop over a List and print every alternate element
friends = ["Rohit", "Ravi", "Adraha", "Aradeep", "Bhargav", "Harsh", "Prince", "Anil", "Raj"]

for index in range(0, len(friends), 2):
    print(friends[index])

# Looping over a Dictionary
movie = {
    'title' : 'Life of Brian',
    'year' : 1979,
    'cast' : ['John','Eric','Michael','George','Terry']
}
# To get the following output
# ---------------------------
## ['title', 'Life of Brian']
## ['year', 1979]
## ['cast', ['John', 'Eric', 'Michael', 'George', 'Terry']]

## Method 1
## --------
for key in movie:
    print([key, movie[key]])

## Method 2
## --------
for key, value in movie.items():
    print([key, value])

```

---

## Loops: Break and Continue

- **`continue`**: Stops the current iteration and moves to the next iteration of the loop without running any further operations for the current iteration
- **`break`**: Exits the loop altogether

```py
friends = ["Rohit", "Ravi", "Adraha", "Aradeep", "Bhargav", "Harsh", "Prince", "Anil", "Raj"]

## Print all friends until Anil (not including), each in a new line except 'Adraha'
## ---------------------------------------------------------------------------------
## Rohit
## Ravi
## Will not print friend: Adraha
## Aradeep
## Bhargav
## Harsh
## Prince

# For Loop
for friend in friends:
    if friend == "Adraha":
        print(f"Will not print friend: {friend}")
        continue
    elif friend == "Anil":
        break
    print(friend)



# While Loop
i = 0
while(i < len(friends)):
    friend = friends[i]
    i += 1
    if friend == "Adraha":
        print(f"Will not print friend: {friend}")
        continue
    elif friend == "Anil":
        break
    print(friend)
```

---

## Loops: Using Built-in Function - `enumerate()`

Takes a collection (e.g. a tuple, string, list) and returns it as an enumerate object.

**Syntax**:

```py
# Syntax
enumerate_object = enumerate(iterable, start)

# How enumerate works
print(type enumerate(friends))              # <class 'enumerate'>
print(enumerate(friends))                   # <enumerate object at 0x7f213e028c00>

# To view, we need to create a List out of the enumerate object
print(list(enumerate(friends)))             # [(0, 'Rohit'), (1, 'Ravi'), (2, 'Adraha'), (3, 'Aradeep'), (4, 'Bhargav'), (5, 'Harsh'), (6, 'Prince'), (7, 'Anil'), (8, 'Raj')]
```

```py
friends = ["Rohit", "Ravi", "Adraha", "Aradeep", "Bhargav"]

## Print all friends in the following way:
## --------------------------------------
## 1 Rohit
## 2 Ravi
## 3 Adraha
## 4 Aradeep
## 5 Bhargav

# Using for-loop without enumerate
i = 1
for friend in friends:
    print(i, friend)
    i += 1

# Using the index method
for friend in friends:
    print(friends.index(friend) + 1, friend)

# Using for-loop with enumerate
## `enumerate(iterable, start)`: Takes a collection (e.g. a tuple) and returns it as an enumerate object. An enumerate object contains tuples of each list element in the following format:
## `(start + index, element)`
for index, friend in enumerate(friends, 1):
    print(index, friend)

# To confirm if the elements of an enumerated object are indeed tuples and the keyword arguments as per syntax work
for enumerated in enumerate(start = 1, iterable = friends):
    print(enumerated, type(enumerated))     # Example: (2, 'Ravi') <class 'tuple'>
    index, friend = enumerated              # Destructuring
    print(index, friend)                    # Example: 2 Ravi
```

---

# Filehandling

```py
# `open(path, mode)`: Opens a File for processing. Where `path` is the location of the file and `mode` is the mode:
## r = 'read'
## w = 'write'
my_file = open('index.html', 'r')
print(my_file.read())               # Read the opened file --> index.html
print(my_file.read(20))             # Read first 20 characters of the file
print(my_file.readlines())
print(my_file.read().splitlines())
my_file.close()                     # Close the file

# Reading CSV file
# ----------------
# - Read `friends.csv`
# - Return each row in the format - 'In 2030, John will be 41 years old!'

## Method 1: Using `open(path, mode)` method
## ----------------------------------------------------------------
file = open('friends.csv', 'r')
lines = file.read()
for line in lines.split('\n'):
    name, year = line.split(',')
    print(f'In 2030, {name} will be {2030 - int(year)} years old!')

file.close()

## Method 2: Using Context Manager with for-loop to loop over each line (row)
## ----------------------------------------------------------------
with open('friends.csv', 'r') as f:
    for line in f:
        name, year = line.split(',')
        print(f'In 2030, {name} will be {2030 - int(year)} years old!')

## Method 3: Using Context Manager with csv module to read CSV file
## ----------------------------------------------------------------
import csv
with open('friends.csv', 'r') as f:
    reader = csv.reader(f)
    print(reader)               ## <_csv.reader object at 0x7f6543ff0970>
    friends = list(reader)
    print(friends) ## [['John', '1989'], ['Eric', '2003'], ['Michael', '1993'], ['Graham', '1981'], ['Terry', '1991'], ['Samuel', '1994']]
    for name, year in friends: print(f'In 2030, {name} will be {2030 - int(year)} years old!')
```

---

# Exceptions

Most programming languages have a `try/catch/finally` block to handle exceptions and a way to throw errors.

The Python equivalent for handling exceptions is the `try/except/else/finally` block and `raise` to throw errors to be caught by the except blocks.

**Syntax**:

```py
#try:
    # Code you want to run
#except:
    # Executed if error occurs in sequence. Can be followed by other except statements.
#else:
    # Executed if no error
#finally:
    # Always executed
```

```py
try:
    num=int(input('Enter a number between 1 and 30: '))
    num1 = 30/num
    if num > 30:
        raise ValueError(num)
except ZeroDivisionError as err:
    print(err, "You can't divide by Zero!!!")
except ValueError as err:
    print(err, "Bad Value not between 1 and 30!")
except:
    print("Invalid Input!")
else:
    print("30 divided by",num, "is: ", 30/num)
finally:
    print("**Thank you for playing!**")
```

---

# Classes and Objects

## Classes: Overview

A **Class** is a custom datatype that provides a blueprint for objects to be created out of it.

- All classes have a constructor function called `__init__()`, which is always executed when the class is being initiated.

- Variables declared within a class are called attributes. There are two kinds of attributes:

  - **Instance Attributes**: Attributes defined within the `__init__()` function using the `self` keyword (by convention).
  - **Class Attributes**: Attributes that are defined in the class body and not in any function

- Methods are functions created within the class.

An **Object** is a single instance of the Class. It has access to the class attributes and methods of its parent class.

The following is a basic implementation of a Python Class:

```py
# Example: Create a Movie class to create movies you want to watch. Objects created from this class will have a `watched` attribute that is set to False by default.
class Movie:
    def __init__(self, title, year, imdb_score, watched = False):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.watched = watched

django = Movie("Django Unchained", 2012, 8.4)
incept = Movie("Inception", 2010, 8.8)

print(isinstance(django, Movie))                                    # True
print(isinstance(incept, Movie))                                    # True

# Accessing Attribute values
# --------------------------
print(incept.title, incept.year, incept.imdb_score, incept.watched) # Inception 2010 8.8 False
print(django.title, django.year, django.imdb_score, django.watched) # Django Unchained 2012 8.4 False

# Printing the object
# -------------------
## Printing just the object returns the object as its location in memory
print(django)                                       # <__main__.Movie object at 0x7fe0a336bfa0>

## We can modify this default print behaviour by modifying the `__str__()` Special Method. More on this in a later section.

## To return the attributes as a dictionary
## ----------------------------------------
### Method 1: Use the __dict__ special object method. Returns a dictionary.
django_dict = django.__dict__
type(django_dict)                                   # <class 'dict'>
print(django_dict)                                  # {'title': 'Django Unchained', 'year': 2012, 'imdb_score': 8.4, 'watched': True}

### Method 2: Use `vars(object)` Built-in function which does the same with some caveats (Does not work for "slotted" classes). Returns a dictionary.
django_dict_vars = vars(django)
type(django_dict)                                   # <class 'dict'>
print(django_dict)                                  # {'title': 'Django Unchained', 'year': 2012, 'imdb_score': 8.4, 'watched': True}

# You've watched "Django Unchained". Update the watched property
django.watched = True
print(django.watched)                                               # True ---> Changed
print(incept.watched)                                               # False --> Still unchained

# Objects are instances of the classes that uses the class blueprint during initialization but then behave as independent objects that can be modified and changed on their own.

del incept                                                          # deletes the object from memory
```

---

## Classes: Inheritance

Inheritance refers to a Child Class inheriting the attributes of a Parent Class.

To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.

> **Note**: A child class can inherit from multiple parents (send multiple parent classes separated by commas). If there is a collission of method, the first Parent Class' method is preferred.

**Concepts related to inheritance and the child class**:

1. **The `pass` keyword**: Use the `pass` keyword when you do not want to add any other properties or methods to the class. The Child Class then has the same properties and methods as the Parent Class.

   ```py
   class Student(Person):
       pass
   ```

2. **The `__init__()` function**:

   - When you add the `__init__()` function, the child class will no longer inherit the parent's `__init__()` function. The child's `__init__()` function overrides the inheritance of the parent's `__init__()` function.
   - To keep the inheritance of the parent's `__init__()` function, add a call to the parent's `__init__()` function:

     ```py
     class Student(Person):
        def __init__(self, fname, lname):
            Person.__init__(self, fname, lname)
     ```

3. **`super()`**: Python also has a `super()` function that will make the child class inherit all the methods and properties from its parent. You can then additional properties specific to the child class.

   ```py
   class Person:
        def __init__(self, fname, lname):
            self.fname = fname
            self.lname = lname

   class Student(Person):
        def __init__(self, fname, lname, year):
            super().__init__(fname, lname)
            self.graduation_year = year

    student1 = Student("Mike", "Olsen", 2019)
    print(isinstance(student1, Student))            # True
    print(student1.graduation_year)                 # 2019
   ```

---

## Classes: Using a Dictionary to Initialize an Object

While working with data, JSON has become a standard format. In Python, the closest representation of a JSON object is the Dictionary.

So it will be convenient to create an object out of a class, passing a dictionary to the Class Constructor.

```py
# Instead of creating an object like this:
person = Person("Jayanta", "Samaddar", 30)

# Create Object like this instead:
person = Person({ 'fname': "Jayanta", 'lname': "Samaddar", 'age': 30 })
```

**Implementation of Class**:

We will be using the Python Built-in Method for Objects:

- `setattr(object, name, value)`: Sets the attribute of an object

```py
# Method 1: Initialize an Object by passing a dictionary and have it defined as instance attributes
# -------------------------------------------------------------------------------------------------
class Person:
    def __init__(self, dictionary):
        for key, value in dictionary.items():
            setattr(self, key, value)

person = Person({ 'fname': "Jayanta", 'lname': "Samaddar", 'age': 30 })
print(vars(person)) # {'fname': 'Jayanta', 'lname': 'Samaddar', 'email': 'jayanta@example.com'}
```

> **Important**: As we can see, the problem with the above method is that, any key-value pairs can be passed as a dictionary. We need to have some sort of checks in place to handle that. In addition, so far we haven't validated types.

---

## Classes: Special Methods

A Class can implement certain operations that are invoked by special syntax (such as arithmetic operations or subscripting and slicing) by defining methods with special names. This is Python’s approach to operator overloading, allowing classes to define their own behavior with respect to language operators. For instance, if a class defines a method named `__getitem__()`, and `x` is an instance of this class, then `x[i]` is roughly equivalent to `type(x).__getitem__(x, i`). Except where mentioned, attempts to execute an operation raise an exception when no appropriate method is defined (typically `AttributeError` or `TypeError`).

The following is an example of modifying one of these methods.

**Example**:

- Let's modify the **`object.__str__()`** method.
- The `object.__str__()` method is called by `str(object)` and the built-in functions `format()` and `print()` to compute the "informal" or nicely printable string representation of an object. The return value must be a string object.
- The default implementation defined by the built-in type object calls `object.__repr__()`. The `__repr__()` function returns the "official" string representation of an object.

**Default behaviour**:

```py
class Movie:
    def __init__(self, title, year, imdb_score, watched):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.watched = watched

django = Movie("Django Unchained", 2012, 8.4, True)
print(repr(django))     # <__main__.Movie object at 0x7fbb2cb36c10>  --> Returns the repr
print(django)           # <__main__.Movie object at 0x7fbb2cb36c10>  --> By default returns the repr
print(vars(django))     # {'title': 'Django Unchained', 'year': 2012, 'imdb_score': 8.4, 'watched': True}
```

```py
class Movie:
    def __init__(self, title, year, imdb_score, watched = False):
        self.title = title
        self.year = year
        self.imdb_score = imdb_score
        self.watched = watched

    # Modify the Default Print behaviour
    def __str__(self):
        return str({
            "title": self.title,
            "year": self.year,
            "imdb_score": self.imdb_score,
            "watched": self.watched
        })

print(django)       # {'title': 'Django Unchained', 'year': 2012, 'imdb_score': 8.4, 'watched': True}
print(repr(django)) # <__main__.Movie object at 0x7fbb2cb36c10>  --> We modified only the str
print(isinstance(django, Movie))                                # True
print(django.title, django.year, django.imdb_score)             # Django Unchained 2015 9.5
```

For Details on each of these Special Methods: **[Read the Python Documentation](https://docs.python.org/3/reference/datamodel.html)**

---

## Classes: Checks and Basic Type Validation

**Problem**:
We want to initialize an Object of a `Person` Class using a Dictionary but also ensure that only certain attributes can be added AND that those attributes have a certain data type.

```py
# Initialize an Object by passing a dictionary and have it defined as instance attributes but allow only specific dictionary keys to be passed and ensure the conform to type
# -------------------------------------------------------------------------------------------------
class Person:
    def __init__(self, dictionary):
        # Check if argument passed is a dictionary, else throw an error
        if not(isinstance(dictionary, dict)):
            raise TypeError('Unexpected Type: Dictionary expected')

        # Types
        ## Mandatory attributes
        mandatory_attr = {
            'fname': str,
            'lname': str,
            'age': int
        }.items()
        ## Optional attributes
        optional_attr = {
            'is_student': bool
        }.items()

        # Loop to validate and set mandatory attributes
        for key, value in mandatory_attr:
            # Validation 1: Check if key is in the dictionary
            if key not in dictionary:
                raise KeyError(f"Expected Mandatory keys: {', '.join(mandatory_attr.keys())}")

            # Set instance attribute. Throws error if input value cannot be correctly type casted
            setattr(self, key, value(dictionary[key]))

        # Loop to set optional attributes (if any)
        for key, value in optional_attr:
            # Continue running through the optional attributes
            if key not in dictionary: continue

            # Set instance attribute
            setattr(self, key, value(dictionary[key]))
```

**Run Tests by intitializing objects**:

```py
# Create Person object from a dictionary with all mandatory attributes with correct types
person = Person({ 'fname': "Jayanta", 'lname': "Samaddar", 'age': 30 })
print(vars(person))         # {'fname': 'Jayanta', 'lname': 'Samaddar', 'age': 30}

# Create Person object from a dictionary with mandatory + optional attributes with correct types
person1 = Person({ 'fname': "Thiago", 'lname': "Silva", 'age': 36, 'is_student': False })
print(vars(person))         # {'fname': 'Thiago', 'lname': 'Silva', 'age': 36, 'is_student': False}

# Create Person object from a dictionary with unavailable mandatory key
footballer = Person({ 'fname': "Cristiano", 'age': 38, 'is_student': False })
# KeyError: 'Expected Mandatory keys: fname, lname, age'

# Create Person object from a dictionary with unavailable optional key and extra key
footballer = Person({ 'fname': "Cristiano", 'lname': "Ronaldo", 'age': 38, 'is_footballer': True })
print(vars(footballer))     # {'fname': 'Cristiano', 'lname': 'Ronaldo', 'age': 38} --> ignored extra

# Create Person object from a dictionary with wrong data type that can be correctly type casted
footballer1 = Person({ 'fname': "Mo", 'lname': "Salah", 'age': "31", 'is_student': False })
print(vars(footballer1))    # {'fname': 'Mo', 'lname': 'Salah', 'age': 31, 'is_student': False}

# Create Person object from a dictionary with wrong data type that cannot be correctly type casted
superhero = Person({ 'fname': "Steve", 'lname': "Rogers", 'age': "ageless" })
# ValueError: invalid literal for int() with base 10: 'ageless'
```

---

# Modules

**Importing module(s) and accessing properties and functions**

```py
import platform, os                     # Import one or many modules, separated by commas

print(dir(platform))                    # Prints a list of all available methods and properties
print(platform.python_version())        # 3.8.10    --> method
print(os.name)                          # posix     --> property
```

**Importing particular method(s) from a module**

```py
from platform import python_version as pv, system   # Aliasing python_version as 'pv'

print(pv())                                         # 3.8.10
print(system())                                     # Linux
```

---

# Zip / Unzip

For iterables of the same length, zipping means to pair the elements of the same index for each iterable into a single Tuple. Returns a zip object which is a iterator of tuples. Can be converted into a List using Built-in-function: `list()`. In case of uneven lists, returns pairs equal to the smallest iterable's length.

**Zipping**

```py
# Iterables
nums = [1,2,3,4]
letters = "abcd"
names = ['John','Eric','Michael','Graham','Joe']

combo = zip(nums, letters)
print(combo)                            # <zip object>
print(list(combo))                      # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Convert Two-Dimensional Iterable into a Dictionary. Will return empty dictionary if cannot type cast.

## Method 1: Using the `dict(iterable)` Built-in-Function
combo_dict = dict(combo)
print(combo_dict)                       # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

## Method 2: With Dictionary Comprehension
## ---------------------------------------
combo_dict_compre = {key: value for key, value in combo}
print(combo_dict_compre)                # {1: 'a', 2: 'b', 3: 'c', 4: 'd'}

combo2 = zip(nums, letters, names)      # Note: names have one element more
print(tuple(combo2))                    # ((1, 'a', 'John'), (2, 'b', 'Eric'), (3, 'c', 'Michael'), (4, 'd', 'Graham')) ---> Ignored the last element in `names`
combo2_dict = dict(combo)
print(combo2_dict)                      # {} ---> Could not type cast

letters.append('e')                     # Adding an element to letters. Now we have 2 lists with 5 elements and one list with 4
combo3 = zip(nums, letters, names)      # Note: names have one element more
print(tuple(combo3))                    # ((1, 'a', 'John'), (2, 'b', 'Eric'), (3, 'c', 'Michael'), (4, 'd', 'Graham')) ---> Ignored the last element in `names` and `letters`.
```

**Unzipping**

```py
# Iterables
nums = [1,2,3,4]
letters = "abcd"
names = ['John','Eric','Michael','Graham','Joe']

# Zipping
combo = list(zip(nums, letters, names))

# Unzipping
num, let, nam = zip(*combo)             # Using unpacking to unzip
print(num, let, nam)                    # ('1', '2', '3', '4') ('a', 'b', 'c', 'd') ('John', 'Eric', 'Michael', 'Graham')

# Unzipping a Dictionary
combo_dict = dict(zip(nums, names))     # Setup
print(combo_dict)                       # {1: 'John', 2: 'Eric', 3: 'Michael', 4: 'Graham'}

## Method 1: Converting keys and values of the dictionary to iterable and unpacking / destructuring
## ------------------------------------------------------------------------------------------------
nums1, names1 = list(combo_dict.keys()), list(combo_dict.values())
print(nums1, names1)                    # [1, 2, 3, 4] ['John', 'Eric', 'Michael', 'Graham']

## Method 2: Using Unzipping (Returns Tuples)
## ------------------------------------------
nums2, names2 = zip(*combo_dict.items())
print(nums2, names2)                    # (1, 2, 3, 4) ('John', 'Eric', 'Michael', 'Graham')
```

---

# Lambda Functions

Lambda Functions or anonymous functions exist in Python and allow you to write single-line function definitions that you might just use once and throw away or you can use multiple times and give it a name. They can be quite convenient but aren't always the right choice to use.

```py
# Regular Python Function Definition
def square(x): return x*x

print(square(3))                                                    # 9

# Lambda Function: `lambda parameter(s): expression`
square1 = lambda x: x*x

print(square1(3))                                                   # 9

# Immediately invoke Lambda Function
print((lambda a,b,c: a+b+c)(2,3,4))                                 # 9
print((lambda *nums: sum(nums))(2,3,4,5))                           # 14  --> Using unpacking
```

---

## Lambda Functions: Examples

```py
# ------------------------------------------------------------------------------------------------
# Example 1: Sorting a List on Last Name
# ------------------------------------------------------------------------------------------------
# List of Names
monty_python = ['John Marwood Cleese','Eric Idle','Michael Edward Palin','Terrence Vance Gilliam','Terry Graham Perry Jones', 'Graham Arthur Chapman']

## Using Regular Function Definition
def sort_names(name):return name.split(' ')[-1]
monty_python.sort(key = sort_names)
print(monty_python)

## Using Lambda Function
monty_python.sort(key = lambda name:name.split(' ')[-1])
print(monty_python)

# ------------------------------------------------------------------------------------------------
# Example 2: Sorting a List on the Integer part of Strings
# ------------------------------------------------------------------------------------------------
# List of IDs
signups = ['MPF104', 'MPF20', 'MPF2', 'MPF17', 'MPF3', 'MPF45']
print(sorted(signups)) # ['MPF104', 'MPF17', 'MPF2', 'MPF20', 'MPF3', 'MPF45'] --> Lexicographic

## Sorting by integer
print(sorted(signups, key = lambda id: int(id[3:]))) ## ['MPF2', 'MPF3', 'MPF17', 'MPF20', 'MPF45', 'MPF104']

# ------------------------------------------------------------------------------------------------
# Example 3: Sorting List of Objects based on attribute
# ------------------------------------------------------------------------------------------------
class Player:
   def __init__(self, name, score):
       self.name = name
       self.score =  score

Eric = Player('Eric', 116700)
John = Player('John', 24327)
Terry = Player('Terry', 150000)
player_list = [Eric, John, Terry]

# Sorting player_list by highest score using lambda and list comprehension
player_list.sort(key = lambda player: player.score, reverse = True )
print([player.name for player in player_list])

# ------------------------------------------------------------------------------------------------
# Example 4: Return a function that uses the same arguments but has a different calculation method for different plans
# ------------------------------------------------------------------------------------------------
def price_calc(start,hourly_rate): return lambda hours: start + hourly_rate * hours
print(price_calc)                       # <function price_calc at 0x7ff514c50700>

# Different calculation method for different plans using the same arguments
walkin_cost = price_calc(10,30)
premium_cost = price_calc(1,25)

print(walkin_cost)                      # <function price_calc.<locals>.<lambda> at 0x7ff51437b4c0>
print(premium_cost)                     # <function price_calc.<locals>.<lambda> at 0x7ff5137e4670>

# Running the different functions we created
print(walkin_cost(2))                   # 70        --> 10 + 30 * 2
print(premium_cost(2))                  # 51        --> 1 + 25 * 2
print(price_calc(1,25)(2))              # 51        --> 1 + 25 * 2
```

---

# Comprehensions

## Comprehensions: Lists

```py
nums = [1,2,3,4,5,6,7,8,9]

# Regular For-Loop
new_list = []
for num in nums:
    new_list.append(num*num)
print(new_list)                         # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# List Comprehension
# ------------------
## Return the list containing the square of the elements of the original list
new_list = [num*num for num in nums]    ## Give me a list with num squared for each num in numbers
print(new_list)                         ## [1, 4, 9, 16, 25, 36, 49, 64, 81]

# ---------------------------------------------------------------------------------------------------
# Return the list containing only the even numbers present in the original list
# ---------------------------------------------------------------------------------------------------

## Using List Comprehension
print([num for num in nums if num % 2 == 0])        ## [2, 4, 6, 8]

## Alternate: Using Filter and Lambda
print(list(filter(lambda num: num % 2 == 0, nums))) ## [2, 4, 6, 8]

# ---------------------------------------------------------------------------------------------------
# Return a (letter, num) pair for each letter in 'spam' and each number from 0-4
# ---------------------------------------------------------------------------------------------------
# Desired Result:
# [('s', 0), ('s', 1), ('s', 2), ('s', 3), ('p', 0), ('p', 1), ('p', 2), ('p', 3), ('a', 0), ('a', 1), ('a', 2), ('a', 3), ('m', 0), ('m', 1), ('m', 2), ('m', 3)]

## With For-Loop
new_list = []
for letter in 'spam':
   for num in range(4):
       new_list.append((letter,num))

print(new_list)

## Using List Comprehension
print([(letter, num) for letter in 'spam' for num in range(4)])
```

---

## Comprehension: Dictionaries

---

# Randomness

```py
import random

friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']

# `random.randrange(start, stop[, step])`
print(random.randrange(0, 100))                 # Return a random integer between 0 - 100
print(random.randrange(1, 100, 2))              # Return a random odd integer between 1 - 100
print(random.randrange(2, 100, 2))              # Return a random even integer between 2 - 100

# `random.choice(seq)`
print(random.choice(friends_list))              # Returns a random element from the sequence

# `random.choices(population, weights=None, *, cum_weights=None, k=1)`
print(random.choices(friends_list, k = 3))      # Returns any 3 random elements from the sequence
print(random.choices(friends_list, k = 6))      # Returns all elements in the sequence (length: 5) + an extra any [k - length] random element(s) from the sequence. So the same element(s) can appear more than once

# `random.sample(population, k, *, counts=None)`
print(random.sample(friends_list,3))            # Gets any 3 random elements from the sequence.
print(random.sample(friends_list, 6))           # ValueError: Sample larger than population or is negative

# `random.shuffle(x)`: Shuffle the sequence x in place.
random.shuffle(friends_list)
print(friends_list)                             # Prints the shuffled list
```

---

# Timeit and Performance

A solution can be implemented in multiple ways. How do we know which of the multiple implementations that yield the same results is faster?

```py
from timeit import timeit
print('Performance and Timeit module')
# Experiment with sieve of Eratosthenes

# All function results yield: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149]


## Implementation 1
def test1():
    return [x for x in range(1, 151) if not any([x % y == 0 for y in range(2, x)]) and not x == 1]

## Implementation 2
def test2(): return [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]

## Implementation 3
def test3():
    primes = []
    for possiblePrime in range(2, 151):
        # Assume number is prime until shown it is not.
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes

# Run 10 cycles of each function
print(timeit('test1()', globals=globals(), number=100))     # 0.1083836629986763
print(timeit('test2()', globals=globals(), number=100))     # 0.10506472800625488
print(timeit('test3()', globals=globals(), number=100))     # 0.01700814999639988

# Thus we can conclude that the test3 function is the fastest of the three.
```

---

# Example: Crypto Engine

```py
def enigma_light():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    #print(keys)
    #print(values)
# create two dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys))
#user input 'the message' and mode
    msg = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decode by default: ')
# run encode or decode
    if mode.lower() == 'e':
        new_msg = ''.join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = ''.join([dict_d[letter] for letter in msg.lower()])

    return new_msg

print(enigma_light())
```

---

# References

- [Python: Data Model](https://docs.python.org/3/reference/datamodel.html)
- [Python: Built-in Functions](https://docs.python.org/3/library/functions.html)
- [Python: Modules](https://docs.python.org/3/py-modindex.html)
