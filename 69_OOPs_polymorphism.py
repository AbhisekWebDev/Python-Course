# Class Polymorphism
# Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

# For example, 
# say we have three classes: 
# Car, Boat, and Plane, and they all have a method called move():

class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car = Car("Ford", "Mustang")       #Create a Car class
boat = Boat("Ibiza", "Touring 20") #Create a Boat class
plane = Plane("Boeing", "747")     #Create a Plane class

for x in (car, boat, plane): # Look at the for loop at the end. Because of polymorphism we can execute the same method for all three classes.
  x.move()






# Inheritance Class Polymorphism

# What about classes with child classes with the same name? Can we use polymorphism there?
# Yes. If we use the example above and make a parent class called Vehicle, 
# and make Car, Boat, Plane child classes of Vehicle, the child classes inherits the Vehicle methods, 
# but can override them:

# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle:
  def __init__(self, brand1, model1):
    self.brand1 = brand1
    self.model1 = model1

  def move1(self):
    print("Move1!")

class Car1(Vehicle):
  pass

class Boat1(Vehicle):
  def move1(self):
    print("Sail1!")

class Plane1(Vehicle):
  def move1(self):
    print("Fly1!")

car1 = Car1("Ford1", "Mustang1") #Create a Car object
boat1 = Boat1("Ibiza1", "Touring 201") #Create a Boat object
plane1 = Plane1("Boeing1", "7471") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand1)
  print(x.model1)
  x.move1()




# Child classes inherits the properties and methods from the parent class.

# In the example above you can see that the Car class is empty, but it inherits brand, model, and move() from Vehicle.

# The Boat and Plane classes also inherit brand, model, and move() from Vehicle, but they both override the move() method.

# Because of polymorphism we can execute the same method for all classes.