from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

item = Menu()
coffeemaker = CoffeeMaker()
money = MoneyMachine()

implement = "y"

while implement == "y":
    total = 0
    choice = input(f"What would you like? {item.get_items()} :").lower()
    if choice == "report":
        coffeemaker.report()
        money.report()
    elif choice == "off":
        implement = "n"
    else:
        order = item.find_drink(choice)
        if coffeemaker.is_resource_sufficient(order) and money.make_payment(order.cost):
            coffeemaker.make_coffee(order)
