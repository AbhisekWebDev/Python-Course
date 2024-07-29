class Student:
    def __init__(self, name, roll, age):
        self.name = name # self.name = isko attribute khte h ---------- name -> public - access modifier
        self._roll = roll # _roll -> protected - access modifier
        self.__age = age # __age -> private - access modifier
    
    def display(self):
        print(f"Hi {self.name} here from class student, my roll is {self._roll} and my age is {self.__age}")

class Branch(Student):
    pass

branch = Branch("Abhi", 3, 29)
branch.display()
print(branch._roll) # ye access ho jyga branch se kyunki ye protected h aur ye access modifier dusre function (method) me accessible h
print(branch.__age) # ye access nhi ho pyga branch se kyunki ye private h aur ye access modifier dusre function (method) me accessible nhi hota