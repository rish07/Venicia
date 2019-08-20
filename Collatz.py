#!/user/bin/python
great = 0
b = 0
m = 0
n = 0
for a in range(1, 1000001):
    m = a
    while m > 1:
        if m % 2 == 0:
            m /= 2
        elif m % 2 != 0:
            m = 3 * a + 1
        n += 1
    temp = n
    if temp > great:
        great = temp
        b = a
print b