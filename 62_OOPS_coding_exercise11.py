class University:
    def __init__(self, uni_name):
        self.uni_name = uni_name

    def showDetails(self):
        print(f"The name of the university is = {self.uni_name}")

class Course(University):
    def __init__(self, uni_name, course_name):
        University.__init__(self, uni_name)
        self.course_name = course_name

    def showDetails(self):
        print(f"The name of the university is = {self.uni_name} & the course name is = {self.course_name}")

class Branch(University):
    def __init__(self, uni_name, branch_name):
        University.__init__(self, uni_name)
        self.branch_name = branch_name

    def showDetails(self):
        print(f"The name of the university is = {self.uni_name} & the branch name is = {self.branch_name}")

class Student(Course, Branch):
    def __init__(self, uni_name, course_name, branch_name, student_name):
        Course.__init__(self, uni_name, course_name)
        Branch.__init__(self, uni_name, branch_name)
        self.student_name = student_name

    def showDetails(self):
        print(f"The name of the university is = {self.uni_name}, the course name is = {self.course_name}, the branch name is = {self.branch_name} & the name of the student is {self.student_name}")

class Faculty(Branch):
    def __init__(self, uni_name, branch_name, faculty_name):
        super().__init__(uni_name, branch_name)
        self.faculty_name = faculty_name

    def showDetails(self):
        print(f"The name of the university is = {self.uni_name}, the branch name is = {self.branch_name} & the name of the faculty is = {self.faculty_name}")

university = University("BCET")
university.showDetails()

course = Course("BCET", "Python")
course.showDetails()

branch = Branch("BCET", "BCA")
branch.showDetails()

student = Student("BCET", "Python", "BCA", "Abhi")
student.showDetails()

faculty = Faculty("BCET", "BCA", "Dr. XYZ")
faculty.showDetails()
