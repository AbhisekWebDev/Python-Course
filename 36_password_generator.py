import random

print(f"**************************\nPassword Generator\n**************************")


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', 
           '[', ']', '{', '}', ';', ':', '\'', '"', '\\', '|', ',', '.', '<', '>', 
           '/', '?', '`', '~']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


letters_input = int(input("Enter how many letters do you want in your password : "))

symbols_input = int(input("Enter how many symbols do you want in your password : "))

numbers_input = int(input("Enter how many numbers do you want in your password : "))


password_list = []


for i in range(1, letters_input + 1):
    password_list.append(random.choice(letters))


for i in range(1, symbols_input + 1):
    password_list.append(random.choice(symbols))


for i in range(1, numbers_input + 1):
    password_list.append(random.choice(numbers))


random.shuffle(password_list)


password = ""

for char in password_list:
    password += char

print("\nYour Generated Password is : ")
print(f"*****************************\n{password}\n*****************************")