count = 1

while count <= 5: print(count); count += 1
print("out of loop")


count1 = 5

while count1 > 0:
    print(count1)
    count1 -= 1
else:
    print("in else block")

print("out of the loop")


count2 = 5

while count2 > 0:
    print(count2)
    count2 -= 1
    if count2 == 3:
        break
else:
    print("in else block")

print("out of the loop")


number = int(input("Enter a number (-1 to abort) : "))

while number != -1:
    print(number)
    number = int(input("Enter a number (-1 to abort) : "))
else:
    print("in else block")

print("out of the loop")


count3 = 0

while True:
    print(count3)
    count3 += 1
    if count3 == 5:
        break
else:
    print("in else block")

print("out of the loop")


# assignment
num = int(input("Enter a number to find the sum of them : "))

total = 0

while True:
    total += num
    num = int(input("Enter a number to find the sum of them : "))
    if num == 0:
        print("invalid entry")
        break
print(f"Sum is {total}")

# another way of the assignment - dusra tareeka 
while num != 0:
    total += num
    num = int(input("Enter a number to find the sum of them : "))
print(f"Sum is {total}")