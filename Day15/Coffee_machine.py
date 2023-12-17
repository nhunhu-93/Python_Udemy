import data

def resources_check(choice):
    resource = data.resources
    for i in choice:
        if choice[i] > resource[i]:
            print(f"​Sorry there is not enough {i}.")
            return False
    return True

def pay_coins():
    print("Please insert coins")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def is_enough_coins(money, drink):
    if money < drink:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money - drink, 2)
        print(f"Here is ${change} dollars in change.")
        global coins_final
        coins_final += change
        return True
    
def make_drink(name_drink, ingredients_drink):
    for i in ingredients_drink:
        data.resources[i] -= ingredients_drink[i]
    print(f"Here is your {name_drink} ☕️. Enjoy!")
    
coins_final = 0
continues = True

while continues:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "report":
        print(f"Water: {data.resources['water']}ml")
        print(f"Milk: {data.resources['milk']}ml")
        print(f"Coffee: {data.resources['coffee']}gam")
        print(f"Money: ${coins_final}")
    elif choice == "off":
        continues = False
    else:
        drink = data.MENU[choice]
        if resources_check(drink["ingredients"]):
            money = pay_coins()
            if is_enough_coins(money, drink["cost"]):
                make_drink(choice, drink["ingredients"])
    


        
    
            


