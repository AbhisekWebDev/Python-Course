class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"name = {self.name} and age = {self.age}")

    def eat(self):
        print("I can eat")
    
    def work(self):
        print("I can work")

class Male(Human):
    def __init__(self, name, age, location):
        Human.__init__(self, name, age)
        self.location = location

    def display(self):
        print(f"name = {self.name}, age = {self.age} and location = {self.location}")

    def sleep(self):
        print("I can sleep whole day")

class Female(Human):
    def __init__(self, name, age, dancer):
        super().__init__(name, age)
        self.dancer = dancer

    def display(self):
        print(f"name = {self.name}, age = {self.age} and dancer = {self.dancer}")

    def work(self):
        print("I can code")

# female = Female("Abhi", 29)
female = Female("Nriti", 26, True)
female.work()
female.eat()
# we cannot access sleep() in this class because female has no connection with the male i.e. female is not inheriting the male, only the human is being inherited by the female
female.display()

male = Male("Abhinav", 23, "Hyderabad")
male.sleep()
male.eat()
male.work()
male.display()