import random

a = random.randint(1,9)

print(a)

b = random.random()

print(b)

c = random.uniform(1,9)

print(c)

list = [0,1,2,3,4,5,6,7,8,9]

d = random.choice(list)

print(d)

random.shuffle(list)

print(list)