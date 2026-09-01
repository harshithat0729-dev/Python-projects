# Tiranga ASCII Art Generator
# Project 14 - By Thara

def tiranga(name):
    print("\n" + "=" * 45)
    print("             TIRANGA")
    print("=" * 45)

    # Saffron
    print("🟧" * 25)
    print("🟧" * 25)
    print("🟧" * 25)
    print("🟧" * 25)

    # White
    print("⬜" * 25)
    print("⬜" * 5 + " HAPPY INDEPENDENCE DAY " + "⬜" * 5)
    print("⬜" * 10 + " 🔵 " + "⬜" * 10)
    print("⬜" * 9 + name + "⬜" * 9)
    print("⬜" * 25)

    # Green
    print("🟩" * 25)
    print("🟩" * 25)
    print("🟩" * 25)
    print("🟩" * 25)

    print("=" * 45)
    print("\n🇮🇳 15th August 1947 - 2026 🇮🇳")
    print("🇮🇳 Celebrating 79 Years of Independence 🇮🇳")
    print("🇮🇳 Jai Hind! 🇮🇳")


name = input("Enter your name: ")
tiranga(name)
