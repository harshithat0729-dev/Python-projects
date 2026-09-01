print("=" * 45)
print("       GAME INVENTORY SYSTEM")
print("=" * 45)

inventory = []
maxsize = int(input("Enter maximum inventory size: "))

while True:
    print("\n===== INVENTORY MENU =====")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Search Item")
    print("4. Display Inventory")
    print("5. Inventory Count")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    # Add item
    if choice == 1:
        if len(inventory) >= maxsize:
            print("Inventory is full!")
        else:
            item = input("Enter item: ")
            inventory.append(item)
            print("Item added to inventory.")

    # Remove item
    elif choice == 2:
        if len(inventory) == 0:
            print("Inventory is empty!")
        else:
            item = input("Enter item to remove: ")
            if item in inventory:
                inventory.remove(item)
                print(item, "removed from inventory.")
            else:
                print("Item not found in inventory.")

    # Search item
    elif choice == 3:
        item = input("Enter item to search: ")

        if item in inventory:
            print("Item is found in inventory.")
        else:
            print("Item not found in inventory.")

    # Display inventory
    elif choice == 4:
        if len(inventory) == 0:
            print("Inventory is empty.")
        else:
            print("Current inventory:")
            for item in inventory:
                print(item)

    # Inventory count
    elif choice == 5:
        print("Inventory Count:", len(inventory))

    # Exit
    elif choice == 6:
        print("Program completed.")
        break

    else:
        print("Invalid choice. Please try again.")
