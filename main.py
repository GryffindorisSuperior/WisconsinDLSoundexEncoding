import datetime

# User Inputs
first = input("Enter your first name as it appears on your driver's license: ")
if first == "":
    print("First name cannot be empty. Please enter your first name.")
    first = input("Enter your first name as it appears on your driver's license: ")
elif first.isalpha() == False:
    print("First name must contain only letters. Please enter a valid first name.")
    first = input("Enter your first name as it appears on your driver's license: ")

middle = input("Enter middle initial (press Enter if none): ")
if middle and (len(middle) != 1 or not middle.isalpha()):
    print("Middle initial must be a single letter or blank.")
    middle = input("Enter middle initial (press Enter if none): ")

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


# Last Name Encoding
lastname = last.upper()
mapping = {
    "B":"1", "F":"1", "P":"1", "V": "1",
    "C":"2", "G":"2", "J":"2", "K":"2", "Q":"2", "S":"2", "X":"2", "Z":"2",
    "D":"3", "T":"3",
    "L":"4",
    "M":"5", "N":"5",
    "R":"6"
}

soundex = lastname[0]
for char in lastname[1:]:
    if char in mapping:
        code = mapping[char]
        if code != soundex[-1]:
            soundex += code
    else:
        soundex += "0"

soundex = (soundex + "000")[:4]


# First Name Encoding
firstname = first.upper()
middle_initial = middle.upper() if middle else ""
table_first = {
    "A": 0, "B": 60, "C": 100, "D": 160, "E": 200,
    "F": 240, "G": 280, "H": 320, "I": 400, "J": 420,
    "K": 500, "L": 520, "M": 540, "N": 620, "O": 640,
    "P": 660, "Q": 700, "R": 720, "S": 780, "T": 800,
    "U": 840, "V": 860, "W": 880, "X": 900, "Y": 940, "Z": 960
}
first_code = table_first.get(firstname[0], 0)

# Gender Encoding
if gender == "F":
    first_code += 500

# Middle Initial
middle_table = {
    "A": 1, "B": 2, "C": 3, "D": 4, "E": 5,
    "F": 6, "G": 7, "H": 8, "I": 9, "J": 10,
    "K": 11, "L": 12, "M": 13, "N": 14, "O": 14,
    "P": 15, "Q": 15, "R": 16, "S": 17, "T": 18,
    "U": 18, "V": 18, "W": 19, "X": 19, "Y": 19, "Z": 19
}
if middle_initial:
    first_code += middle_table.get(middle_initial, 0)

# DOB Encoding
yy = year % 100 # give remainder of year divided by 100
month_code = (month - 1) * 40
day_code = day
dob_code = yy + month_code + day_code

# Final WI DL Number
license_number = str(soundex) + str(first_code) + str(dob_code)
print("Your Wisconsin Driver's License Number is: " + str(license_number))