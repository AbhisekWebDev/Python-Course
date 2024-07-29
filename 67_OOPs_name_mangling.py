class BaseClass:
    def __init__(self):
        self.__private_attr = "I'm private!"

    def __private_method(self):
        print("This is a private method.")

    def access_private(self):
        print(self.__private_attr)
        self.__private_method()

class SubClass(BaseClass):
    def __init__(self):
        super().__init__()
        self.__private_attr = "I'm another private attribute in SubClass!"

    def access_private_in_subclass(self):
        # Attempting to access the private attribute and method from the base class
        try:
            print(self.__private_attr)
        except AttributeError:
            print("Cannot access private attribute directly in SubClass.")

        try:
            self.__private_method()
        except AttributeError:
            print("Cannot access private method directly in SubClass.")

# Create an object of SubClass
sub_obj = SubClass()

# Accessing private attributes and methods in the base class using a public method
sub_obj.access_private()

# Attempt to access private members in the subclass
sub_obj.access_private_in_subclass()

# Name mangling can be observed by accessing the mangled attribute name
# The private attribute can be accessed using _ClassName__attribute_name
print(sub_obj._BaseClass__private_attr)  # Accessing the private attribute of the base class
sub_obj._BaseClass__private_method()     # Accessing the private method of the base class



# Name mangling is a mechanism in Python that alters the name of a private attribute to avoid name clashes in subclasses. 
# This is achieved by prefixing the attribute name with a double underscore (__). 
# When an attribute name starts with double underscores, Python internally changes the name to include the class name as a prefix.


# BaseClass:

# Contains a private attribute __private_attr and a private method __private_method().
# These private members are accessed internally within the class and through a public method access_private().


# SubClass:

# Inherits from BaseClass.
# Attempts to define its own private attribute __private_attr.
# The method access_private_in_subclass() tries to access the private attribute and method from the base class, 
# but fails because of name mangling.


# Name Mangling:

# Python internally changes the names of private attributes and methods to include the class name as a prefix. 
# For example, __private_attr in BaseClass becomes _BaseClass__private_attr.
# This name mangling prevents accidental access and overrides by subclasses.
# However, name mangling is not a security feature. The mangled names can still be accessed if the correct name is known, 
# as demonstrated with sub_obj._BaseClass__private_attr.


# Output:

# The access_private() method successfully accesses the private attribute and method from BaseClass.
# The access_private_in_subclass() method fails to access the private members of the base class directly, resulting in AttributeError.
# The private members are still accessible using the mangled name, 
# though this practice is generally discouraged as it goes against the principles of encapsulation.