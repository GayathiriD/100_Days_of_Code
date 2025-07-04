from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

report = CoffeeMaker()
money_machine= MoneyMachine()
menu = Menu()
report.report()
money_machine.report()

is_on = True
#
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like ({options}): ")
    if choice == 'off':
        is_on=False
    elif choice == 'report':
        report.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if report.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            report.make_coffee(drink)