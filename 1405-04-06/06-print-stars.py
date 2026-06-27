star_num = input('Insert a number: ')

try:
    star_num = int(star_num)
except ValueError:
    print('Just integer values.')
    raise SystemExit 

for i in range(star_num, 0, -1):
    print('*'*i)