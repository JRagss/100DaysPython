# print report
# check if there is enough resources
# process coins (Check if enough money as given and return proper change)
# check that the transaction as
# make coffee, deduct resourcess


from data import MENU
from data import resources


def enough_resources(drink):
    if MENU[drink]['ingredients']['water'] <= resources['water']:
        if MENU[drink]['ingredients']['coffee'] <= resources['coffee']:
            if 'milk' in MENU[drink]['ingredients']:
                if MENU[drink]['ingredients']['milk'] <= resources['milk']:
                    return True
                else:
                    return 'insufficient milk'
            else:
                return True
        else:
            return 'insufficient coffee'
    else:
        return 'insufficient water'


# potentially add a way for the user to tell the machine they have re-filled the required resource


def enough_money(drink, paid):
    if paid >= MENU[drink]['cost']:
        return True
    else:
        return False


def coffee_machine():
    serve_another = True
    while serve_another:
        # User inputs which drink they would like to order
        order = input('What would you like? (espresso/ latte/ cappuccino): ').lower()

        # If they ask for a report print the remaining quantities of each ingredient in the machien
        if order == "report":
            print(resources)
            coffee_machine()

        # If they turn the machine off, exit the while loop
        elif order == "off":
            return

        # Call enough_resources() to check if the drink can be made. Then ask what coins they input
        elif enough_resources(order) == True:
            quarters = int(input('How many quarters?: '))
            dimes = int(input('How many dimes?: '))
            nickles = int(input('How many nickles?: '))
            pennies = int(input('How many pennies?: '))
            total = .25 * quarters + .1 * dimes + .05 * nickles + .01 * pennies

            # After collecting money, calculate change and deduct the resources from the reserves
            if enough_money(order, total):
                change = total - MENU[order]['cost']
                print(f'Your change is ${change:.2f}')
                resources['water'] -= MENU[order]['ingredients']['water']
                resources['coffee'] -= MENU[order]['ingredients']['coffee']

                # If the drink contains milk deduct the resources
                if 'milk' in MENU[order]['ingredients']:
                    resources['milk'] -= MENU[order]['ingredients']['milk']
                    coffee_machine()

                coffee_machine()

            # If the user has not input enough money, tell them that, refund the money, and recall the function
            else:
                print('you dont have enough money, your money has been refunded')
                coffee_machine()


coffee_machine()
