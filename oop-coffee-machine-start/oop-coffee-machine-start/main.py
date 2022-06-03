from menu import Menu\
    # , MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
items = menu.get_items()
money_machine = MoneyMachine()

is_on = True

while is_on:

    # todo 1  prompt the user for a drink
    user_req = input(f"What would you like? {items}: ").lower()

    if user_req == "off":
        print("Turning off now...")
        is_on = False

    elif user_req in items:
        print(f"You've asked for a {user_req}")
        drink_object = menu.find_drink(user_req)

        can_i_make = coffee_maker.is_resource_sufficient(drink_object)

        if can_i_make:
            print(f"Please insert coins with a total of ${drink_object.cost}")
            if money_machine.make_payment(drink_object.cost):
                coffee_maker.make_coffee(drink_object)
            else:
                print("Please insert the correct amount of money.")

    elif user_req == "report":
        coffee_maker.report()
        money_machine.report()

    # todo 2 check for resources - if sufficient to make the drink

    # todo 3 ask for money and check the value against the cost, return change
    # todo 4 make the coffee and display a prompt for another drink
