#Program for Loan Eligibility Checker
print("==========LOAN ELIGIBILITY CHECKER==========")

applicant_name=input("Enter Applicant Name:")
age=int(input("Enter your age:"))
monthly_income=int(input("Enter monthly income:"))
credit_score=int(input("Enter credit score:"))
has_existing_loan=input("Do you have existing loan?(yes/no):")
eligible=True

print("-"*75)

#Checking Age
if age>=21 and age<=60:
    print("Your age is valid")
else:
    print("Your age is not valid.")
    eligible=False

#Checking Income
if monthly_income>=30000:
    print("Your income is valid.")
else:
    print("Your income is too low.")
    eligible=False

#Checking Credit Score
if credit_score>=700:
    print("Credit score is valid.")
else:
    print("Your credit score is too low.")
    eligible=False

#Checking Existing loan
if has_existing_loan.lower()=="no":
    print("No Existing loan.")
else:
    print("Your existing loan is detected.")
    eligible=False

print("-"*75)

#Final Decision
if eligible:
    print("Congratulations!",applicant_name)
    print("Your Loan is approved")
else:
    print("Sorry",applicant_name)
    print("Your Loan is rejected.")
