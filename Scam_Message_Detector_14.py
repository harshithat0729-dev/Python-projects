# SCAM MESSAGE DETECTOR
def check_message(message):
    # Convert message into lowercase
    message = message.lower()

    score = 0
    warnings = []

    # Scam keywords
    scam_words = {
        "won": 20,
        "prize": 20,
        "lottery": 20,
        "otp": 25,
        "password": 25,
        "urgent": 10,
        "click": 15,
        "verify": 10,
        "bank": 15,
        "upi": 15,
        "money": 20,
        "free": 10,
        "offer": 10,
        "congratulations": 20
    }

    # Check each word
    for word in scam_words:

        if word in message:
            score = score + scam_words[word]
            warnings.append(word)

    # Maximum score = 100
    if score > 100:
        score = 100

    # Display result
    print("=" * 45)
    print("          SCAM MESSAGE DETECTOR")
    print("=" * 45)

    print("\nRisk Score:", score, "%")

    if score <= 30:
        print("Result: SAFE")
    elif score <= 60:
        print("Result: SUSPICIOUS")
    else:
        print("Result: HIGH RISK SCAM")

    # Display warning words
    if len(warnings) > 0:
        print("\nWarning Signs Found:")
        for word in warnings:
            print("-", word)
    else:
        print("\nNo major warning signs found.")

    print("-" * 45)
    print("Safety Advice:")
    print("Be careful with this message.")
    print("Verify the sender before responding.")
    print("=" * 45)


print("=" * 45)
print("       WELCOME TO SCAM MESSAGE DETECTOR")
print("=" * 45)

message = input("Enter your message: ")
check_message(message)

print("\n[Program finished]")
