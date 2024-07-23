# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.


# The self Parameter
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
# It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
    



class Instructor:
    followers = 0 # class object variable
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def display(self, course): # this is a method & isme self keyword dalna compulsary h
        print(f"Kumar {self.name} is learning {course}")
    
    def update_follower(self, follower_name):
        self.followers += 1

instructor1 = Instructor("Abhi", "Bihar")
instructor2 = Instructor("Abhivav", "Bihar")

print(instructor1.followers)

instructor1.display("python")

instructor1.update_follower("Abhinav")
print(instructor1.followers)

instructor2.update_follower("Abhisek")
print(instructor2.followers)




# Modify Object Properties
# &
# Delete Object Properties

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)

p1.age = 40 # modify the object property
print(p1.age)

del p1.age # delete the object property
print(p1.age)