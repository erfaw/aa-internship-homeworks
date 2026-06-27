_number = input("Please insert a integer number: ")

try:
    _number = int(_number)
except ValueError:
    print('Just integer values.')
    raise SystemExit 

range = range(1, _number+1)
_number = list(range)

for j in range:
    for i in _number:
        print(i, end="")
    _number.pop(0)
    print()
