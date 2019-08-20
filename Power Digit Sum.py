#!/bin/user/python
import math
n = int(math.pow(2, 1000))
m = n
print n
sum = 0
while (m > 0):

    r = m % 10
    sum += r
    m /= 10
    print m , sum , r
print sum
