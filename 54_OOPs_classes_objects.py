class Instructor: # class
    pass

intructor1 = Instructor() # instructor1 is an object

intructor1.name = "Abhisek"
print(intructor1.name)



class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)





# The __init__() Function : -

# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Use the __init__() function to assign values to object properties, 
# or other operations that are necessary to do when the object is being created:

class ClassName:
   def __init__(self):
      print("Abhisek Kumar")

object1 = ClassName()
object2 = ClassName()




class Class:
   def __init__(self, name, address):
      self.Myname = name
      self.Myaddress = address

objectName1 = Class("Abhisek", "Kolkata")
print(objectName1.Myname)
print(objectName1.Myaddress)

objectName2 = Class("Abhinav", "Hyderabad")
print(objectName2.Myname)
print(objectName2.Myaddress)







# The __str__() Function - controls what should be returned when the class object is represented as a string.

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):                    # isko string k trah use kr skte h f-string use r k
    return f"{self.name}({self.age})"

p1 = Person("Abhi", 30)
p2 = Person("Kumar", 45)

print(p1)
print(p2)