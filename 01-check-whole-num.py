"""
What is `Perfect Number`? 
    In number theory, a perfect number is a positive integer that is equal to the sum of its positive proper divisors, that is, divisors excluding the number itself. (Google search)
"""

import subprocess as sp

sp.call("clear", shell=True)

def is_perfect_number(n) -> bool:
    """
    checks a number is perfect or not. 
    """
    # Check if input is a numeric value
    try: 
        number = float(n)
    except ValueError: 
        print("Please insert a valid input. (integer number)")

    # Check inputted number to be int
    if not number == int(number):
        return False
    else: 
        number = int(number)

    # Check for positivity
    if not number > 0:
        return False
    
    # End check to be perfect 
    for i in range(1, number): # we knew 6 is a perfect number so it must result 1, 2, 3 for a 6 input.
        if number % i == 0:
            print(i)

    return True

_number:str = input('This program get a number and check is it a `perfect number` or not.\n\nPlease insert a number: ')

print(
    is_perfect_number(_number)
)
