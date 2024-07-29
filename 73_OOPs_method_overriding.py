# Superclass
class Animal:
    def sound(self):
        return "Some generic animal sound"

# Subclass
class Dog(Animal):
    def sound(self):
        return "Bark"

# Another subclass
class Cat(Animal):
    def sound(self):
        return "Meow"

# Example usage
animal = Animal()
dog = Dog()
cat = Cat()

print("Animal sound:", animal.sound())  # Output: Some generic animal sound
print("Dog sound:", dog.sound())        # Output: Bark
print("Cat sound:", cat.sound())        # Output: Meow
