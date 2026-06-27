import subprocess as sp

sp.call('clear', shell=True)

_number = int(input('please enter a valid number:\t '))

def calculate_factorial(n):
    """
    Calculate factorial of recieved number. with recursive way.
    """
    if n >= 1:
        return n * calculate_factorial(n-1)
    else: 
        return 1

print(
    calculate_factorial(_number)
)
