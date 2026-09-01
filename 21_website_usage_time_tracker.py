import time

print("="*45)
print("     WEBSITE USAGE TIME TRACKER")
print("="*45)

website = input("Enter website/app name: ")

print()
print("Press Enter to START tracking.")
input()

start_time = time.time()

print("Tracking started for:", website)
print("Use the website/app now.")
print("Press Enter when you STOP using it.#")
input()

end_time = time.time()

usage_time = end_time - start_time

hours = int(usage_time // 3600)
minutes = int((usage_time % 3600) // 60)
seconds = int(usage_time % 60)

print()
print("="*45)
print("          USAGE REPORT")
print("="*45)

print("Website/App :", website)
print("Time Spent :", hours, "hours", minutes, "minutes", seconds, "seconds")

print("="*45)

if usage_time >= 7200:
    print("Warning: You spent more than 2 hours!")
elif usage_time >= 3600:
    print("You spent more than 1 hour.")
else:
    print("Usage time is below 1 hour.")

print("="*45)
