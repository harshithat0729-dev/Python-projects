print("========== LOAN ELIGIBILITY CHECKER ==========")

applicant_name = input("Enter Applicant Name: ")
age = int(input("Enter your age: "))
monthly_income = int(input("Enter monthly income: "))
credit_score = int(input("Enter credit score: "))
has_existing_loan = input("Do you have existing loan? (yes/no): ")

eligible = True

print("-" * 45)

def check_age(age):
    if age >= 21 and age <= 60:
        print("Your age is valid.")
        return True
    else:
        print("Your age is not valid.")
        return False

def check_income(monthly_income):
    if monthly_income >= 30000:
        print("Your income is valid.")
        return True
    else:
        print("Your income is too low.")
        return False

def check_credit(credit_score):
    if credit_score >= 700:
        print("Credit score is valid.")
        return True
    else:
        print("Your credit score is too low.")
        return False

def check_loan(has_existing_loan):
    if has_existing_loan.lower() == "no":
        print("No Existing Loan.")
        return True
    else:
        print("Your existing loan is detected.")
        return False

if not check_age(age):
    eligible = False
if not check_income(monthly_income):
    eligible = False
if not check_credit(credit_score):
    eligible = False
if not check_loan(has_existing_loan):
    eligible = False

print("-" * 45)

if eligible:
    print("Congratulations!", applicant_name)
    print("Your Loan is approved.")
else:
    print("Sorry", applicant_name)
    print("Your Loan is rejected.")
