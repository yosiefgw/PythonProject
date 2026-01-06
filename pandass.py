"""Pandas is a Python library and Pandas is used to analyze data.
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
Pandas allows us to analyze big data and make conclusions based on statistical theories.
Pandas can clean messy data sets, and make them readable and relevant.
alias: In Python alias are an alternate name for referring to the same thing."""
import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)
# to know the pandas version
print(pd.__version__)
# A Pandas Series is like a column in a table.
# It is a one-dimensional array holding data of any type.
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)
# If nothing else is specified, the values are labeled with their index number. First value has index 0, second value has index 1 etc.
# This label can be used to access a specified value.
print(myvar[1])
# With the index argument, you can name your own labels.
a = [1, 7, 2]
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)
# You can also use a key/value object, like a dictionary, when creating a Series.
# The keys of the dictionary become the labels
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)
# Pandas use the loc attribute to return one or more specified row(s)
#refer to the row index:
# This example returns a Pandas Series.
print(df.loc[0])
# Return row 0 and 1:
# When using [], the result is a Pandas DataFrame.
#use a list of indexes:
print(df.loc[[0, 1]])
# to return haeders and row we use head() method
print(df.head(5))
# The number of rows returned is defined in Pandas option settings.
# You can check your system's maximum rows with the pd.options.display.max_rows statement.
print(pd.options.display.max_rows)  # we can make it large pd.options.display.max_rows = 10000
"""JSON = Python Dictionary
SON objects have the same format as Python dictionaries.
If your JSON code is not in a file, but in a Python Dictionary, you can load it into a DataFrame directly:"""
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}
df = pd.DataFrame(data)
print(df)
"""One of the most used method for getting a quick overview of the DataFrame, is the head() method.
The head() method returns the headers and a specified number of rows, starting from the top.
There is also a tail() method for viewing the last rows of the DataFrame.
The tail() method returns the headers and a specified number of rows, starting from the bottom."""
df = pd.read_csv('data.csv')
print(df.head(10))
# The DataFrames object has a method called info(), that gives you more information about the data set.
print(df.info())
"""Data cleaning means fixing bad data in your data set.
Bad data could be:
Empty cells
Data in wrong format
Wrong data
Duplicates"""
"""Empty Cells
Empty cells can potentially give you a wrong result when you analyze data.
Remove Rows
One way to deal with empty cells is to remove rows that contain empty cells.
This is usually OK, since data sets can be very big, and removing a few rows will not have a big impact on the result."""
# By default, the dropna() method returns a new DataFrame, and will not change the original.
df = pd.read_csv('data.csv')
new_df = df.dropna()
print(new_df.to_string())
# If you want to change the original DataFrame, use the inplace = True argument:
df = pd.read_csv('data.csv')
df.dropna(inplace = True)
print(df.to_string())
"""Another way of dealing with empty cells is to insert a new value instead.
This way you do not have to delete entire rows just because of some empty cells.
The fillna() method allows us to replace empty cells with a value:"""
df = pd.read_csv('data.csv')
df.fillna(130, inplace = True)
print(df.to_string())
#Notice in the result: empty cells got the value 130 (in row 18, 22 and 28).
# To only replace empty values for one column, specify the column name for the DataFrame:
df = pd.read_csv('data.csv')
df.fillna({"Calories": 130}, inplace=True)
print(df.to_string())
#This operation inserts 130 in empty cells in the "Calories" column (row 18 and 28).
"""A common way to replace empty cells, is to calculate the mean, median or mode value of the column.
Pandas uses the mean() median() and mode() methods to calculate the respective values for a specified column:"""
df = pd.read_csv('data.csv')
x = df["Calories"].mean()
df.fillna({"Calories": x}, inplace=True)
print(df.to_string())
#As you can see in row 18 and 28, the empty values from "Calories" was replaced with the mean: 304.68
df = pd.read_csv('data.csv')
x = df["Calories"].mode()[0]
df.fillna({"Calories": x}, inplace=True)
"""Cells with data of wrong format can make it difficult, or even impossible, to analyze data.
To fix it, you have two options: remove the rows, or convert all cells in the columns into the same format.
Pandas has a to_datetime() method for this:"""
#df = pd.read_csv('data.csv')
#df['Date'] = pd.to_datetime(df['Date'], format='mixed')
#print(df.to_string())
""""Wrong data" does not have to be "empty cells" or "wrong format", it can just be wrong, like if someone registered "199" instead of "1.99".
Sometimes you can spot wrong data by looking at the data set, because you have an expectation of what it should be.
If you take a look at our data set, you can see that in row 7, the duration is 450, but for all the other rows the duration is between 30 and 60.
It doesn't have to be wrong, but taking in consideration that this is the data set of someone's workout sessions, we conclude with the fact that this person did not work out in 450 minutes."""
# One way to fix wrong values is to replace them with something else.
# In our example, it is most likely a typo, and the value should be "45" instead of "450", and we could just insert "45" in row 7:
df = pd.read_csv('data.csv')
df.loc[7,'Duration'] = 45
print(df.to_string())
"""For small data sets you might be able to replace the wrong data one by one, but not for big data sets.
To replace wrong data for larger data sets you can create some rules, e.g. set some boundaries for legal values, and replace any values that are outside of the boundaries."""
df = pd.read_csv('data.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.loc[x, "Duration"] = 120
print(df.to_string())
"""Another way of handling wrong data is to remove the rows that contains wrong data.
This way you do not have to find out what to replace them with, and there is a good chance you do not need them to do your analyses."""
df = pd.read_csv('data.csv')
for x in df.index:
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)
#remember to include the 'inplace = True' argument to make the changes in the original DataFrame object instead of returning a copy
print(df.to_string())
"""To discover duplicates, we can use the duplicated() method.
The duplicated() method returns a Boolean values for each row:"""
df = pd.read_csv('data.csv')
print(df.duplicated())
"""The (inplace = True) will make sure that the method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame."""
df = pd.read_csv('data.csv')
df.drop_duplicates(inplace = True)
print(df.to_string())
#Notice that row 12 has been removed from the result
"""A great aspect of the Pandas module is the corr() method.
The corr() method calculates the relationship between each column in your data set."""
df = pd.read_csv('data.csv')    # The corr() method ignores "not numeric" columns
print(df.corr())
"""Pandas uses the plot() method to create diagrams.
We can use Pyplot, a submodule of the Matplotlib library to visualize the diagram on the screen."""
#Three lines to make our compiler able to draw:
import pandas as pd
import matplotlib.pyplot as plt
# Read CSV file
df = pd.read_csv('data.csv')
# Plot the data
df.plot()
# Show the plot window
plt.show()
"""Specify that you want a scatter plot with the kind argument:
kind = 'scatter'
A scatter plot needs an x- and a y-axis.
In the example below we will use "Duration" for the x-axis and "Calories" for the y-axis.
Include the x and y arguments like this:
x = 'Duration', y = 'Calories'"""
df = pd.read_csv('data.csv')
df.plot(kind = 'scatter', x = 'Duration', y = 'Calories')
plt.show()
# another plot
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()
""""Use the kind argument to specify that you want a histogram:
kind = 'hist'
A histogram needs only one column.
A histogram shows us the frequency of each interval, e.g. how many workouts lasted between 50 and 60 minutes?
In the example below we will use the "Duration" column to create the histogram:"""
df = pd.read_csv('data.csv')
df["Maxpulse"].plot(kind = 'hist')
plt.show()
