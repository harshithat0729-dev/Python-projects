print("=" * 45)
print("      MYSTERY DETECTIVE GAME")
print("=" * 45)

print("\nA secret box is locked!")
print("Answer the questions and solve the mystery.")
print("You have 3 rounds.\n")

score = 0
hints_used = 0

# ROUND 1
print("ROUND 1 - EASY QUESTIONS")
print("-" * 45)

print("\nQ1. Which language is famous for its simple syntax?")
print("A. Java")
print("B. Python")
print("C. HTML")
print("D. C++")
answer = input("Your answer: ")

if answer == "B":
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    print("Hint: It starts with P.")

print("\nQ2. How many letters are in 'Python'?")
print("A. 5")
print("B. 6")
print("C. 7")
print("D. 8")
answer = input("Your answer: ")

if answer == "B":
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    print("Hint: P-y-t-h-o-n")

print("\nQ3. Which symbol is used for addition in Python?")
print("A. -")
print("B. *")
print("C. +")
print("D. /")
answer = input("Your answer: ")

if answer == "C":
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    print("Hint: It looks like a cross.")

# ROUND 2
print("\n\nROUND 2 - CLUE CHALLENGE")
print("-" * 45)

print("\nQ4. Which keyword is used for a condition?")
print("A. if")
print("B. print")
print("C. input")
print("D. int")
answer = input("Your answer: ")

if answer == "A":
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    print("Hint: It starts a condition in Python.")

print("\nQ5. Which loop repeats while a condition is true?")
print("A. for")
print("B. while")
print("C. if")
print("D. else")
answer = input("Your answer: ")

if answer == "B":
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    print("Hint: The keyword starts with 'w'.")

# ROUND 3
print("\n\nROUND 3 - FINAL MYSTERY")
print("-" * 45)
print("You are very close to unlocking the box!")

print("\nQ6. What does input() do?")
print("A. Displays output")
print("B. Takes input from user")
print("C. Adds numbers")
print("D. Repeats code")
answer = input("Your answer: ")

if answer == "B":
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    print("Hint: It asks the user for something.")

print("\nQ7. Which data type stores True or False?")
print("A. int")
print("B. str")
print("C. bool")
print("D. float")
answer = input("Your answer: ")

if answer == "C":
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    print("Hint: Boolean values are True or False.")

print("\nQ8. Which function displays something on the screen?")
print("A. input()")
print("B. print()")
print("C. int()")
print("D. len()")
answer = input("Your answer: ")

if answer == "B":
    print("Correct!")
    score = score + 20
else:
    print("Wrong!")
    print("Hint: You use it to show output.")

print("=" * 45)
print("       MYSTERY RESULT")
print("=" * 45)
print("Your Score:", score, "/ 160")

if score >= 140:
    print("Rank: MASTER DETECTIVE")
elif score >= 100:
    print("Rank: SMART DETECTIVE")
elif score >= 60:
    print("Rank: JUNIOR DETECTIVE")
else:
    print("Rank: ROOKIE DETECTIVE")

print("\nMystery Completed!")
print("Thank you for playing!")
