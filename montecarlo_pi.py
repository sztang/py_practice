#!/usr/bin/env python3
# monte carlo method to approximate pi

# create no of darts
# create inside circle check
# iterate loop through all darts till dartCount = 0
# generate random x and y coordinates for [0,1)
# i.e. a circle nested within a square of side 1 unit long
# use distance from zero to check for inside_circle:
# i.e. by pythagoras, h = distance of point from zero, h**2 = x**2 + y**2
# for point inside_circle = True, h must be less than 1 since radius = 1

import math
import random

dartCount = 1000000000
insideCircle = 0

for i in range(0,int(dartCount+1)):
    x = random.random()
    y = random.random()
    h = math.sqrt(x**2 + y**2)
    if h <= 1.0:
        insideCircle += 1

# circleArea/sqArea = pi/4
pi = 4 * (float(insideCircle)/dartCount)
print(f'No of darts in circle = {insideCircle}')
print(f'Total darts = {dartCount}')
print(f'The monte carlo approx of pi using {dartCount} instances is {pi:.10f}')