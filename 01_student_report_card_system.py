# STUDENT REPORT CARD SYSTEM

print("=" * 50)
print("        STUDENT REPORT CARD SYSTEM")
print("=" * 50)

name = input("Enter Student Name: ")
roll_no = input("Enter Roll Number: ")

python_marks = int(input("Enter Python Marks (out of 100): "))
english_marks = int(input("Enter English Marks (out of 100): "))
maths_marks = int(input("Enter Maths Marks (out of 100): "))
ai_marks = int(input("Enter AI Marks (out of 100): "))

total = python_marks + english_marks + maths_marks + ai_marks
percentage = (total / 400) * 100

marks = [python_marks, english_marks, maths_marks, ai_marks]

highest_mark = max(marks)
lowest_mark = min(marks)

if percentage >= 90:
    grade = "A+"
    remarks = "Excellent"
elif percentage >= 80:
    grade = "A"
    remarks = "Very Good"
elif percentage >= 70:
    grade = "B"
    remarks = "Good"
elif percentage >= 60:
    grade = "C"
    remarks = "Average"
elif percentage >= 50:
    grade = "D"
    remarks = "Needs Improvement"
else:
    grade = "F"
    remarks = "Better Luck Next Time"

if percentage >= 35:
    result = "PASS"
else:
    result = "FAIL"

print("\n" + "=" * 50)
print("              REPORT CARD")
print("=" * 50)
print("Student Name :", name)
print("Roll Number  :", roll_no)
print("-" * 50)
print("Python       :", python_marks)
print("English      :", english_marks)
print("Maths        :", maths_marks)
print("AI           :", ai_marks)
print("-" * 50)
print("Total Marks  :", total)
print("Percentage   :", percentage)
print("Highest Mark :", highest_mark)
print("Lowest Mark  :", lowest_mark)
print("Grade        :", grade)
print("Remarks      :", remarks)
print("Result       :", result)
print("=" * 50)

choice = input("Do you want to enter another student? (yes/no): ")

if choice.lower() == "yes":
    print("Run the program again for another student.")
else:
    print("Thank you for using Student Report Card System!")
