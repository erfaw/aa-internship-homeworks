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

if year > CURRENT_DATE.year:
    print("impossible bro! 😂")

month = input("Month: ")
date = input("Day: ")

print(year)
print(month)
print(date)