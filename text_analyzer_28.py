print("="*45)
print("          TEXT ANALYZER")
print("="*45)

text = input("Enter your text: ")

# Basic counts
characters = len(text)
words = text.split()
word_count = len(words)

# Sentence count
sentences = text.split(".")
sentence_count = 0

for sentence in sentences:
    if sentence.strip() != "":
        sentence_count += 1

# Vowels count
vowels = 0

for char in text.lower():
    if char in "aeiou":
        vowels += 1

# Unique words
unique_words = set(words)

# Longest word
longest_word = ""

for word in words:
    if len(word) > len(longest_word):
        longest_word = word

# Results
print("\n========== TEXT ANALYSIS ==========")
print("Characters :", characters)
print("Words      :", word_count)
print("Sentences  :", sentence_count)
print("Unique Words:", len(unique_words))
print("Vowels     :", vowels)
print("Longest Word:", longest_word)
