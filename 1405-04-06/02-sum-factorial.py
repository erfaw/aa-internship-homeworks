import subprocess as sp

sp.call('clear', shell=True)
try:
    _number = int(input('please enter a valid number:\t '))
except ValueError:
    print('Please enter an Integer number.')
    raise SystemExit

if not _number >= 1 :
    print('Factorial needs positive numbers.')

def calculate_factorial(n):
    """
    Calculate factorial of recieved number. with recursive way.
    """
    if n >= 1:
        return n * calculate_factorial(n-1)
    else: 
        return 1


sum = 0
for i in range(1, _number+1): 
    factorial = calculate_factorial(i)
    sum += calculate_factorial(i)
    print(f"i={i}, fact={factorial}")
print(f"\nEnd Result = {sum}")
