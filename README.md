# Python 


## Notes
- install - <https://www.python.org>
- use <https://replit.com> or [visual studio code](https://code.visualstudio.com/) and install python extension
- learn python - <https://www.learnpython.org/>, <https://www.w3schools.com/python/python_intro.asp>, [Python YT playlist](https://youtube.com/playlist?list=PLHl7C8vb5dHanHPOz2TxdZ71NuJU2cyjM)
- how to run python progs - `python`

# Basics

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

## Data types
- integer -  23 or -22
- float - 26.3 or -75.5
- string - "Marj" or 'Marj'
- boolean - true, false
- list - `x = ["red", "purple", "blue"]`
- tuple - `x = ("red", "purple", "blue")`
- dict - `x = {"name" : "Marj", "age" : 21}`
- set `x = {"red", "purple", "blue"}`

## Output and printing
- print(4.5)
- print("Hey world")
- x = "hi", print(x + " world")

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
logical - not, and, or
bitwise - & = AND, | = OR, ~ = NOT

## Escape characs
- \ = escape, \n = new line, \r = return, \t = tab, \b = backspace

## String methods
- `print(hello.upper())` - uppercase entire string 
- `print(hello.lower())` - lowercase
- `print(hello.capatalize())` - capatalize first letter
- `print(hello.count('a'))` - # of times a value is in a string
- `print('hello world'.count('o'))` - chaining
- format() - formats values in string
- index() - searches the string for a value, returns where the value is found
- swapcase() - lower becomes upper, vice versa
- title() - first char of each word is uppercase

## List methods
`myList = ["red", "orange", "yellow", "green", "blue"]` or `myList = list(("red", "orange", "yellow", "green", "blue"))`
- collection which is ordered and changeable, allows duplicate values
- access list - print(myList[:4]) - prints all but blue (1st item has index 0), print(myList[2:]) - prints ygb
- .append() - myList.append("indigo") - adds this to the end of list
- .insert() - myList.insert(2, "indigo") - adds this after orange
- .extend() - myList.extend(secondList) - joins myList and secondList 
- .remove() - myList.remove("yellow")
- .pop() - removes last item, .pop(2) - removes 3rd item
- del myList[2] - removes 3rd item
- .clear() - empties list, no content listed, prints []
- .sort() - sorts alphabetically or numerically, myList.sort(reverse = True) - descending
- make a copy - .copy() or list(myList)

## Tuples
`myTuple = ("red", "orange", "yellow", "green", "blue")` or `myTuple = tuple(("red", "orange", "yellow", "green", "blue"))`
- stores multiple items in a single variable, collection which is ordered and unchangeable or immutable, and allow duplicate values
- convert the tuple into a list to be able to change or add values - `y = list(myTuple)` then `y.append("gray")`, `myTuple = tuple(y)`
- defined as objs with data type 'tuple' `print(type(myTuple))` prints `<class 'tuple'>`
print(len(myTuple)) - # of items in tuple
- create a tuple with only one item - myTuple = ("red",)
- print(myTuple[1]) - prints 2nd item - orange
- [-1] - prints second to last item
- [1:4] - prints oyg
- [:4] - prints all but index 4
- [2:] - prints ygb
- packing - assign values to a tuple. unpacking = extract values
```
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)
```

## Set
`mySet = {"red", "orange", "yellow", "green", "blue"}` or`mySet = set(("red", "orange", "yellow", "green", "blue"))`
-  store multiple items in a single variable, collection which is unordered (no index, changes order every time) and unchangeable, no duplicate values (dupes are ignored)
- built-in methods - add(), discard(), copy, clear, difference, union, update, remove, pop

## Dictionary
- collection which is ordered (version 3.7+) and changeable, no duplicate values (overwrites 1st dupe), used to store data values in key:value pairs
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
- methods to use - copy(), fromkeys(), get(), keys(), update(), values()

## If statements
examples from [W3schools](https://www.w3schools.com/python/python_conditions.asp)
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

## While loops
- can execute a set of statements as long as a condition is true

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

break statement we can stop the loop before it has looped through all the items

Exit the loop when x is "banana":
```
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
```

The continue statement we can stop the current iteration of the loop, and continue with the next

Do not print banana:
```python
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
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

## Functions
- function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

- function is defined using the def keyword:
```python 
def my_function():
  print("Hello from a function")
```
- call a function - my_function()