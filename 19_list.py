num_list = [1,2,3,4,5,6,7,8,9,0,2,1]

name_list = ["Abhi", "Abhi", "Kumar"]

mix_list = [1, "Abhi", 10.9, True, 'A']


print(num_list)

print(name_list)

print(mix_list)

print("length of the list is : " + str(len(num_list)))

print("List allows (-)ve numbers to index from the end of the list : " + str(num_list[-1]))

print("List starts from 0th index to complete end -> [0:] : " + str(num_list[0:]))

print("List starts from 1st index to 3 - 1 position -> [1:3] : " + str(num_list[1:3]))

print("List starts from 0th index to 5 - 1 position -> [1:3] : " + str(num_list[:5]))

print("List starts from 0th index to 5 - 1 position & jump 2 elements-> [0:5:2] : " + str(num_list[0:5:2]))

print(max(num_list))


print("Using sort() function to sort the list : ")

num_list.sort()

print(num_list)


print("Using reverse() function to reverse the list : ")

num_list.reverse()

print(num_list)


print("Using append() function to append in the list this function accepts only one argument: ")

num_list.append(10)

print(num_list)


print("Using insert() function to insert the in list, this function accepts 2 arguments - insert(index_num, value): ")

num_list.insert(2, 11)

print(num_list)


print("Using extend() function to extend the list : ")

num_list.extend([12,13,14,15,16,17,18,19,20])

print(num_list)


print("Using remove() function to remove element from the list : ")

num_list.remove(1)

print(num_list)


print("Using pop() function to remove last element from the list : ")

num_list.pop()

print(num_list)

# there are lots of functions present in the python documentation which you can use apar from the listed above







# some example are : -




# The list() Constructor
# It is also possible to use the list() constructor when creating a new list.

# Example
# Using the list() constructor to make a List:

thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)







# Change a Range of Item Values
# To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values:

# Example
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":

thislist1 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
print(thislist1)
thislist1[1:3] = ["blackcurrant", "watermelon"]
print(thislist1)





# A short hand for loop that will print all items in a list:

thislist2 = ["apple", "banana", "cherry"]
[print(x) for x in thislist2]






# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)




# Sort List

thislist3 = [100, 50, 65, 82, 23]
thislist3.sort()
print(thislist3)





# Sort the list in descending:

thislist4 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist4.sort(reverse = True)
print(thislist4)





# Reverse Order
# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.

# Example
# Reverse the order of the list items:

thislist5 = ["banana", "Orange", "Kiwi", "cherry"]
thislist5.reverse()
print(thislist5)




# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy().

# ExampleGet your own Python Server
# Make a copy of a list with the copy() method:

thislist6 = ["apple", "banana", "cherry"]
mylist = thislist6.copy()
print(mylist)




# Make a copy of a list with the list() method:

thislist7 = ["apple", "banana", "cherry"]
mylist1 = list(thislist7)
print(mylist1)





# Join Two Lists
# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.

# ExampleGet your own Python Server
# Join two list:

list1 = ["a", "b", "c"]

list2 = [1, 2, 3]

list3 = list1 + list2

print(list3)





# Another way to join two lists is by appending all the items from list2 into list1, one by one:

# Example
# Append list2 into list1:

list4 = ["a", "b" , "c"]

list5 = [1, 2, 3]

for x in list5:
  list4.append(x)

print(list4)







# Or you can use the extend() method, where the purpose is to add elements from one list to another list:

# Example
# Use the extend() method to add list2 at the end of list:

list5 = ["a", "b" , "c"]

list6 = [1, 2, 3]

list5.extend(list6)

print(list5)








# Method	            Description
# append()	          Adds an element at the end of the list
# clear()	            Removes all the elements from the list
# copy()	            Returns a copy of the list
# count()	            Returns the number of elements with the specified value
# extend()	          Add the elements of a list (or any iterable), to the end of the current list
# index()	            Returns the index of the first element with the specified value
# insert()	          Adds an element at the specified position
# pop()	              Removes the element at the specified position
# remove()	          Removes the item with the specified value
# reverse()	          Reverses the order of the list
# sort()	            Sorts the list
