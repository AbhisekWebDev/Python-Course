name = 'Abhisek'

for i in name:
    print(name)
    
for i in name:
    print(i)



names = ["Abhi", "Sek", "Kumar"]

for name in names:
    print(name)

    if name == "Abhi":
        print("hey, its me")
    else:
        print("hows ya")



num = [1,2,3,4,5,6,7,8,9]

for i in num:
    sq = i ** 2
    print(sq)



nums = [1,2,3,4,5,6,7,8,9]
sqs = []

for i in nums:
    sq = i ** 2
    sqs.append(sq)

print(sqs)