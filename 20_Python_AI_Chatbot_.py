import datetime

print("=" * 45)
print("          🤖 PYTHON AI CHATBOT")
print("=" * 45)

print("\nBot: Hello! I am PyBot.")
print("Bot: You can talk to me.")
print("Bot: Type 'bye' to exit.")

while True:

    user = input("\nYou: ").lower()

    if user == "hello" or user == "hi" or user == "hey":
        print("Bot: Hello! How can I help you?")

    elif "your name" in user:
        print("Bot: My name is PyBot.")

    elif "how are you" in user:
        print("Bot: I am fine! Thank you.")

    elif "python" in user:
        print("Bot: Python is a programming language.")

    elif "time" in user:
        time = datetime.datetime.now().strftime("%I:%M %p")
        print("Bot: Current time is", time)

    elif user == "help":
        print("Bot: You can ask me about my name, Python, time or say hello.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")

print("\nChatbot ended.")
