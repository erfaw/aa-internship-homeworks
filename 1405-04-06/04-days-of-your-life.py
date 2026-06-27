import subprocess as sp
from datetime import datetime as dt

sp.call("clear", shell=True)

CURRENT_DATE = dt.now()

print(
    "This program calculate counts of days you lived till now.\nPlease insert your birthday... (in Gregorian Calendar)"
)

year = input("Year: ")
try:
    year = int(year)
except ValueError:
    print('Just integer values.')
    raise SystemExit 

if year > CURRENT_DATE.year or year < (CURRENT_DATE.year) - 100 :
    print(f"impossible bro! 😂, are you trying to say you're {CURRENT_DATE.year - year} ?! C'mon...")
    raise SystemExit 

month = input("Month: ")
try:
    month = int(year)
except ValueError:
    print('Just integer values.')
    raise SystemExit 

if not 1 <= month <= 12:
    print('Please insert a valid month number. (1 till 12)')
    raise SystemExit

day = input("Day: ")
try:
    day = int(year)
except ValueError:
    print('Just integer values.')
    raise SystemExit 

if not 1 <= day <= 31:
    print('Please insert a valid day number. (1 till 31)')
    raise SystemExit
    # TODO : insert validation for leapyear
    # TODO : insert validation for each month with calendar.monthrange()

print(year)
print(month)
print(day)