class Circle:
    def __init__(self, r):
        self.radius = r

    def circumference(self):
        return 2 * 3.14159 * self.radius

    def area(self):
        return 3.14159 * self.radius * self.radius

    def display(self):
        print(f"The circumference of the circle with radius {self.radius} is = {self.circumference()}")
        print(f"The area of the circle with radius {self.radius} is = {self.area()}")

circle1 = Circle(5)
circle1.display()  

circle2 = Circle(15)
circle2.display() 
