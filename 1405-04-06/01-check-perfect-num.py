"""
What is `Perfect Number`? 
    In number theory, a perfect number is a positive integer that is equal to the sum of its positive proper divisors, that is, divisors excluding the number itself. (Google search)

    It has to return True with this example values [6, 28, 496, 8128]
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
    sum = 0
    for i in range(1, number): 
        if number % i == 0:
            sum += i
    
    if not number == sum :
        return False

    return True

def main():
    _number:str = input('This program get a number and check is it a `perfect number` or not.\n\nPlease insert a number: ')
    print(
        is_perfect_number(_number)
    )

main()
while input('\nretry? (y/n)').lower() == 'y':
    sp.call('clear', shell=True)
    main()
