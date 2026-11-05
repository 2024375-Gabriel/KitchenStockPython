#imports


print("===================================")
print("     KITCHEN MANAGER SIMULATOR")
print("===================================")

print("\nWelcome to your new kitchen!")

#Dicionarios
inventory = {
    "Beef patty": 50,
    "Burguer bun": 50,
    "Cheese slice": 60,
    "Frozen fries": 20,
    "Coke": 30
}

menu = {
    "Cheeseburger": {
        "Beef patty": 1,
        "Burguer bun": 1,
        "Cheese slice": 1
    },

    "Double Cheeseburguer": {
        "Beef patty": 2,
        "Burguer bun": 1,
        "Cheese slice": 2
    },

    "Fries": {
        "Frozen fries": 1
    },

    "Coke": {
        "Coke": 1
    }

}

#funcoes

def viewInventory():
    print("\n======= INVENTORY ========")

    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

def addInventory():
    print("\n===== ADD STOCK ======")
    
    item_name = input("Enter the item name: ")
     
    if item_name in inventory:
        quantity = int(input("Enter Quantity to add: "))
     
        inventory[item_name] += quantity
     
        print(f"\n{quantity} added to {item_name}.")
        print(f"New quantity: {inventory[item_name]}")
     
    else:
        quantity = int(input("Enter starting quantity: "))
        inventory[item_name] = quantity
        print(f"{item_name} added to inventory.")

def useInventory():
    print("\n=== Use Stock ===.")

    item_name = input("Enter the item name: ")
        
    if item_name in inventory:
        quantity = int(input("Enter Quantity to remove: "))
        
        inventory[item_name] -= quantity
        
        print(f"\n{quantity} added to {item_name}.")
        print(f"New quantity: {inventory[item_name]}")
        
    else:
        print("\nItem not found in inventory")

def stockMenu():
    stock_running = True

    while stock_running:

        print("\n========== STOCK MENU ==========")
        print("1. View inventory")
        print("2. Add stock")
        print("3. Exit")

        choice = input("\nChoose an option: ")

        #inventory
        if choice == "1":
            viewInventory()

        #Add Stock
        elif choice == "2":
            addInventory()
                
        #Closing the app

        elif choice == "3":
            print("\nClosing Stock Menu...")
            stock_running = False

        #error
        else:
            print("\nInvalid option. Please choose 1, 2 or 3.")

def menuScreen():
    print("\n ===== MENU =====")

    for dish, ingredients in menu.items():

        print(f"\n{dish}")

        possible_amounts = []

        for ingredient, amount_needed in ingredients.items():

            stock_amount = inventory.get(ingredient, 0)

            possible = stock_amount // amount_needed

            possible_amounts.append(possible)

            print(
                f"= {ingredient}: {amount_needed} needed"
                f"| Stock: {stock_amount}"
            )

        max_dishes = min(possible_amounts)

        print(f"Can make: {max_dishes}")


# ==== MAIN MENU ====

running = True

while running:

    print("\n========== MAIN MENU ==========")
    print("1. Menu")
    print("2. Stock")
    print("3. Booking")
    print("4. Status")
    print("5. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":
        menuScreen()

    elif choice == "2":
        stockMenu()

    elif choice == "3":
        print("\nBooking section selected.")

    elif choice == "4":
        print("\nStatus section selected.")

    elif choice == "5":
        print("\nClosing Kitchen Manager Simulator...")
        running = False

    else:
        print("\nInvalid option. Please choose 1, 2, 3, 4 or 5.") 