# to check the python version of the editor
import sys
print(sys.version)
# indentation
if 5 > 2:
    print("Five is greater than two!")
# variables are containers to hold data values
# Variables in python are created when value assign to them
# variable can start with letters or underscore but no number
# variable only contains alphanumeric and underscore
# camel case yosiefGebrewahidKdane
# pascal case YosiefGebrewahidKidane
# snake case yosief_gebrewahid_kidane
# assigning multiple value to variables
A, B, C = "orange", "apples", "bananas"
print(A,B,C) # the number of variables and values should be equal
A = B = C = 'orange'
print(A,B,C)
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ['apple', 'orange', 'banana']
x, y, z = fruits
print(x,y,z)
X = 5
y = "Hello, World!"
print(X,',',y)
# to specify data tpye of a varible, use casting
x = str(3)
print(x)
print(type(x))
y = int(3)
print(y)
print(type(y))
z = float(3)
print(z)

# statments can be separetd by semicolon(new line)
print("Hello"); print("How are you?"); print("Bye bye!")

# to out put variables
x = 'yosief'
y = 'gebrewahid'
z = 'kidane'
w = 5
print(x,y,z) # output with spaces
print(x + y + z) # output without spaces and not good for different data type
# print(x + w) error
print(x, w)
# Variables that are created outside of a function are known as global variables.
# Global variable which can be accessed outside and inside functions by everyone
x = 'awesome'
def hello():
    x = 'fantastic'
    print("yosief is " + x)
hello()
print('jossy is ' + x)
# put global variable inside the function
x = 'awesome'
print('persie is ' + x)
def hello():
    global x  # we can access and modify glabal variables from inside the function
    x = 'fantastic'
    print("yosief is " + x)
hello()
print('jossy is ' + x)
# By default, the print() function ends with a new line.
# If you want to print multiple words on the same line, you can use the end parameter:
print("Hello World!", end=' ') # Note that we add a space after end=" " for better readability.
print("I will print on the same line.")
# You can also use the print() function to display numbers:
# However, unlike text, we don't put numbers inside double quotes:
print('3') # string
print(358)
print(50000)
# You can also do math inside the print() function:
print(3 + 3)
print(2 * 5)
# You can combine text and numbers in one output by separating them with a comma:
print("I am", 35, "years old.")
# Float can also be scientific numbers with an "e" to indicate the power of 10.
x = 35e3
y = 12E4
z = -87.7e100

print(type(x))
print(type(y))
print(type(z))
# Complex numbers are written with a "j" as the imaginary part:
x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))
# You can convert from one type to another with the int(), float(), and complex() methods:
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(y) # You cannot convert complex numbers into another number type.

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))

# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
import random
print(random.randrange(1, 10))
# You can assign a multiline string to a variable by using three quotes:
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)
# Like many other popular programming languages, strings in Python are arrays of unicode characters.
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
  print(x)
  # To get the length of a string, use the len() function.
  a = "Hello, World!"
  print(len(a))
  # To check if a certain phrase or character is present in a string, we can use the keyword in.
  txt = "The best things in life are free!"
  print("free" in txt)
  txt = "The best things in life are free!"
  if "free" in txt:
      print("Yes, 'free' is present.")
# Check if "expensive" is NOT present in the following text:
txt = "The best things in life are free!"
print("expensive" not in txt)
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])
# Python has a set of built-in methods that you can use on strings.
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())
a = "Hello, World!"
print(a.lower())
# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))
# The split() method returns a list where the text between the specified separator becomes the list items.
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
c = a + b
print(c)
# To add a space between them, add a " ":
a = "Hello"
b = "World"
c = a + " " + b
print(c)
# As we learned in the Python Variables chapter, we cannot combine strings and numbers like this:
# But we can combine strings and numbers by using f-strings or the format() method!
# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.
age = 36
txt = f"My name is John, I am {age}"
print(txt)
# An escape character is a backslash \ followed by the character you want to insert.

txt = 'It\'s alright.'
print(txt)
txt = "We are the so-called \"Vikings\" from the north."
print(txt)
txt = "Hello\nWorld!"
print(txt)
txt = "Hello\rWorld!"
print(txt)
txt = "Hello\tWorld!"
print(txt)
#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)
"""Almost any value is evaluated to True if it has some sort of content.
Any string is True, except empty strings.
Any number is True, except 0.
Any list, tuple, set, and dictionary are True, except empty ones."""
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
x = "Hello"
y = 15
print(bool(x))
print(bool(y))
"""In fact, there are not many values that evaluate to False,
except empty values, such as (), [], {}, "", the number 0, 
and the value None. And of course the value False evaluates to False."""
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
# One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
  def __len__(self):
    return 0
myobj = myclass()
print(bool(myobj))
# You can create functions that returns a Boolean Value:
def myFunction() :
  return True
print(myFunction())
# Identity Operators
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is - Checks if both variables point to the same object in memory
# == - Checks if the values of both variables are equal
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
# Membership operators are used to test if a sequence is presented in an object:
x = ["apple", "banana"]
print("banana" in x)
fruits = ["apple", "banana", "cherry"]
print("pineapple" not in fruits)
"""List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members."""
# List
# Lists are used to store multiple items in a single variable.
# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
# Lists are created using square brackets:
# List items are ordered, changeable, and allow duplicate values.
thislist = ["apple", "banana", "cherry"]
print(thislist)
# List items can be of any data type:
# A list can contain different data types:
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list1 = ["abc", 34, True, 40, "male"]
print(list1)
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.
# When specifying a range, the return value will be a new list with the specified items.
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# Convert Python objects into JSON strings, and print the values:
import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))