import subprocess as sp

sp.call('clear', shell=True)


def calculate_factorial(n):
    """
    Calculate factorial of recieved number. with recursive way.
    """
    if n >= 1:
        return n * calculate_factorial(n-1)
    else: 
        return 1


def sum_range_factorial(n):
    sum = 0
    for i in range(1, n+1): 
        sum += calculate_factorial(i)
    return sum


def main():
    try:
        _number = int(input('please enter an integer number:\t '))
    except ValueError:
        print('Please enter an Integer number. it must be just digits.')
        return 
    if not _number >= 1 :
        print('Factorial needs positive numbers.')
        return
    
    print(f"sum = {sum_range_factorial(_number)}")


main()
while input('\nretry? (y/n)').lower() == 'y':
    sp.call('clear', shell=True)
    main()
