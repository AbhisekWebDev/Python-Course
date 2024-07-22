# Multiline Strings
# You can assign a multiline string to a variable by using three quotes:

# Example
# You can use three double quotes:

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)



# Slicing

# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string.

# ExampleGet your own Python Server
# Get the characters from position 2 to position 5 (not included):

b = "Hello, World!"
print(b[2:5])

# Note: The first character has index 0.

# Slice From the Start
# By leaving out the start index, the range will start at the first character:

# Example
# Get the characters from the start to position 5 (not included):

c = "Hello, World!"
print(c[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:

# Example
# Get the characters from position 2, and all the way to the end:

d = "Hello, World!"
print(d[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:

# Example
# Get the characters:

# From: "o" in "World!" (position -5)

# To, but not included: "d" in "World!" (position -2):

e = "Hello, World!"
print(e[-5:-2])






# Upper Case

# ExampleGet your own Python Server
# The upper() method returns the string in upper case:

f = "Hello, World!"
print(f.upper())

# Lower Case

# Example
# The lower() method returns the string in lower case:

g = "Hello, World!"
print(g.lower())

# Remove Whitespace

# Whitespace is the space before and/or after the actual text, and very often you want to remove this space.

# Example
# The strip() method removes any whitespace from the beginning or the end:

h = " Hello, World! "
print(h.strip()) # returns "Hello, World!"

# Replace String

# Example
# The replace() method replaces a string with another string:

i = "Hello, World!"
print(i.replace("H", "J"))

# Split String
# The split() method returns a list where the text between the specified separator becomes the list items.

# Example
# The split() method splits the string into substrings if it finds instances of the separator:

j = "Hello, World!"
print(j.split(",")) # returns ['Hello', ' World!']



my_string = "banana"
print(my_string.count('a'))  # Output: 3



my_string1 = "hello"
print(my_string1.find('e'))  # Output: 1



my_string2 = "hello"
print(my_string2.isalpha())  # Output: True



my_string3 = "hello123"
print(my_string3.isalnum())  # Output: True



my_string4 = "12345"
print(my_string4.isdigit())  # Output: True



my_string5 = "   "
print(my_string5.isspace())  # Output: True



my_strin6 = "  hello  "     # strip() removes the white spaces
print(my_strin6.strip())  # Output: hello



my_string7 = "  hello  "    # lstrop() left strip
print(my_string7.lstrip())  # Output: hello  



my_string8 = "  hello  "     # rstrop() right strip
print(my_string8.rstrip())  # Output:   hello



my_list = ["hello", "world"]
print(" ".join(my_list))  # Output: hello world



my_string9 = "hello world"
print(my_string9.title())  # Output: Hello World



my_string10 = "hello world"
print(my_string10.split())  # Output: ['hello', 'world']



my_string11 = "hello world"
print(my_string11.partition(' '))  # Output: ('hello', ' ', 'world')



my_string12 = "hello world"
print(my_string12.replace('world', 'Python'))  # Output: hello Python























# Method	                    Description
# capitalize()	                Converts the first character to upper case
# casefold()	                Converts string into lower case
# center()	                    Returns a centered string
# count()	                    Returns the number of times a specified value occurs in a string
# encode()	                    Returns an encoded version of the string
# endswith()	                Returns true if the string ends with the specified value
# expandtabs()	                Sets the tab size of the string
# find()	                    Searches the string for a specified value and returns the position of where it was found
# format()	                    Formats specified values in a string
# format_map()	                Formats specified values in a string
# index()	                    Searches the string for a specified value and returns the position of where it was found
# isalnum()	                    Returns True if all characters in the string are alphanumeric
# isalpha()	                    Returns True if all characters in the string are in the alphabet
# isascii()	                    Returns True if all characters in the string are ascii characters
# isdecimal()	                Returns True if all characters in the string are decimals
# isdigit()	                    Returns True if all characters in the string are digits
# isidentifier()	            Returns True if the string is an identifier
# islower()	                    Returns True if all characters in the string are lower case
# isnumeric()	                Returns True if all characters in the string are numeric
# isprintable()	                Returns True if all characters in the string are printable
# isspace()	                    Returns True if all characters in the string are whitespaces
# istitle()	                    Returns True if the string follows the rules of a title
# isupper()	                    Returns True if all characters in the string are upper case
# join()	                    Joins the elements of an iterable to the end of the string
# ljust()	                    Returns a left justified version of the string
# lower()	                    Converts a string into lower case
# lstrip()	                    Returns a left trim version of the string
# maketrans()	                Returns a translation table to be used in translations
# partition()	                Returns a tuple where the string is parted into three parts
# replace()	                    Returns a string where a specified value is replaced with a specified value
# rfind()	                    Searches the string for a specified value and returns the last position of where it was found
# rindex()	                    Searches the string for a specified value and returns the last position of where it was found
# rjust()	                    Returns a right justified version of the string
# rpartition()	                Returns a tuple where the string is parted into three parts
# rsplit()	                    Splits the string at the specified separator, and returns a list
# rstrip()	                    Returns a right trim version of the string
# split()	                    Splits the string at the specified separator, and returns a list
# splitlines()	                Splits the string at line breaks and returns a list
# startswith()	                Returns true if the string starts with the specified value
# strip()	                    Returns a trimmed version of the string
# swapcase()	                Swaps cases, lower case becomes upper case and vice versa
# title()	                    Converts the first character of each word to upper case
# translate()	                Returns a translated string
# upper()	                    Converts a string into upper case
# zfill()	                    Fills the string with a specified number of 0 values at the beginning