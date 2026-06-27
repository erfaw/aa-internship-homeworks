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

    # Check number to be int

    return True

_number:str = input('This program get a number and check is it a `perfect number` or not.\n\nPlease insert a number: ')


