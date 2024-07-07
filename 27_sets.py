set1 = {1,2,3,4,5,6,7,8,9} # the sets are unordered, kabhi bhi kuch bhi print krta h

print(set1)

set1.add(99)

print(set1)

set1.remove(8)

print(set1)

set1.discard(6)

print(set1)

set1.pop() # this will remove any random item from the set

print(set1)

set1.add((11,12,13,14,15)) # this will add a tuple in the set

print(set1)

set1.clear()

print(set1)


set2 = {1,2,3,4,5,6,7,8,9, 1,2,3} # in set duplicates are not allowed

print(set2)


set3 = {"Abhi", True, 10.4, -1, 'A'} # mixed set

print(set3)


set4 = set() # empty set

print(set4)