tuple1 = (1,2,3,4,5,6,7,8,9,9,1,5,6,9,8,2,7,3,4,9)

print(type(tuple1))

print(tuple1)

print(tuple1[2])

print(tuple1[2:6]) # isko slicing khte h

print(tuple1[::2])

print(min(tuple1))

print(max(tuple1))

print(tuple1.count(9)) # this count function counts the number of coourences 

print(tuple1.index(8)) # this index function finds the index number


tuple2 = ("Abhi", 32442723003, 4.0, True, 'A+')

print(tuple2)

print(tuple2[-2])


tuple3 = ("Abhi", "Kumar", "Yay")

print(tuple3)


tuple4 = (tuple1, tuple2, tuple3) # nested tuples

print(tuple4)

print(tuple4[2])


tuple5 = tuple1 + tuple2 + tuple3

print(tuple5)

print(len(tuple5))


list = [1,2,3,4,5,6]

print(tuple(list)) # this tuple function converted a list into tuple


tuple6 = (100, ) * 5

print(tuple6)


tuple7 = ("Abhi", ) * 6

print(tuple7)









# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# ExampleGet your own Python Server
# Convert the tuple into a list to be able to change it:

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)






# Add Items
# Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.

# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.

# Example
# Convert the tuple into a list, add "orange", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
z = list(thistuple)
z.append("orange")
thistuple = tuple(z)
