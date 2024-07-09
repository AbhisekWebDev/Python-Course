numbers = input("Enter the list of numners seperated by a space : ")

numbers_list = numbers.split()
print(numbers_list)

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)

max_num = numbers_list[0]

for num in numbers_list:
    if num > max_num:
        max_num = num
print(max_num)