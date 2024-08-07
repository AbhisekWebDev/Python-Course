# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses. 
# You can add as many arguments as you want, just separate them with a comma.
# The following example has a function with one argument (fname). 
# When the function is called, we pass along a first name, 
# which is used inside the function to print the full name:

# Example
def my_function(fname):
  print(fname + " Kumar")

my_function("Abhi")
my_function("Nav")
my_function("Jay")


# Parameters or Arguments?
# The terms parameter and argument can be used for the same thing: information that are passed into a function.

# From a function's perspective:
# A parameter is the variable listed inside the parentheses in the function definition.
# An argument is the value that is sent to the function when it is called.

# Number of Arguments
# By default, a function must be called with the correct number of arguments. 
# Meaning that if your function expects 2 arguments, 
# you have to call the function with 2 arguments, not more, and not less.

# Example
# This function expects 2 arguments, and gets 2 arguments:

def my_function1(fname, lname): # parrameters or formal parameters
  print(fname + " " + lname)

my_function1("Abhisek", "Kumar") # arguments of actual parameters


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, 
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:

# Example
# If the number of arguments is unknown, add a * before the parameter name:

# 1
def my_function2(*kids):
  print("The youngest child is " + kids[2])

my_function2("Emil", "Tobias", "Linus")

# 2
def addNum(*numbers):
  total = 0
  print(numbers[1])
  for i in numbers:
    total += i
  print(f"sum is : {total}")

addNum(1,2,3,4,5,6,7,8,9) # this acts as a tuple and tuples are immutable
addNum(1,2,3,4,5,6,7)


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, 
# add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:

# Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:

# 1
def my_function3(**kid):
  print("His last name is " + kid["lname"])

my_function3(fname = "Tobias", lname = "Refsnes")

# 2
def info_person(**info):
  for key, value in info.items():
    print(key, value)

info_person(name = "Abhi", age = 29, dept = "BCA")
info_person(name = "Nav", dept = "B.Tech")


# Default Parameter Value
# The following example shows how to use a default parameter value.
# If we call the function without argument, it uses the default value:

# Example
def my_function4(country = "Norway"):
  print("I am from " + country)

my_function4("Sweden")
my_function4("India")
my_function4()
my_function4("Brazil")


# Passing a List as an Argument
# You can send any data types of argument to a function (string, number, list, dictionary etc.), 
# and it will be treated as the same data type inside the function.

# E.g. if you send a List as an argument, it will still be a List when it reaches the function:

# Example
def my_function5(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function5(fruits)


# Return Values
# To let a function return a value, use the return statement:

# Example
def my_function6(x):
  return 5 * x

print(my_function6(3))
print(my_function6(5))
print(my_function6(9))


# Recursion
# Python also accepts function recursion, which means a defined function can call itself.
# Recursion is a common mathematical and programming concept. It means that a function calls itself. 
# This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be quite easy to slip into writing a 
# function which never terminates, or one that uses excess amounts of memory or processor power. However, 
# when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). 
# We use the k variable as the data, which decrements (-1) every time we recurse. 
# The recursion ends when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly this works, 
# best way to find out is by testing and modifying it.

# Example
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)










# Types of functions

# Function Without Argument and Without Return

def greet():
    print("Hello, welcome to Python programming!")

greet()



# Function With Argument and Without Return
# This function takes a name as an argument and prints a greeting message.

def greet_user(name):
    print(f"Hello, {name}! Welcome to Python programming!")

greet_user("Alice")



# Function Without Argument and With Return

def get_greeting():
    return "Hello, welcome to Python programming!"

message = get_greeting()
print(message)



# Function With Argument and With Return
# This function takes two numbers as arguments and returns their sum.

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(f"The sum of 5 and 3 is {result}")



# Title Case Program

def format_name(f_name, l_name):
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"

fname = input("Enter first name : ")
lname = input("Enter last name : ")

print(format_name(fname, lname))









import statistics

def mean_median_mode(list):
  return statistics.mean(list), statistics.median(list), statistics.mode(list)

a, b, c = mean_median_mode([1,2,3,4,5,6,7,8,9,3,5,9,8,8,3,5,4,3])

print(f"Mean = {a}, Median = {b}, Mode = {c}")
