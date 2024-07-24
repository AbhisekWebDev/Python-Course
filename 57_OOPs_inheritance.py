class Human: # parent/super class
    def __init__(self, fingers):
        self.eyes = 2
        self.nose = 1
        self.fingers = fingers

    def eat(self):
        print("I can eat")

    def work(self):
        print("I can work")

class Male(Human): # child/sub class
    def __init__(self, name, fingers): # idhr agr init function define kr rhe h, aur parent ka attributes & methodss access krna h to - super().__init__() likhna hoga
        super().__init__(fingers)
        self.name = name

    def sex(self):
        print("I am female")

    def work(self): # ***method overriding***
        super().work() # super method gives the access to attributes & methods of parent class 
        print("&")
        print("I can code")

    def display(self):
        print(f"Hi I am {self.name} and i have {self.fingers} fingers")

Male = Male("Abhi", 10)
Male.eat()
Male.sex()
Male.work()
print(Male.eyes)
print(Male.name)
print(Male.fingers)
Male.display()



# Inheritance - allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


# super() function - will make the child class inherit all the methods and properties from its parent
# By using the super() function, you do not have to use the name of the parent element, 
# it will automatically inherit the methods and properties from its parent.