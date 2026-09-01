tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == 2:
        if not tasks:
            print("No tasks available.")
        else:
            print("\nYour Tasks:")
            for task in tasks:
                print(task)

    elif choice == 3:
        task = input("Enter task to delete: ")

        if task in tasks:
            tasks.remove(task)
            print("Task deleted successfully!")
        else:
            print("Task not found!")

    elif choice == 4:
        print("Exiting To-Do List...")
        break

    else:
        print("Invalid choice!")
