"""
What is `Perfect Number`? 
    In number theory, a perfect number is a positive integer that is equal to the sum of its positive proper divisors, that is, divisors excluding the number itself. (Google search)
"""

import subprocess as sp

sp.call("clear", shell=True)

def is_perfect_number(n:float) -> bool:
    """
    checks a number is perfect or not. 
    """
    return True

_number:str = input('This program get a number and check is it a `perfect number` or not.\n\nPlease insert a number: ')

try: 
    input_num = float(_number)
except ValueError: 
    print("Please insert a valid input. (integer number, float number)")
