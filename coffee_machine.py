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


def rss_sufficient(ingredient):
    for rss in ingredient:
        if ingredient[rss] > resources[rss]:
            print(f"Sorry there is not enough {rss}.")
            return False
    return True


def coins():
    print('Please insert coins.')
    # Insert how many coins?
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    # Total number of coins inserted and the price of selected coffee
    total = (0.25 * quarters) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    return total


def transactions(coffee, money_received):
    price = MENU[coffee]['cost']
    if money_received > price:
        leftover = round(money_received - price, 2)
        print(f'Here is ${leftover} in change.\nHere is your {coffee}☕. Enjoy!')
        global profit
        profit += price
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def processing(ingredient):
    for rss in ingredient:
        # Deduct the relevant ingredients after making a coffee
        resources[rss] -= ingredient[rss]


is_on = True
while is_on:
    coffee_type = input('What would you like? (espresso/latte/cappuccino)\n')
    if coffee_type == "off":
        print("Bye-bye!")
        is_on = False
    elif coffee_type == "report": # Check for resources
        for key in resources:
            if key != 'coffee':
                print(f"{key}: {resources[key]}ml")
            else:
                print(f"{key}: {resources[key]}g")
                print(f"Money: ${profit}")
    else:
        drink_ingredient = MENU[coffee_type]['ingredients']
        if rss_sufficient(drink_ingredient):
            payment = coins()
            if transactions(coffee_type, payment):
                processing(drink_ingredient)


