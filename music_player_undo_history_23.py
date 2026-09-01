# Program for Music Player using stack

history = []

while True:
    print("\n===== MUSIC PLAYER =====")
    print("1. Play song")
    print("2. Pause song")
    print("3. Next song")
    print("4. Previous song")
    print("5. Undo last action song")
    print("6. Show history")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        song = input("Enter song name: ")
        action = "Play" + " " + song
        history.append(action)
        print("Song is playing.")

    elif choice == 2:
        history.append("Pause song")
        print("Song paused.")

    elif choice == 3:
        history.append("Next song.")
        print("Playing next song.")

    elif choice == 4:
        history.append("Previous song.")
        print("Playing previous song.")

    elif choice == 5:
        if len(history) == 0:
            print("No action to undo.")
        else:
            last_action = history.pop()
            print("Undo:", last_action)

    elif choice == 6:
        if len(history) == 0:
            print("No history available.")
        else:
            print("\n------ ACTION HISTORY ------")
            for action in reversed(history):
                print(action)

    elif choice == 7:
        print("Thank you for using Music Player!")
        break

    else:
        print("Invalid choice! Please try again.")
