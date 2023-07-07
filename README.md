# Python Fundamentals


## Notes
- install - <https://www.python.org>
- use <https://replit.com> or [visual studio code](https://code.visualstudio.com/) and install python extension
- learn python - <https://www.learnpython.org/>, <https://www.w3schools.com/python/python_intro.asp>, [Python YT playlist](https://youtube.com/playlist?list=PLHl7C8vb5dHanHPOz2TxdZ71NuJU2cyjM), [python overview](https://www.w3schools.com/python/python_reference.asp), [FCC - Python Playbook](https://www.freecodecamp.org/news/the-python-handbook/#introductiontopython)
- how to run python progs - `python`
- Projects - [Bite-Size Python](https://amzn.to/3wlxPjY) (afflitate), [Big Book of Python projects](https://amzn.to/302qucI) (afflitate), YouTube - [Python playlist](https://youtube.com/playlist?list=PLHl7C8vb5dHanHPOz2TxdZ71NuJU2cyjM)

- mutable = flexible / lists, dicts, sets
- immutable  delete and recreate / ints, floats, str, bools, tuples, frozenset
- type() - returns data type `type(1) = int`

## Comments

- `# comment here`
- `name = "Marj" # another comment here`
- multi-line
```python
"""
multi line
comment
"""
```

## Vars 
- `name = 'Marj'`, vars stores data, no special characs or start with a #, snake case = 'var_name' or camel case = varName, vars are case sensitive
- track vars - %who (list vars) or %whos (lists vars, type, data/info)
- concatenate: 
```python
x = 'hi'
y = 'world'
z = x + " " + y
print(z) # prints hi world
```

Casting - specify a type on to a variable
- str(3) = '3'
- int(3) = 3
- float(3) = 3.0

Conversion
"enables you to change the int variable from int to str so that you can combine the two variables together. Calling str() on either a float or an int will change the value to a str.
However, keep in mind that this change applies only to the output and does not
change the type of the original variable."

```python
city = 'NYC'
state = 'NY'
zip_code = 10003

location = city + ', ' + state + ' ' + str(zip_code)
print(location)
```

## Data types
- integer (int) -  23 or -22
- float - 26.3 or -75.5
- complex - 3 + 2j
- string (str) - "Marj" or 'Marj'
- boolean (bool) - true, false
- list - `x = ["red", "purple", "blue"]`
- tuple - `x = ("red", "purple", "blue")`
- dict - `x = {"name" : "Marj", "age" : 21}`
- set `x = {"red", "purple", "blue"}`

## Output and printing
- print(4.5)
- print("Hey world")
- x = "hi", print(x + " world")
- print(variable.find('string')) - `print(month.find('u'))` prints index of charac
- print(variable[index]) - `print(car[2])` prints specific index / `print(car[−2])` prints 2nd to last charac

## Input
-  `input('Name: ')`
- view users input, assign to var 
```python
name = input('Name: ')
print(name)
```

## Operators
'=' assigns a value to operator - `age = 21`
assignment ops - `x += 3` same as `x = x + 3` and `x *= 3` same as `x = x * 3`, also - -=, /=, %=, \**=
arithmetic operators - +, -, \*, /, %, \** (exponents: `x ** y`), // = floor division   
comparisons - ==, !=, <, >, >=, <= -
logical - not, and, or / if 1st expression chained by 'and' is false or 'or is True, rest of cluase not evaluated, put simples clauses 1st
bitwise - & = AND, | = OR, ~ = NOT 
- use () to control order of evaluation
- Membership tests - in, not in - 'rain' in message = True


## Escape characs
- \ = escape, \n = new line, \r = return, \t = tab, \b = backspace

## User Input

Python 3.6 uses the input() method. Can ask user for input. 
```python 
username = input("Enter username:")
print("Username is: " + username) 
```

```python
name = input("What's your name?: ")
age = input("How old are you?: ")

print("Hello " + name + "! You are " + age + " years old.")
```

# F Strings 

```
name = "Marj G"
print(f"Your name is {name}.") # 'Your name is Marj G'
```

```python
user = {name: "Marj G", email: "youremail@gmail.com"}
print(f{"Hello, {user['name']}. Your email address is: {user['email']}.")
```

## String methods
- `print(hello.upper())` - uppercase entire string 
- `print(hello.lower())` - lowercase
- `print(hello.capatalize())` - capatalize first letter
- `print(hello.count('a'))` - # of times a value is in a string
- `print('hello world'.count('o'))` - chaining / `message[6::].lower().split()` - removes 6 characs, lowercase for remaining, split into list
- format() - formats values in string
- index() - searches the string for a value, returns where the value is found / items.index(200.14) / index(list) <2: (can use start/stop)
- swapcase() - lower becomes upper, vice versa
- title() - first char of each word is uppercase `print(book.title())`
- strip() - strips away certain characs, or leading and trailing spaces `print(mood.strip('!'))`
- replace() - replace with 2nd argument `print(opinion.replace('hard', 'fun'))`
- len() - # of characs in a string `print(len(state))`, len(list_name) = # of elements in list
- .find(string) - case sensitive, .split(), .join()


## List methods
`myList = ["red", "orange", "yellow", "green", "blue"]` or `myList = list(("red", "orange", "yellow", "green", "blue"))`
- collection which is ordered and changeable/mutable, allows duplicate values
- access list - print(myList[:4]) - prints all but blue (1st item has index 0), print(myList[2:]) - prints ygb
- .append() - myList.append("indigo") - adds this to the end of list
- .insert() - myList.insert(2, "indigo") - adds this after orange
- .extend() - myList.extend(secondList) - joins myList and secondList 
- .remove() - myList.remove("yellow") /  use for larger lists - new_items.remove('coat') / if 'C001' in customer_list: customer_list.remove('C005')
- .pop() - removes last item, .pop(2) - removes 3rd item
- del myList[2] - removes 3rd item / del new_items[1:3]
- .clear() - empties list, no content listed, prints []
- .sort() - in place, sorts alphabetically or numerically permanently, myList.sort(reverse = True) - descending
- .sorted() - not in place, sorts list, original unchanged
- .copy() - make a copy, copies over main list to new list, original list the same
- .deepcopy() - need to import library, creates independent copy of nested list
- .reverse() - in place/permanent, use negative slice for reverse not tin place 

## Slice Operators
can use on lists, sets, tuples

- sliced = [start:stop] or sliced = [start:stop:step] 
- start - default = 0 : stop - includes all previous at start (not inclusive) : step size - increment default = 1 (returns every element)

- [-1] - prints second to last item
- [1:4] - start at 1 and stop at 4
- [:4] - stop at index 4 but don't include
- [2:] - start at 2 and stop at end
- [::2] - start at beg, stop at end, every second one
- [::-1] - reverse a list
- [-2:] - last two characs or elements 


## Tuples
- less memory than lists, executes quicker, reduces user erros
`myTuple = ("red", "orange", "yellow", "green", "blue")` or `myTuple = tuple(("red", "orange", "yellow", "green", "blue"))`
- stores multiple items in a single variable, collection which is ordered and unchangeable or immutable, and allow duplicate values
- convert the tuple into a list to be able to change or add values - `y = list(myTuple)` then `y.append("gray")`, `myTuple = tuple(y)`
- defined as objs with data type 'tuple' `print(type(myTuple))` prints `<class 'tuple'>`
- print(len(myTuple)) - # of items in tuple
- create a tuple with only one item - myTuple = ("red",)
- print(myTuple[1]) - prints 2nd item - orange
- packing - assign values to a tuple. 
- tuple() - unpacking = extract values 

```python
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```

## Set
- collection of unique values, unordered - no indexing or keys, mutable values, set values = unique and immutable, no repeats/duplicates are removed
- use cases - more efficient than lists whe performing membership tests ('item' in list), gather unique values w/o looping `list(set(shipments_today))`, find date shared or not shared btwn items w/o looping `set(shipment_today).difference(set(shipment_yesterday))`

`mySet = {"red", "orange", "yellow", "green", "blue"}` or`mySet = set(("red", "orange", "yellow", "green", "blue"))`
- built-in methods - add(), discard(), copy, clear, difference, update, remove, pop

- union() - unique values in both sets `weekend_set = set(sat_cust).union(sun_cust)`
- intersection() - all values in both sets - `weekend_set.intersection(set(fri_cust))`
- difference() - returns values in set1 not set2 / set1 - set2, order matters
- symmetric_difference() - values not shared, opposite of intersection / set1.symmetric_difference(set2)



## Dictionary
- collection which is ordered (version 3.7+) and changeable, no duplicate values (overwrites 1st dupe), used to store data values in key:value pairs / keys = unique and immutable, values = not unique, use any data type

```python
myFamily = {
  "child1": {
  "name": "Marj",
  "age": 22,
  "city": "Atlanta"
  },
  "child2": {
  "name": "Vee",
  "age": 27,
  "city": "Orlando"
  }
}
```
- methods to use - copy(), fromkeys(), get() - value for given key `get(k, value if key not found)`, update('k':v) - appends, items() - pairs tuples, keys() - returns keys, values() - returns values

- call - item['skis'] 
- add or reassign - item['skis'] = 14.99
- delete - del item['coffee'] 
- item_details.values()
- item_details.get("item", "we don't carry that item") - used to avoid errors in case item not found
- item_details.update({'item': [29.99, 0, 'sold out']})

**zip** builds dicts, 2 iterables only
```python
list_one = [[..], [..]] # v
list_two = ['..', '..'] # k

item_dict = dict(zip(list_two, list_one))

# output {'..': [..], '..': [..]}


# mulitple iterables
dict(zip(item_ids, zip(names, prices, category, sizes)))

# 1st zip for key, 2nd zip for values
```

Nested dictionaries
outerdict(keys:{innerdict(values): [..], [..]})
item_list = {
  2019:{'skis':[249.99,10,'instock'], 'snowboards': [99.99,0,'sold out']}, 
  2020:{'skis':[259.99,10,'instock'], 'snowboards': [109.99,0,'sold out']},
  2021:{'skis':[269.99,10,'instock'], 'snowboards': [129.99,0,'sold out']}
}
- call - item_list[2020]['price']


## Comprehension
List comprehension - when you want to create a new list based on the values of an existing list. For dict, lists, sets. For tuples `x = tuple(condition)`

Syntax
`newlist = [expression for item in iterable if condition == True]`

```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) # prints ['apple', 'banana', 'mango']
```

nested lists
```python
list = [
  ['a', 'b', 'c'], 
  ['d', 'e', 'f'],
  ['g', 'h', 'i']
  ]

```
- list[1] = ['d', 'e', 'f']
- list[1][1] = 'e'
- list[1].append('k') = defk


## If statements
examples from [W3schools](https://www.w3schools.com/python/python_conditions.asp)
indentation is muy importante! 

```python
a = 33
b = 200

if b > a:
  print("b is greater than a")
  ```

elif
  ```python 
a = 33
b = 33  

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
  ```

else 
```python 
a = 200
b = 33

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
  ```

shorthand if 
`if a > b: print("a is greater than b")`

shorthand if else 
```python
a = 2
b = 330

print("A") if a > b else print("B")
```

and
```python 
a = 200
b = 33
c = 500

if a > b and c > a:
  print("Both conditions are True")
```

or 
```python 
a = 200
b = 33
c = 500

if a > b or a > c:
  print("At least one of the conditions is True")
```

Nested
if condition:
  if :
  else :
elif :
else :


## While loops
- can execute a set of statements as long as a condition is true (`while condition == True:`)

Print i as long as i is less than 6:
```python 
i = 1

while i < 6:
  print(i)
  i += 1
```   

The **break** statement we can stop the loop even if the while condition is true. 

Exit the loop when i is 3:
```python
i = 1

while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
```

The continue statement we can stop the current iteration, and continue with the next

Continue to the next iteration if i is 3:
```python 
i = 0

while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
```

## For loops
used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). can execute a set of statements, once for each item in a list, tuple, set.

for item in iterable:
  do this

Print each fruit in a fruit list:
```python 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
```

Prints each letter in a list
```
for x in "banana":
  print(x)
```

- range function - sequence of ints, generated by start, stop, step or 2 args - start, stop, works well with loops

```python
for i in range(10, -1, -1): 
  print(i)
```
range(0,100,10)[5] = 50
list(range(0,100,10)) = 0,10,20,30,40,50

### loop controls
**break** statement stops the loop before completion, avoid infinite loops

Exit the loop when x is "banana":
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```

The **continue** statement skips to next iteration in loop, repeats prev code

Do not print banana:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
```
**pass** serves as a placeholder for future code, avoiding run errors with incomplete logic
```python
if 'ski' in item
  pass # comment for later

```

**try, except** help with error and exception handling, for resolving errors in a loop without stopping execution midway

```python
for rating in ratings:
  try:
    print(int(rating[0]))
  except ValueError: # TypeError, ValueError, ZeroDivisionError
    print('incorrect data') 
```

The **try** block lets you test a block of code for errors. The try block will generate an exception, because x is not defined:
```python
try:
  print(x)
except:
  print("An exception occurred")
```

The **except** block lets you handle the error.
In this example, the try block does not generate any error:
```python
try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")
```  

The **finally** block lets you execute code, regardless of the result of the try- and except blocks.
```python
try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")
```


Print all numbers from 0 to 5, and print a message when the loop has ended:
```python 
for x in range(6):
  print(x)
else:
  print("Finally finished!")
```
for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error

```python
for x in [0, 1, 2]:
  pass
```
**enumerate** function - returns index and item for each item in an iterable as it loops thru
```python
for index, element in enumerate(list_name):
  print(index, element)
# output (index, element) - 0 5.27 1 8.79 2 17.59 3 21.99 

``` 

multiple lists
```python
for index, element in enumerate(list_name):
  print(list[index].element)
# output snowboard 5.27 boots 8.79 helmet 17.59  

```

```python
# for -singular- in -plural-
taxes = []
total = []

for subtotal in subtotals:
  tax = round(subtotal * .08, 2)
  total = round(subtotal + tax, 2)
  taxes.append(tax)
  totals.append(total)

print(taxes)
print(totals)
```
```python
for i, subtotal in enumerate(subtotals):
  if location[i] == 'Sun Valley':
    tax = round(subtotal * .08, 2)
  elif location[i] == 'Stowe':
    tax = round(subtotal * .06, 2)
  else:
    tax = round(subtotal * .0775, 2)

  total = round(subtotal + tax, 2)  
  taxes.append(tax)
  totals.append(total)

print(taxes)
print(totals)
```

Nested loops
```python
for item in item_list:
  for size in size_list:
    print(f"{item} is available in {size}")

```

## Functions
- reusable blocks of code that perform tasks when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. ex. min(), max(), len()
- use cases - when repeating code or copying and pasting code - DRY, when you'll use in the future, when you need to share with others, make complex program made readable
- tip - package pieces of data cleaning or analysis workflow into funcs to save time

- input = args
- function - what the input does, call a func, stored elsewhere
- output = values to return
- side effects - changes or actions made by func

def func(args):
  do this
  return output

- function is defined using the **def** keyword:
```python 
def function_name(args):
  print("Run")
  
func() # call a function
```
- **parameters** - is the variable listed inside the parentheses in the function definition
- **arguments** (args) - var names separated by commas, info can be passed into functions, value that is sent to the function when it is called. (below: fname and lname are args)

if your function expects 2 arguments, you have to call the function with 2 arguments

```python 
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Marj", "Gee")
```

Arbitrary Arguments, _*args_ tuples, pass 1+ args
If the number of arguments is unknown, add a * before the parameter name:
```python
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")
```

unpack operator *
```python
def func(x, y):
  print(x, y)

pairs = [(1,2), (3,4)]

for pair in pairs:
  func(*pair) # prints 1 2 \n 3 4
```
for dict - `func(**{'x': 2, 'y': 5})`

_**kwargs_ - keyword args = dicts, any # or args, use to unpack dicts and pass it as kwargs (machine learning)

**Return** Values - to let a function return a value, use the return statement:

```python
def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))
```

**pass** statement - func def cant be empty - 

```def myfunction():
  pass
```
### docstrings

```python
def concatenator(string1, string2):
  """ what this func  does
  args
    string1(str): ..
    string2(str): ..
  returns

  """
return string1 + " " + string2

# use ? to retrieve docstring 'concatenator?'
```
- arg types - docstrings = *positional* args - passed in order defined, *keyword* any order


## Math Functions 
- min() and max() functions can be used to find the lowest or highest value in an iterable
- round() - 'round(#, # of digits)' / `round(transactions * .08, 2)`
- abs() - absolute(-3) = 3
- sum() - sum(1,2,3), sum(transactions)
- find average - sum(list_name) / len()

```python 
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x) # prints 5
print(y) # prints 25
```
built-in module called math, which extends the list of mathematical functions. To use - `import math` can use the `math.sqrt()` method 
- math.pi (prints 3.141592653589793), math.ceil(), math.floor()

```python
import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
```


### Lambda Functions 
A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression. Use lambda functions when an anonymous function is required for a short period of time. 

Syntax `lambda arguments : expression`

Add 10 to argument a, and return the result:
```python
x = lambda a : a + 10
print(x(5))
```

map and filter
```python
x = [1,5,7,10,23,50]

mp = map(lambda i: i + 2, x)

print(list(mp)) # adds 2 to the values and prints new list in brackets

```
filter `mp = filter(lambda i: i % 2 == 0, x)` - only return values that are even


## Classes and objects
Python is an OOP. most things in Python are objects, with its props and methods. Class = blueprint for creating objects.

Create a class named MyClass, with a property named x, create an object named p1, print value of x:
```python 
class MyClass: 
  x = 5 

p1 = MyClass() 

print(p1.x) # prints 5
```

All classes have a function called `__init__()`, which is always executed when the class is being initiated. 

Use the `__init__()` function to assign values to object properties, or other operations that are necessary to do when the object is being created:

```python 
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name) # prints John
print(p1.age) # prints 36
```
The `__init__()` function is called automatically every time the class is being used to create a new object.


**Object Methods** - objects can also contain methods. Methods in objects are functions that belong to the object. 
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class. (Doesn't have to be called 'self')

```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() 

# prints Hello my name is John
```

- del - `del p1.age` = dels age prop from the p1 obj, del p1 = dels p1 obj 

## Iterators
- an object that contains a countable number of values. [w3schools](https://www.w3schools.com/python/python_iterators.asp)

## Modules 
Consider a module to be the same as a code library. A file containing a set of functions you want to include in your application.

To create a module just save the code you want in a file with the file extension .py. Save this code in a file named mymodule.py:

```python
def greeting(name):
  print("Hello, " + name)
```  

When using a function from a module, use the syntax: `module_name.function_name`:

```python
import mymodule
mymodule.greeting("Marj")
```

- `import mymodule as mx` - can rename module
- dir(module) - built-in function to list all the function names (or variable names) in a module
- `from mymodule import person1, print (person1["age"])` - can choose to import only parts from a module, by using the from keyword (imports only the person1 dictionary from the module)


## JSON in Python 

- `import json`
- If you have a JSON string, you can parse it by using the json.loads() method.
- If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

```python 
import json

# a Python object (dict):
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

# prints  {"name": "John", "age": 30, "city": "New York"}
```

When you convert from Python to JSON, Python objects are converted into the JSON (JavaScript) equivalent:

Python | JSON
--- | ---
dict | Object
list | Array
tuple | Array
str | String
int | Number
float | Number
True | true
False | false
None | null

## Regular Expression, RegEx
- a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern. [w3schools](https://www.w3schools.com/python/python_regex.asp)
- built-in package called re, which can be used to work with Regular Expressions. `import re`

Function | Description
--- | ---
findall() | Returns a list containing all matches
search() | Returns a Match object if there is a match anywhere in the string
split() | Returns a list where the string has been split at each match
sub() | Replaces one or many matches with a string

## PIP
Package manager for Python packages, or modules if you like. For Python version 3.4 or later, PIP is included by default.

What's a package? A package contains all the files you need for a module. Modules are Python code libraries you can include in your project.

- Install pip. to download a pkg - pip install camelcase
- Find pkgs - <https://pypi.org>
- Remove pkgs - pip uninstall camelcase
- List pkgs - pip list


