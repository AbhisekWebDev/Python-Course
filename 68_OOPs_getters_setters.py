class Employee:
    def __init__(self, name, age, salary):
        self._name = name
        self._age = age
        self._salary = salary

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if isinstance(value, str) and value.strip():
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string.")

    # Getter for age
    @property
    def age(self):
        return self._age

    # Setter for age
    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive integer.")

    # Getter for salary
    @property
    def salary(self):
        return self._salary

    # Setter for salary
    @salary.setter
    def salary(self, value):
        if isinstance(value, (int, float)) and value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary must be a non-negative number.")

# Example usage
try:
    emp = Employee("Alice", 30, 70000)
    print(f"Employee Name: {emp.name}")
    print(f"Employee Age: {emp.age}")
    print(f"Employee Salary: {emp.salary}")

    # Modifying attributes using setters
    emp.name = "Bob"
    emp.age = 35
    emp.salary = 80000

    print(f"Updated Employee Name: {emp.name}")
    print(f"Updated Employee Age: {emp.age}")
    print(f"Updated Employee Salary: {emp.salary}")

    # Attempting to set invalid values
    emp.age = -1  # This will raise a ValueError
except ValueError as e:
    print(e)




# Getters and setters are methods used to access and modify the private attributes of a class. 
# In Python, you can use the @property decorator to define a getter method 
# and the @<property_name>.setter decorator to define a setter method.


# Employee Class:

# The class represents an employee with attributes: name, age, and salary.
# The attributes are prefixed with an underscore (e.g., _name, _age, _salary) to indicate they are intended to be private.


# Getters and Setters:

# Getter for name: The @property decorator is used to define the name method, which acts as a getter for the _name attribute. 
# It allows access to the _name attribute using emp.name.
# Setter for name: The @name.setter decorator defines a method to set the _name attribute. 
# It includes validation to ensure the value is a non-empty string. If the value is invalid, a ValueError is raised.
# Similarly, getters and setters are defined for the age and salary attributes, with appropriate validation checks.


# Example Usage:

# An Employee object is created with initial values for name, age, and salary.
# The attributes are accessed using the getter methods, and modified using the setter methods.
# If an invalid value is provided, the setter method raises a ValueError with a descriptive message.