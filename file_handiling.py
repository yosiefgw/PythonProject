# To open the file, use the built-in open() function.
# The open() function returns a file object, which has a read() method for reading the content of the file:
with open("jossy.txt") as f:
 print(f.read())
# Close the file when you are finished with it:
f = open("jossy.txt")
print(f.readline())
f.close()
# to return return one line by using the readline() method:
with open("jossy.txt") as f:
  print(f.readline())
# By looping through the lines of the file, you can read the whole file, line by line:
with open("jossy.txt") as f:
  for x in f:
    print(x)
# To write to an existing file, you must add a parameter to the open() function:
# "a" - Append - will append to the end of the file
# "w" - Write - will overwrite any existing content
f = open("jossy.txt", "a")
f.write("Now the file has more content!")
#open and read the file after the appending:
with open("jossy.txt") as f:
  print(f.read())
# To overwrite the existing content to the file, use the w parameter:
with open("jossy.txt", "w") as f:
  f.write("Woops! I have deleted the content!")
# open and read the file after the overwriting:
with open("jossy.txt") as f:
  print(f.read())# To create a new file in Python, use the open() method, with one of the following parameters:
# "x" - Create - will create a file, returns an error if the file exists
# "a" - Append - will create a file if the specified file does not exists
# "w" - Write - will create a file if the specified file does not exists
# This will create a new file:
f = open("myfile.txt", "x")
# If the file already exist, an error will be raised.
# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("myfile.txt")
# To avoid getting an error, you might want to check if the file exists before you try to delete it:
import os
if os.path.exists("demofile.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")
# To delete an entire folder, use the os.rmdir() method:
# You can only remove empty folders
import os
os.rmdir("myfolder")