print("=" * 45)
print("        INTERNET SPEED CALCULATOR")
print("=" * 45)

size = float(input("Enter file size in MB: "))
time = float(input("Enter download time in seconds: "))

speed = size / time

print("\n--------------- RESULT ---------------")
print("File Size       :", size, "MB")
print("Download Time   :", time, "seconds")
print("Download Speed  :", round(speed, 2), "MB/s")

if speed >= 10:
    print("Status          : Excellent")
elif speed >= 5:
    print("Status          : Good")
else:
    print("Status          : Slow")

print("="*45)
