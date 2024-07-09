tuple = (2,56,34,3,5,-1)

for i in tuple:
    print(i)
else:
    print("success")



tuple1 = (2,56,34,3,5,-1)

for i in tuple1:
    print(i)

    if i == 34:
        break

else:
    print("success")

print("out of for..else")



tuple2 = (2,56,34,3,5,-1)

for i in tuple2:
    if i % 6 == 0:
        print(i)
        break
    else:
        print(f"{i} is not number is divisible by 6")

else:
    print("success")

print("out of for..else")



tuple3 = (2,56,34,3,5,-1)

for i in tuple2:
    if i % 6 == 0:
        print(i)
        break     
else:
    print("no number is divisible by 6")