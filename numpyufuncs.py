import numpy as np
"""ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
ufuncs also take additional arguments, like:
where boolean array or condition defining where the operations should take place.
dtype defining the return type of elements.
out output array where the return value should be copied.
Converting iterative statements into a vector based operation is called vectorization.
It is faster as modern CPUs are optimized for such operations."""
# One way of doing it is to iterate over both of the lists and then sum each elements.
# Without ufunc, we can use Python's built-in zip() method:
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []
for i, j in zip(x, y):
  z.append(i + j)
print(z)
# NumPy has a ufunc for this, called add(x, y) that will produce the same result.
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = np.add(x, y)
print(z)
"""To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:
function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays."""
def myadd(x, y):
  return x+y
myadd = np.frompyfunc(myadd, 2, 1)
print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(myadd([1, 2, 3, 4], [5, 6, 7, 8])))
 # Simple Arithmetic
"""You could use arithmetic operators + - * / directly between NumPy arrays, but this section discusses an extension of the same where we have functions that can take any array-like objects e.g. lists, tuples etc. and perform arithmetic conditionally."""
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])
newarr = np.add(arr1, arr2) # subtruct, divide, multiply, power, remainder(mod), divmod, absolute(abs)
print(newarr)
"""Rounding Decimals
There are primarily five ways of rounding off decimals in NumPy:
truncation
fix
rounding
floor
ceil"""
# Remove the decimals, and return the float number closest to zero. Use the trunc() and fix() functions.
arr = np.trunc([-3.1666, 3.6667])
print(arr)
# The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
arr = np.around(3.1666, 2)
print(arr)
# The floor() function rounds off decimal to nearest lower integer.
arr = np.floor([-3.1666, 3.6667])
print(arr)
# The ceil() function rounds off decimal to nearest upper integer.
arr = np.ceil([-3.1666, 3.6667])
print(arr)
"""NumPy provides functions to perform log at the base 2, e and 10.
We will also explore how we can take log for any base by creating a custom ufunc.
All of the log functions will place -inf or inf in the elements if the log can not be computed."""
 # The arange(1, 10) function returns an array with integers starting from 1 (included) to 10 (not included).
 # Use the log2() function to perform log at the base 2.
arr = np.arange(1, 10)
print(arr)
print(np.log2(arr))  # log10()
# Use the log() function to perform log at the base e.
arr = np.arange(1, 10)
print(np.log(arr))
"""NumPy does not provide any function to take log at any base, so we can use the frompyfunc() function along with inbuilt function math.log() with two input parameters and one output parameter:"""
from math import log
nplog = np.frompyfunc(log, 2, 1)
print(nplog(100, 15))
# Addition is done between two arguments whereas summation happens over n elements.
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2])
print(newarr)
# If you specify axis=1, NumPy will sum the numbers in each array.
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])
newarr = np.sum([arr1, arr2], axis=1)
print(newarr)
"""Cummulative sum means partially adding the elements in array.
E.g. The partial sum of [1, 2, 3, 4] would be [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
Perfom partial sum with the cumsum() function."""
arr = np.array([1, 2, 3])
newarr = np.cumsum(arr)
print(newarr)
# To find the product of the elements in an array, use the prod() function.
arr = np.array([1, 2, 3, 4])
x = np.prod(arr)
print(x)
# If you specify axis=1, NumPy will return the product of each array.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([5, 6, 7, 8])
newarr = np.prod([arr1, arr2], axis=1)
print(newarr)
"""Cummulative product means taking the product partially.
E.g. The partial product of [1, 2, 3, 4] is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
Perfom partial sum with the cumprod() function."""
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print(newarr)
"""A discrete difference means subtracting two successive elements.
E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
To find the discrete difference, use the diff() function."""
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr)
print(newarr)
# We can perform this operation repeatedly by giving parameter n.
# E.g. for [1, 2, 3, 4], the discrete difference with n = 2 would be [2-1, 3-2, 4-3] = [1, 1, 1] , then, since n=2, we will do it once more, with the new result: [1-1, 1-1] = [0, 0]
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print(newarr)
# The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)
# To find the Lowest Common Multiple of all values in an array, you can use the reduce() method.
# The reduce() method will use the ufunc, in this case the lcm() function, on each element, and reduce the array by one dimension.
arr = np.array([3, 6, 9])
x = np.lcm.reduce(arr)
print(x)
# Find the LCM of all values of an array where the array contains all integers from 1 to 10:
arr = np.arange(1, 11)
x = np.lcm.reduce(arr)
print(x)
# The GCD (Greatest Common Divisor), also known as HCF (Highest Common Factor) is the biggest number that is a common factor of both of the numbers.
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)
# To find the Highest Common Factor of all values in an array, you can use the reduce() method.
# The reduce() method will use the ufunc, in this case the gcd() function, on each element, and reduce the array by one dimension.
arr = np.array([20, 8, 32, 36, 16])
x = np.gcd.reduce(arr)
print(x)
# NumPy provides the ufuncs sin(), cos() and tan() that take values in radians and produce the corresponding sin, cos and tan values.
x = np.sin(np.pi/2)
print(x)
# array
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.sin(arr)
print(x)
# By default all of the trigonometric functions take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)
# radian o degree
arr = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x = np.rad2deg(arr)
print(x)
"""Finding angles from values of sine, cos, tan. E.g. sin, cos and tan inverse (arcsin, arccos, arctan).
NumPy provides ufuncs arcsin(), arccos() and arctan() that produce radian values for corresponding sin, cos and tan values given."""
x = np.arcsin(1.0)
print(x)
# Find the angle for all of the sine values in the array
arr = np.array([1, -1, 0.1])
x = np.arcsin(arr)
print(x)
# Finding hypotenues using pythagoras theorem in NumPy.
# NumPy provides the hypot() function that takes the base and perpendicular values and produces hypotenues based on pythagoras theorem.
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)
"""Hyperbolic Functions
NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians and produce the corresponding sinh, cosh and tanh values.."""
x = np.sinh(np.pi/2)
print(x)
# array
arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print(x)
"""Finding angles from values of hyperbolic sine, cos, tan. E.g. sinh, cosh and tanh inverse (arcsinh, arccosh, arctanh).
Numpy provides ufuncs arcsinh(), arccosh() and arctanh() that produce radian values for corresponding sinh, cosh and tanh values given."""
x = np.arcsinh(1.0)
print(x)
"""A set in mathematics is a collection of unique elements.
Sets are used for operations involving frequent intersection, union and difference operations.
Create Sets in NumPy
We can use NumPy's unique() method to find unique elements from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays."""
arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)
# To find the unique values of two arrays, use the union1d() method.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.union1d(arr1, arr2)
print(newarr)
# To find only the values that are present in both arrays, use the intersect1d() method.
arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])
newarr = np.intersect1d(arr1, arr2, assume_unique=True)
print(newarr)
# To find only the values in the first set that is NOT present in the seconds set, use the setdiff1d() method.
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setdiff1d(set1, set2, assume_unique=True)
print(newarr)
# To find only the values that are NOT present in BOTH sets, use the setxor1d() method.
set1 = np.array([1, 2, 3, 4])
set2 = np.array([3, 4, 5, 6])
newarr = np.setxor1d(set1, set2, assume_unique=True)
print(newarr)