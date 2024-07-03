print("Order your pizza")

size = input("Enter pizza size \n S for small \n M for medium \n L for large : ")

bill = 0

if size == 'S' or size == 's':
    bill += 100
    print("Small pixxa Prixe = 100")
elif size == 'M' or size == 'm':
    bill += 200
    print("Medium pixxa Prixe = 200")
else:
    bill += 300
    print("Large pixxa Prixe = 100")

add_pepperoni = input("Do you want pepperoni - \n Y for yes & N for no : ")

if add_pepperoni == 'Y' or add_pepperoni == 'y':
    if size == 'S' or size == 's':
        bill += 30
    elif size == 'M' or size == 'm':
        bill += 60
    else:
        bill += 90

extra_cheese = input("Want extraaaaaa chizz - \n Y for yes & N for no : ")

if  extra_cheese == 'Y' or  extra_cheese == 'y':
        bill += 50


print(f"Total = {bill}")