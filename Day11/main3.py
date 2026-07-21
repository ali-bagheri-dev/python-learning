import message

print(message.welcome("Ali"))

from geometry import rectangle_area
from geometry import rectangle_perimeter
print(rectangle_area(10,15))
print(rectangle_perimeter(10,15))

import random
number=random.randint(0,20)
while True:
    i=int(input("enter your number"))
    if i==number:
        print(f'{number} is correct')
        break
    elif i<number:
        print('Too Low')
    elif i>number:
        print('Too High')

