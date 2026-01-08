import scipy
"""SciPy is a scientific computation library that uses NumPy underneath.
SciPy stands for Scientific Python.
It provides more utility functions for optimization, stats and signal processing.
constants: SciPy offers a set of mathematical constants, one of them is liter which returns 1 liter as cubic meters."""
from scipy import constants
print(constants.liter)
# If SciPy uses NumPy underneath, why can we not just use NumPy?
# SciPy has optimized and added functions that are frequently used in NumPy and Data Science.
"""As SciPy is more focused on scientific implementations, it provides many built-in scientific constants.
These constants can be helpful when you are working with Data Science.
PI is an example of a scientific constant."""
# A list of all units under the constants module can be seen using the dir() function.
print(dir(constants))
