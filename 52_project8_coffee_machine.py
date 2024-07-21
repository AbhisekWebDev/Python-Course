menu = {
    "latte" : {
        "ingredients" : {
            "water" : 200,
            "milk" : 150,
            "coffee" : 25
        }, "cost" : 150
    },
    "espresso" : {
        "ingredients" : {
            "water" : 50,
            "coffee" : 20
        }, "cost" : 100
    },
    "cappuccino" : {
        "ingredients" : {
            "water" : 250,
            "milk" : 100,
            "coffee" : 30
        }, "cost" : 200
    }
}

profit = 0

resources = {
    "water": 100000,
    "milk": 100000,
    "coffee": 100000
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not enough {item}")
            return False
    return True

def process_coins():
    print("Insert coins : ")

    total = 0

    coins5 = int(input("How many Rs. 5 coins? : "))
    coins10 = int(input("How many Rs. 10 coins? : "))
    coins20 = int(input("How many Rs. 20 coins? : "))

    total = coins5 * 5 + coins10 * 10 + coins20 * 20

    return total

def is_payment_successfuf(money_recieved, coffee_cost):
    if money_recieved >= coffee_cost:
        
        global profit
        profit += coffee_cost
        change = money_recieved - coffee_cost
        
        print(f"Here is your change Rs. {change}")

        return True
    
    else:
        print("Not enough money, Money refunded.")

        return False
    
def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    print(f"Here is your {coffee_name.capitalize()}")

is_onn = True

while is_onn:
    choice = input("What would you like to have today? \n Latte, Espresso or Cappuccino : ").lower()
    if choice == "off":
        is_onn = False
    elif choice == "report":
        for key, value in resources.items():
            print(f"{key.capitalize()} : {value} ml")
        print(f"Money : Rs. {profit}")
    elif choice in menu:
        coffee_type = menu[choice]
        print(coffee_type)
        if check_resources(coffee_type["ingredients"]):
            payment = process_coins()
            if is_payment_successfuf(payment, coffee_type["cost"]):
                make_coffee(choice, coffee_type["ingredients"])
    else:
        print("Please choose a valid option : Latte, Espresso, Cappuccino, report, or off.")
