a = 1
b = 2

print("With third variable")
print(f"Before swap a = {a} b = {b}")

temp = a
a = b
b = temp

print(f"After swap a = {a} b = {b}")


x, y = 10, 20

print("Without third variable")
print(f"Before swap x = {x} y = {y}")

x = x + y
y = x - y
x = x - y

print(f"After swap x = {x} y = {y}")