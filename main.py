import datetime

# User Inputs
first = input("Enter your first name as it appears on your driver's license: ")
if first == "":
    print("First name cannot be empty. Please enter your first name.")
    first = input("Enter your first name as it appears on your driver's license: ")
elif first.isalpha() == False:
    print("First name must contain only letters. Please enter a valid first name.")
    first = input("Enter your first name as it appears on your driver's license: ")

last = input("Enter your last name as it appears on your driver's license: ")
if last == "":
    print("Last name cannot be empty. Please enter your last name.")
    last = input("Enter your last name as it appears on your driver's license: ")
elif last.isalpha() == False:
    print("Last name must contain only letters. Please enter a valid last name.")
    last = input("Enter your last name as it appears on your driver's license: ")

gender = input("Enter your gender as it appears on your driver's license (M/F): ")
if gender not in ["M", "F"]:
    print("Gender must be M or F.")
    gender = input("Enter your gender as it appears on your driver's license (M/F): ")

birth = input("Enter your date of birth (YYYY-MM-DD): ")
try:
    year, month, day = map(int, birth.split("-"))
    datetime.date(year, month, day)
except ValueError:
    print("Invalid date format. Please enter your date of birth in the format YYYY-MM-DD.")
    birth = input("Enter your date of birth in the proper format (YYYY-MM-DD): ")
