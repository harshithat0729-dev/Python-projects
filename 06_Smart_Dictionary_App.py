# Project 24 - Smart Dictionary App
print("=" * 45)
print("          SMART DICTIONARY APP")
print("=" * 45)

dictionary = {
    "python": {
        "meaning": "A programming language used to build software and applications.",
        "part_of_speech": "Noun",
        "example": "I am learning Python."
    },
    "curious": {
        "meaning": "Wanting to know or learn something.",
        "part_of_speech": "Adjective",
        "example": "She was curious about the new project."
    },
    "brave": {
        "meaning": "Ready to face difficult situations.",
        "part_of_speech": "Adjective",
        "example": "The brave girl helped others."
    },
    "success": {
        "meaning": "The achievement of a desired goal.",
        "part_of_speech": "Noun",
        "example": "Hard work leads to success."
    },
    "learn": {
        "meaning": "To gain knowledge or skill.",
        "part_of_speech": "Verb",
        "example": "I learn something new every day."
    }
}

def search_word(word):
    word = word.lower()

    if word in dictionary:
        data = dictionary[word]

        print("-" * 15, "WORD DETAILS", "-" * 15)
        print("Word:", word.title())
        print("Meaning:", data["meaning"])
        print("Part of Speech:", data["part_of_speech"])
        print("Example:", data["example"])
        print("=" * 45)

    else:
        print("\nWord not found in the dictionary.\n")


while True:

    print("-" * 14, "DICTIONARY MENU", "-" * 14)
    print("1. Search Word")
    print("2. Show Available Words")
    print("3. Exit")
    print("=" * 45)

    choice = input("Enter your choice: ")

    if choice == "1":
        word = input("Enter a word: ")
        search_word(word)

    elif choice == "2":
        print("\nAvailable Words:")

        for word in dictionary:
            print(word.title())

    elif choice == "3":
        print("\nThank you for using Smart Dictionary!")
        break

    else:
        print("\nInvalid choice. Please try again.")
