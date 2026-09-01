import os
import shutil

def organize_files(folder_path):
    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
        "Videos": [".mp4", ".mkv", ".avi"],
        "Audio": [".mp3", ".wav"],
        "Python": [".py"],
        "Zip files": [".zip", ".rar"]
    }

    if not os.path.exists(folder_path):
        print("\nFolder not found!")
        return

    counts = {
        "Images": 0,
        "Documents": 0,
        "Videos": 0,
        "Audio": 0,
        "Python": 0,
        "Zip files": 0,
        "Others": 0
    }

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isdir(file_path):
            continue

        extension = os.path.splitext(file)[1].lower()
        category = "Others"

        for folder, extensions in categories.items():
            if extension in extensions:
                category = folder
                break

        category_path = os.path.join(folder_path, category)
        os.makedirs(category_path, exist_ok=True)

        shutil.move(file_path, os.path.join(category_path, file))
        counts[category] += 1

    print("=" * 45)
    print("           📁 SMART FILE ORGANIZER")
    print("=" * 45)
    print("Images       :", counts["Images"])
    print("Documents    :", counts["Documents"])
    print("Videos       :", counts["Videos"])
    print("Audio        :", counts["Audio"])
    print("Python       :", counts["Python"])
    print("Zip files    :", counts["Zip files"])
    print("Others       :", counts["Others"])
    print("=" * 45)
    print("           ORGANIZATION COMPLETED")
    print("=" * 45)

folder = input("Enter folder path: ")
organize_files(folder)
