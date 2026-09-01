print("=" * 45)
print("            CONTACT BOOK")
print("=" * 45)

contacts = {}

while True:
    print("\n----- MENU -----")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")
    print("---------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")

        contacts[name] = phone
        print("Contact added successfully!")

    elif choice == 2:
        print("\n----- CONTACTS -----")

        if len(contacts) == 0:
            print("No contacts found.")
        else:
            for name in contacts:
                print(name, ":", contacts[name])

    elif choice == 3:
        name = input("Enter contact name to search: ")

        if name in contacts:
            print("Contact found!")
            print("Phone:", contacts[name])
        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter contact name to delete: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    elif choice == 5:
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice!")
