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
    else:
        order = menu.find_item(user_input)
    if not order:
        return main()
    if not money_machine.process_payment(order.price):
        return main()

main()