import subprocess as sp

sp.call("clear", shell=True)

print(
    "This program calculate counts of days you lived till now.\nPlease insert your birthday... (in Gregorian Calendar)"
)

year = input("Year: ")
try:
    year = int(year)
except ValueError:
    print('Just integer values.')
    raise SystemExit 

month = input("Month: ")
date = input("Day: ")

print(year)
print(month)
print(date)