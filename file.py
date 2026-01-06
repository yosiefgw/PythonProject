# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:
with open("jossy.txt") as f:
 print(f.read())
f = open("jossy.txt")
print(f.readline())
f.close()
with open("jossy.txt") as f:
  print(f.readline())
  with open("jossy.txt") as f:
      for x in f:
          print(x)
f = open("jossy.txt", "a")
f.write("Now the file has more content!")
with open("jossy.txt") as f:
  print(f.read())
  with open("jossy.txt", "w") as f:
      f.write("Woops! I have deleted the content!")
  # open and read the file after the overwriting:
  with open("jossy.txt") as f:
      print(f.read())
# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists
#This will create a new file:
f = open("myfile.txt", "x")
#If the file already exist, an error will be raised.
