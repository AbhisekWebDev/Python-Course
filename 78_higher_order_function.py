def greet(language):
    """Returns a greeting function based on the given language."""
    def greet_in_english(name):
        return f"Hello, {name}!"

    def greet_in_spanish(name):
        return f"Hola, {name}!"

    def greet_in_french(name):
        return f"Bonjour, {name}!"

    if language == "english":
        return greet_in_english
    elif language == "spanish":
        return greet_in_spanish
    elif language == "french":
        return greet_in_french
    else:
        return lambda name: f"Hello, {name}! (Language not recognized)"

def apply_twice(func, arg):
    """Applies a function twice to an argument."""
    return func(func(arg))

# Example usage of greet function
english_greet = greet("english")
spanish_greet = greet("spanish")
french_greet = greet("french")
unknown_greet = greet("german")

print(english_greet("Alice"))  # Output: Hello, Alice!
print(spanish_greet("Bob"))    # Output: Hola, Bob!
print(french_greet("Claire"))  # Output: Bonjour, Claire!
print(unknown_greet("Dave"))   # Output: Hello, Dave! (Language not recognized)

# Example usage of apply_twice function
def add_three(x):
    return x + 3

print(apply_twice(add_three, 5))  # Output: 11 (5 + 3 + 3)




# greet(language):

# This higher-order function takes a string language as an argument and returns a function that greets in the specified language.
# Inside greet, there are three inner functions: greet_in_english, greet_in_spanish, and greet_in_french. 
# Each function returns a greeting message in the corresponding language.
# Depending on the language argument, greet returns the appropriate greeting function. 
# If the language is not recognized, it returns a default function that provides a message indicating the language is not recognized.


# apply_twice(func, arg):

# This higher-order function takes another function func and an argument arg as inputs.
# It applies func to arg twice, returning the result. 
# This demonstrates how higher-order functions can manipulate functions and arguments.


# Example usage:

# The greet function is used to create language-specific greeting functions (english_greet, spanish_greet, french_greet, unknown_greet).
# The apply_twice function is used with the add_three function to demonstrate applying a function multiple times.
