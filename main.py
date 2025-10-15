MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.0,  
}

while True:
    choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()

    if choice == "off":
        print("Turning off the coffee machine.")
        break

    if choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']:.2f}")
        continue

    if choice not in MENU:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")
        continue

    drink = MENU[choice]
    need = drink["ingredients"]

    # 1) 자원 충분성 먼저 확인
    lacking = None
    for item, amt in need.items():
        if resources.get(item, 0) < amt:
            lacking = item
            break
    if lacking:
        print(f"Sorry, there is not enough {lacking}.")
        continue  

    # 2) 동전 처리
    quarters = int(input("Insert quarters: "))
    dimes = int(input("Insert dimes: "))
    nickels = int(input("Insert nickels: "))
    pennies = int(input("Insert pennies: "))
    total_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    # 3) 결제 검증
    cost = drink["cost"]
    if total_inserted < cost:
        print("Sorry, that's not enough money. Money refunded.")
        continue  

    change = round(total_inserted - cost, 2)
    if change > 0:
        print(f"Here is ${change:.2f} in change.")

    resources["money"] += cost
    for item, amt in need.items():
        resources[item] -= amt

    print(f"Here is your {choice}. Enjoy!")
