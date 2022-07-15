from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

def menu_choice():
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    return choice

def main():
    menu.show_menu()
    user_input = menu_choice()
    if user_input == 'report':
        coffee_machine.report()
        money_machine.report()
        main()
    elif user_input == 'off':
        exit(1)
    else:
        order = menu.find_item(user_input)

    if not order:
        main()

    if not money_machine.process_payment(order.price):
        main()

    if not coffee_machine.resources_suffcient(order):
        main()
    coffee_machine.make_coffee(order)
    main()

main()