class Bank:
    def __init__(self, acc_holder_name, balance = 0):
        self.acc_holder_name = acc_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited Successfully! \n Amount : {amount}")

    def withdraw(self, withdraw_amount):
        if withdraw_amount > self.balance:
            print("Not Enough Balance!")
        else:
            self.balance -= withdraw_amount
            print(f"Withdrawal complete! \n Cash Withdrawn : {withdraw_amount}")

    def __str__(self):
        return f"Account Holder Name : {self.acc_holder_name} \nBalance : {self.balance}"

object = Bank("Abhisek", 100)
print(object)
object.deposit(200)
print(object)
object.withdraw(500)
print(object)