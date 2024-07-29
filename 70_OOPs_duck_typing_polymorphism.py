class Bird:
    def sound(self):
        pass

class Duck(Bird):
    def sound(self):
        return "Quack"

class Sparrow(Bird):
    def sound(self):
        return "Chirp"

class Penguin(Bird):
    def sound(self):
        return "Squawk"

def make_sound(bird):
    print(bird.sound())

# Creating instances of different bird types
duck = Duck()
sparrow = Sparrow()
penguin = Penguin()

# Demonstrating polymorphism through duck typing
make_sound(duck)      # Output: Quack
make_sound(sparrow)   # Output: Chirp
make_sound(penguin)   # Output: Squawk




# Polymorphism in Python can be demonstrated using duck typing, 
# which is a concept where the type or class of an object is less important than the methods it defines 
# or the operations that can be performed on it. In other words, 
# if an object walks like a duck and quacks like a duck, it is treated as a duck, regardless of its actual type.



# We define a base class Bird with a method sound().
# Three classes (Duck, Sparrow, Penguin) inherit from Bird and implement the sound() method.
# The function make_sound() takes an object of type Bird and calls its sound() method.
# Even though duck, sparrow, and penguin are instances of different classes, 
# they can all be passed to make_sound() because they all implement the sound() method. 
# 
# This is an example of polymorphism in Python, where the function behaves differently based on the object passed to it, 
# leveraging the concept of duck typing.






