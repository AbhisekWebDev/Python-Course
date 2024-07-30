class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __repr__(self):
        return f"ComplexNumber({self.real}, {self.imaginary})"

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real + other.real
            imaginary = self.imaginary + other.imaginary
            return ComplexNumber(real, imaginary)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real - other.real
            imaginary = self.imaginary - other.imaginary
            return ComplexNumber(real, imaginary)
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real = self.real * other.real - self.imaginary * other.imaginary
            imaginary = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(real, imaginary)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, ComplexNumber):
            return self.real == other.real and self.imaginary == other.imaginary
        return NotImplemented

# Example usage
num1 = ComplexNumber(2, 3)
num2 = ComplexNumber(1, 4)

print("num1:", num1)  # Uses __str__()
print("num2:", num2)

# Adding complex numbers
result_add = num1 + num2
print("Addition (num1 + num2):", result_add)  # Uses __str__()

# Subtracting complex numbers
result_sub = num1 - num2
print("Subtraction (num1 - num2):", result_sub)

# Multiplying complex numbers
result_mul = num1 * num2
print("Multiplication (num1 * num2):", result_mul)

# Checking equality
is_equal = num1 == num2
print("Are num1 and num2 equal?", is_equal)  # Uses __eq__()





# Dunder methods, also known as magic methods, are special methods in Python with double underscores 
# at the beginning and end of their names. They allow developers to define the behavior of objects 
# for built-in functions and operators. Some common dunder methods include __init__ for object initialization, 
# __str__ for string representation, __add__ for addition, and many more.