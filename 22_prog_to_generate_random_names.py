# WAP which will select a random name from the list of names and the selected name will pay the food bill

import random

names = input("Enter names seperated by a comma : ")

names_split = names.split(',')

#print(names_split)

length = len(names_split)

random_names = random.randint(0, length - 1)

print(f"{names_split[random_names]} will pay the food bill")


# the easiest way to do this

random_name = random.choice(names_split)

# print(random_name)

print(f"{random_name} will pay the food bill")