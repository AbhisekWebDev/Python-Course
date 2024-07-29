class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overload the + operator"""
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overload the - operator"""
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        """Overload the * operator for scalar multiplication"""
        return Vector(self.x * scalar, self.y * scalar)

    def __str__(self):
        """String representation of the Vector"""
        return f"Vector({self.x}, {self.y})"

# Create two vectors
vector1 = Vector(1, 2)
vector2 = Vector(3, 4)

# Demonstrate + operator overloading
result_add = vector1 + vector2
print(f"vector1 + vector2 = {result_add}")  # Output: Vector(4, 6)

# Demonstrate - operator overloading
result_sub = vector1 - vector2
print(f"vector1 - vector2 = {result_sub}")  # Output: Vector(-2, -2)

# Demonstrate * operator overloading for scalar multiplication
result_mul = vector1 * 3
print(f"vector1 * 3 = {result_mul}")  # Output: Vector(3, 6)



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __gt__(self, other):
        if self.age > other.age: return True
        else: return False

person1 = Person("Abhisek", 29)
person2 = Person("Abhinav", 23)

if person1 > person2:
    print(f"{person1.name} will pay the bill")
else:
    print(f"{person2.name} will pay the bill")




# Polymorphism through operator overloading in Python allows us to define the behavior of operators like +, -, *, etc., 
# for user-defined types (classes). We achieve this by implementing special methods in our classes.



# Class Definition (Vector):
# The Vector class has two attributes: x and y, representing the vector's coordinates.


# Operator Overloading Methods:

# __add__(self, other): Overloads the + operator to add two vectors. 
# It returns a new Vector object with coordinates that are the sum of the respective coordinates of the two vectors.

# __sub__(self, other): Overloads the - operator to subtract one vector from another. 
# It returns a new Vector object with coordinates that are the differences of the respective coordinates.

# __mul__(self, scalar): Overloads the * operator for scalar multiplication. 
# It multiplies each coordinate by a scalar value and returns a new Vector object.

# __str__ Method: Provides a string representation of the Vector object, useful for printing.


# Usage:

# We create two Vector objects (vector1 and vector2) and demonstrate the use of the overloaded +, -, and * operators.
# This example shows how different operators can be customized to work with user-defined types, enabling polymorphic behavior.