# WI DL numbers are encoded as follows: SSSS-FFFY-YDDD-NN (NN is overflow, not used in this program)
# SSSS is the Soundex code of the last name
# FFF is the first three letters of the first name, 
# Y is the last 2 digits of the birth year 
# and DDD is the birth date in MMDD format

# User Inputs
first = input("Enter first name: ")
last = input("Enter last name: ")
middle = input("Enter middle inital (press Enter if none): ")
year = input("Enter last two digits of birth year: ")
month = input("Enter birth month (1-12): ")
day = input("Enter birth day (1-31): ")
gender = input("Enter gender (M/F): ")

# Soundex Encoding (Last Name))
# Letters with the same soundex number that are immediately next to each other are discarded
# If two letters with the same soundex number seperated by "H" or "W", only use the first letter.
# The first letter of the last name is always used at the beginning of the soundex code, even if it has a soundex number of 0.
# Ignored Letters: A, E, I, O, U, H, W, Y
lastname = last.upper()
soundex_table = {
    'B': '1', 'F': '1', 'P': '1', 'V': '1',
    'C': '2', 'G': '2', 'J': '2', 'K': '2', 'S': '2', 'Z': '2',
    'D': '3', 'T': '3',
    'L': '4',
    'M': '5', 'N': '5',
    'R': '6'
}
soundex_first = lastname[0]
soundex = soundex_first
prev_digit = soundex_table.get(soundex_first, '')
for i in range(1, len(lastname)):
    char = lastname[i]
    # Determine digit
    if char in "AEIOUY":
        digit = ''
        prev_digit = '' # vowels reset prev_digit
    elif char in "HW":
        digit = ''   # H/W do NOT reset prev_digit
    else:
        digit = soundex_table.get(char, '')

    # Apply Soundex rules
    if digit != '' and digit != prev_digit:
        soundex += digit

    # Only update prev_digit if digit is non-empty
    if digit != '':
        prev_digit = digit
print(f"Soundex code: {soundex}")

# First Name Encoding
first_initial = first.upper()[0]
firstname_table = {
    "A": "000", "B": "060", "C": "100", "D": "160", "E": "200",
    "F": "240", "G": "280", "H": "320", "I": "400", "J": "420",
    "K": "500", "L": "520", "M": "540", "N": "620", "O": "640",
    "P": "660", "Q": "700", "R": "720", "S": "780", "T": "800",
    "U": "840", "V": "860", "W": "880", "X": "940", "Y": "960",
    "Z": "980"
}
first_code = int(firstname_table.get(first_initial, "000"))

# Middle Initial Adjustment
middle_initial = middle.upper()
middle_table = {
    "": "0",
    "A": "1", "B": "2", "C": "3", "D": "4", "E": "5",
    "F": "6", "G": "7", "H": "8", "I": "9", "J": "10",
    "K": "11", "L": "12", "M": "13", "N": "14", "O": "14",
    "P": "15", "Q": "15", "R": "16", "S": "17", "T": "18",
    "U": "18", "V": "18", "W": "19", "X": "19", "Y": "19", "Z": "19"
}
middle_code = int(middle_table.get(middle_initial, "0"))

# Full Name Code Calculation
full_name_code = first_code + middle_code
# Must be 3 digits
fff = str(full_name_code).zfill(3)
print(f"First name code: {fff}")

# DOB Encoding
yy = year.zfill(2)
mm = month.zfill(2)
dd = day.zfill(2)

# Convert MMDD to integer
date_value = int(mm + dd)

# Apply gender offset
if gender.upper() == "F":
    date_value += 500

# Convert back to 4 digits
ddd = str(date_value).zfill(4)

# Final WI DL Number
wi_dl_number = f"{soundex}-{fff}{yy}-{ddd}-NN"
print(f"WI DL Number: {wi_dl_number}")
