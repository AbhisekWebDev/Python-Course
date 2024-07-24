class Human:
    def __init__(self, city):
        self.eyes = 2
        self.nose = 1
        self.city = city

    def eat(self):
        print("I can eat")
    
    def sleep(self):
        print("I sleep for 10 hours")
    
class Male():
    def __init__(self, name):
        self.name = name

    def work(self):
        print("I can code")

    def sleep(self):
        print("I sleep for 20 hours")

class Boy(Human, Male):
    def __init__(self, name, language, city):
        self.language = language

        Human.__init__(self, city)   # Call the Human __init__ method explicitly
        Male.__init__(self, name)  # Call the Male __init__ method explicitly

    def age(self):
        print("I am 19 yrs. old")

    def display(self):
        print(f"My name is {self.name} i am learning {self.language} and i live in {self.city}")

boy = Boy("Abhi", "python", "kolkata")
boy.eat()
boy.work()
boy.age()
Male.sleep(boy)
print(Boy.mro()) # MRO - method resolution order
print(boy.name)
print(boy.language)
print(boy.city)
boy.display()



# The super() function in Python is used to call methods from a parent or sibling class. 
# It's particularly useful in multiple inheritance situations because it helps to avoid directly specifying the parent class, 
# making the code more maintainable and easier to understand. However, super() works based on the method resolution order (MRO), 
# which defines the order in which base classes are searched when executing a method.

# In this case, the MRO for the Boy class is:

# Boy
# Human
# Male
# object

# When you use super().__init__(name) in the Boy class's __init__ method, Python looks for the next __init__ method in the MRO after Boy. 
# According to the MRO, Human is next, but the Human class's __init__ method does not accept any arguments other than self. 
# This leads to a TypeError because you are trying to pass an additional name argument that Human.__init__ is not designed to accept.

# In multiple inheritance, super() only moves one step up in the MRO. 
# It doesn't know which class's __init__ method to call with which arguments unless you have a consistent method signature 
# across all parent classes, which is not the case here. Therefore, you have to explicitly call the __init__ methods of each base class, 
# like Human.__init__(self) and Male.__init__(self, name), to ensure all necessary initializations are performed correctly.