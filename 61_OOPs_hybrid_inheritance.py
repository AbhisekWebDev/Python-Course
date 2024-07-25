class A:
    def __init__(self, name):
        self.name = name
        print(f"Initialized A with name: {self.name}")
        
    def display(self):
        print(f"display from class A: {self.name}")
        
    def common_method(self):
        print(f"common_method from class A: {self.name}")

class B(A):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
        print(f"Initialized B with name: {self.name}, age: {self.age}")
        
    def display(self):
        print(f"display from class B: {self.name}, age: {self.age}")
        
    def specific_method_b(self):
        print(f"specific_method_b from class B: {self.name}, age: {self.age}")

class C:
    def __init__(self, hobby):
        self.hobby = hobby
        print(f"Initialized C with hobby: {self.hobby}")
        
    def show(self):
        print(f"show from class C: {self.hobby}")
        
    def specific_method_c(self):
        print(f"specific_method_c from class C: {self.hobby}")

class D(B, C):
    def __init__(self, name, age, hobby, location):
        B.__init__(self, name, age)
        C.__init__(self, hobby)
        self.location = location
        print(f"Initialized D with name: {self.name}, age: {self.age}, hobby: {self.hobby}, location: {self.location}")
        
    def display(self):
        print(f"display from class D: {self.name}, age: {self.age}, hobby: {self.hobby}, location: {self.location}")
        
    def specific_method_d(self):
        print(f"specific_method_d from class D: {self.name}, age: {self.age}, hobby: {self.hobby}, location: {self.location}")

# Create an instance of D and demonstrate method calls
d = D("Abhi", 29, "Photography", "Kolkata")
d.display()          # Calls D's display method
d.common_method()    # Calls A's common_method
d.specific_method_b()# Calls B's specific_method_b
d.specific_method_c()# Calls C's specific_method_c
d.specific_method_d()# Calls D's specific_method_d

# Print the Method Resolution Order (MRO)
print(D.mro())
