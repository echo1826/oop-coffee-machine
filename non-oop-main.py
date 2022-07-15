MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0

def main():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'espresso':
        process_order(MENU['espresso'], 'espresso')
    elif choice == 'latte':
        process_order(MENU['latte'], 'latte')
    elif choice == 'cappuccino':
        process_order(MENU["cappuccino"], 'cappuccino')
    elif choice == 'report':
        report()
    elif choice == 'off':
        exit(1)
    else:
        print("Incorrect choice inputted.\nPlease try again.")
        main()
    main()


def report():
    print("Printing report...")
    print(f"""
    Water: {resources['water']}ml
    Milk: {resources['milk']}ml
    Coffee: {resources['coffee']}ml
    Money: ${profit:.2f}
    """)

def resource_check(order_ingredients):
    for ingredient_name in order_ingredients:
        if order_ingredients[ingredient_name] > resources[ingredient_name]:
            print(f"Sorry there is not enough {ingredient_name}.")
            return False
    return True

def ask_coins():
    
    prompting = True
    while prompting:
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total = (quarters * .25) + (dimes * .10) + (nickels * .05) + (pennies * .01)
            return round(total, 2)
        except ValueError:
            print("Input only numbers!")
            continue

def process_order(order, drink_name):
    if not resource_check(order['ingredients']):
        main()
    inserted_money = ask_coins()
    if inserted_money < order['cost']:
        print("Not enough money inserted. Refunding money...")
        main()
    remainder = inserted_money - order['cost']
    global profit 
    profit += order['cost']

    for ingredient_name in order['ingredients']:
        resources[ingredient_name] = resources[ingredient_name] - order['ingredients'][ingredient_name]

    if remainder > 0:
        # print(f"Your change is {round(remainder, 2)}")
        format_change = "{:.2f}".format(remainder)
        print(f"Your change is {format_change}")
    print(f"Here is your {drink_name}")



main()