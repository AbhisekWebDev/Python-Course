height = int(input("Enter height : "))

bill = 0

if height > 3:
    print("You can ride")

    age = int(input("Enter age : "))

    if age < 12:
        bill = 150
        print("Tricket cost = 150")
    elif age <= 18:
        bill = 250
        print("Tricket cost = 250")
    else:
        bill = 500
        print("Tricket cost = 500")

    want_pic = input("Do you want a pic? - press Y for yes & N for no : ")

    if want_pic == 'y' or want_pic == 'Y':
        bill += 50
        print(f"Your total bill is {bill}")

else:
    print("Cant ride")

print("Thanka")