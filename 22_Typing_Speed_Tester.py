import time

print("="*45)
print("         TYPING SPEED TESTER")
print("="*45)

sentences = [
    "I love Python",
    "Python is easy to learn",
    "I am learning Python programming",
    "Python is useful for data science",
    "Artificial intelligence is changing the world"
]

for sentence in sentences:

    print()
    print("Typing Speed Tester")
    print("Type this sentence:")
    print(sentence)

    input("Press Enter to start")

    start = time.time()

    text = input("Type: ")

    end = time.time()

    time_taken = end - start

    words = len(text.split())

    wpm = (words / time_taken) * 60

    sentence = sentence.lower().strip()
    text = text.lower().strip()

    correct = 0

    for i in range(min(len(sentence), len(text))):
        if sentence[i] == text[i]:
            correct += 1

    accuracy = (correct / len(sentence)) * 100

    print()
    print("Time:", round(time_taken, 2), "seconds")
    print("Words:", words)
    print("Typing Speed:", round(wpm, 2), "WPM")
    print("Accuracy:", round(accuracy, 2), "%")

    if wpm >= 50:
        print("Speed: Fast")
    elif wpm >= 30:
        print("Speed: Average")
    else:
        print("Speed: Slow")
    print("="*45)
