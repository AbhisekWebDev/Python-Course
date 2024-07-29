class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number  # Private attribute
        self.__balance = balance                # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
                print(f"Withdrew {amount}. New balance: {self.__balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

    def get_balance(self):
        return self.__balance

# Creating a BankAccount object
account = BankAccount("123456789", 1000)

# Depositing money
account.deposit(500)

# Withdrawing money
account.withdraw(200)

# Trying to access the private attribute directly (will raise an AttributeError)
# print(account.__balance)

# Accessing balance using the public method
print(f"Current balance: {account.get_balance()}")

# Attempting to withdraw an amount greater than the balance
account.withdraw(2000)







# BankAccount Class:

# The class represents a simple bank account with an account number and balance.
# The __init__ method initializes the private attributes __account_number and __balance. These are private attributes, 
# indicated by the double underscore prefix, meaning they cannot be accessed directly outside the class.

# The deposit method allows the user to deposit money into the account. 
# It checks if the deposit amount is positive before adding it to the balance.

# The withdraw method allows the user to withdraw money from the account. 
# It checks if the withdrawal amount is positive and does not exceed the available balance.

# The get_balance method is a public method that returns the current balance. 
# This is an example of a getter method, which provides controlled access to a private attribute.


# Encapsulation:

# The private attributes __account_number and __balance are encapsulated within the BankAccount class. 
# They are not directly accessible from outside the class.

# The methods deposit, withdraw, and get_balance provide controlled access to the balance attribute. 
# This helps in protecting the integrity of the data by preventing unauthorized or inappropriate access.


# Access Control:

# Direct access to private attributes is restricted, which helps in preventing unintended changes to the data. 
# For example, trying to print account.__balance would result in an AttributeError.

# Encapsulation allows the internal representation of the object to be changed without affecting code that uses the object, 
# provided the public interface remains unchanged.