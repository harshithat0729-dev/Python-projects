def analyze_password(password):
    score = 0

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    print("\nPassword Analysis:")

    # Length check
    if len(password) >= 8:
        print("Good password length")
        score += 1
    else:
        print("Password should contain at least 8 characters")

    # Uppercase check
    if has_upper:
        print("Uppercase letter present")
        score += 1
    else:
        print("Add an uppercase letter")

    # Lowercase check
    if has_lower:
        print("Lowercase letter present")
        score += 1
    else:
        print("Add a lowercase letter")

    # Number check
    if has_digit:
        print("Number present")
        score += 1
    else:
        print("Add a number")

    # Special character check
    if has_special:
        print("Special character present")
        score += 1
    else:
        print("Add a special character")

    print("\nScore:", score, "/ 5")

    if score <= 2:
        print("Strength: WEAK")
    elif score <= 4:
        print("Strength: MEDIUM")
    else:
        print("Strength: STRONG")

print("=" * 45)
print("     PASSWORD STRENGTH ANALYZER")
print("=" * 45)

password = input("Enter your password: ")
analyze_password(password)
