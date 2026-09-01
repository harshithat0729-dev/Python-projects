# Data Cleaner
print("=" * 45)
print("             DATA CLEANER")
print("=" * 45)

data = [" Python ", "", "AI", " ", "ML", "", " ACI",
        " Data Structures", "Data Science"]

cleaned_data = []

for item in data:
    item = item.strip()

    if item != "":
        cleaned_data.append(item)

print("Original Data:", data)

print("-" * 45)
print("Cleaned Data:", cleaned_data)
print("-" * 45)
