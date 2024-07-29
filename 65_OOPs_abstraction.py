from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.1416 * self.radius

# Instantiate the objects
rect = Rectangle(10, 5)
circle = Circle(7)

# Display the area and perimeter of the rectangle
print(f"Rectangle: Width = {rect.width}, Height = {rect.height}")
print(f"Area = {rect.area()}")
print(f"Perimeter = {rect.perimeter()}")

# Display the area and perimeter of the circle
print(f"\nCircle: Radius = {circle.radius}")
print(f"Area = {circle.area()}")
print(f"Perimeter = {circle.perimeter()}")




# ***************************************************************************************************************************************
# Shape Class (Abstract Class):
# The Shape class is an abstract base class (ABC) that defines the blueprint for other shapes.
# It contains two abstract methods: area() and perimeter(). 
# These methods do not have an implementation in the Shape class and must be implemented in any subclass.


# Rectangle Class:
# Inherits from the Shape class.
# Implements the area() and perimeter() methods, specific to a rectangle.
# The area() method calculates the area of the rectangle, and the perimeter() method calculates its perimeter.


# Circle Class:
# Also inherits from the Shape class.
# Implements the area() and perimeter() methods, specific to a circle.
# The area() method calculates the area of the circle, and the perimeter() method calculates its circumference.


# Key Points:-

# Abstraction: The Shape class defines a common interface for all shapes but does not provide any specific implementation. 
# This allows the Rectangle and Circle classes to provide their specific implementations of area() and perimeter().

# Encapsulation: The implementation details of the methods are hidden within the Rectangle and Circle classes. 
# The user only interacts with the public interface provided by the Shape class and its concrete subclasses.