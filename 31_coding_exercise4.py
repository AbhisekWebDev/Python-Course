height = input("Enter the height seperated by a space : ")

height_list = height.split()

# ye loop luiye h no of elements ko count krne k lye
count = 0

for height in height_list:
    count += 1
print(f"Number of heights entered: {count} 🧮")

# ye loop h saare elements ko string se integer me typecast krne k lye
for i in range(count):
    height_list[i] = int(height_list[i])
print(f"Height list (in cm) : {height_list} 📏")

total = 0

# ye loop h height_list k saare elements ko add krne k lye
for person in height_list:
    total += person
print(f"Total height : {total} cm ➕")

avg = total/count
print(f"Average height : {round(avg)} cm 📊")