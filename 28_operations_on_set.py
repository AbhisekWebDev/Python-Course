set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = {5,6,7,8}

print(set1.intersection(set2))

print(set2 & set3) # ye python me intersection ka symbol h

print(set1.difference(set2))

print(set2 - set3)

set1.difference_update(set2)
print(set1)

print(set2.symmetric_difference(set3))

print(set1 ^ set2 ^ set3) # ye python me symmetric update ka symbol h

set2.symmetric_difference_update(set1)
print(set2)

print(set1.union(set2))

print(set1.union((1,3)))  # union k andr tuple jor diya set k sath compare krne k lye

set1.update(set3)
print(set1)

print(set1 | set2) # ye python me union ka symbol h




set4 = {"Abhi", "Sek", "Nav"}
set5 = {"Sky", "Sek", "Kumar"}
set6 = {"Abhi", "Nav", "Verma"}

print(set4 | set5 | set6)

print(set4.union(("Raj", "Sek")))

print(set4.union(set5, set6))

set5.update(["Abhisek", "Kumar", "Ram", "Shyam", "sky"]) # update me list jor diya set ko update krne k lye
print(set5)

set5 |= set6 # ye set update krne ka symbolic method h
print(set5)

print(set4.isdisjoint(set5))

print(set5.issubset(set6))

print(set6.issuperset(set5))

print(set4.issubset(set5))

print(set4.issuperset(set5))




set7 = {9,8,7,6,-2,-8,1,2,6,5,4,1,2,3,4,5}
set8 = {6,5,4,3,-7,-9,1,2,8,7,-8,1,2,3,4,5}
set9 = {-1,-3,-5,2,0,1,8,9,-9,3,1,2,3,4,5}

print(set7.isdisjoint(set8))

print(set8.issubset(set9))

print(set8.issuperset(set7))

print(set7.issubset(set8))

print(set7.issuperset(set8))

del set9
print(set9)




set10 = {1,2,3,4,5,6}
set11 = {3,4,5,6.2,1}
set12 = {5,6,7,8.1}

print(set10 <= set11)

print(set11 <= set12)

print(set10 >= set11)

print(set11 >= set12)

print(set10.isdisjoint(set11))

print(set11.issubset(set12))

print(set12.issuperset(set11))

print(set12.issubset(set11))

print(set11.issuperset(set12))