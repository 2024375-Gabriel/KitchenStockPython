#imports


print("===================================")
print("     KITCHEN MANAGER SIMULATOR")
print("===================================")

print("\nWelcome to your new kitchen!")

#Stock
inventory = {
    "Beef patty": 50,
    "Burguer bun": 50,
    "Cheese Slice": 60,
    "Frozen Fries": 20,
    "Coke": 30
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


#Looping
running = True

while running:

    print("\n========== MAIN MENU ==========")
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
        print("\nClosing Kitchen Manager Simulator...")
        running = False

    #error
    else:
        print("\nInvalid option. Please choose 1, 2, 3 or 4.")