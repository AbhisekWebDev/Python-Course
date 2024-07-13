# Break Statement

# 1
count = 1
while count <=10:
    print(count)
    count += 1

    if count == 7:
        break
    print("Hi")
print("out of loop")

# 2
greetings = ["Hi", "Hello", "Welcome"]
names = ["Abhisek", "Abhinav", "Jay"]

for greet in greetings:
    for name in names:
        print(greet, name)

        if greet == "Hello" and name == "Abhisek":
            break
    print("Out of inner loop")
print("Out of outer loop")



# Continue Statement

# 1
count1 = 1
while count1 <=10:
    print(count1)
    count1 += 1

    if count1 == 7:
        continue
    print("Hi")
print("out of loop")

# 2
for i in range(1, 11):
    if i == 7:
        continue
    else:
        print(i)



# Pass Statement

for i in range(5):
    pass

# pass ka matlab - do nothing