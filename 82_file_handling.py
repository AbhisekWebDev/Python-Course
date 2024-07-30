# File Handling

# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist
# "a" - Append - Opens a file for appending, creates the file if it does not exist
# "w" - Write - Opens a file for writing, creates the file if it does not exis
# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode
# "b" - Binary - Binary mode (e.g. images)

# Syntax - To open a file for reading it is enough to specify the name of the file:
# f = open("demofile.txt")

# The code above is the same as:
# f = open("demofile.txt", "rt")

# Because "r" for read, and "t" for text are the default values, you do not need to specify them.

# Note: Make sure the file exists, or else you will get an error.







# Open a File on the Server

# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:

# ExampleGet your own Python Server

f = open("82_file_handling.txt", "r")
print(f.read())

# Open a file on a different location:
# f = open("D:\\myfiles\welcome.txt", "r")
# print(f.read())

# Read Only Parts of the File
# By default the read() method returns the whole text, but you can also specify how many characters you want to return:

# Example
# Return the 5 first characters of the file:

f = open("82_file_handling.txt", "r")
print(f.read(5))

# Read Lines
# You can return one line by using the readline() method:

# Example
# Read one line of the file:

f = open("82_file_handling.txt", "r")
print(f.readline())
print(f.readline())
# By calling readline() two times, you can read the two first lines:

# By looping through the lines of the file, you can read the whole file, line by line:

# Example
# Loop through the file line by line:

f = open("82_file_handling.txt", "r")
for x in f:
  print(x)

# Close Files
# It is a good practice to always close the file when you are done with it.

# Example
# Close the file when you are finish with it:

f = open("82_file_handling.txt", "r")
print(f.readline())
f.close()


# Write to an Existing File
# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

# ExampleGet your own Python Server
# Open the file "demofile2.txt" and append content to the file:

f = open("82_file_handling.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("82_file_handling.txt", "r")
print(f.read())

f = open("82_file_handling.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the overwriting:
f = open("82_file_handling.txt", "r")
print(f.read())

# Create a file called "myfile.txt":

# f = open("82_myfile.txt", "x")

# Create a new file if it does not exist:

# f = open("82_myfile_1.txt", "w")


# Delete a File
# To delete a file, you must import the OS module, and run its os.remove() function:

# ExampleGet your own Python Server
# Remove the file "demofile.txt":

import os

# os.remove("82_myfile_1.txt")

# Check if File exist:
# To avoid getting an error, you might want to check if the file exists before you try to delete it:

if os.path.exists("myfile.txt"):
  os.remove("myfile.txt")
else:
  print("The file does not exist")

# Delete Folder
# To delete an entire folder, use the os.rmdir() method:

# Example
# Remove the folder "myfolder":

# import os
# os.rmdir("myfolder")  Note: You can only remove empty folders.