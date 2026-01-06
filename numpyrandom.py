"""NumPy offers the random module to work with random numbers."""
from numpy import random
import numpy as np
x = random.randint(100)
print(x)
# The random module's rand() method returns a random float between 0 and 1.
x = random.rand()
print(x)
"""In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.
Integers and float
The randint() method takes a size parameter where you can specify the shape of an array."""
# Generate a 1-D array containing 5 random integers from 0 to 100:
x=random.randint(100, size=(5))
print(x)
# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:
x = random.randint(100, size=(3, 5))
print(x)
# The rand() method also allows you to specify the shape of the array.
# Generate a 1-D array containing 5 random floats:
x = random.rand(5)
print(x)
x = random.rand(3, 5)
print(x)
'''The choice() method allows you to generate a random value based on an array of values.
The choice() method takes an array as a parameter and randomly returns one of the values.'''
x = random.choice([3, 5, 7, 9])
print(x)
# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.
x = random.choice([3, 5, 7, 9], size = (3, 5))
print(x)
"""A random distribution is a set of random numbers that follow a certain probability density function.
Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.
We can generate random numbers based on defined probabilities using the choice() method of the random module.
The choice() method allows us to specify the probability for each value.
The probability is set by a number between 0 and 1, where 0 means that the value will never occur and 1 means that the value will always occur."""

"""Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.
The probability for the value to be 3 is set to be 0.1
The probability for the value to be 5 is set to be 0.3
The probability for the value to be 7 is set to be 0.6
The probability for the value to be 9 is set to be 0"""
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)
"""A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
The NumPy Random module provides two methods for this: shuffle() and permutation().
Shuffle means changing arrangement of elements in-place. i.e. in the array itself."""
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
# The shuffle() method makes changes to the original array.
# The permutation() method returns a re-arranged array (and leaves the original array un-changed).
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))

"""Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
Displot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array."""
import matplotlib.pyplot as plt
import seaborn as sns
sns.displot([0, 1, 2, 3, 4, 5])
plt.show()
# Plotting a Displot Without the Histogram
sns.displot([0, 1, 2, 3, 4, 5], kind='kde')
plt.show()

  # Normal distribution
"""Use the random.normal() method to get a Normal Data Distribution.
It has three parameters:
loc - (Mean) where the peak of the bell exists.
scale - (Standard Deviation) how flat the graph distribution should be.
size - The shape of the returned array."""
x = random.normal(size=(2, 3))
print(x)
# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
#    Visualization of Normal Distribution
sns.displot(random.normal(size=1000), kind="kde")
plt.show()

# Binomial Distribution
"""Binomial Distribution is a Discrete Distribution.
It describes the outcome of binary scenarios, e.g. toss of a coin, it will either be head or tails.
It has three parameters:
n - number of trials.
p - probability of occurrence of each trial (e.g. for toss of a coin 0.5 each).
size - The shape of the returned array."""
x = random.binomial(n=10, p=0.5, size=10)
print(x)
 # Visualization of Binomial Distribution
sns.displot(random.binomial(n=10, p=0.5, size=1000))
plt.show()
"""Difference Between Normal and Binomial Distribution
The main difference is that normal distribution is continous whereas binomial is discrete, 
but if there are enough data points it will be quite similar to normal distribution with certain loc and scale."""
data = {
  "normal": random.normal(loc=50, scale=5, size=1000),
  "binomial": random.binomial(n=100, p=0.5, size=1000)
}
sns.displot(data, kind="kde")
plt.show()
# Poisson Distribution
"""Poisson Distribution is a Discrete Distribution.
It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?
It has two parameters:
lam - rate or known number of occurrences e.g. 2 for above problem.
size - The shape of the returned array."""
 #Generate a random 1x10 distribution for occurrence 2:
x = random.poisson(lam=2, size=10)
print(x)
# Visualization of Poisson Distribution
sns.displot(random.poisson(lam=2, size=1000))
plt.show()
  # Logistic Distribution
"""Logistic Distribution is used to describe growth.
Used extensively in machine learning in logistic regression, neural networks etc.
It has three parameters:
loc - mean, where the peak is. Default 0.
scale - standard deviation, the flatness of distribution. Default 1.
size - The shape of the returned array."""
x = random.logistic(loc=1, scale=2, size=(2, 3))
print(x)
# Visualization of Logistic Distribution
sns.displot(random.logistic(size=1000), kind="kde")
plt.show()
