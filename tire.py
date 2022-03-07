import math

w = float(input('Enter the width of the tire in mm '))
a = float(input('Enter the aspect ratio of the tire '))
d = float(input('Enter the diameter of the wheel in inches '))

volume = (math.pi * w*w*a*(w*a+2540*d)/10000000000)

print(f'The volume of air in the tire is {volume}')

from datetime import datetime
datetime.now(tz=None)

city = 'Fort Worth'
elevation = 203
population = 927720

with open('cities.txt','at') as cities_file:
    print(city, file=cities_file)
    print(f'{elevation}, {population}', file=cities_file)