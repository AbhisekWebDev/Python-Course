# sum of even number from 1 to 100 including 1 & 100

total = 0

for i in range(2,101,2):
    print(f"Even number in the list from 1 to 100 : {i}")
    total += i
print(total)